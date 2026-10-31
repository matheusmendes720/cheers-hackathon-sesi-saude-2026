# A proposta — uma página

**Equipe Cheers · 31/10/2026 · documento canônico do produto**
Marca: `[fato]` verificável com fonte · `[hipótese]` leitura nossa · `[a confirmar]` depende da organização.

> Este documento é a resposta a "o que exatamente a gente constrói". Ele **funde** as duas listas de escopo que existiam separadas no repo (`docs/00` §4 e `docs/03` §4) em **uma só**, e fecha o escopo de 30 h com um **plano de corte** declarado. Se o desafio revelado em 13/11 for outro, o §8 diz como reposicionar sem refazer nada.

---

## 1. O nome, a frase e a proposta em 10 segundos

| | |
|---|---|
| **Nome** | **SINAL** — *o sinal que antecede a falta* |
| **Alternativas** | **Elo 1** (o elo invisível da cadeia, autoexplicativo depois do slide 2) · **Escuta** (o mais direto, o mais genérico) |
| **Proposta de valor** (a frase do topo do README e do repo) | *"O SINAL mede o trabalho que causa o risco — e devolve, por posto, as 3 alavancas priorizadas que a empresa aplica, antes da falta."* — **Voz mensurável para o trabalhador. Ação priorizada para a empresa. A 7ª dimensão do ASSTI, finalmente medida, para o SESI.** |
| **Frase de 10 s** (o gancho do pitch) | *"A gente mede o trabalho que causa o risco — não só o risco."* |
| **Frase de 30 s** (o pitch) | *"Hoje o SESI mede o risco que o trabalhador corre. Não mede o trabalho que causa o risco. O SINAL dá ao trabalhador uma voz mensurável e devolve à empresa, em alavancas priorizadas, o que mudar no trabalho — antes da falta."* |
| **Checagem pendente** | Disponibilidade do nome no INPI + busca por marca registrada no setor de saúde ocupacional — 20 min, antes de 08/11 (o nome vai no formulário) |

---

## 2. O problema, com o número

**O SESI mede o risco que o trabalhador corre. Não mede o trabalho que causa o risco.**

| Evidência | Valor | Fonte |
|---|---|---|
| A 7ª dimensão do ASSTI — *fatores de redução da produtividade* — foi **declarada e nunca analisada**, apesar de ter validade psicométrica validada (CR = 0,863) | 1 dimensão morta | VigIndústria Brasil 2026, **p. 16** `[fato]` |
| O instrumento de coleta completo (p. 110–119) tem **zero itens** para autonomia, decisão, sugestão, propósito, confiança ou segurança psicológica | **0 itens** na dimensão que o Anexo I exige | VigIndústria, Anexo I `[fato]` |
| 20,0% dos trabalhadores faltaram ≥1 dia por semana por saúde; 6,5% ≥3 dias | n = 123.355 | SESI/ASSTI, *Estilo de Vida, Saúde e Produtividade* `[fato]` |
| 106 milhões de dias perdidos em acidentes de trabalho (2016–2025); 4,1 mi afastamentos no INSS (2025, +17,1%) | custo do fim da cadeia | CANPAT · INSS `[fato]` |
| **65,6%** dos trabalhadores dizem que a comunicação sobre prevenção de acidentes é **suficiente** — em micro/pequenas empresas, só **56,2%** | 1 em 3 não acha suficiente | VigIndústria, Tabela 36, p. 95 `[fato]` |
| O relatório **recomenda** "fortalecer competências de liderança, comunicação aberta e ambiente psicologicamente seguro" — e não tem **nenhum** item que meça isso | a fonte pede o que o instrumento não mede | VigIndústria, **p. 98** `[fato]` |

> **A lacuna não é nossa interpretação — está escrita na fonte do próprio desafio.** O Anexo I do regulamento exige *autonomia, participação, bem-estar e senso de propósito*. O instrumento oficial que a indústria brasileira usa para medir saúde do trabalho tem **zero** itens nessa dimensão.

---

## 3. A solução: o ciclo, em três passos

```
   TRABALHADOR                EMPRESA / SESI                RESULTADO
   ───────────                ──────────────                ─────────
   6 itens offline      →     índice de contexto       →    exposição prevista
   no celular, opt-out        do posto (k ≥ 10)             (onde o risco está)
   (~90 s)                     + índice de exposição           │
                               prevista (CNAE×porte×região)    │
                                       ↓                        │
                               3 alavancas priorizadas         │
                               (com o indicador nacional        │
                               que justifica cada uma)         │
                                       ↓                        │
                               ──────── o absenteísmo é a consequência, não a promessa
```

