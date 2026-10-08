# Kit de prática 1 · Um Claude que já sabe como você trabalha

**IA com Claude · Do Zero à Produtividade Total** · R. Lima · IEL Ceará

> **A turma não recebe este arquivo.** Desde 05/10, o kit 1 chega só pela página do curso, prática a prática, sem ZIP. Este README é a fonte dos prompts que a página mostra: mudou aqui, rode `_build/montar-site.py`.

## Antes de começar

1. Abra o **Claude** no navegador ou no aplicativo, logado com a conta **Pro** do curso.
2. Crie no seu computador uma pasta chamada `curso-claude` e salve nela tudo o que baixar da página do curso. Na noite 4, você abre essa pasta na aba Code.
3. Abra também o arquivo `antes-e-depois`, que é onde você vai guardar as três respostas da pergunta-teste. Ele está em dois formatos, com o mesmo conteúdo: `antes-e-depois.docx`, que abre no Word, e `antes-e-depois.md`, que abre em qualquer editor de texto ou em markdownlivepreview.com. Use o que abrir mais fácil no seu computador.

| Pasta | O que tem |
|---|---|
| `arquivos/` | as planilhas e os documentos que você anexa no Claude. Os dados são fictícios. |
| `_para-copiar/` | os textos que você cola |
| `_gabarito/` | **abra só depois de fazer** |

---

## Prática 0 · A pergunta-teste, momento 1 (5 min)

Abra uma **conversa nova**, fora de qualquer projeto. Anexe `arquivos/execucao-convenio-2025.xlsx` e cole:

```
Olha esta planilha e me diz o que precisa de decisão.
```

Copie a resposta para `antes-e-depois.md`, no **Momento 1**.

**O que esperar:** um resumo da planilha, provavelmente longo, e talvez umas perguntas de volta. Ainda não está ruim: está **sem contexto**. Você vai fazer a mesma pergunta mais duas vezes hoje.

---

## Prática 1 · O mesmo pedido, de dois jeitos (15 min)

**Conversa A**, nova, com `execucao-convenio-2025.xlsx` e `fechamento-trimestral-2025.xlsx` anexados:

```
analise esta planilha de execução do convênio e me diga como está a prestação de contas
```

**Conversa B**, outra conversa nova, com os mesmos dois arquivos:

```
Sou analista de prestação de contas de convênio, e confiro execução contra o que foi contratado. Anexei a planilha de execução de um convênio do Instituto Farol, exportada do sistema, e o fechamento trimestral que a coordenação mandou. A planilha tem uma linha por registro, com as colunas Registro, Data, Unidade, Atividade, Horas, Valor Hora, Valor Total e Fonte do Recurso. São quatro trimestres executados em doze unidades, e o relatório vai ao financiador na semana que vem.
O que eu preciso: uma página com o total executado por Unidade e por trimestre, as três unidades mais fora da curva no topo, e a lista do que precisa de decisão antes de eu fechar a prestação. As demais unidades em uma linha só no fim. Está bom quando o coordenador consegue decidir o que fazer com as pendências lendo só essa primeira página, sem abrir a planilha.
Restrições: use apenas o que está nos dois arquivos. Não estime valor que estiver faltando, não junte nomes parecidos na coluna Unidade por conta própria, e confira o total do fechamento contra a soma da coluna Valor Total antes de afirmar qualquer número.
Na dúvida: se encontrar registro duplicado, valor em branco, data em formato diferente ou nome de unidade escrito de dois jeitos, liste o que encontrou e me pergunte antes de decidir. Não conserte por conta própria.
```

**O que esperar:** a A costuma achar bastante coisa, mas decide sozinha: tira o duplicado e soma o texto como valor, sem perguntar. A B acha o mesmo e para para perguntar antes de decidir. O campo que mudou a resposta foi o **Na dúvida**.

**Se a B voltar com perguntas antes da página**, é o pedido funcionando. Responda a cada uma, ou cole:

> aceito as suas leituras sugeridas e some todas as fontes do recurso. Agora monte a página.

