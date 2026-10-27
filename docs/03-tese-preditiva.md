# Tese preditiva na cadeia de valor — TAM, SAM, SOM

**Equipe Cheers · 27/10/2026 · direção proposta por Matheus, calibrada contra a pesquisa**
Marca: `[fato]` verificável com fonte · `[hipótese]` leitura nossa · `[a confirmar]`.

---

## 1. A reframe: "preditivo" onde ninguém olha

A direção que você propôs — **revolucionar a indústria com tecnologia preditiva, na cadeia de valor completa** — bate com a estratégia do próprio SESI e do MES. O MES tem, para 2026–2027, exatamente três eixos, e **dois são o seu instinto**:

> **Eixo 1 — Dados e Inteligência em Saúde:** reduzir fragmentação, fortalecer a governança da informação.
> **Eixo 3 — Modelos Assistenciais Sustentáveis:** eficiência, qualidade e equilíbrio econômico.

⚠️ **Mas a leitura literal de "tecnologia preditiva na indústria" é um problema, e é um problema de primeira linha.** O exemplo canônico de Indústria 4.0 é **manutenção preditiva de máquina** — sensor em ativo, algoritmo prever falha, trocar antes de quebrar. Se o pitch abre com essa imagem:

1. a banca mapeia mentalmente para "mais um dashboard de IoT industrial" — exatamente a *"incorporação de novas tecnologias"* que o Anexo I diz que **não** é a resposta;
2. manutenção preditiva **não toca nenhuma das 4 dimensões** do Anexo I;
3. é o produto mais crowded que existe: Siemens, AVEVA, PTC, Bosch Rexroth, e os players de SST (SOC, SGG, WOTY) já vendem dashboard.

**A saída não é abandonar o instinto — é escolher a cadeia errada.** A cadeia que o SESI ocupa tem uma dinâmica preditiva **muito mais valiosa e muito menos disputada**: a cadeia de **desfecho de saúde do trabalho**.

> **O dado que decide o enquadramento** — a própria Palestra Magistral do SESI Paraná, 2025: *"O absenteísmo é um indicador sensível da saúde organizacional. Quando a empresa passa a olhar para isso de forma estratégica, ela não só reduz faltas, mas melhora o engajamento, a produtividade e a sustentabilidade do negócio."* (Guilherme Murta, médico do trabalho, Coordenador de Saúde do Sesi Paraná)

E o estudo que dá a base conceitual, publicado em 2026 (*PharmacoEconomics*, funcional federal, 2012–2024):

> *"Absenteeism should not be interpreted as unproductivity, but may reflect a **health indicator of organizational distress** and a warning sign of systemic imbalance."* `[fato]`

**Tradução de pitch:** a falta não é um evento de saúde. É um **sinal do negócio**. E é o único sinal que a empresa não consegue ver hoje.

---

## 2. A cadeia de valor completa — 7 elos, o custo de cada um e onde a predição entra

O encadeamento não é uma metáfora: é a sequência causal que a pesquisa documenta, com dado público e custo em cada elo.

```
   [1] PRESENTEÍSMO  →  [2] EXPOSIÇÃO/RISCO  →  [3] EVENTO  →  [4] AFASTAMENTO
        (invisível)          (ASSTI 46 ind.)      (CAT)         (INSS)
                                                                 ↓
   [7] RESULTADO  ←  [6] SAÍDA  ←  [5] INCAPACIDADE
    (4% do PIB)      (aposentadoria)   (dias perdidos)
```