**O que a engenharia entrega** (o software, em uma frase): *um dispositivo de captura de sinal em dois lados — o trabalhador fala 6 itens num PWA instalável e offline; o agregado anônimo por posto vira um índice que cruza com um modelo de exposição previsto sobre bases públicas; um motor de regras transparente traduz o par (exposição, contexto) em 3 alavancas organizacionais com a evidência que as sustenta.*

---

## 4. As 4 dimensões do Anexo I — e onde a proposta ainda hoje é incompleta

| Dimensão (Anexo I) | O que o SINAL mede/agrega | Fonte do dado | Status |
|---|---|---|---|
| **Comportamento** | o que o trabalhador já faz — o bloco comportamental do VigIndústria, priorizado por recorte (hoje ele existe, mas não diz "aqui está o foco desta empresa") | VigIndústria: álcool 34,2% · sedentarismo no lazer 44,3% · tela 33,9% · tabaco 6,5% | 🟡 parcial |
| **Ambiente** | ambiente seguro percebido 71,4% · insatisfação com condições de trabalho 8,1% | VigIndústria T32/T16 | 🟡 parcial |
| **Organização do trabalho** | **os 6 itens** (demanda, controle, apoio, reconhecimento, propósito, segurança) + cultura (liderança 72,6% · prevenção 70,2% · treinamento 69,8% · comunicação 65,6%) | HSE Management Standards (adaptado) + VigIndústria | 🟢 **forte** |
| **Participação das pessoas** | **o canal em si** — o trabalhador responde, pode pular qualquer bloco, e o agregado só volta com k ≥ 10 no mesmo posto | **criado do zero** — 0 itens no instrumento atual | 🟢 **novo** |

> **Por que isso é a proposta e não um app:** a dimensão que o Anexo I pede é a única que **não tem instrumento nenhum** no Brasil. Uma proposta que cobre comportamento, ambiente e organização do trabalho é um dashboard melhor — e dashboard de SST é o que SOC, SGG, WOTY e o próprio ASSTI já vendem. A diferença está no que **não** existia.

---

## 5. O MVP de 30 h — escopo único, com plano de corte

**Janela real:** 14/11 07h30 → 15/11 15h30 ≈ 32 h de relógio, menos refeições, absorção do desafio e ensaio do pitch → **~36–40 dev-hours** (2 devs). O escopo abaixo fecha em **32 h** com **ordem de sacrifício declarada**.

| # | Componente | h | Saída verificável | Corte |
|---|---|---|---|---|
| 1 | **Escuta** — 6 itens adaptados do HSE (demanda, controle, apoio, reconhecimento, propósito, segurança), opt-out por bloco, ~90 s, offline | 6 | 6 itens funcionando no celular, com consentimento por resposta | 🔴 1º a cortar — vira 4 itens |
| 2 | **Plano do trabalhador** — PWA instalável, offline-first; devolve **as 2 alavancas dele**; agregação **k ≥ 10** por posto; nada de dado individual compartilhado | 8 | tela do trabalhador + contador de k | 🟡 2º a cortar — devolve 1 alavanca |
| 3 | **Modelo de exposição prevista** — perfil agregado (CNAE × porte × região × nº de trabalhadores) sobre VigIndústria + CAT, **todos os pesos à vista** | 8 | índice 0–100 + composição em waterfall + risco por causa | 🔴 3º a cortar — vira tabela |
| 4 | **Motor de alavancas** — regras explicáveis (não é IA): do par (exposição, contexto) saem **3 alavancas priorizadas**, cada uma citando o indicador nacional que a justifica | 6 | slide de 3 alavancas com número e fonte | 🟢 núcleo — **nunca cortar** |
| 5 | **Export** — Bundle FHIR R4 perfil RNDS + validador eSocial S-2210/S-2220 | 4 | arquivo validado + log de validação | 🔴 4º a cortar |

**Regras de engenharia que não se negociam** (§11.2 — a organização não fornece notebook; a demo roda na máquina de um membro):

1. **Offline é requisito de arquitetura**, não conveniência: sem CDN, sem fonte externa, sem chamada de rede na demo.
2. **Zero dado individual de trabalhador** para fora do aparelho dele. Agregação com k ≥ 10 no posto. Nada de LGPD art. 11 §4º/§5º, nada de NR-7 (ASO sigiloso).
3. **IA só em função administrativa/apoio**, sem influência decisória em diagnóstico (Res. CFM 2.454/2026, art. 4º I e Anexo II, I = baixo risco). O motor de alavancas é **regras**, e isso é mais forte no pitch, não mais fraco.
4. **Modelo transparente**: os pesos do índice de exposição ficam à vista, com "como o modelo funciona" aberto na tela. Caixa-preta é o que o mercado já vende.

---

## 6. O que a proposta **não** é (a armadilha, e como ela morre)

