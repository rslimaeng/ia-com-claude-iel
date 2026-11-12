---
name: relatorio-receita-escola
description: 'Monta o relatório mensal de receita da escola numa página HTML pronta: orçado × realizado por unidade e por curso, com o desvio separado em aluno a menos (volume) e preço a menos (ticket), a partir da planilha de receita do mês. Use sempre que pedirem o fechamento, o resultado ou o relatório de receita dos cursos, com ou sem a planilha anexada: sem ela, peça. Ative com falas como "monta o relatório do mês", "como fechou a receita", "fechamento mensal da escola", "resultado dos cursos", "qual unidade ficou abaixo do orçado", "por que a receita caiu", "orçado contra realizado", "relatório de receita para a diretoria", "quanto faltou para bater a meta". Ative mesmo que a pessoa não fale em planilha nem em orçamento: o gatilho é querer saber como a receita dos cursos fechou. Não use para planilha que não é de receita da escola, como a de execução de convênio, nem para post ou texto de divulgação dos cursos.'
---

# Relatório mensal de receita da escola

Você recebe a planilha de receita dos cursos → devolve, sem parar no meio, **o relatório pronto num arquivo HTML de uma página** que a diretoria lê em dois minutos: onde a receita ficou abaixo do orçado, se faltou aluno ou faltou preço, e o que fazer, com dono e prazo. Esta skill **não** corrige a base sem declarar o que corrigiu, não faz previsão de fechamento do ano, não lê planilha de outro assunto (a de execução de convênio, por exemplo) e não afirma causa que a planilha não mostra.

## Input: o que pedir

**Necessário:** a planilha de receita (`.xlsx` ou `.csv`), com as colunas descritas em `references/plano-de-contas.md`. Se ela não veio, peça e pare. Não monte relatório com número que a pessoa disse de cabeça.

**Não pare para perguntar.** A pessoa quer o relatório pronto. O que a planilha responde (o período, as unidades, os cursos, o ano de referência), você assume: o acumulado do ano mais recente. Se a pessoa citou um mês que não existe na planilha, use o período mais recente e diga isso na primeira frase da conclusão.

**Pare só em dois casos:** a planilha não veio, ou faltam colunas obrigatórias (o script avisa). No segundo, a planilha não é esta: diga o que falta e pare.

## Método: como fazer

O método é a **análise de variação orçado × realizado** da contabilidade gerencial (Horngren, *Contabilidade de Custos*): o desvio de receita se divide em **efeito volume** (alunos) e **efeito preço** (ticket), e os dois somam o total. Para escolher o que vai para a página, o **princípio de Pareto** (Juran): poucos pares curso × unidade costumam concentrar a maior parte da queda. Para escrever, a **pirâmide de Minto**: conclusão primeiro, evidência depois.

### 1. Raio-X da base, antes de qualquer conta

Rode o script **sem** tratar nada:

```bash
python3 scripts/somar_orcado_realizado.py <arquivo>
```

Ele devolve o inventário (linhas, colunas, anos, valores de cada coluna de texto) e quatro tipos de problema: linha 100% repetida, grafia diferente da mesma coisa (`messejana `, `Marco`), motivo vazio em desvio de 15% ou mais, e receita que não fecha com alunos × ticket.

**Nunca pule esta etapa.** Duas receitas com um zero a mais mudam o ano em mais de um milhão, e o total parece plausível.

### 2. Trate com o padrão, e declare

Aplique o tratamento padrão, sem perguntar:

| Problema | Tratamento padrão |
|---|---|
| linha repetida | fica uma |
| grafia diferente | vira a forma oficial (`references/plano-de-contas.md`) |
| receita que não fecha | passa a valer alunos × ticket, porque são dois números pequenos digitados em vez de um grande |
| motivo vazio | fica vazio; no relatório, aparece como "sem motivo registrado" |

O script faz isso no passo 3 e escreve no rodapé do relatório o que foi tratado. Na seção "A confirmar", diga em uma linha o tratamento que mais mexe no número (na planilha de exemplo, as duas receitas com um zero a mais). **Tratar sem declarar é o erro; tratar declarando é o trabalho.**

Se aparecer um problema que o padrão não cobre (uma unidade ou um curso fora da lista do plano de contas), não junte nada: some como item separado e registre em "A confirmar".

