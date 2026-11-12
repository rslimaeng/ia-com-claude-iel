#!/usr/bin/env python3
"""
somar_orcado_realizado.py — a parte da skill que é conta, e por isso é script.

Lê a planilha de receita dos cursos (.xlsx ou .csv) e imprime, em texto:

  1. INVENTÁRIO   linhas, colunas, período, valores de cada coluna de texto
  2. PROBLEMAS    linhas repetidas, grafias diferentes da mesma coisa, motivo
                  vazio em desvio grande, receita que não fecha com alunos × ticket
  3. NÚMEROS      só com --tratar: orçado × realizado por ano, por unidade e por
                  curso, a decomposição do desvio em volume (alunos) e preço
                  (ticket), e os desvios por curso × unidade, do maior para o menor

Não interpreta nada e não decide nada. Sem --tratar, não mexe em nenhum número:
lista os problemas para a pessoa decidir. Com --tratar, aplica o tratamento
padrão e diz exatamente o que fez:
  - linha 100% repetida sai (fica uma)
  - grafias diferentes viram a forma mais frequente
  - receita que não fecha com alunos × ticket passa a valer alunos × ticket

Uso:
    python3 somar_orcado_realizado.py <arquivo>                 # raio-X, sem tratar
    python3 somar_orcado_realizado.py <arquivo> --tratar        # raio-X + números
    python3 somar_orcado_realizado.py <arquivo> --tratar --ano 2026

Só usa openpyxl e a biblioteca padrão.
"""

import argparse
import csv
import sys
import unicodedata
from collections import Counter, defaultdict

MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
         "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
TEXTO = ["Curso", "Modalidade", "Unidade", "Mes", "Motivo_Desvio"]
OBRIGATORIAS = ["Curso", "Unidade", "Mes", "Ano", "Alunos_Orcados", "Alunos_Matriculados",
                "Ticket_Medio_Orcado", "Ticket_Medio_Realizado", "Receita_Orcada",
                "Receita_Realizada"]
DESVIO_GRANDE = 15.0   # % de desvio a partir do qual o motivo vazio vira problema


# ----------------------------------------------------------------- leitura
def carregar(caminho):
    if caminho.lower().endswith((".xlsx", ".xlsm")):
        import openpyxl
        ws = openpyxl.load_workbook(caminho, data_only=True, read_only=True).worksheets[0]
        linhas = list(ws.iter_rows(values_only=True))
    else:
        with open(caminho, encoding="utf-8-sig", newline="") as f:
            amostra = f.read(4096)
            f.seek(0)
            dialeto = csv.Sniffer().sniff(amostra, delimiters=";,\t")
            linhas = list(csv.reader(f, dialeto))
    cab = [str(c).strip() for c in linhas[0]]
    dados = [dict(zip(cab, l)) for l in linhas[1:] if any(v not in (None, "") for v in l)]
    return cab, dados


def num(v):
    if v is None or v == "":
        return 0.0
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace("R$", "").replace(" ", "")
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return 0.0


def chave(txt):
    """A forma que compara grafias: sem acento, sem espaço sobrando, minúscula."""
    s = unicodedata.normalize("NFKD", str(txt or "")).encode("ascii", "ignore").decode()
    return " ".join(s.split()).casefold()


def brl(v):
    return ("R$ " + f"{v:,.0f}").replace(",", ".") if v >= 0 else "−R$ " + f"{-v:,.0f}".replace(",", ".")


def pct(real, orc):
    return 100 * (real - orc) / orc if orc else 0.0


