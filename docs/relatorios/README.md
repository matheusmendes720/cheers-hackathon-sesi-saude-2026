# O dossiê em PDF

A consolidação de **tudo que a pesquisa produziu fora do grupo de WhatsApp** — 4 documentos, **58 páginas**, A4, com sumário clicável e a **fonte ao lado de cada número**.

**É este material que vai para o time.** O repositório guarda a fonte; os PDFs são a forma de ler.

| Doc | Arquivo | Páginas | O que responde |
|---|---|---|---|
| 01 | `01-horizonte-de-trabalho.pdf` | 12 | O mapa do que exploramos, o delta em relação ao grupo, as decisões em aberto, o calendário real |
| 02 | `02-nucleo-e-gaps.pdf` | 15 | A tese, a 7ª dimensão do ASSTI, os 4 gaps, o mecanismo e o impacto honesto |
| 03 | `03-evidencia-mercado-regulacao.pdf` | 18 | Os 33 indicadores, a base científica, o mapa de preços, o escudo regulatório, as metas ODS |
| 04 | `04-kit-13-11-e-build.pdf` | 13 | O protocolo de 90 min, os 5 kernels, as 32 h de build, os 8 riscos, o checklist do pitch |

---

## Como o HTML foi feito

- **A4 retrato**, margens 14 mm × 12 mm, `@page` explícito no CSS.
- **Zero recurso externo**: sem CDN, sem fonte web, sem chamada de rede. Os gráficos são **SVG inline** (vetoriais — imprimem nítidos e pesam 0 KB de imagem).
- **Tipografia do sistema** (`-apple-system`, Segoe UI, Roboto, Arial) — nada para baixar.
- **Sumário clicável**: cada linha é `<a href="#id">` e cada seção tem `id` estável. É o contrato de navegação do PDF.
- **Rodapé por seção** com a página real de início e o total — recalculado do próprio render, não chutado.

## Paleta

Herda da identidade da demo (`pitch/demo.html`): acento teal `#0D9488`, superfícies `#F5F7FA` / `#FFFFFF`, linhas `#D6DEE8`, e os semânticos `#2563EB` (info) · `#B45309` (atenção) · `#BE123C` (risco) · `#047857` (confirmado) · `#6D28D9` (destaque).

---

## Como regerar

**Pré-requisitos (Windows):** Node 18+, `playwright` importável (`npm install -g playwright`), e `poppler` no PATH (`pdfinfo`, `pdftotext`, `pdftoppm`).

```powershell
# um documento
node docs/relatorios/render_pdf.cjs `
  --in docs/relatorios/01-horizonte-de-trabalho.html `
  --out docs/relatorios/01-horizonte-de-trabalho.pdf `
  --format A4 --label "Cheers - Horizonte de Trabalho"
```

**Todos os quatro, com o sumário recalculado a partir da paginação real:**

```powershell
python docs/relatorios/fix_toc2.py 01-horizonte-de-trabalho 02-nucleo-e-gaps 03-evidencia-mercado-regulacao 04-kit-13-11-e-build
```

> `fix_toc2.py` **lê** o PDF já renderizado, **descobre a página real de cada seção** (o `runhead` é único por seção e aparece no topo de cada página dela), reescreve os números do sumário e **renderiza de novo** só se algo mudou. **Um render ≈ 40–70 s** — divida o comando em lotes para não estourar timeout.

**Verificar depois de mudar:**

```powershell
python docs/relatorios/verify.py 01-horizonte-de-trabalho 02-nucleo-e-gaps 03-evidencia-mercado-regulacao 04-kit-13-11-e-build
```

Confere: contagem e tamanho de página, âncoras do sumário com destino, links clicáveis, e **varredura de caracteres não latinos no HTML e no texto extraído do PDF**.

---

## Por que o rodapé é do motor, e não do HTML

Cada `<section>` do HTML ocupa **exatamente uma página**. O número da página no rodapé vem do **próprio motor de PDF** (`displayHeaderFooter` + `pageNumber`/`totalPages` do Playwright), não de um `<div>` posicionado no HTML.

**Por quê:** um `<div>` de rodapé dentro da seção só aparece na **primeira** página dela. Se uma seção estourar uma página, o rodapé se repete com o número errado — e ninguém vê no diff, só na impressão. Delegando a numeração ao motor, **cada página sai com o número certo**, mesmo que uma seção ocupe duas.

O sumário continua sendo o mapa navegável (com âncoras clicáveis e a página real), e a checagem `verify.py` confere que âncora e página batem.

---

## Os scripts desta pasta

| Script | Para que serve |
|---|---|
| `render_pdf.cjs` | HTML → PDF (Playwright): rodapé numerado pelo motor, A4 retrato ou paisagem |
| `fix_toc2.py` | **Recalcula a paginação real** e reescreve o sumário (lê o PDF já renderizado) |
| `fix_toc.py` | Versão anterior do recalculo de paginação |
| `verify.py` | Verificação final: páginas, âncoras, links, não-latinos |
| `_check.py` | Diagnóstico: qual seção estoura a página |
| `_tighten.py` | Aplica a classe `.tighter` nas tabelas longas |
| `_polish.py` · `_renum.py` · `_strip_runfoot.py` | Ajustes finos de HTML e rodapé |

Os que começam com `_` são auxiliares. **Rode a varredura de não-latinos antes de commitar** — a regra está em [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md).

---

## Regra editorial do dossiê

1. **Todo número leva fonte** — link, data e página/tabela.
2. **Nada de promessa de economia, ROI ou % de absenteísmo.** Em ensaio randomizado (n = 32.974) o ROI é **−49%**.
3. **Nada de "manutenção preditiva".** O Anexo I rejeita "incorporação de novas tecnologias" como resposta.
4. **Toda referência a ODS é ODS 3 + ODS 9.** "Saúde e Bem-Estar" é o **ODS 3** na Agenda 2030.
5. **Marca de evidência em tudo:** `[fato]` · `[hipótese]` · `[a confirmar]` · `§N`.

A lista viva de correções está em [`../../AGENTS.md`](../../AGENTS.md) → *Correções pendentes*.
