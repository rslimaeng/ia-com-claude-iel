# Prompt 1 · Gerar o time de especialistas

**Como usar:** crie um Project no claude.ai, suba as fontes no conhecimento (o livro, a pesquisa, ou os dois) e cole o bloco abaixo como primeira mensagem. Se preferir, cole as fontes na própria mensagem, antes do prompt. O prompt trabalha em três fases e para no fim de cada uma para você aprovar. O que sai da Fase 3 é o arquivo `time-de-especialistas.md`, que vai no conhecimento de um segundo Project, o do time.

---

```
Você vai transformar as fontes deste Project em um time de especialistas que eu vou usar dentro do Claude. Trabalhe em três fases e PARE ao fim de cada uma para eu aprovar. Escreva em português do Brasil.

## Antes de tudo: leia as fontes inteiras

Leia cada arquivo do começo ao fim antes de escrever qualquer coisa. Não resuma pela introdução, pelo sumário nem pelas primeiras páginas. Ao terminar, devolva só o inventário abaixo:

| arquivo | palavras (aprox.) | estrutura (partes, capítulos, seções) | tipo |

Onde tipo é um destes três:
- PRIMÁRIA: o material do próprio autor (livro, curso, transcrição, manual, artigo original).
- DERIVADA: texto de terceiro ou de IA sobre a primária (resumo, pesquisa, resenha, relatório).
- CONTEXTO: material que não é sobre o tema, mas sobre onde ele vai ser aplicado (dados do mercado, da empresa, do setor).

Abaixo do inventário, uma seção "Danos e limites": o que a conversão perdeu (fórmula, tabela, imagem, gráfico), trechos truncados, idioma, e o que nenhuma fonte cobre.

Regras de precedência, que valem para todas as fases:
1. A primária manda. Especialista, conceito, regra e exemplo saem dela.
2. A derivada só entra para traduzir um termo ou preencher o que a primária não cobre, e sempre marcada como derivada.
3. Onde derivada e primária discordam, vale a primária, e você lista a discordância numa tabela "a derivada diz / a primária diz".
4. O que você completar por conta própria vai marcado como [completado].
5. Se não houver primária, diga isso na primeira linha e trabalhe com a derivada como se fosse primária, mantendo as marcas.

## Fase 1: a proposta do time

Extraia da PRIMÁRIA os especialistas. Critérios:
- Cada especialista corresponde a um bloco de conhecimento com fronteira clara na fonte (uma parte, um capítulo, um framework, um processo). Cite de onde vem.
- Cada especialista devolve UM entregável concreto que o usuário leva embora (um diagnóstico, uma tabela, uma decisão, um plano, um texto). Especialista que só "orienta" ou "apoia" não entra.
- Entre 5 e 8 especialistas. Menos que 5 costuma esconder dois dentro de um; mais que 8 costuma separar o que a fonte trata junto.
- A ordem segue a ordem em que a fonte constrói o conhecimento: o que ela ensina primeiro vem primeiro. Essa ordem vira as CAMADAS do time.
- Sem sobreposição: se dois especialistas responderiam à mesma pergunta, funda os dois ou redesenhe a fronteira.

Devolva a tabela:

| # | Camada | Especialista | Chame quando… | O que devolve | Base na fonte |

"Chame quando…" é uma situação na 2ª pessoa, na língua de quem vai usar, sem nome de framework. Certo: "Chame quando você está crescendo e o caixa piora". Errado: "Chame para aplicar o Growth Box".

Abaixo da tabela:
- O que ficou de fora da fonte e por quê (partes que não viraram especialista, e para onde foram).
- O que a derivada acrescentaria, se eu quiser, marcado como derivado.
- Quais especialistas dependem de outros (por exemplo: o 5 só faz sentido depois do 1 ao 4).

PARE. Pergunte se aprovo a proposta, se quero mudar, fundir ou separar algum. Se puder oferecer as escolhas como opções selecionáveis, ofereça.

## Fase 2: um especialista por vez

Depois da minha aprovação, escreva UM especialista por mensagem, na ordem das camadas, no formato abaixo. Ao terminar cada um, pergunte se sigo para o próximo. Nunca escreva dois na mesma mensagem.

Formato de cada especialista, em Markdown, começando pelo título:

# [Nome do especialista]
**Camada N de M** · [uma linha com o que ele devolve]

## Chame quando
3 a 5 situações na 2ª pessoa, uma por linha.

## Como este especialista conversa
- Abre com uma hipótese sobre a situação do usuário, tirada do que ele já disse, e pergunta se acertou. Nunca abre com pergunta em branco.
- Faz no máximo 3 perguntas por vez, e só as que mudam a resposta. O resto ele assume e declara que assumiu.
- Em no máximo 2 rodadas de pergunta, entrega. Se faltar dado, entrega com a lacuna marcada.
- Quando o usuário se contradiz, diz isso, com as duas frases lado a lado.
- Quando há mais de um caminho, apresenta os caminhos como alternativas para o usuário escolher, em vez de escolher por ele.

## O que ele sabe
Os conceitos, regras, critérios e exemplos que a fonte dá para este tema. Cada bloco leva a marca de origem: [primária, cap. X], [derivada: nome do arquivo] ou [completado]. Inclua os exemplos e as histórias que a fonte usa, porque são eles que dão vida à conversa. Inclua as fórmulas por extenso quando houver. É a seção mais longa: entre 400 e 900 palavras, e mais perto de 900 quando a fonte dedica um capítulo inteiro ao tema.

## O que ele devolve
O entregável, com estrutura definida: título das seções e o que cada uma contém. Se for tabela, mostre as colunas. Se for lista, diga o tamanho.

## O que ele NÃO faz
2 a 4 linhas: o que fica com outro especialista (cite qual, pelo nome) e o que a fonte não cobre.

## Ficha técnica
Fonte: [autor, obra, ano, capítulos usados]. Confiança: alta se veio inteiro da primária; média se misturou derivada; baixa se tem [completado] em ponto central.

Não use travessão (o sinal "—") em lugar nenhum. Use ponto, vírgula ou dois pontos.

## Fase 3: montar o arquivo

Quando o último especialista estiver aprovado, me diga como juntar tudo num único arquivo chamado time-de-especialistas.md, nesta ordem:
1. Cabeçalho: nome do time, fonte, data.
2. A tabela da Fase 1, sem a coluna "Base na fonte".
3. Os especialistas na ordem das camadas, separados por uma linha com três traços.

Esse arquivo vai para o conhecimento de um novo Project. O próximo prompt escreve o orquestrador que coordena esse time.
```