| Elo | O que é | Dado público | Custo / volume | Fonte |
|---|---|---|---|---|
| **1 · Presenteísmo** | Trabalhador presente, produtividade reduzida 20–40% | **Não existe em nenhum sistema** — folha de ponto só registra ausência | R$ 200–600 bi/ano | IBEF-SP via AXENYA, 2024 `[a confirmar]` |
| **2 · Exposição** | Condições de trabalho, demanda, ergonomia, cultura | **ASSTI — 46 indicadores**; 2,74 mi vidas ativas na Plataforma Viva+ | 79.119 empresas atendidas (meta 2026) | CN-SESI PAO 2026 |
| **3 · Evento** | Acidente de trabalho | **CAT** (INSS/eSocial) | 6,4 mi acidentes · 27.486 óbitos · **106 mi dias perdidos** · 249 mi dias debitados | CANPAT/AFT |
| **4 · Afastamento** | Benefício por incapacidade | INSS | **4,1 mi afastamentos/ano** (+17,1%) · 2,6 mi novas concessões acidentárias · **546.254 por saúde mental** (+15%) | INSS · G1 |
| **5 · Incapacidade** | Permanência e agravamento | Estudos | 35,6 mi dias por 5 causas apenas no funcional federal = **R$ 10,25 bi**; saúde mental = **R$ 3,94 bi** (38%) | *PharmacoEconomics*, 2026 |
| **6 · Saída** | Aposentadoria precoce, pensão, invalidez | INSS | **R$ 173 bi** em benefícios acidentários desde 2012 | OIT/UN Brasil |
| **7 · Resultado** | Perda de produtividade consolidada | PIB | **4% do PIB = ~R$ 468 bi/ano**; saúde mental = **2,8% do PIB potencial = R$ 179 bi** | OIT/UN Brasil · IFEMG 2026 |

### Onde a predição dá mais valor que a reação

| Momento | O que dá para fazer | Valor |
|---|---|---|
| **Depois do evento** (elos 3–6) | Emitir ASO, acionar INSS, pagar | Reação. Custo certo, mas tardio |
| **Antes do evento** (elos 1–2) | Prever **qual exposição vira incapacidade** e **mexer no trabalho antes** | **Prevenção. É aqui que a tecnologia paga** |

**O ciclo de adoecimento, na formulação da fonte:** *"estresse crônico não gerenciado → presenteísmo (queda de 20–40%) → transtornos de ansiedade e depressão → afastamentos por CID F → impacto no FAP e na sinistralidade do plano de saúde"* (AXENYA/IBEF-SP).

> **O elo 1 é o elo de ouro e o elo invisível.** O estudo é literal: *"Empresas que medem apenas faltas estão vendo metade do problema."* Não dá para prever o que não se mede. **Ninguém no mercado mede o presenteísmo** — e é exatamente ele que sinaliza a incapacidade antes dela acontecer.

### A régua de decisão: onde a predição é tecnicamente viável e legal

| Elo | Previsão individual? | Viável em 30 h? | Legal? |
|---|---|---|---|
| 1 · Presenteísmo | ❌ individual é dado sensível | ✅ com indicador agregado | ✅ |
| 2 · Exposição | ✅ por posto/empresa, via PGR/NR-7 | ✅ | ✅ |
| 3–6 · Evento → saída | ⚠️ individual exige dado de saúde | ⚠️ só agregado | ❌ se individualizado (LGPD art. 11, NR-7) |

**Conclusão:** a predição defensável é **por perfil de empresa e por posto**, nunca por pessoa. É o que cabe no MVP e o que a Res. CFM 2.454/2026 (baixo risco) permite.

---

## 3. TAM · SAM · SOM

Três camadas, cada uma com a fonte explícita. Sem número sem lastro.

### TAM — o valor total em jogo (Brasil, trabalho)

| Componente | Valor | Fonte |
|---|---|---|
| Perda de produtividade por doenças e acidentes de trabalho | **~R$ 468 bi/ano** (4% do PIB) | OIT/UN Brasil (PIB 2024 = R$ 11,7 tri, IBGE) |
| — subset saúde mental | **R$ 179 bi/ano** (2,8% do PIB potencial; 21,2 mi pessoas ocupadas) | IFEMG, jan/2026 |
| Despesas assistenciais em saúde empresarial | **R$ 276,9 bi/ano** (R$ 256,8 bi em 2024) | ANS Panorama + DIOPS |
| Benefícios acidentários INSS (acumulado desde 2012) | **R$ 173 bi** | OIT/UN Brasil |

> **Não somar.** Os três pools se sobrepõem parcialmente. O TAM é o *valor em jogo*, não uma receita endereçável — e é assim que se apresenta para a banca.