**Se a B vier longa ou sem pendência, cole um destes:**
- `corte para uma página, e deixe no topo só o que exige decisão minha.`
- `você conferiu o total do fechamento contra a soma da planilha? Me mostre a diferença, se houver.`
- `desfaça o agrupamento, liste os nomes exatamente como estão na planilha, e me pergunte quais são a mesma.`

---

## Prática 2 · Conferir antes de assinar (15 min)

Na **conversa B**, cole o trecho de conferência (`_para-copiar/trecho-de-conferencia.md`):

```
Antes de me dar a resposta final, faça a conferência abaixo e me mostre o resultado dela.
O que eu preciso: para cada número que aparecer, de onde ele saiu, com a aba, a coluna e quantas linhas foram somadas. E a lista do que você procurou e não encontrou no material.
Restrições: não complete dado que estiver faltando, e não arredonde diferença. Se dois registros parecem a mesma coisa escrita de jeitos diferentes, mostre os dois como estão e não junte.
Na dúvida: pergunte antes de decidir por mim. Deixar um item em aberto é o resultado certo quando a informação não está no material.
```

**Agora você:** marque cada pendência numa das quatro camadas.

| Camada | A pergunta | Quem confere |
|---|---|---|
| 1 | Está preenchido? | a IA |
| 2 | O número fecha? | a IA, se o pedido mandar |
| 3 | É o documento certo? | só você |
| 4 | A conclusão se sustenta? | só você |

**Deu certo se:** você achou pelo menos uma coisa que a resposta anterior tinha passado em silêncio.

---

## Prática 3 · O seu perfil, por entrevista (25 min)

1. Abra uma **conversa nova**.
2. Anexe `_para-copiar/modelo-de-perfil.md` e cole o prompt de `_para-copiar/prompt-entrevista-do-perfil.md`.
3. Responda às rodadas de opções. No fim, ele te mostra uma v1.
4. Copie a v1 e cole em **Configurações › Conta › Instruções para o Claude**. Salve.
5. **Pergunta-teste, momento 2:** abra uma **conversa nova**, anexe de novo `execucao-convenio-2025.xlsx` e cole a mesma pergunta da prática 0. Copie a resposta para `antes-e-depois.md`, no **Momento 2**.

**O que esperar:** no momento 2, a resposta já começa pelo que exige decisão, no seu vocabulário, e para para perguntar em vez de juntar nomes parecidos.

**Se veio igual ao momento 1, há três causas:**
- a conversa foi aberta antes de salvar;
- você escreveu preferência de estilo em vez de regra;
- o perfil ficou uma apresentação sua, e não uma calibragem.

**A régua de cada linha:** *se eu apagar isto, a resposta muda?* Se não muda, a linha sai.

---

## Prática 4 · O projeto pronto em 15 minutos (30 min)

1. Abra **Projetos › Novo projeto** e dê o nome **Relatório de execução do convênio**.
2. Em **Instruções**, cole o conteúdo inteiro de `arquivos/system-prompt-relatorio-execucao.md`.
3. Em **Contexto**, suba `arquivos/design-system-iel.html`.
4. Dentro do projeto, abra uma conversa, anexe `arquivos/execucao-convenio-2025.xlsx` e `arquivos/fechamento-trimestral-2025.xlsx` e cole:

```
Anexei a execução. Monta o relatório.
```

**O que esperar:** antes do relatório, três conferências (registros lidos, grafias de unidade, soma contra o fechamento). A soma **não bate**: a diferença é de R$ 673.895,00, que são os R$ 675.215,00 das 422 células de texto menos os R$ 1.320,00 do registro repetido. *Conferência que fecha não é conferência que está certa.* Depois das conferências, duas peças: o **relatório** e a **apresentação** no molde das aulas, as duas com o **plano de ação** no fim.

**Precisa em PowerPoint?** Na mesma conversa, cole (o recurso de criar arquivos precisa estar ligado nas configurações da conta; o .pptx abre também no Google Slides):

> Converta a apresentação em um arquivo .pptx para eu baixar: um slide do PowerPoint para cada slide, com os mesmos textos, números e cores. Os gráficos viram gráficos do próprio PowerPoint, com os mesmos valores. Não mude nem arredonde nenhum número.

