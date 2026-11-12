---
name: relatorio-receita-escola
description: 'Monta o relatório mensal de receita da escola em uma página: orçado × realizado por unidade e por curso, com o desvio separado em aluno a menos (volume) e preço a menos (ticket), a partir da planilha de receita do mês. Use sempre que pedirem o fechamento, o resultado ou o relatório de receita dos cursos, com ou sem a planilha anexada: sem ela, peça. Ative com falas como "monta o relatório do mês", "como fechou a receita", "fechamento mensal da escola", "resultado dos cursos", "qual unidade ficou abaixo do orçado", "por que a receita caiu", "orçado contra realizado", "relatório de receita para a diretoria", "quanto faltou para bater a meta". Ative mesmo que a pessoa não fale em planilha nem em orçamento: o gatilho é querer saber como a receita dos cursos fechou. Não use para planilha que não é de receita da escola, como a de execução de convênio, nem para post ou texto de divulgação dos cursos.'
---

# Relatório mensal de receita da escola

Você recebe a planilha de receita dos cursos → devolve o relatório de uma página que a diretoria lê em dois minutos: onde a receita ficou abaixo do orçado, se faltou aluno ou faltou preço, e o que fazer, com dono e prazo. Esta skill **não** corrige a base sem perguntar, não faz previsão de fechamento do ano, não lê planilha de outro assunto (a de execução de convênio, por exemplo) e não afirma causa que a planilha não mostra.

## Input: o que pedir

**Necessário:** a planilha de receita (`.xlsx` ou `.csv`), com as colunas descritas em `references/plano-de-contas.md`. Se ela não veio, peça e pare. Não monte relatório com número que a pessoa disse de cabeça.

**Não pergunte** o que a planilha responde: o período, as unidades, os cursos, o ano de referência. Assuma o acumulado do ano mais recente e diga isso na primeira linha.

**Pergunte só quando a resposta muda o relatório:**
- a pessoa citou um mês ou uma unidade que não existe na planilha;
- faltam colunas obrigatórias (o script avisa). Nesse caso a planilha não é esta: diga o que falta e pare.

## Método: como fazer

O método é a **análise de variação orçado × realizado** da contabilidade gerencial (Horngren, *Contabilidade de Custos*): o desvio de receita se divide em **efeito volume** (alunos) e **efeito preço** (ticket), e os dois somam o total. Para escolher o que vai para a página, o **princípio de Pareto** (Juran): poucos pares curso × unidade costumam concentrar a maior parte da queda. Para escrever, a **pirâmide de Minto**: conclusão primeiro, evidência depois.

### 1. Raio-X da base, antes de qualquer conta

Rode o script **sem** tratar nada:

```bash
python3 scripts/somar_orcado_realizado.py <arquivo>
```

Ele devolve o inventário (linhas, colunas, anos, valores de cada coluna de texto) e quatro tipos de problema: linha 100% repetida, grafia diferente da mesma coisa (`messejana `, `Marco`), motivo vazio em desvio de 15% ou mais, e receita que não fecha com alunos × ticket.

**Nunca pule esta etapa.** Duas receitas com um zero a mais mudam o ano em mais de um milhão, e o total parece plausível.

### 2. Pergunte antes de tratar

Mostre os problemas numa lista curta, cada um com o tratamento que você propõe:

| Problema | Tratamento padrão |
|---|---|
| linha repetida | fica uma |
| grafia diferente | vira a forma oficial (`references/plano-de-contas.md`) |
| receita que não fecha | passa a valer alunos × ticket, porque são dois números pequenos digitados em vez de um grande |
| motivo vazio | fica vazio; no relatório, aparece como "sem motivo registrado" |

Pergunte uma vez: "Trato assim, ou algum item é diferente?". **Não corrija nada sozinho.** Se a pessoa aprovar, siga para o passo 3.

### 3. Os números

```bash
python3 scripts/somar_orcado_realizado.py <arquivo> --tratar [--ano AAAA]
```

Leia o resultado de cima para baixo: o ano, as unidades, os cursos, e por fim os pares curso × unidade. Em cada nível, responda quatro perguntas:

- **Está concentrado?** Use o acumulado da última tabela: quantos pares fazem 80% da queda. Se uma unidade aparece em todos os cursos, o problema é a unidade, não o curso.
- **Volume ou preço?** A coluna que pesa mais diz onde agir: volume é captação, evasão ou turma cancelada; preço é desconto, bolsa ou tabela.
- **Desde quando?** Quantos meses abaixo do orçado, e como a mesma unidade estava no ano anterior, **nos mesmos meses**. Uma queda que começou neste ano é diferente de uma que sempre existiu.
- **O que a planilha diz?** O motivo mais registrado. Motivo é o que a unidade escreveu, não causa comprovada.

Traga também **o maior desvio positivo**: o que deu certo é parte do fechamento.

Se não houver execução de código, faça as mesmas somas à mão, pelas igualdades do plano de contas, e diga na seção "A confirmar" que as contas foram feitas sem o script.

### 4. O relatório

Monte a página com `templates/relatorio.md`, nesta ordem: a conclusão em até 3 linhas, a tabela do ano por unidade, os 3 pontos de atenção, as 3 recomendações e a seção "A confirmar".

Cada recomendação nasce de um ponto de atenção e tem **dono, prazo e um número que dá para conferir no mês seguinte**. Se você não consegue dizer qual número vai mostrar que deu certo, a recomendação ainda é genérica.

## Formato de saída

A página de `templates/relatorio.md`, preenchida. As regras de forma:

- **Uma página.** A tabela em R$ mil; no texto, o valor exato quando é citado.
- **Cada número diz de onde saiu:** unidade, curso e período.
- **Hipótese só em "A confirmar"**, nunca na conclusão.
- Sem jargão de programação e sem nome de ferramenta: quem lê é a diretoria.
- No rodapé, o arquivo, o número de linhas, o período e o tratamento aprovado no passo 2.

Nunca cole a saída do script na resposta. Ela é matéria-prima, não entrega.

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
> **A confirmar:** se os cancelamentos de Messejana explicam a queda dos outros cursos, porque a planilha registra motivos diferentes em cada um. Duas receitas de outubro de 2025 tinham um zero a mais e foram recalculadas por alunos × ticket, com a aprovação de quem pediu.

## Anti-padrões

**Nunca trate a base sem perguntar**, porque quem assina o relatório precisa saber que dois números foram trocados. Sem tratar, as duas receitas com um zero a mais da planilha de exemplo inflam 2025 em R$ 1,1 milhão.

**Nunca pare no total**, porque "a receita caiu 11%" é o que qualquer pessoa vê na planilha. O relatório existe para dizer onde e por quê.

**Nunca entregue o desvio sem separar volume e preço**, porque as duas causas pedem ações opostas: captar mais aluno ou rever desconto.

**Nunca compare um ano incompleto com o ano anterior inteiro**, porque nove meses contra doze fabricam uma queda que não existe.

**Nunca escreva o motivo registrado como causa comprovada**, porque ele é o que a unidade anotou. A causa que a planilha não mostra vai para "A confirmar".

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
