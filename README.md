# Cheers — Hackathon+ SESI Saúde 2026

Repositório da equipe **Cheers** (5 pessoas) para o Hackathon+ SESI Saúde — SESI Bahia + Grupo Rede+, Salvador, **14 e 15 de novembro de 2026**.

> **Se você é do time e abriu isso agora:** o que você precisa está na seção **"Só leia 3 coisas"** e em **"O que fazer até sexta"**. O resto é para quando precisar ir fundo.

---

## A proposta em 3 linhas

> **O SESI mede o risco que o trabalhador corre, mas não mede o trabalho que causa o risco.**
> A sétima dimensão do ASSTI — *fatores de redução da produtividade* — foi **declarada e nunca analisada** (VigIndústria Brasil 2026, p. 16), e o instrumento oficial não tem **nenhum** item de autonomia, participação ou propósito (p. 110–119). Essa é a 4ª dimensão do Anexo I do desafio.
> A gente **operacionaliza** essa dimensão: o trabalhador responde 6 itens no celular (offline, 90 s, pode pular qualquer um); o agregado anônimo do posto (k ≥ 10) vira um índice; cruza com a exposição prevista e vira **3 alavancas priorizadas** para a empresa.

**Produto (MVP de 32 h):** Escuta (6 h) · Plano do trabalhador (8 h) · Exposição prevista (8 h) · Motor de alavancas (6 h) · Export FHIR/eSocial (4 h) — com **plano de corte declarado**.

---

## Só leia 3 coisas

| # | Documento | Por quê |
|---|---|---|
| 1️⃣ | **`pitch/apresentacao-interna.md`** | A proposta em 10 min, sem contexto prévio. **Comece por aqui** — é a apresentação para o time |
| 2️⃣ | **`docs/05-inscricao-formulario.md`** | As 22 perguntas do formulário + **o texto pronto do seu campo**. É a sua tarefa até sexta |
| 3️⃣ | **`docs/09-por-que-esta-proposta.md`** | A justificativa completa: os 4 gaps, a 7ª dimensão na prática, o impacto real e por que não é agrotech |

---

## O que fazer até **sexta, 06/11**

> ⚠️ **08/11 (o fim oficial das inscrições) é um DOMINGO.** O prazo real é **sexta 06/11**. São **5 dias úteis**.

| Quem | O quê | Onde está o texto |
|---|---|---|
| **Os 5** | **Preencher a inscrição individual** — §3 do doc 2️⃣, cada um com a sua voz | `docs/05-inscricao-formulario.md` §3 |
| **Esteves** | **Decidir o slot de DESIGN** e marcar "Design" no formulário (sem isso a equipe aparece com 3 dos 4 perfis do §5.3) | `docs/05-inscricao-formulario.md` §3.3 |
| **Matheus + Omena** | **Nome do produto** — "SINAL" é a recomendação; checar INPI antes | `docs/04-proposta.md` §1 |
| **Time** | **Quem é o líder** (§9.5 — o prêmio cai na conta de uma pessoa só) | — |
| **Time** | **Quem responde o e-mail de confirmação em 24 h** (pode cair no fim de semana) | — |

**Os 5 com o mesmo nome de equipe: `Cheers`.** Sem exceção (§5.2).

---

## O hackathon em 6 linhas

| | |
|---|---|
| **Tema (fixo)** | *Desafios e soluções para a **sustentabilidade dos modelos assistenciais de saúde*** (§2.1 + Anexo I) |
| **O que é revelado** | O **desafio específico**, na abertura de **13/11, 18h30** (§7.3) — por isso a proposta não é travada: tem **5 bifurcações** |
| **Entregável** | Protótipo **funcional** + pitch de **3 minutos** (§6.3). Protótipo até **15h30 de domingo** |
| **Nota** | `Final = (Pitch × 6) + (Protótipo × 4)` — cada critério de pitch vale **1,5×** cada de protótipo |
| **Sem equipamento** | §11.2: a organização **não fornece notebook**. A demo roda na máquina de um de nós, **offline** |
| **O evento é fim de semana** | Sábado 14 + domingo 15, com check-in **07h30 de sábado**. Planejar como plantão de ~30 h, não como dois dias de trabalho |

