## O que muda

<!-- Uma linha. O que este PR muda e por quê. -->

## Por que

<!-- A razão, não a descrição. O diff já mostra o que mudou. -->

## Tipo

- [ ] `docs` — pesquisa, decisão, contexto
- [ ] `fix` — correção de erro factual (numérico, de citação ou de leitura de fonte)
- [ ] `feat` / `pitch` — conteúdo novo de produto ou de pitch
- [ ] `data` — curadoria de dado com fonte
- [ ] `chore` / `refactor` / `build` / `ci` — infraestrutura

## Checklist de evidência

- [ ] Toda afirmação nova tem marca: `[fato]` · `[hipótese]` · `[a confirmar]` · `§N`
- [ ] Todo número tem fonte: link + data + página/tabela
- [ ] Nenhuma promessa de economia, ROI ou % de redução de absenteísmo
- [ ] Nenhuma ocorrência de "manutenção preditiva" como tese, nem "ODS 2" para saúde
- [ ] Nenhum dado pessoal de trabalhador (LGPD art. 11) — nem em exemplo, nem em print
- [ ] Varredura de caracteres não latinos rodada antes do commit

**Varredura de não-latinos** — rode antes do commit, no PowerShell:

```powershell
Select-String -Path <arquivos alterados> -Pattern '[\u4E00-\u9FFF\uAC00-\uD7AF\u0400-\u04FF\u0600-\u06FF\u0900-\u097F]'
```

> O mesmo regex está em `docs/relatorios/verify.py`. Cobre **chinês, japonês, coreano, cirílico, árabe e devanagari** — as três formas que já passaram por aqui: glifo de outro script no meio de uma palavra, separador introduzido e **palavra em inglês colada** (que escapam do scan de não-latinos — confira também o diff com olho).

## Se tocou documentos canônicos

- [ ] `docs/04-proposta.md` → atualizei também o §10 (bifurcações), se a mudança afeta o escopo
- [ ] `AGENTS.md` → atualizei o contador de correções pendentes e a estrutura do repositório
- [ ] `docs/05-inscricao-formulario.md` → conferi que o texto do formulário continua válido
- [ ] `pitch/roteiro-3min.md` → o roteiro continua cabendo em 3 minutos

## Checagem

- [ ] Links quebrados conferidos
- [ ] `main` está verde
