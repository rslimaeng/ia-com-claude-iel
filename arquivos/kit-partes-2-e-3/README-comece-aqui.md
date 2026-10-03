# Comece aqui · pasta de prática do PMO

**IA com Claude · Do Zero à Produtividade Total** · R. Lima · IEL Ceará · partes 2 e 3

> ⚠️ **Tudo nesta pasta é fictício, para treinamento**: a empresa (Horizonte), o empreendimento, as pessoas, os números e a reunião.
> Depois do curso, esta mesma estrutura pode receber as suas reuniões reais.

**Noite 2:** a pergunta-teste e as práticas 1, 2 e 3. **Noite 3:** as práticas 4, 5 e 6.

## Como abrir

1. Abra o app **Claude** no computador e entre na aba **Code**.
2. Escolha **esta pasta** (`pmo-horizonte`) como pasta de trabalho.
3. Escreva na caixa de mensagem. Cada prática abaixo tem a frase para colar.

**O app vai pedir permissão** algumas vezes: para abrir um link, para gravar um arquivo, para gravar fora desta pasta. É normal. Leia o que ele quer fazer e aprove.

**"Conversa nova"** é uma sessão nova, na mesma pasta. Ela importa porque o Claude lê o CLAUDE.md **quando a conversa começa**: o que você grava no meio da conversa só vale na próxima.

## As seis práticas

### Antes de tudo · a pergunta-teste

Esta pergunta volta três vezes. Ela mostra o que muda quando o Claude passa a ler os seus arquivos:

> Vou preparar a ata de uma reunião. Em 5 linhas: como você vai trabalhar comigo e o que precisa de mim? Depois, copie esta resposta para antes-e-depois.md, no primeiro momento vazio.

## Noite 2 · O Claude que trabalha numa pasta

### Prática 1 · O seu CLAUDE.md global

1. Cole a **pergunta-teste**. É o momento 1: ainda não existe nenhum CLAUDE.md.
2. Cole o prompt da entrevista (está também em `_para-copiar/prompt-claude-md-global.md`):

> Quero criar o meu CLAUDE.md global, que você lê em toda conversa. Use como base https://raw.githubusercontent.com/multica-ai/andrej-karpathy-skills/main/CLAUDE.md (se o link não abrir, use _para-copiar/base-karpathy.md): ele foi escrito para quem programa, então traduza os 4 princípios para o meu trabalho. Nada sobre esta pasta nem sobre o PMO: isso vai no manual da pasta. Se ~/.claude/CLAUDE.md já existir, não apague: proponha o que acrescentar. Me entreviste com perguntas de opção, no máximo 4 por rodada, seguindo _para-copiar/perfil-do-usuario.md. Me mostre a v1, com até 40 linhas, antes de gravar em ~/.claude/CLAUDE.md.

3. Escolha as opções. Leia a v1 e corrija o que não soar como você antes de aprovar.
4. Veja o arquivo que nasceu. Cole:

> Me mostre o meu CLAUDE.md global inteiro.

5. **Conversa nova** e a pergunta-teste de novo: momento 2.
6. Escolha **uma** coisa da resposta que não é do seu jeito e cole, trocando o colchete:

> Na resposta da pergunta-teste, [o que não é do meu jeito]. Acrescente uma linha no meu CLAUDE.md global para isso não voltar. Me mostre a linha antes de gravar.

7. **Conversa nova** e a pergunta-teste: momento 2b. Uma linha a mais no arquivo, e a resposta muda.

**O que esperar:** duas ou três rodadas de perguntas com opções e uma v1 curta. No momento 2 a resposta já fala do seu jeito; no 2b, a sua correção aparece sem você pedir de novo.

**Confira:** a v1 tem até 40 linhas e não cita PMO, Horizonte nem as pastas daqui. Isso é do manual da pasta, não seu.

**Se a v1 vier genérica, diga:** *"isso serve para qualquer pessoa; me pergunte mais sobre como eu gosto de receber as coisas"* ou *"tire a linha sobre X, ela não muda nada no meu trabalho"*.

### Prática 2 · A pasta, explicada pelo Claude

**Conversa nova** e cole:

> Sem mudar nada e sem abrir _gabarito/, me explique esta pasta como se eu tivesse chegado hoje: numa tabela, para que serve cada pasta e arquivo e quem escreve em cada um; depois, o que muda quando uma ata sai de em-validacao/ e vai para aprovadas/. No fim, até 5 coisas que você não conseguiu entender só olhando.

Guarde a lista do fim: é o que o manual da pasta vai precisar dizer.

**Agora no seu (5 min):** crie, no seu computador, uma pasta para a tarefa da sua ficha do projeto final, com 2 ou 3 arquivos reais (ou fictícios) dela. Abra essa pasta na aba Code e cole o mesmo pedido acima.

**O que esperar:** uma tabela com cada pasta e quem escreve nela. No fim, dúvidas como "quem move a ata para aprovadas?" e "o que acontece com a ata reprovada?". Ele não sabe porque ninguém escreveu ainda.

### Prática 3 · O manual desta pasta, e a memória

Cole:

> Agora o CLAUDE.md desta pasta. Leia o meu CLAUDE.md global e olhe as pastas daqui. Me entreviste com perguntas de opção, no máximo 4 por rodada, e escreva o manual com: o seu papel aqui, o mapa das pastas e as regras que não mudam. Inclua que você lê o 00-aqui-paramos.md no começo de toda conversa. Não repita o que já está no global. Me mostre antes de gravar em CLAUDE.md.

Veja o manual que nasceu. Cole:

> Me mostre o CLAUDE.md desta pasta inteiro.

É o manual, lido em toda conversa aqui. Depois, **conversa nova** e a pergunta-teste: momento 3.

Por fim, outra **conversa nova**, e só:

> Onde paramos e qual é o próximo passo?

**O que esperar:** no momento 3 ele se apresenta como analista do PMO, cita as pastas e diz que você valida. Na última pergunta, ele responde o próximo passo escrito no `00-aqui-paramos.md`: a conversa é nova, quem lembrou foi o arquivo. O `_gabarito/CLAUDE-da-pasta.md` tem um manual pronto para comparar.

**Confira:** o manual tem a linha do `00-aqui-paramos.md` e não repete nenhuma regra do seu global. Regra repetida não reforça: dilui.

**Agora no seu (10 min):** na pasta da sua tarefa, cole o mesmo pedido do manual. O seu global já existe: o manual só diz o que é daqui.

**Se vier repetido ou vago, diga:** *"a regra X já está no meu global, tire daqui"* ou *"no mapa das pastas, diga quem escreve em cada uma"*.

## Noite 3 · O procedimento que fica

### Prática 4 · Uma skill emprestada: desenhar o fluxo

A skill `diagram-design` (de Cathryn Lavery, licença MIT) está em `_para-copiar/skills/`. Cole:

> Instale a skill que está em _para-copiar/skills/diagram-design: copie a pasta inteira para .claude/skills/diagram-design, sem mudar nada dentro dela. Ela vai valer só nesta pasta.

Gravar dentro de `.claude/` pede uma aprovação a mais: aprove. Depois, **conversa nova** e cole:

> Use a skill diagram-design para desenhar o fluxo da ata desta pasta, da gravação à ata aprovada, mostrando quem faz cada etapa. Leia o manual e as pastas antes. Me diga qual tipo de desenho escolheu e por quê, e grave em fluxos/fluxo-da-ata.html.

Abra o arquivo de `fluxos/` no navegador. Depois, cole:

> Agora o mesmo fluxo como um slide 16:9, para eu mostrar à diretoria. Grave em fluxos/fluxo-da-ata--slide.html.

**O que esperar:** alguns minutos de trabalho (no teste, 11). Sai um desenho em raias, com o gravador, o Claude e você, e os dois pontos em que você aprova. Ele diz por que escolheu esse tipo. Se a skill perguntar pelas cores, por hoje mantenha o padrão.

**Global ou local:** a skill instalada assim vale só nesta pasta, como o manual. Para valer em toda pasta, como o seu CLAUDE.md global, peça para copiá-la para `~/.claude/skills/`.

**Agora no seu (5 min):** faça a skill valer em toda pasta. Cole:

> Copie a skill .claude/skills/diagram-design desta pasta para ~/.claude/skills/diagram-design, sem mudar nada dentro dela.