### SAM — o que o SESI alcança (canal institucional)

| Componente | Valor | Fonte |
|---|---|---|
| Empresas atendidas em SST (meta 2026) | **79.119** (+23% vs 2025) | CN-SESI PAO 2026 retificado |
| Pessoas atendidas | **3.973.375** (+11%) | CN-SESI |
| Pessoas em programas de SST | **6.756.318** (+23%) | CN-SESI |
| **Vidas ativas na Plataforma de Saúde e Segurança (Viva+)** | **2.738.306** | CN-SESI, SMD |
| **Empresas atendidas na Bahia** | **10.800** (meta 2026) | CN-SESI PAO 2026, BA |
| Planos coletivos empresariais (o que a empresa **já gasta**) | **38.977.827** beneficiários · **2,3 mi** contratantes | ANS/SIB ago/2026 · IESS TD 118/2026 |
| MES (clientes-membro) | **76 empresas** | CN-SESI, 25/02/2026 |

**O SAM que o time deve mirar: 10.800 empresas na Bahia + 76 do MES.** É onde um piloto cabe.

### SOM — o que a equipe captura em 12 meses

Benchmark de preço, ancorado na **Salú** (o maior ativo de software de saúde ocupacional do Brasil): 800+ clientes, ~460 mil vidas, **R$ 76,8 mi de receita (2025) = R$ 13,9 por vida/mês**; ARR R$ 97,2 mi; **vendida por R$ 318,7 mi (~4× ARR)**.

| Cenário | Contratos | Vidas | Preço/vida/mês | Receita/ano |
|---|---|---|---|---|
| **Conservador** — 3 pilotos via SESI Bahia | 3 | 1.500 | R$ 13,9 (Salú) | **R$ 750 mil** |
| **Base** — 10 clientes (MES + SESI/BA) | 10 | 3.000 | R$ 15 | **R$ 5,4 mi** |
| **Alcance** — via Hub SESI/BA (Demo Day 18–20/11) | 25 | 5.000 | R$ 18 | **R$ 27 mi** |

`[hipótese]` — premissas: 5–15% de penetração sobre a base de empresas atendidas na Bahia; conversão via canal SESI (sem custo de aquisição); preço por vida copatrocinado pela empresa. **O SOM é a parte que a banca vai pedir para justificar** — ela é a que a equipe precisa levar pronta.

---

## 4. O produto: preditivo, na cadeia, num elo só

> ⚠️ **Disciplina de escopo.** A cadeia completa é o **enquadramento do pitch**. O MVP tem que ser **um elo**. Três elos numa maratona de 30 h é slideware.

### O MVP proposto — "previsão de exposição, com a alavanca que age antes"

| # | Componente | Horas | Saída |
|---|---|---|---|
| 1 | **Modelo preditivo agregado** — profile por CNAE × porte × região, treinado em CAT/INSS público (6,4 mi registros: natureza da lesão, dias de afastamento) cruzado com a prevalência do VigIndústria | 10 | "Sua empresa tem perfil de exposição X: Y% de risco de afastamento por causa Z" |
| 2 | **Camada de presenteísmo** — 6 itens derivados de HSE (demanda, controle, apoio, reconhecimento, propósito, segurança), aplicados no aggregate | 6 | O indicador que hoje não existe em lugar nenhum |
| 3 | **Motor de alavanca** — do perfil de exposição + presenteísmo, sai a alavanca organizacional com a evidência que a sustenta | 6 | 3 alavancas, cada uma com o número do VigIndústria |
| 4 | **Plano do trabalhador** — PWA offline, o trabalhador recebe as alavancas dele, agregação k ≥ 10 de volta | 8 | Participação, com o trabalhador como dono do plano |
| 5 | **Export** — Bundle FHIR R4 perfil RNDS + validador eSocial S-2210/S-2220 | 6 | Sofisticação técnica verificável |

**Stack:** Vite + React + TS, dados locais, PWA instalável. Python para o modelo. **Offline é requisito** (§11.2: não fornecem notebook; a demo roda na máquina de um membro).

