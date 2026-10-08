# Do chat ao procedimento · prática 4a

Uma conversa inteira, do jeito que ela acontece de verdade: você anexa a planilha, o Claude analisa, você pede o relatório, corrige, e aprova. Depois de aprovado, a conversa já fez o trabalho dela. Se o relatório volta todo mês, ela vira **um projeto** ou **uma skill**.

**A planilha:** `receita-cursos-escola-aurora.xlsx`, da página. Escola Aurora é fictícia: 4 unidades, 6 cursos, orçado × realizado de janeiro de 2025 a setembro de 2026, 506 linhas.

**Como fazer:** uma conversa nova no chat, fora de qualquer projeto. Os cinco prompts vão na **mesma** conversa, um de cada vez. A planilha só vai no primeiro.

## Prompt 1 · O raio-X da base (anexe a planilha)

```
[P] Você é um analista financeiro sênior de uma escola de cursos livres, especialista em orçado × realizado.

[C] A Escola Aurora tem 4 unidades (Aldeota, Centro, Messejana e Sobral) e 6 cursos. A planilha anexa tem a receita orçada e a realizada de cada curso, por unidade e por mês, de janeiro de 2025 a setembro de 2026. Antes de qualquer relatório, quero entender a base.

[T] Faça uma análise exploratória: o que cada coluna significa e o tipo de cada uma, o período e os totais. Aponte valores vazios, linhas repetidas, grafias diferentes para a mesma coisa e contas que não fecham (alunos × ticket = receita). Sugira 3 perguntas de negócio que esta base responde.

[F] Quatro blocos: (a) Estrutura da base; (b) Qualidade dos dados, com cada problema e onde ele está; (c) Primeira fotografia: orçado × realizado por ano; (d) 3 perguntas para investigar.

[L] Sem gráficos e sem relatório ainda. Não corrija nada sozinho: liste os problemas e me pergunte como tratar.

[Critério de sucesso] Um gestor entende o que tem em mãos, e quanto pode confiar, sem abrir a planilha.
[Negativo] Sem jargão de programação e sem nome de ferramenta ou biblioteca.
```

**O que esperar:** a estrutura das 16 colunas e, na qualidade, os problemas plantados de propósito: motivo vazio, linhas repetidas, "Marco" sem cedilha, "messejana " com minúscula e espaço, e duas receitas que não fecham com alunos × ticket. No fim, ele pergunta como tratar.

## Prompt 2 · Onde está o desvio

```
Sobre os problemas: as linhas repetidas saem; grafias diferentes viram uma só (Messejana, Março); onde alunos × ticket não fecha com a receita, vale alunos × ticket. Os motivos vazios ficam como "sem motivo registrado". Refaça os totais com isso.

Agora compare orçado × realizado de 2026 por unidade e por curso. Encontre os 3 maiores desvios negativos e o maior positivo. Para cada um: quanto (em R$ e em %), desde quando, e o motivo que a planilha registra.

Uma tabela por unidade, uma por curso, e uma seção curta por desvio. Causa, só a que a planilha mostra; o que for hipótese, marque como hipótese.
```

**O que esperar:** Messejana muito abaixo das outras unidades em 2026, e Power BI como o único curso acima do orçado. Os números do raio-X mudam um pouco, porque agora os problemas foram tratados.

## Prompt 3 · O relatório

```
Agora o relatório para a diretoria, em uma página. Comece pela conclusão em 3 linhas. Depois, a tabela de 2026 por unidade, os 3 pontos de atenção e 3 recomendações, cada uma com um dono e um prazo. Valores em R$ mil.
```

**O que esperar:** um relatório que já serve, mas com alguma recomendação genérica e número sem origem. É de propósito: o prompt 4 é a sua revisão.

## Prompt 4 · A sua correção

```
Três ajustes antes de eu aprovar:
1. A recomendação para Messejana está genérica. Diga o que fazer, com um número que dê para conferir no mês que vem.
2. Cada número do texto diz de onde saiu: unidade, curso e período.
3. Tire da conclusão o que é hipótese. Leve para uma seção no fim chamada "A confirmar".
```

**O que esperar:** a mesma página, mais curta na conclusão e mais precisa nas recomendações. Se ainda faltar algo, corrija de novo: a conversa é sua até você aprovar.

## Prompt 5 · Aprovado. E agora?

O relatório ficou do seu jeito. **Esta conversa não serve mais para o mês que vem**: ela carrega os números deste mês e as idas e vindas. O que serve é o **procedimento** que nasceu dela. Escolha um dos dois caminhos.

### 5a · Vira o system prompt de um projeto

```
Aprovado. Este relatório vai se repetir todo mês, com a planilha nova. Escreva o system prompt de um projeto do Claude que faça este trabalho do jeito que ficou aqui: o papel; o que ele recebe; os passos, nesta ordem (o raio-X e as perguntas sobre os problemas, depois os números, depois o relatório); o formato final; e cada correção que eu fiz nesta conversa, escrita como regra. Não use os números deste mês. Me entregue em um bloco só, para eu colar nas instruções do projeto.
```

**Depois:** Projetos › Novo projeto › cole nas instruções. No mês que vem, uma conversa nova dentro do projeto e só a planilha nova.

### 5b · Vira uma skill

```
Aprovado. Transforme este trabalho numa skill chamada relatorio-receita-mensal. A descrição diz quando usar: quando eu mandar a planilha de receita do mês. O passo a passo segue esta conversa (o raio-X e as perguntas sobre os problemas, depois os números, depois o relatório), e cada correção que eu fiz vira uma regra. Não use os números deste mês. Me entregue o arquivo para eu instalar no Claude.
```

**Depois:** instale o arquivo no Claude. No mês que vem, em qualquer conversa, mande a planilha nova e peça o relatório de receita.

## Qual dos dois?

| | Projeto | Skill |
|---|---|---|
| Onde vale | dentro do projeto | em qualquer conversa ou projeto |
| Bom quando | o trabalho tem material fixo junto (um modelo, um design, um histórico) | o procedimento é o mesmo, onde quer que você esteja |
| Na prática 4 | o system prompt que você usou nasceu assim | a parte 3 do curso é sobre isto |
