---
name: gerar-status
description: Gera o status report semanal de um empreendimento do PMO a partir da ata aprovada, do registro de decisões e da ficha. Use quando o Sérgio pedir "faz o status", "status da semana", "como está o empreendimento X" ou numa sexta, depois das atas aprovadas.
---

# Gerar status

> Gabarito do treinamento. A sua skill nasce do trabalho que você fez na Prática 6;
> compare com esta depois de embalar a sua.

## Antes de começar

1. Leia as atas da semana em `atas/aprovadas/`. **Ata em validação não entra**: ainda não vale.
2. Leia o `registro-de-decisoes.md` e a ficha do empreendimento em `empreendimentos/`.

## O que o status tem, nesta ordem

1. **Em uma linha:** o estado real do empreendimento. Não "a semana foi produtiva": o que andou ou o que travou.
2. **O que andou:** com a decisão ou a ficha de onde veio.
3. **Em andamento:** tabela com frente, situação, responsável e prazo em data.
4. **Sem dono ou sem prazo:** cada ação que a reunião deixou solta. Sugira travar a data, sem inventar uma.
5. **Riscos e tensões:** o que trava o quê. Procure três coisas: a cadeia de dependências, a ação sem prazo e o prazo que já escorregou antes.
6. **Plano de ação:** ação, responsável, prazo e de onde veio.

## Regras

- **Discutido não é decidido.** Proposta não entra em "o que andou".
- **Não invente dono nem prazo.** O que a reunião não disse fica "não definido".
- Nome de pessoa só da `pessoas.md`, como na ata.

## Onde gravar

`relatorios/status/<aaaa-mm-dd>_STATUS_<Nome>.md`, com a data da sexta.

## Depois de gravar

1. Atualize o `00-aqui-paramos.md`: status gerado, esperando validação.
2. Mostre ao Sérgio. **O status só circula com o OK dele.**