**O pitch (3 min), com este enquadramento:**

| Tempo | Bloco | O que se diz |
|---|---|---|
| 0:00–0:30 | Gancho | *"Seu trabalhador não falta. Ele está lá, produzindo 60% — e ninguém sabe. 4% do PIB brasileiro some assim."* |
| 0:30–1:15 | A cadeia | *"A cadeia vai de presenteísmo a aposentadoria. Hoje a gente só instrumenta o fim dela. A previsão começa no elo que ninguém mede."* |
| 1:15–2:00 | Demo | O trabalhador responde no celular (offline) → a empresa recebe 3 alavancas com o número que as justifica |
| 2:00–2:30 | Impacto | *106 mi dias perdidos · R$ 468 bi/ano · 20,0% faltaram ≥1 dia/semana* |
| 2:30–2:50 | Viabilidade | *Não é startup de fora: é módulo da Plataforma Viva+ (2,74 mi vidas ativas), piloto via SESI/BA e MES* |
| 2:50–3:00 | Fechamento | *"Sustentabilidade de um modelo assistencial não se mede no custo. Mede-se em quantos dias a pessoa volta a produzir — e em quantos ela teria voltado sem a gente."* |

---

## 5. O ângulo institucional que é imbatível

O **Plano de Ação e Orçamento 2026 do Sistema SESI** (CN-SESI) tem, entre os objetivos estratégicos, literalmente:

> **"Promover a gestão integrada da saúde dos trabalhadores por meio das soluções digitais e da inovação"** (objetivo com indicador "Número de trabalhadores na plataforma de saúde e segurança": **2.738.306**)
> **"Aplicar inteligência de dados"**

E a **Plataforma SESI Viva+** é descrita, no mesmo documento, como o *"Sistema Informatizado para a Gestão de SST e Promoção da Saúde, cujo objetivo é disponibilizar informações estruturadas dos trabalhadores, por empresa, por segmento industrial, bem como análises epidemiológicas"*. Componentes: S+, Telemedicina SESI, SESI Cursos, SESI Facilita PGR, Vacina SESI, **ASSTI**, **Mentis 360**.

> **O argumento que fecha o pitch:**
> *"Não estamos propondo um produto novo para a indústria. Estamos propondo **a coisa que o SESI já declarou como objetivo estratégico para 2026** — gestão integrada pela plataforma digital — e que **ainda não tem a camada de previsão nem a camada de participação**. A plataforma já tem 2,74 milhões de vidas ativas. O que falta é o modelo preditivo e o elo onde o trabalhador tem voz."*

Isso responde, de uma vez: **por que nós** (somos do ecossistema), **por que agora** (é a meta de 2026), **por que não é mais um app** (é camada da casa que já existe) e **por que a banca vai lembrar** (o Elenco do SESI já o declarou).

---

## 6. O que NÃO fazer — os riscos desta direção

| # | Risco | Por que mata | Como evitar |
|---|---|---|---|
| **R1** | **Chamar de "manutenção preditiva"** | A banca lê como IoT industrial, que é o crowded e o que o Anexo I rejeita | Dizer **"previsão de desfecho de saúde do trabalho"**, nunca "manutenção preditiva". Nenhum sensor, nenhuma máquina no slide |
| **R2** | **Prometer economia** | Em RCT, o ROI de absenteísmo é **−49%**; o "1:2 a 1:4" é artefato de estudo não randomizado | Falar em **dias expostos** e **alavanca recomendada**. Se pedirem economia: *"não prometemos ROI; prometemos medir o efeito"* — e isso é mais forte, porque a OIT pede *"monitoramento de rotina"*, não promessa |
| **R3** | **Tentar cobrir os 7 elos** | 30 h, 2 devs, demo offline. Três elos é slideware | A cadeia é o **slide 2**. O MVP é **um elo**. Escolher o elo 1+2 (exposição e presenteísmo) porque é onde a predição é legal e o dado é público |
| **R4** | **Prever por trabalhador** | LGPD art. 11 §5º; sigilo do ASO (NR-7); Res. CFM 2.454/2026 | Prever **por empresa, por posto, por causa**. Individual é eliminação certa |
| **R5** | **Deixar a proposta fora da casa** | "Startup de fora" compete com SOC/SGG/WOTY e não tem canal | **Módulo da Plataforma Viva+**, piloto via SESI/BA. É o que o §5.3 quer (multidisciplinar) e o que a banca recompensa |