| A banca vai dizer | A resposta, com evidência |
|---|---|
| *"É mais um app de bem-estar"* | Mede contexto de trabalho, não movimento. E atividade física **no trabalho** é **exposição**: +20 min/dia no trabalho → **+15%** de risco de afastamento longo; no lazer → −20% (p = 0,02). App de atividade mede a coisa errada `[fato]` |
| *"É um dashboard de indicador"* | Não entregamos indicador — entregamos **mudança organizacional priorizada** com a evidência que a justifica. Dashboard de SST é o que SOC/SGG/WOTY/ASSTI já vendem `[fato]` |
| *"Telemedicina corporativa"* | Commodity a R$ 19,90–79,90/colaborador/mês `[fato]` |
| *"O programa reduz absenteísmo"* | Em RCT (n = 32.974): 2,5% vs 2,6% (P = 0,09); gasto médico US$ 3.583 vs 3.953 (P = 0,32). **Não prometemos ROI** — em ensaio randomizado o ROI de absenteísmo é **−49%**. Prometemos **medir o efeito** `[fato]` |
| *"É manutenção preditiva industrial"* | Nunca diga isso. É **previsão de desfecho de saúde do trabalho**; nenhum sensor, nenhuma máquina no slide. A leitura "manutenção preditiva" mapeia para IoT industrial — que o Anexo I rejeita `[fato]` |
| *"Job strain não é preditor de ausência"* | Meta-análise: strain OR 1,20 (IC95% 0,94–1,52) **não** significativo; **demanda** OR 1,57 (1,04–2,36) significativo; **apoio no trabalho** OR 0,58 (0,41–0,83) reduziu ausência. → Por isso os itens são **demanda e apoio**, não "autonomia genérica" `[fato]` |

---

## 7. Impacto: o que medimos (e o que não prometemos)

| Métrica | Como é medida | Fonte da base |
|---|---|---|
| **Dias expostos** | dias de afastamento potenciais por posto, derivados do modelo de exposição | CANPAT (CAT) + VigIndústria |
| **Alavancas priorizadas** | nº de alavancas com evidência nacional que as justifica | VigIndústria — ver `data/vigindustria-2026.md` |
| **Mudança organizacional** | antes/depois por posto: demanda, apoio, reconhecimento, comunicação, treinamento | VigIndústria, 2 ondas |
| **Ausência** | consequência a medir no piloto — **não** promessa de pitch | INSS / eSocial |

**Contexto de mercado** (para a banca, não para o gancho): perda de produtividade por doenças e acidentes no trabalho ≈ **R$ 468 bi/ano** (4% do PIB, OIT/UN Brasil); saúde mental ≈ **R$ 179 bi/ano** (IFEMG, jan/2026); despesas assistenciais em saúde empresarial **R$ 276,9 bi/ano** (ANS Panorama + DIOPS). **Não somar** — os três pools se sobrepõem.

**Modelo de negócio e canal** — a proposta não é uma startup de fora:

| Camada | Valor | Fonte |
|---|---|---|
| Plataforma Viva+ | **2.738.306 vidas ativas** | CN-SESI, PAO 2026 (retificado) |
| Empresas atendidas na Bahia (meta 2026) | **10.800** | CN-SESI, PAO 2026/BA |
| MES (empresas-membro) | **76** | CN-SESI, 25/02/2026 |
| Preço de referência | **R$ 13,9 por vida/mês** (Salú: 800+ clientes, ~460 mil vidas, R$ 76,8 mi de receita 2025; vendida por R$ 318,7 mi ≈ 4× ARR) | Fato relevante CVM |

> **O argumento institucional que fecha o pitch:** o Plano de Ação do SESI 2026 tem como objetivo estratégico, literalmente, *"promover a gestão integrada da saúde dos trabalhadores por meio das soluções digitais e da inovação"*. **Não estamos propondo um produto novo. Estamos propondo a camada de previsão e a camada de participação que a plataforma de 2,7 milhões de vidas ainda não tem.**

---

## 8. Equipe (bloco de 20 s)

| Membro | Papel | Linha |
|---|---|---|
| **Moisés** | Especialista · speaker | Informática em saúde, doutorado em IA no atendimento médico — e estagiário de saúde real |
| **Esteves** | Designer *(slot §5.3 — **D7 em aberto**)* | Articulação com o ecossistema SESI/MES e validação clínica com o parceiro médico |
| **Omena** | Gestor | Visão de produto e de negócio — o que o cliente adota e por que escala |
| **luquinhas** | TI 2 | Velocidade de prototipagem — é o que traz o time do zero ao protótipo |
| **Matheus** | TI 1 · Product Owner | Coordenação e front-end do protótipo; ponte para o ecossistema de incubação (Liga Jovem SEBRAE, Aluno Empreendedor) |

