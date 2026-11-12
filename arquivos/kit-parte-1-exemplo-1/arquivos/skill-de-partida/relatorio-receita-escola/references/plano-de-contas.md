# Plano de contas da receita dos cursos

Consulte este arquivo quando precisar saber o que uma coluna significa, como ela se relaciona com as outras, ou qual é a grafia oficial de uma unidade, curso ou mês. O passo a passo do `SKILL.md` não depende dele.

## As 16 colunas

| Coluna | O que é | Como se confere |
|---|---|---|
| `Curso` | o curso vendido | nome oficial, lista abaixo |
| `Modalidade` | Presencial, Online ou Híbrido | três valores, nada além |
| `Unidade` | onde a turma acontece | nome oficial, lista abaixo |
| `Mes` | o mês da receita, por extenso | `Janeiro` a `Dezembro`, com acento e inicial maiúscula |
| `Ano` | o ano da receita | número de 4 dígitos |
| `Turmas_Previstas` | turmas planejadas no mês | inteiro |
| `Turmas_Realizadas` | turmas que de fato rodaram | inteiro, normalmente igual ou menor que o previsto |
| `Alunos_Orcados` | alunos que o orçamento contava | inteiro |
| `Alunos_Matriculados` | alunos que de fato pagaram | inteiro |
| `Ticket_Medio_Orcado` | preço médio por aluno no orçamento, em R$ | — |
| `Ticket_Medio_Realizado` | preço médio cobrado de fato, em R$ | menor que o orçado = desconto ou bolsa |
| `Receita_Orcada` | a meta de receita, em R$ | **= Alunos_Orcados × Ticket_Medio_Orcado** |
| `Receita_Realizada` | o que entrou, em R$ | **= Alunos_Matriculados × Ticket_Medio_Realizado** |
| `Variacao_R$` | o desvio em reais | **= Receita_Realizada − Receita_Orcada** |
| `Variacao_Pct` | o desvio em % | **= Variacao_R$ ÷ Receita_Orcada × 100** |
| `Motivo_Desvio` | a explicação que a unidade registrou | texto livre; vazio em desvio grande é problema |

As três igualdades em negrito são a conferência da base. Linha em que elas não fecham tem erro de digitação, quase sempre um zero a mais ou a menos. Nesse caso, a conta de alunos × ticket é a fonte mais confiável, porque são dois números pequenos digitados em vez de um grande.

## Grafias oficiais

**Unidades:** Aldeota · Centro · Messejana · Sobral

**Cursos:** Excel Avançado · Gestão de Projetos · Liderança · MBA Executivo · Oratória · Power BI

**Meses:** Janeiro · Fevereiro · Março · Abril · Maio · Junho · Julho · Agosto · Setembro · Outubro · Novembro · Dezembro

Qualquer outra forma (`messejana `, `Marco`, `Power Bi`) é a mesma coisa escrita diferente: some com a forma oficial, nunca como item separado.

Se aparecer uma unidade ou curso fora dessas listas, **não é grafia: é item novo**. Pergunte antes de juntar.

## As duas partes do desvio

O desvio de receita de uma linha se divide em duas partes que somam o total:

| Parte | Conta | Responde |
|---|---|---|
| **Efeito volume** | (alunos matriculados − alunos orçados) × ticket orçado | quanto faltou porque vieram menos alunos |
| **Efeito preço** | (ticket realizado − ticket orçado) × alunos matriculados | quanto faltou porque cada aluno pagou menos |

Volume + preço = realizado − orçado, sempre que a receita fecha com alunos × ticket. É a análise de variação de preço e quantidade da contabilidade gerencial (Horngren, *Contabilidade de Custos*), aplicada à receita.

**Por que importa:** "a receita caiu 30%" pede ações diferentes conforme a causa. Se foi volume, o problema é captação, evasão ou turma cancelada. Se foi preço, o problema é desconto, bolsa ou tabela. O total sozinho não diz qual dos dois.

## Ano de referência e período comparável

O relatório olha o **acumulado do ano mais recente** da planilha. Se esse ano está incompleto (por exemplo, janeiro a setembro), a comparação com o ano anterior usa **os mesmos meses**, nunca o ano anterior inteiro.
