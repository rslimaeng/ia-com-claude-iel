---
name: fim-de-sessao
description: Encerra uma sessão de trabalho gravando onde paramos no 00-aqui-paramos.md da pasta, e diz se a próxima conversa pede /compact ou conversa nova. Use quando eu disser que vou parar, trocar de tarefa ou continuar outro dia, ou perguntar se devo compactar; ou quando a conversa estiver longa e o próximo passo for outra tarefa. Frases que ativam, mesmo sem a palavra skill - "vamos parar por aqui", "registra onde paramos", "atualiza o aqui paramos", "devo dar compact?", "abro conversa nova?", "amanhã eu continuo". Não use no meio de uma tarefa que vai continuar na mesma conversa.
---

# Fim de sessão

Baseada na skill de Rafael Lima, do curso IA com Claude (IEL Ceará).

O Claude não lembra da conversa de ontem. Quem lembra é o arquivo `00-aqui-paramos.md`, na pasta do trabalho. Esta skill deixa esse arquivo em dia no fim de cada sessão.

## 1 · Atualize o 00-aqui-paramos.md

Crie o arquivo se ele não existir. Escreva no topo a data de hoje e responda quatro perguntas, com frases curtas:

1. **O que foi decidido** nesta sessão: decisão, não a história da conversa.
2. **Onde estamos:** o que está pronto e o que ficou pela metade.
3. **O próximo passo:** a primeira coisa a fazer na próxima conversa, concreta.
4. **Em aberto:** o que depende de uma decisão minha.

Reescreva, não empilhe: o arquivo diz onde estamos **agora**, em no máximo 30 linhas. O que ficou velho ou já foi resolvido sai. Mostre o que vai gravar antes de gravar.

## 2 · Confira o CLAUDE.md da pasta

Se o `CLAUDE.md` da pasta não diz para ler o `00-aqui-paramos.md` no começo de cada conversa, proponha esta linha e espere o meu OK:

> No começo de cada conversa, leia o 00-aqui-paramos.md antes de qualquer pedido.

## 3 · Diga o que fazer na próxima conversa

| Situação | O que fazer |
|---|---|
| Mesma tarefa, conversa longa | `/compact`: a conversa encolhe e o trabalho continua |
| Mudou de tarefa | conversa nova: ela começa lendo o `00-aqui-paramos.md` |
| Vai continuar outro dia | conversa nova: retomar pelo arquivo é mais confiável que pela conversa antiga |

O critério é **mudar de tarefa**, não o tamanho da conversa.