Depois, na aba Code, abra a pasta da sua tarefa e, numa **conversa nova**, cole:

> Use a skill diagram-design para desenhar o fluxo da minha tarefa, do começo à entrega, mostrando quem faz cada etapa. Grave em fluxo-da-tarefa.html.

### Prática 5a · Ler a reunião

Cole:

> Leia inteira a transcrição reunioes/brutas/2026-09-29-comite-residencial-alvorada.md. Escreva uma nota de leitura com: quem é quem (e como você sabe), o que foi dito por tema, as decisões que a sala fechou, e o que não fecha. Não invente nome nem data: o que faltar vira [a confirmar]. Grave em reunioes/leituras/ e me mostre as decisões antes de seguir.

**O que esperar:** uma nota com 5 falantes, 4 decisões e uma lista de pontos que não fecham.

**Confira:** a reunião tem **seis armadilhas** de propósito. Quantas a nota pegou?

### Prática 5b · A ata, e depois as suas skills

Cole:

> Com a nota aprovada, gere a ata no modelo de atas/modelo/modelo-ata.md. Grave em atas/em-validacao/, acrescente as decisões ao registro-de-decisoes.md e atualize o 00-aqui-paramos.md.

**Revise a ata como revisaria a de um analista.** Peça as correções em frases normais.

Quando estiver bom, cole:

> Transforme o que fizemos hoje, a leitura e a ata, com as correções que eu pedi, em duas skills: ler-transcricao e gerar-ata, em .claude/skills/. Me mostre antes de gravar.

Gravar em `.claude/skills/` pede a mesma aprovação da Prática 4.

**Teste:** abra uma conversa nova e diga só *"gera a ata da reunião de 29/09"*.

### Prática 6 · O status report, e a skill dele

A ata conta a reunião. O status conta o empreendimento: o que andou, o que trava o quê e o que ficou sem dono. Primeiro, aprove a ata. Cole:

> Aprovo a ata de 29/09. Mova para atas/aprovadas/ e atualize o 00-aqui-paramos.md.

Depois, cole:

> Faça o status report do Residencial Alvorada como se hoje fosse sexta, 02/10/2026, a partir da ata aprovada, do registro-de-decisoes.md e da ficha do empreendimento. Na primeira linha, o estado real em uma frase. Depois: o que andou, o que está em andamento e o que ficou sem dono ou sem prazo. O plano de ação numa tabela: ação, responsável, prazo e de onde veio. Não invente dono nem prazo: o que faltar fica "não definido". Grave em relatorios/status/ e me mostre antes de seguir.

**Revise o status como revisaria o de um analista.** Peça as correções em frases normais. Quando estiver bom, cole:

> Transforme o status report, com as correções que eu pedi, numa skill gerar-status, em .claude/skills/. Me mostre antes de gravar.

**Teste:** abra uma conversa nova e diga só *"faz o status do Alvorada desta semana"*.

**O que esperar:** uma frase no topo com o estado real, não "a reunião foi produtiva". A área verde esperando a viabilidade, que vence no próprio dia 02/10.

**Confira:** três coisas que um status pega e um resumo não pega.
1. **A cadeia:** viabilidade → área verde → aprovação → registro → lançamento.
2. **A ação sem prazo:** o cronograma do estudo de fauna.
3. **O prazo que já escorregou:** os números de vendas chegaram no dia 12 no mês passado.

**Se vier um resumo da ata, diga:** *"isso é a ata de novo; quero o estado do empreendimento e o que trava o quê"*.

**Agora no seu (10 min):** escolha um passo da tarefa da sua ficha que se repete. Faça esse passo uma vez com o Claude, na pasta da sua tarefa, corrigindo até ficar do seu jeito. Depois, cole:

> Transforme o que fizemos, com as correções que eu pedi, numa skill em .claude/skills/. Me mostre antes de gravar.

**Deu certo se:** numa conversa nova, um pedido curto abre a sua skill sem você explicar de novo.

## Gabarito

A pasta `_gabarito/` tem um manual da pasta, uma nota, uma ata, um status report e três skills prontas. **Abra só depois de fazer.**
O seu vai ser diferente do meu, e tudo bem. Compare a estrutura, não as palavras.