### 3. Os números, já no HTML

```bash
python3 scripts/somar_orcado_realizado.py <arquivo> --html relatorio-receita-<periodo>.html [--ano AAAA]
```

O script trata a base, calcula tudo e escreve o arquivo a partir de `templates/relatorio.html`, com o título, os cinco indicadores, as tabelas por unidade e por curso e o rodapé já preenchidos. **Os números do relatório são os do script; você não digita número de tabela.**

Leia a saída do script de cima para baixo: o ano, as unidades, os cursos, e por fim os pares curso × unidade. Em cada nível, responda quatro perguntas:

- **Está concentrado?** Use o acumulado da última tabela: quantos pares fazem 80% da queda. Se uma unidade aparece em todos os cursos, o problema é a unidade, não o curso.
- **Volume ou preço?** A coluna que pesa mais diz onde agir: volume é captação, evasão ou turma cancelada; preço é desconto, bolsa ou tabela.
- **Desde quando?** Quantos meses abaixo do orçado, e como a mesma unidade estava no ano anterior, **nos mesmos meses**. Uma queda que começou neste ano é diferente de uma que sempre existiu.
- **O que a planilha diz?** O motivo mais registrado. Motivo é o que a unidade escreveu, não causa comprovada.

Traga também **o maior desvio positivo**: o que deu certo é parte do fechamento.

Se não houver execução de código, faça as mesmas somas à mão, pelas igualdades do plano de contas, preencha o template você mesmo e diga na seção "A confirmar" que as contas foram feitas sem o script.

### 4. Os textos, e a entrega

No arquivo que o script escreveu, sobram quatro marcadores. Substitua cada um:

| Marcador | O que vai | Forma |
|---|---|---|
| `{{CONCLUSAO}}` | a conclusão, em até 3 linhas: quanto, onde, volume ou preço, desde quando | texto corrido |
| `{{PONTOS}}` | os 3 pontos de atenção: os 2 maiores desvios negativos e o maior positivo | `<ol class="pontos"><li>…</li></ol>` |
| `{{RECOMENDACOES}}` | 3 recomendações, uma por ponto | `<table class="texto">` com O quê · Dono · Prazo · O número que confere |
| `{{A_CONFIRMAR}}` | toda hipótese, e o tratamento que mais mexeu no número | `<ul><li>…</li></ul>` |

Confira que não sobrou nenhum `{{` no arquivo. Entregue **o arquivo HTML**, como arquivo para baixar ou como artefato, o que o ambiente oferecer. Na conversa, escreva só a conclusão e onde está o arquivo.

Cada recomendação nasce de um ponto de atenção e tem **dono, prazo e um número que dá para conferir no mês seguinte**. Se você não consegue dizer qual número vai mostrar que deu certo, a recomendação ainda é genérica.

## Formato de saída

Um arquivo `.html`, a partir de `templates/relatorio.html`, que abre no navegador e imprime numa folha A4. As regras de forma:

- **Uma página.** As tabelas em R$ mil, vindas do script; no texto, o valor exato quando é citado.
- **Não mude o layout nem o estilo do template.** Só os quatro marcadores de texto são seus.
- **Cada número diz de onde saiu:** unidade, curso e período.
- **Hipótese só em "A confirmar"**, nunca na conclusão.
- Sem jargão de programação e sem nome de ferramenta: quem lê é a diretoria.
- O rodapé é do script: o arquivo, o número de linhas, o período e o tratamento aplicado.

Nunca cole a saída do script na resposta, nem o relatório inteiro no chat. A saída é matéria-prima; a entrega é o arquivo.

## Barra de qualidade

Entrega excelente responde em três linhas o que a diretoria perguntaria: quanto, onde e por quê, com a causa separada em volume e preço. Ela compara o período certo, mostra o positivo junto com o negativo e termina com ações que dá para cobrar.

**Exemplo de entrega excelente** (a planilha fictícia da prática, Escola Aurora, com os números saídos do script):