---

## Onde está cada coisa

| Se você quer… | Vá para |
|---|---|
| **Entender a proposta** | `docs/04-proposta.md` (canônico) · `pitch/apresentacao-interna.md` (versão para o time) |
| **Entender por que não é outra coisa** | `docs/09-por-que-esta-proposta.md` · `docs/07-alavancas-regulamento.md` (alavancas de nota + restrições) |
| **Ver a demo** | `pitch/demo.html` — abre offline, duplo clique. Tela "Modo pitch" = o ensaio cronometrado |
| **Ver o roteiro do pitch** | `pitch/roteiro-3min.md` — palavra por palavra, 8 perguntas de banca, protocolo de 10 ensaios |
| **Ver o slide** | `pitch/slide-impacto.html` — A4 paisagem, imprimível |
| **Entender a evidência** | `data/vigindustria-2026.md` (33 indicadores com página e tabela) · `docs/pesquisa/01-mapa-competitivo.md` (11 players) |
| **Entender a regulação** | `docs/viabilidade-stack-dados-regulatorio.md` · o PDF do regulamento na raiz |
| **Saber o que construir** | `docs/04-proposta.md` §5 (escopo + plano de corte) · `docs/10-mapa-de-build-32h.md` (o plano hora a hora) |
| **Preparar o reveal** | `docs/08-plano-90min.md` — grade de decisão de 4 testes, escopo travado às 20h de 13/11 |
| **Ir à live de 12/11** | `docs/11-perguntas-para-a-organizacao.md` — one-pager imprimível com as 8 perguntas, em ordem de prioridade |
| **Ver as fontes primárias** | `docs/sources/` (9 documentos) · `data/vigindustria-2026-raw.txt` (texto integral do relatório) |

---

## As 5 regras que ninguém pode quebrar

1. **Não prometer economia.** Em ensaio randomizado o ROI de absenteísmo é **−49%**. A gente promete **medir** dias expostos, antes e depois.
2. **Não dizer "manutenção preditiva".** O Anexo I rejeita a leitura de IoT industrial. É previsão de desfecho de saúde do trabalho.
3. **Não atribuir os R$ 468 bi (4% do PIB) ao presenteísmo.** Esse número é de doenças e acidentes de trabalho.
4. **Não tocar em código de produto antes de 14/11.** §7.3 (o desafio só aparece na abertura) + §11.8 (vantagem indevida desclassifica o grupo).
5. **Nada de dado individual de trabalhador.** Agregado com **k ≥ 10**, sem identificação, sem ASO, sem decisão de emprego.

---

## O time

| Membro | Papel | Slot §5.3 |
|---|---|---|
| **Matheus Mendes** | Coordenação do repo e do time · tech, front e UX · **Product Owner** | TI (1/2) |
| **luquinhas** | Tech · velocidade de prototipagem | TI (2/2) |
| **Omena** | Visão de produto e de negócio | **Gestor** |
| **Moisés** | Especialista · informática em saúde, IA no atendimento médico · **speaker do pitch** | **Especialista** |
| **Gabriel Esteves** | Articulação com o SESI/MES · validação clínica | **Designer** ⚠️ (D7) |

---

## O kit de mapeamento (por que o repo tem tanta coisa)

O §7.3 do regulamento diz que o **detalhamento do desafio só é apresentado na abertura**. Chegar com uma solução travada quebra o nivelamento entre as 12 equipes. Por isso o repo guarda o **kit**, não a solução:

- `docs/02-cruzamento-whatsapp.md` — a grade das 4 dimensões do Anexo I + 5 bifurcações
- `docs/08-plano-90min.md` — como absorver o desafio em 90 min e travar o escopo
- `docs/01-produtos-brainstorm.md` — as 10 ideias e o porquê das 3 escolhidas

**Em 13/11 às 18h30 a gente descobre o tema real.** Até lá: inscrição, slide e ensaio.
