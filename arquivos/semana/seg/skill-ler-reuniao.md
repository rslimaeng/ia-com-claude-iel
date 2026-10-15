---
name: ler-reuniao
description: Lê a transcrição de uma reunião e escreve a nota de leitura antes de qualquer ata ou status - quem falou, o que foi dito, o que foi decidido, o que ficou pendente e o que não fecha. Use quando chegar uma transcrição em entrada/ ou quando eu pedir "lê essa reunião", "o que saiu da reunião", "faz a leitura".
---

# Ler reunião

Ler é uma tarefa; escrever a ata é outra, e vem depois. A nota de leitura existe para que o erro apareça aqui, onde custa uma frase, e não na ata que já circulou.

> Versão simplificada da skill leitura-de-fonte, de Rafael Lima, para o curso IA com Claude (IEL).

## 1 · Leia inteira antes de decidir o que importa

Do começo ao fim, sem resumir enquanto lê. Você ainda não sabe o que é importante.

## 2 · O resumo automático não é a reunião

Se a transcrição traz um resumo no topo (Copilot, Teams, Zoom), ele é **leitura de máquina**. A fonte é a fala. O resumo costuma:

- transformar **intenção em fato** ("vou ver" vira "vai entregar");
- transformar **proposta em decisão** ("pensei em duas turmas" vira "ficou decidido");
- dar **data** a algo que ninguém datou.

Tudo o que só existe no resumo vai para "O que não fecha".

## 3 · Quem falou

- Nome de pessoa sai da lista de pessoas da pasta. Pessoa nova vira pergunta para mim antes de entrar na lista.
- Rótulo sem nome ("Participante", "telefone") fica `[a confirmar]`, a não ser que outra reunião diga quem era. Nesse caso, diga qual.
- A mesma pessoa pode aparecer em grafias diferentes (apelido, nome com e sem "h"). Junte e avise.
- Nome citado dentro da fala identifica quem foi **mencionado**, não quem falou.

## 4 · A nota, nesta ordem

1. **Cobertura:** a reunião, a data, quantas falas e quem participou.
2. **Quem é quem:** cada participante com nome e função, e como você sabe.
3. **O que foi dito:** um título curto por tema, 2 a 4 bullets.
4. **Decisões:** só o que a sala fechou ("fica assim", "fechado", "fica decidido"). Proposta, intenção e "vou ver" **não são decisão**.
5. **Pendências:** ação, responsável e prazo. Prazo relativo vira data, com a conta ("até quarta", numa segunda 19/10 → 21/10). Responsável que não estava na sala, avise.
6. **O que não fecha:** número corrigido na fala (vale o último), o que o resumo diz e a fala não, divergência com o que a pasta já sabia.
7. **Para o status de sexta:** o que muda o estado do projeto.

## 5 · Pare e mostre

Grave a nota onde o manual da pasta manda guardar as leituras, com o nome da reunião e `--leitura` no fim. Depois mostre as decisões e as dúvidas, e **espere o meu OK** antes de escrever a ata. Dúvida vira pergunta de opção.
