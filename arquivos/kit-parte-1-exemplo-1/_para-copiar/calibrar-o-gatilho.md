# Teste o gatilho · prática 4c

A skill `relatorio-receita-escola` vem com a description no padrão: diz **o quê**, **quando**, **com que falas** e **quando não**. Aqui você testa se ela acerta, frase por frase.

## Instalar

Baixe `relatorio-receita-escola.skill` da página. No Claude: **Personalizar › Habilidades › Adicionar › Fazer upload de habilidade**, e escolha o arquivo. Se pedir, ligue a execução de código nas configurações. Tem a skill do 5b instalada? Desligue durante o teste.

## As cinco frases do teste

Uma **conversa nova** para cada frase. Na frase 1, anexe `receita-cursos-escola-aurora.xlsx`, a planilha da prática 4a. Repare se aparece o Claude lendo a skill antes de responder.

| # | Frase | Deve acionar? |
|---|---|---|
| 1 | Segue a planilha de receita de setembro. Monta o relatório do mês. | sim |
| 2 | Como fechou a receita dos cursos esse mês? | sim |
| 3 | Preciso do fechamento mensal da escola para a diretoria. | sim |
| 4 | Analisa esta planilha de execução do convênio. | não |
| 5 | Escreve um post para o Instagram sobre os cursos da escola. | não |

## Leia a description

Abra a skill em Personalizar › Habilidades e ache as quatro camadas:

1. **O quê:** o que ela entrega, numa frase.
2. **Quando:** a situação, não o assunto.
3. **As falas:** as frases entre aspas, do jeito que a pessoa pede.
4. **Quando não:** os pedidos parecidos que não são dela.

Para cada frase do teste, diga qual camada fez ela entrar, ou não entrar.

## O pedido de ajuste

Use só se alguma frase errou: entrou quando não devia, ou não entrou quando devia.

```
A skill relatorio-receita-escola [entrou / não entrou] quando eu escrevi: "[cole a frase]". Ela [não deveria / deveria] entrar. Ajuste só a description: acrescente a fala que faltou, ou o caso que faltou no "não use para". Mantenha as outras camadas e não passe de 1.024 caracteres. Me mostre o antes e o depois, e atualize a skill.
```

Depois, repita só a frase que errou, numa conversa nova.
