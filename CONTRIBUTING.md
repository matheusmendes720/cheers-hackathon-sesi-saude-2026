# Como contribuir

Este repositório é o **kit de mapeamento** da equipe **Cheers** para o Hackathon+ SESI Saúde 2026 (SESI Bahia + Grupo Rede+, Salvador, 14–15/11/2026). Ele existe para que o time consiga absorver o desafio revelado em 13/11 em 90 minutos — e para registrar a evidência que sustenta a proposta.

**Leia antes de mexer:** [`README.md`](README.md) (entrada do time) e [`docs/README.md`](docs/README.md) (mapa da documentação).

---

## As 6 regras do repositório

1. **Toda afirmação carrega uma marca.** `[fato]` verificável, com link e data · `[hipótese]` leitura nossa, sujeita a teste · `[a confirmar]` depende da organização · `§N` vem do regulamento. **Nunca chute número clínico nem estatística de mercado.**
2. **Toda referência a ODS é ODS 3 + ODS 9.** "Saúde e Bem-Estar" é o **ODS 3** na Agenda 2030 (o SESI rotulou "ODS 2" na comunicação oficial — é erro de numeração deles). Escreva *Saúde e Bem-Estar (ODS 3 na Agenda 2030)*.
3. **Não prometa economia, ROI nem % de redução de absenteísmo.** Em ensaio randomizado (n = 32.974) o ROI é **−49%**. A proposta **mede**; não promete.
4. **Não escreva "manutenção preditiva".** O Anexo I do desafio rejeita "incorporação de novas tecnologias" como resposta.
5. **Não propague os erros do grupo.** A lista viva está em [`AGENTS.md`](AGENTS.md) → *Correções pendentes*.
6. **Varra caracteres não latinos antes de commitar.** Um glifo colado no meio de uma palavra em português já passou por aqui mais de uma vez — e ninguém vê no diff. O regex está no checklist do PR.

---

## Fluxo de trabalho

**Um tema por commit. Conventional Commits, assunto e corpo em português do Brasil, sem acentos.**

```
docs: adiciona a grade das 4 dimensoes do Anexo I
fix: inverte o sinal do indicador de 65,6%
pitch: ajusta o bloco de viabilidade do roteiro de 3 min
```

Prefixos aceitos: `docs` · `fix` · `feat` · `pitch` · `data` · `chore` · `refactor` · `test` · `perf` · `build` · `ci`.

**Branches.** `main` é o que está no ar e deve estar sempre verde. Para trabalho novo:

```
git switch -c feat/mapa-de-build
```

**Pull request.** Toda mudança passa por PR — nenhum commit direto na `main`. O template está em [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md).

**Commitsconventional.** Corpo explaining *por quê*, não *o quê* — o diff já mostra o quê. Sem acentos, porque a comparação de strings e os greps do time funcionam melhor assim.

---

## O que entra e o que não entra

| Entra | Não entra |
|---|---|
| Pesquisa com fonte (link + data + página) | Número sem fonte |
| Decisão de time, com responsável e prazo | Conclusão sem o trecho que a sustenta |
| Correção de erro factual | Exemplo de ferramenta sem o que sustenta |
| Texto do formulário, o roteiro, o plano | Dado pessoal de trabalhador, ATESTADO, ASO, eSocial individualizado |

**Dados de trabalhador são sensíveis (LGPD art. 11).** Nada de dado individual entra no repositório — nem em exemplo, nem em print. O protótipo agrega com **k ≥ 10** por posto.

---

## Antes de abrir o PR

- [ ] Toda afirmação nova tem marca de evidência (`[fato]`, `[hipótese]`, `[a confirmar]`, `§N`).
- [ ] Todo número tem fonte (link, data, página/tabela).
- [ ] Nenhuma promessa de economia, ROI ou % de absenteísmo.
- [ ] Nenhuma ocorrência de "manutenção preditiva" como tese, nem "ODS 2" para saúde.
- [ ] Varredura de não-latinos rodada (item 6 acima).
- [ ] Se tocou `AGENTS.md`, atualizou também o contador de correções pendentes.
- [ ] Links quebrados conferidos.

---

## Dúvidas

Fale no grupo do time. Para dúvidas de **regulamento**, a fonte de verdade é o PDF na raiz — não a página de marketing, não o export do WhatsApp. Quando o regulamento e o grupo divergirem, o regulamento vence.