def secao(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


# ----------------------------------------------------------------- 1 e 2
def inventario(cab, dados):
    secao("1. INVENTÁRIO")
    print(f"Linhas: {len(dados)} | Colunas: {len(cab)}")
    print("Colunas:", ", ".join(cab))
    faltam = [c for c in OBRIGATORIAS if c not in cab]
    if faltam:
        print(f"\n⚠ Faltam colunas que a skill usa: {', '.join(faltam)}")
        print("  Esta planilha não parece a de receita dos cursos. Pare e pergunte.")
        return False
    anos = sorted({int(num(d["Ano"])) for d in dados})
    print(f"Anos: {anos}")
    for c in TEXTO:
        if c in cab and c != "Motivo_Desvio":
            cont = Counter(repr(d[c]) for d in dados)
            print(f"{c}: " + " · ".join(f"{k} ({n})" for k, n in sorted(cont.items())))
    return True


def problemas(cab, dados):
    secao("2. PROBLEMAS DA BASE (nada foi corrigido)")
    achados = {}

    vistos, repetidas = Counter(), []
    for i, d in enumerate(dados, start=2):
        k = tuple(d.get(c) for c in cab)
        vistos[k] += 1
        if vistos[k] == 2:
            repetidas.append((i, d))
    print(f"\na) Linhas 100% repetidas: {len(repetidas)}")
    for i, d in repetidas:
        print(f"   linha {i}: {d['Curso']} · {d['Unidade']} · {d['Mes']}/{d['Ano']}")
    achados["repetidas"] = len(repetidas)

    print("\nb) Grafias diferentes para a mesma coisa:")
    n_graf = 0
    for c in ["Curso", "Modalidade", "Unidade", "Mes"]:
        if c not in cab:
            continue
        grupos = defaultdict(Counter)
        for d in dados:
            grupos[chave(d[c])][d[c]] += 1
        for formas in grupos.values():
            if len(formas) > 1:
                n_graf += 1
                print(f"   {c}: " + " · ".join(f"{f!r} ({n})" for f, n in formas.most_common()))
    if not n_graf:
        print("   nenhuma")
    achados["grafias"] = n_graf

    if "Motivo_Desvio" in cab:
        vazios = [d for d in dados if not str(d.get("Motivo_Desvio") or "").strip()
                  and abs(pct(num(d["Receita_Realizada"]), num(d["Receita_Orcada"]))) >= DESVIO_GRANDE]
        print(f"\nc) Motivo vazio em desvio de {DESVIO_GRANDE:.0f}% ou mais: {len(vazios)}")
        for d in vazios:
            p = pct(num(d["Receita_Realizada"]), num(d["Receita_Orcada"]))
            print(f"   {d['Curso']} · {d['Unidade']} · {d['Mes']}/{d['Ano']}: {p:+.1f}%")
        achados["motivo_vazio"] = len(vazios)

    print("\nd) Receita que não fecha com alunos × ticket:")
    n_conta = 0
    for lado, al, tk, rc in [("realizada", "Alunos_Matriculados", "Ticket_Medio_Realizado", "Receita_Realizada"),
                             ("orçada", "Alunos_Orcados", "Ticket_Medio_Orcado", "Receita_Orcada")]:
        for d in dados:
            conta = num(d[al]) * num(d[tk])
            if abs(conta - num(d[rc])) > 1:
                n_conta += 1
                print(f"   {lado}: {d['Curso']} · {d['Unidade']} · {d['Mes']}/{d['Ano']}: "
                      f"{num(d[al]):.0f} × {brl(num(d[tk]))} = {brl(conta)}, está {brl(num(d[rc]))}")
    if not n_conta:
        print("   nenhuma")
    achados["nao_fecha"] = n_conta

    print("\nPergunte como tratar cada item acima antes de rodar com --tratar.")
    return achados


# ----------------------------------------------------------------- tratamento
def tratar(cab, dados):
    secao("TRATAMENTO APLICADO (padrão do --tratar)")
    vistos, saida, fora = set(), [], 0
    for d in dados:
        k = tuple(d.get(c) for c in cab)
        if k in vistos:
            fora += 1
            continue
        vistos.add(k)
        saida.append(dict(d))
    print(f"- {fora} linha(s) repetida(s) removida(s)")

    for c in ["Curso", "Modalidade", "Unidade", "Mes"]:
        if c not in cab:
            continue
        grupos = defaultdict(Counter)
        for d in saida:
            grupos[chave(d[c])][d[c]] += 1
        oficial = {}
        for formas in grupos.values():
            alvo = formas.most_common(1)[0][0]
            if c == "Mes":   # mês tem forma oficial: a do calendário
                alvo = next((m for m in MESES if chave(m) == chave(alvo)), alvo)
            for f in formas:
                oficial[f] = alvo
        trocas = sum(1 for d in saida if oficial[d[c]] != d[c])
        for d in saida:
            d[c] = oficial[d[c]]
        if trocas:
            print(f"- {c}: {trocas} célula(s) unificada(s) na forma mais frequente")

    for al, tk, rc in [("Alunos_Matriculados", "Ticket_Medio_Realizado", "Receita_Realizada"),
                       ("Alunos_Orcados", "Ticket_Medio_Orcado", "Receita_Orcada")]:
        n = 0
        for d in saida:
            conta = num(d[al]) * num(d[tk])
            if abs(conta - num(d[rc])) > 1:
                d[rc] = conta
                n += 1
        if n:
            print(f"- {rc}: {n} linha(s) passaram a valer alunos × ticket")
    return saida


# ----------------------------------------------------------------- 3
def somar(dados, campo_grupo=None, filtro=None):
    acc = defaultdict(lambda: defaultdict(float))
    for d in dados:
        if filtro and not filtro(d):
            continue
        g = d[campo_grupo] if campo_grupo else "Total"
        a = acc[g]
        a["orc"] += num(d["Receita_Orcada"])
        a["real"] += num(d["Receita_Realizada"])
        # decomposição do desvio, linha a linha (contabilidade gerencial):
        #   efeito volume = (alunos realizados − alunos orçados) × ticket orçado
        #   efeito preço  = (ticket realizado − ticket orçado) × alunos realizados
        #   volume + preço = realizado − orçado, quando a receita fecha com alunos × ticket
        a["vol"] += (num(d["Alunos_Matriculados"]) - num(d["Alunos_Orcados"])) * num(d["Ticket_Medio_Orcado"])
        a["preco"] += (num(d["Ticket_Medio_Realizado"]) - num(d["Ticket_Medio_Orcado"])) * num(d["Alunos_Matriculados"])
        a["linhas"] += 1
    return acc


def tabela(acc, titulo):
    print(f"\n--- {titulo} ---")
    print(f"{'':28}{'Orçado':>16}{'Realizado':>16}{'Desvio':>16}{'%':>8}{'Volume':>15}{'Preço':>15}")
    for g, a in sorted(acc.items(), key=lambda kv: pct(kv[1]["real"], kv[1]["orc"])):
        print(f"{str(g)[:27]:28}{brl(a['orc']):>16}{brl(a['real']):>16}{brl(a['real'] - a['orc']):>16}"
              f"{pct(a['real'], a['orc']):>+7.1f}%{brl(a['vol']):>15}{brl(a['preco']):>15}")


def numeros(dados, ano_ref):
    secao("3. ORÇADO × REALIZADO")
    anos = sorted({int(num(d["Ano"])) for d in dados})
    ano = ano_ref or anos[-1]
    meses_ano = sorted({d["Mes"] for d in dados if int(num(d["Ano"])) == ano},
                       key=lambda m: MESES.index(m) if m in MESES else 99)
    print(f"Ano de referência: {ano} · meses com dado: {meses_ano[0]} a {meses_ano[-1]} ({len(meses_ano)})")

    tabela(somar(dados, "Ano"), "Por ano")
    no_ano = lambda d: int(num(d["Ano"])) == ano
    tabela(somar(dados, "Unidade", no_ano), f"{ano} por unidade")
    tabela(somar(dados, "Curso", no_ano), f"{ano} por curso")
    ultimo = meses_ano[-1]
    tabela(somar(dados, "Unidade", lambda d: no_ano(d) and d["Mes"] == ultimo), f"{ultimo}/{ano} por unidade")

    if len(anos) > 1:
        ant = [a for a in anos if a < ano][-1:]
        if ant:
            mesmo_periodo = lambda d: int(num(d["Ano"])) == ant[0] and d["Mes"] in meses_ano
            tabela(somar(dados, "Unidade", mesmo_periodo), f"{ant[0]}, mesmos meses ({meses_ano[0]} a {ultimo}), por unidade")

    print(f"\n--- {ano}: desvios por curso × unidade, do mais negativo ao mais positivo ---")
    combo = defaultdict(list)
    for d in dados:
        if no_ano(d):
            combo[(d["Curso"], d["Unidade"])].append(d)
    linhas = []
    for (c, u), ds in combo.items():
        orc = sum(num(d["Receita_Orcada"]) for d in ds)
        real = sum(num(d["Receita_Realizada"]) for d in ds)
        neg = [d["Mes"] for d in sorted(ds, key=lambda d: MESES.index(d["Mes"]) if d["Mes"] in MESES else 99)
               if num(d["Receita_Realizada"]) < num(d["Receita_Orcada"])]
        motivos = Counter(str(d.get("Motivo_Desvio") or "").strip() for d in ds
                          if str(d.get("Motivo_Desvio") or "").strip())
        mot = motivos.most_common(1)[0] if motivos else ("(sem motivo registrado)", 0)
        linhas.append((real - orc, c, u, orc, real, len(neg), len(ds), mot))
    total_neg = sum(l[0] for l in linhas if l[0] < 0)
    acum = 0.0
    for dv, c, u, orc, real, n_neg, n, mot in sorted(linhas):
        if dv < 0:
            acum += dv
        fatia = f"  acumulado {100 * acum / total_neg:4.0f}% da queda" if dv < 0 and total_neg else ""
        print(f"{c[:20]:21}{u[:10]:11}{brl(dv):>14}{pct(real, orc):>+7.1f}%  "
              f"{n_neg}/{n} meses abaixo · motivo mais citado: {mot[0]} ({mot[1]}x){fatia}")

    secao("FIM")
    print("Isto é matéria-prima, não o relatório. Siga o SKILL.md: conclusão primeiro,"
          " cada número com unidade, curso e período, e hipótese só em 'A confirmar'.")


def main():
    ap = argparse.ArgumentParser(description="Raio-X e orçado × realizado da planilha de receita dos cursos")
    ap.add_argument("arquivo")
    ap.add_argument("--tratar", action="store_true", help="aplica o tratamento padrão e calcula os números")
    ap.add_argument("--ano", type=int, default=None, help="ano de referência (padrão: o mais recente)")
    args = ap.parse_args()

    cab, dados = carregar(args.arquivo)
    print(f"Arquivo: {args.arquivo}")
    if not inventario(cab, dados):
        return 1
    problemas(cab, dados)
    if args.tratar:
        numeros(tratar(cab, dados), args.ano)
    return 0


if __name__ == "__main__":
    sys.exit(main())