> **Receita dos cursos · janeiro a setembro de 2026**
>
> **A receita ficou R$ 2,57 milhões abaixo do orçado (−11,3%), e dois terços disso vêm de uma unidade só: Messejana, com −R$ 1,73 milhão (−30,5%). Lá faltou aluno, não preço: R$ 1,66 milhão do desvio é volume. Nos mesmos meses de 2025, Messejana estava em −7,6%: a queda é deste ano.**
>
> **Pontos de atenção**
> 1. **MBA Executivo · Messejana:** −R$ 1.116.000 (−34,4%), abaixo do orçado nos 9 meses. Sozinho, é 38% da queda do ano. O motivo mais registrado é "Cancelamentos por questões financeiras dos alunos".
> 2. **Os outros cursos de Messejana:** Liderança, Gestão de Projetos, Excel Avançado e Oratória, todos entre −28,6% e −29,8% e abaixo do orçado nos 9 meses. Não é um curso: é a unidade.
> 3. **Power BI, o único acima do orçado:** +R$ 372.030 (+28,7%), puxado por Aldeota, Centro e Sobral (+37% a +38%), todo por volume. O motivo mais registrado é "Parceria com empresa local".
>
> **A confirmar:** se os cancelamentos de Messejana explicam a queda dos outros cursos, porque a planilha registra motivos diferentes em cada um. Duas receitas de outubro de 2025 tinham um zero a mais e foram recalculadas por alunos × ticket; o tratamento completo está no rodapé.

## Anti-padrões

**Nunca trate a base sem declarar**, porque quem assina o relatório precisa saber que dois números foram trocados: o rodapé e a seção "A confirmar" dizem o quê. Sem tratar, as duas receitas com um zero a mais da planilha de exemplo inflam 2025 em R$ 1,1 milhão.

**Nunca pare no total**, porque "a receita caiu 11%" é o que qualquer pessoa vê na planilha. O relatório existe para dizer onde e por quê.

**Nunca entregue o desvio sem separar volume e preço**, porque as duas causas pedem ações opostas: captar mais aluno ou rever desconto.

**Nunca compare um ano incompleto com o ano anterior inteiro**, porque nove meses contra doze fabricam uma queda que não existe.

**Nunca escreva o motivo registrado como causa comprovada**, porque ele é o que a unidade anotou. A causa que a planilha não mostra vai para "A confirmar".

**Nunca digite à mão um número que o script já calculou**, porque é ali que o relatório erra sem ninguém ver: a tabela vem do script, o texto cita a tabela.

**Nunca escreva recomendação sem dono, prazo e número**, porque "melhorar a captação em Messejana" não se cobra no mês seguinte.

**Mesmo pedido, saída ruim × saída boa:**

> ❌ *Ruim:* "A receita de 2026 está abaixo do orçado em 11,3%. A unidade Messejana teve o pior desempenho, provavelmente por causa da crise econômica. Recomendo intensificar o marketing e melhorar a retenção de alunos."
>
> Por que é ruim: não diz quanto de Messejana é aluno e quanto é preço; chama de causa uma hipótese ("crise econômica"); não compara com os mesmos meses de 2025; esquece o Power BI; e as recomendações não têm dono, prazo nem número.
>
> ✅ *Boa:* o exemplo da Barra de qualidade.

## Limites

Esta skill lê **uma** planilha: a de receita dos cursos, no formato do plano de contas. Planilha de outro assunto, como a de execução de convênio, não é dela: diga isso e pare, em vez de adaptar.

Ela compara orçado com realizado. **Não** faz previsão de fechamento do ano, não olha caixa nem inadimplência, e não substitui a contabilidade da escola.

O motivo do desvio vem do que a unidade registrou. A skill não confere se é verdade: aponta onde a pergunta deve ser feita.

O script precisa de execução de código. Sem ela, as contas são feitas à mão, conferíveis pelas igualdades do plano de contas, e o relatório avisa isso.

Para o significado de cada coluna, as grafias oficiais e a conta de volume e preço, consulte `references/plano-de-contas.md`.

## Base

- **Análise de variação orçado × realizado, com a separação em preço e quantidade:** contabilidade gerencial; Charles T. Horngren, *Contabilidade de Custos*. Método público, fora de qualquer leitura feita para este curso.
- **Princípio de Pareto:** Vilfredo Pareto, levado à gestão da qualidade por Joseph M. Juran.
- **Conclusão primeiro, evidência depois:** Barbara Minto, *O Princípio da Pirâmide*.
- **O formato do relatório e as regras de número com origem e hipótese em "A confirmar":** a conversa da prática 4a do curso *IA com Claude · Do Zero à Produtividade Total*.