5. **Pergunta-teste, momento 3:** ainda dentro do projeto, abra uma conversa nova, anexe `execucao-convenio-2025.xlsx` e cole a pergunta da prática 0. Copie a resposta para o **Momento 3**.

---

## Prática 4a · Do chat ao procedimento (25 min)

1. Conversa nova no chat, **fora de qualquer projeto**. Anexe `arquivos/receita-cursos-escola-aurora.xlsx`: a Escola Aurora, fictícia, com 4 unidades, 6 cursos e 506 linhas.
2. Mande os cinco prompts de `_para-copiar/do-chat-ao-procedimento.md` (o mesmo texto está no `.pdf`, para ler), **na mesma conversa**, um de cada vez: o raio-X da base, onde está o desvio, o relatório, a sua correção e a aprovação.
3. No prompt 5, escolha um caminho: o **5a** escreve o system prompt de um projeto; o **5b** escreve uma skill.

**O que esperar:** no raio-X, os problemas plantados de propósito (motivo vazio, linhas repetidas, "Marco", "messejana " e duas receitas que não fecham). Depois, Messejana muito abaixo das outras unidades em 2026, e o Power BI como o único curso acima do orçado. A lição: **aprovou, a conversa fez o trabalho dela**. O que serve para o mês que vem é o procedimento, num projeto ou numa skill.

---

## Prática 4b · Um time pronto, funcionando (12 min)

1. Abra **Projetos › Novo projeto** e dê o nome **Time de marca**.
2. Em **Contexto**, suba `arquivos/time-de-marca.md`: seis especialistas, cada um com uma entrega, e as perguntas de desempate.
3. Em **Instruções**, cole o conteúdo inteiro de `_para-copiar/orquestrador-time-de-marca.md`.
4. Numa conversa nova do projeto, mande as três mensagens de `_para-copiar/teste-do-time-de-marca.md`, uma de cada vez. Na caixa **"por onde você quer começar?"**, não clique em nenhuma opção: cole o caso da escola no campo de texto da caixa. Se clicar, você escolhe o especialista e o desempate não acontece.

**O que esperar:** a tabela do time e uma pergunta só. No caso da escola, uma **pergunta de desempate** antes de escolher (Posicionamento ou Evidência?), depois a resposta assinada **[Especialista · Camada N]**, com uma hipótese antes de perguntar. No "outro lado", o vizinho que discorda, com as duas posições lado a lado. Montar um time a partir de um material seu é o “Monte o seu time”, para casa, na página do curso.

---

## Reforço · Onde cada regra mora (sem prática)

O slide 29 já mostra as sete regras respondidas: a frequência escolhe o lugar.

| # | Regra | Sempre, às vezes ou nunca | Onde mora |
|---|---|---|---|
| 1 | Valores em reais, com vírgula | sempre | Instruções |
| 2 | Os 12 passos do fechamento trimestral | às vezes, e ele percebe | Skill |
| 3 | Sem termo em inglês nos documentos | sempre | Instruções |
| 4 | Emitir o certificado de quem concluiu | às vezes, e você chama | Comando, e não skill: errar o momento sai caro |
| 5 | Buscar o relatório no sistema da casa | nunca se guarda, se busca | Conector |
| 6 | Conferir a presença de uma turma | às vezes, e ele percebe | Skill |
| 7 | Um pacote com três peças para a área de turmas | depende do que tem dentro | Plugin |

A mesma tabela está em `_gabarito/sete-regras.md`.

---

## Fecho · A ficha do seu projeto final (15 min)

Preencha a ficha, em `_para-copiar/ficha-do-projeto-final.docx` (Word) ou `.md` (a coluna do meio é um exemplo preenchido: copie o jeito, não a tarefa), e crie no Claude **um projeto vazio**, só com o nome no formato:

```
<a sua tarefa> · <N>x/mês
```

**Deu certo se:** o nome aparece na sua lista de Projetos. Na parte 2, ele ganha uma pasta e um manual.
