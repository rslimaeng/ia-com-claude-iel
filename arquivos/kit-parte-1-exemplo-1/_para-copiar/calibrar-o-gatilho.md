# Calibre o gatilho · prática 4c

A skill de partida, `relatorio-receita-escola`, faz o trabalho certo, mas a description dela só diz **como** faz. Não diz **quando** usar. Aqui você testa, reescreve e testa de novo.

## As cinco frases do teste

Uma **conversa nova** para cada frase. Repare se aparece o Claude lendo a skill antes de responder.

| # | Frase | Deve acionar? |
|---|---|---|
| 1 | Segue a planilha de receita de outubro. Monta o relatório do mês. | sim |
| 2 | Como fechou a receita dos cursos esse mês? | sim |
| 3 | Preciso do fechamento mensal da escola para a diretoria. | sim |
| 4 | Analisa esta planilha de execução do convênio. | não |
| 5 | Escreve um post para o Instagram sobre os cursos da escola. | não |

## O pedido de reescrita

```
Reescreva a description da skill relatorio-receita-escola. Diga o que ela entrega e quando usar, com as frases de quem pede: "relatório de receita", "fechamento do mês", "como fechou a receita", "resultado dos cursos". Se a planilha não vier, a skill pede. Diga também quando não usar: planilha que não é de receita da escola, como a de execução de convênio, e pedido de texto sem planilha. No máximo três frases. Me mostre a description nova e atualize a skill.
```

Depois, repita só as frases que erraram, cada uma numa conversa nova.