---

## 9. Riscos assumidos, com o plano

| # | Risco | Como o time lida |
|---|---|---|
| R1 | **Amostra por conveniência** — o VigIndústria recolhe empresas que *voluntariamente* demandaram serviço ao SESI (viés declarado no relatório). É o contra-argumento mais forte contra nós | Declaramos no slide. O modelo é **transversal e transparente**, e o piloto é o teste: o próprio relatório pede "a continuidade do monitoramento sistemático" (p. 100) |
| R2 | **Tese travada antes do reveal** (§7.3) | Ver §8 abaixo — a tese é o ponto de partida tático, não o destino |
| R3 | **Item de design descoberto** (§5.3) | D7, prazo 08/11 — vai escrito no formulário |
| R4 | **Prêmio só para o líder** (§9.5) e §9.7: a organização **não media** desacordo entre membros | D8, prazo 10/11 — conversa de time, não de secretaria |
| R5 | **A demo cai no meio do pitch** | O roteiro tem um parágrafo de fallback (números na tela, fala continua). Cada um roda o protótipo na própria máquina |

---

## 10. §8 · Se o desafio revelado em 13/11 for outro

O detalhamento do desafio é apresentado **na abertura, às equipes** (§7.3). Esta proposta é o **ponto de partida tático** — não o destino. O kit de mapeamento cobre 5 bifurcações prontas, e o critério de escolha é sempre o mesmo:

| Se o desafio vier sobre… | Bifurcação do kit | Núcleo que permanece |
|---|---|---|
| **participação / autonomia / propósito** | **O3** (esta proposta) + W1 (a empresa como paciente) | escuta instrumentada + alavancas |
| **absenteísmo / custo / previsão de desfecho** | **O1** (ponte saúde↔absenteísmo) + docs/03 cadeia de 7 elos | modelo de exposição prevista + motor de alavancas |
| **risco / exposição / prevenção / laudo** | **O5** (do laudo à intervenção) + ideia 5 (Prazo) | exposição + alavancas + orquestração de prazo |
| **retorno ao trabalho / incapacidade / readaptação** | **O2** (RTW/SAW) + ideia 10 (Catálogo de posto) | catálogo de demandas por posto + plano de retorno |
| **fragmentação / interoperability /SUS-plano** | **O4** (cuidado coordenado) | export FHIR/RNDS + trajectory |

**Teste de 15 minutos, na live de 13/11:** o desafio se articula às **4 dimensões** do Anexo I? Se sim, é a direção certa. Se não, é alerta — e a bifurcação correspondente assume.

---

## 11. O que ainda falta para 08/11 (ordem de prioridade)

| # | Pendência | Responsável | Prazo | Por que é crítico |
|---|---|---|---|---|
| 1 | **D1 — inscrição individual dos 5**, cada um informando o time "Cheers" (§3.3.1, §5.2) | cada um | **08/11** | Sem inscrição não há demo |
| 2 | **D7 — quem cobre o slot de designer** (§5.3) e o texto do formulário (L1) | time | **08/11** | §4.1 avalia o preenchimento; §5.4.1 prioriza equipe indicada |
| 3 | **D11 — 5 ou 6 pessoas?** (§5.4.2 completa equipes com menos de 6) | Matheus | **08/11** | Se a organização completar a equipe, quem entra e em que slot? |
| 4 | **Nome no formulário** (§1 desta página) — checar INPI | Matheus | 08/11 | O formulário é o primeiro pitch da equipe |
| 5 | **D8 — líder da equipe** para o prêmio (§9.5) | time | 10/11 | §9.7: a organização não media desacordo entre membros |
| 6 | **D12 — todo mundo online 13/11 18h30** | todos | 13/11 | O desafio é revelado ali |

**Perguntas para a organização** (12/11, live de orientações) e **para os mentores** (13/11): ver `AGENTS.md`.

---

## Fontes

`docs/00-portfolio-oportunidades.md` · `docs/01-produtos-brainstorm.md` · `docs/02-cruzamento-whatsapp.md` · `docs/03-tese-preditiva.md` · `docs/pesquisa/01-mapa-competitivo.md` · `docs/research/falhas-do-modelo-atual.md` · `docs/viabilidade-stack-dados-regulatorio.md` · `data/vigindustria-2026.md` · 9 fontes primárias em `docs/sources/`

**Regulamento:** §3.3.1 (inscrição individual) · §4.1 (seleção) · §5.1–5.4 (equipe) · §6.2 (cronograma) · §6.3 (entregável) · §7.3 (detalhamento na abertura) · §8.2.4 (fórmula da nota) · §9.5/§9.7 (prêmio e líder) · §11.2 (sem equipamento)