---

## 7. O que ainda precisa ser confirmado

| # | Pergunta | Para quem | Prazo |
|---|---|---|---|
| **P1** | **A proposta entra como camada da Plataforma Viva+?** Se sim, isso muda o pitch de "startup" para "produto institucional" | SESI/mentores | 12/11 |
| **P2** | **O ASSTI tem 46 indicadores** (PAO 2026) — a 7ª dimensão (fatores de redução da produtividade) é um deles? O caderno técnico de 2023 (107 p.) responde | Moisés | 10–11/11 |
| **P3** | **O SESI já mede presenteísmo?** Se sim, a camada 1 do produto já existe e a proposta muda de forma | Moises + mentores | 12/11 |
| **P4** | A **Res. CFM 2.454/2026** classifica um modelo preditivo agregado sobre CAT como "baixo risco"? | Professor de Moisés (L3) | 10–11/11 |
| **P5** | **As 10.800 empresas atendidas na Bahia** — qual o perfil de porte e o canal de entrada para um piloto? | SESI/BA | 12/11 |
| **P6** | A demo entra nos 3 minutos ou o protótipo é julgado à parte? (§8.3) | Organização | 12/11 |

---

## Fontes

**Primárias (verificadas)**
1. CN-SESI. *Plano de Ação e Orçamento 2026 — Sistema SESI* (retificado) — metas de empresas/pessoas atendidas, 2.738.306 vidas ativas na Plataforma Viva+, objetivo "gestão integrada… por meio das soluções digitais e da inovação", meta da Bahia (10.800 empresas) — `docs/sources/`
2. CN-SESI. *Demonstração de Resultados* (Jan–Ago/2026) — 71.373 empresas · 3.985.231 pessoas atendidas
3. SESI/DN. *Estilo de Vida, Saúde e Produtividade* (2018–2021) — 20,0% faltaram ≥1 dia/semana (n = 123.355) — `docs/sources/sesi_produtividade_2023.txt`
4. Auditores-Fiscais do Trabalho. *Acidentes do trabalho no Brasil 2016–2025* (CAT/INSS/eSocial) — `docs/sources/canpat_2025.txt`
5. ANS. *Panorama Saúde Suplementar* ed. dez/2025 + DIOPS — `docs/sources/ans_panorama_nov2025.txt`
6. IESS. *TD nº 118/2026* — `docs/sources/iess_td118.txt`
7. CFM. *Res. nº 2.454/2026* (IA em medicina) — `docs/sources/cfm_2454_2026.txt`
8. SESI/PAO 2026 e sessão com Guilherme Murta (Sesi Paraná), *Info SST* — "o absenteísmo é um indicador sensível da saúde organizacional"
9. OIT/UN Brasil. *Observatório — afastamentos por saúde mental* — 4% do PIB = R$ 468 bi/ano; R$ 173 bi em benefícios acidentários desde 2012
10. IFEMG. *Gerência de Economia e Finanças Empresariais*, jan/2026 — saúde mental: R$ 179,15 bi/ano, 2,8% do PIB potencial, 21,2 mi pessoas ocupadas
11. *PharmacoEconomics*, 2026 — absenteísmo por transtornos mentais no funcional federal: 13,9 mi dias, R$ 3,94 bi (38%); "absenteeism… a health indicator of organizational distress"
12. AXENYA/IBEF-SP, 2024 — presenteísmo R$ 200–600 bi/ano; absenteísmo na indústria 3,5–5,0%; ciclo de adoecimento; 3–5% da folha

**Derivados no repo**
- `docs/00-portfolio-oportunidades.md` · `docs/01-produtos-brainstorm.md` · `docs/02-cruzamento-whatsapp.md` · `data/vigindustria-2026.md`
