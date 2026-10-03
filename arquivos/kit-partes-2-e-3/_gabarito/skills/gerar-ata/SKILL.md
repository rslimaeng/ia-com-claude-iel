---
name: gerar-ata
description: Gera a ata formal de uma reunião do PMO a partir da nota de leitura, no modelo da pasta atas/modelo/, e registra as decisões. Use quando o Sérgio pedir "gera a ata", "faz a ata da reunião de X" ou depois que ele aprovar uma nota de leitura.
---

# Gerar ata

> Gabarito do treinamento. A sua skill nasce do trabalho que você fez na Prática 5b;
> compare com esta depois de embalar a sua.

## Antes de começar

1. A nota de leitura existe em `reunioes/leituras/` e o Sérgio aprovou. Se não existe, use a skill `ler-transcricao` primeiro.
2. Abra `atas/modelo/modelo-ata.md`. A ata segue os blocos dele, na mesma ordem.

## Regras

- **Participantes:** nome e função da `pessoas.md`. Quem não foi identificado entra como `[a confirmar]`.
- **Síntese:** um título curto por tema e bullets. Nada de parágrafo corrido.
- **Decisões:** só as da parte 4 da nota. Proposta vira encaminhamento.
- **Riscos:** só os que a reunião levantou.
- **Encaminhamentos:** ação, responsável (área, e o nome entre parênteses só se a reunião nomeou) e prazo **em data**. Sem data dita, escreva "a definir".
- Linguagem formal: a ata circula para fora do PMO.

## Onde gravar

`atas/em-validacao/<aaaa-mm-dd>_ATA_<Tipo>_<Nome>.md`

## Depois de gravar

1. Acrescente cada decisão ao `registro-de-decisoes.md`, numerada, com a ata de origem.
2. Atualize o `00-aqui-paramos.md`: ata gerada, esperando validação.
3. Mostre a ata ao Sérgio. **Ela só vai para `atas/aprovadas/` com o OK dele.**
