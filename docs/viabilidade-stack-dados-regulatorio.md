# Viabilidade técnica e regulatória — protótipo SESI Saúde (≈30 h, 2 devs)

`[fato]` verificado em 27/10/2026 · `[hipótese]` leitura nossa · `[a confirmar]` depende da organização.

**Correção de premissa:** a norma de IA em medicina não é a Res. CFM 2.328/2022 (orçamentária do CFM), e sim a **Res. CFM nº 2.454/2026** (DOU 27/02/2026), **vigente desde 26/08/2026** — já vale em 14/11. Exige supervisão humana e proíbe delegar diagnóstico, prognóstico e decisão terapêutica à IA. `[fato]`

## Stack vs. critérios da banca

| Opção | Setup (h/dev) | Offline | Maturidade | Sofisticação | UX | Veredicto |
|---|---|---|---|---|---|---|
| Vite + React + TS, dados locais (JSON + SQLite) | 4 | sim | 4 | 3 | 4 | **base recomendada** |
| Next.js (export estático) | 6–8 | sim | 4 | 4 | 4 | ok; build consome folga |
| Python + Streamlit/Gradio | 3 | sim | 3 | 3 | 3 | fallback para a parte de IA |
| PWA instalável (service worker) | +2 | sim | 4 | 4 | 5 | **melhor custo/benefício: app no celular sem loja** |
| Tauri / Electron desktop | 6–10 | sim | 3 | 4 | 3 | não compensa |
| Flutter / React Native | 12–20 | sim | 3 | 4 | 5 | cortar: a banca não tem device |
| LLM local (llama.cpp/Ollama, GGUF 1–3 B) | +3 e 1–2 GB | sim | 3 | 5 | 3 | só se sobrar tempo |

Sofisticação vem de **dados e padrões**, não de framework. Vite + PWA sobra folga para 2 devs. `[hipótese]`

**Posicionamento a assumir no pitch:** a Res. CFM 2.454/2026, art. 12-13 e Anexo II, I, classifica de **baixo risco** a IA que "não exerce influência decisória direta em diagnósticos ou tratamentos individuais, atuando tipicamente em funções administrativas, operacionais ou de apoio de baixo impacto". As tarefas abaixo cabem nessa faixa. `[fato]`

## Datasets públicos

| Dataset | URL | Granularidade | Offline | Uso na solução |
|---|---|---|---|---|
| CAT — INSS (acidentes de trabalho) | `dadosabertos.inss.gov.br/dataset/comunicacoes-de-acidente-de-trabalho-cat-plano-de-dados-abertos-jun-2023-a-jun-2027` | 1 acidente: CID-10, CBO, CNAE, natureza da lesão, afastamento | sim (CSV mensal) | **núcleo**: sinistralidade, absenteísmo, mapa de risco |
| VigIndústria Brasil 2026 (baixado, não versionado) | `static.portaldaindustria.com.br/.../relatorio_vigindustria_-_conecta_saude_2026.pdf` | agregada: 825 empresas, 57.952 trabalhadores, 33 indicadores | sim | baseline do pitch e 4 dimensões do Anexo I |
| ANS Panorama nov/2025 (baixado, não versionado) | `docs/sources/ans_panorama_nov2025.pdf` | agregada nacional | sim | despesas assistenciais e sinistralidade setorial |
| ANS SIB/ICB por UF | `dadosabertos.ans.gov.br/FTP/PDA/dados_de_beneficiarios_por_operadora/` | por beneficiário, sem dado clínico (BA ≈ 44 MB) | sim | absenteísmo/turnover por perfil |
| ANS TISS ambulatorial/hospitalar + dicionário | `dadosabertos.ans.gov.br/FTP/PDA/TISS/` | mensal por UF, XML | sim (1 UF/1 mês) | custo assistencial; prova de leitura de padrão real |
| ANS painel de glosas | `dadosabertos.ans.gov.br/FTP/PDA/painel_de_glosas-057/` | agregada | sim | custo da negação: onde o modelo vaza dinheiro |
| DATASUS TabNet (SIA, SIH, SIM, SINAN, CNES) | `tabnet.datasus.gov.br` | agregada por município/UF/CID/procedimento | sim (exporta CSV) | contexto e comparabilidade |
| e-SUS AB / Sisab (Previne) | `dadosabertos.saude.gov.br` | agregada municipal | sim | atenção primária como contraponto ao modelo corporativo |
| IBGE SIDRA (PNS, PNAD Contínua) | `apisidra.ibge.gov.br` | agregada | sim | denominadores populacionais |
| CID-10 (`CID10CSV.ZIP`, 297 KB) | `www2.datasus.gov.br/cid10/V2008/descrcsv.htm` | código → descrição | sim | padronizar saída e agrupar causas |
| eSocial S-1.3: leiautes + XSD (S-2210, S-2220) | `gov.br/esocial/pt-br/documentacao-tecnica` | schema XML | sim | base do validador de conformidade |

**Não utilizáveis:** ASSTI/CN-SESI e dados das empresas do MES (sem acesso público); microdados do Censo 2022 (acesso controlado); TISS nacional completo (GB); eSocial enviado (certificado digital); base individualizada de trabalhadores (LGPD); "MIME/CGHS" não corresponde a nenhuma base pública identificável — o catálogo oficial de padrões é o CPIISS (Portaria 2.073/2011) `[a confirmar]`.

## Padrões de interoperabilidade

| Padrão | Para quê | Realista em 30 h? | Sinal para a banca |
|---|---|---|---|
| HL7 FHIR R4, perfil RNDS | Bundle/Questionnaire/Observation em JSON | sim (3–6 h) | **alto** — padrão oficial do país (Portaria 1.434/2020; Decreto 12.560/2025) |
| eSocial S-2210/S-2220 + XSD | validar e gerar XML de CAT/ASO | sim (4–8 h) | **alto** — leiaute do governo, conferido por schema |
| CID-10 / CBO / CNAE | vocabulário dos campos | sim | médio |
| TISS | ler um arquivo mensal + dicionário | parcial | médio (regulador reconhece) |
| OpenEHR, HL7 CDA, DICOM, LOINC, SNOMED-CT | interoperabilidade plena | não | zero valor em 30 h |

## Tarefas de IA / software defensáveis

| Tarefa | Viabilidade | Risco | Dado | O que a banca vê |
|---|---|---|---|---|
| Classificar relato de turno (texto → tema de risco; TF-IDF/logreg) | 5 | Baixo | texto sintético de SST | IA como apoio, supervisionada (Res. 2.454/2026) |
| CID-10 → grupo de doença ocupacional (determinístico) | 5 | Baixo | CAT + CID-10 | terminologia oficial, não chute |
| Mapa de risco CNAE × natureza da lesão × afastamento | 5 | Baixo | CAT (INSS) | preventivo, não apenas reativo |
| Prever dias de afastamento por equipe/mês | 4 | Baixo-Médio | CAT + agregados | modelo com AUC e validação honesta |
| Relatório analítico do PCMSO (NR-7, item 7.6.2) | 4 | Médio | agregados | entregável que o SESI emite |
| Checklist PGR → exames de vigilância (NR-1 1.5.5.4 + NR-7 7.5) | 4 | Médio | PGR sintético | liga risco a plano de cuidado |
| Validador eSocial S-2210/S-2220 + gerador de XML | 4 | Baixo | XSD oficial | sofisticação técnica verificável |
| Export FHIR (Bundle RNDS) do plano de vigilância | 4 | Baixo-Médio | sintético | ponte com o RNDS do Ministério da Saúde |
| Chat das normas (NR-1, NR-7, Res. 2.454/2026) com citação + fallback por regras | 3 | Médio | PDFs das normas | IA auditável, sem "oráculo" |
| Painel de vigilância agregada por setor (sinais psicossociais, afastamento, tendência) | 4 | Médio | VigIndústria + sintético | nível gestor, zero laudo individual |

## 3 tarefas que NÃO vamos fazer

1. **Score individual de risco que vire decisão de emprego** ("apto/inapto", afastamento, escolha de plano). CLT art. 442: exame pré-admissional só se justifica quando o PGR indica risco específico (STF, 2016, RE 828.580/837.610 `[a confirmar]` os números); LGPD art. 11 § 5 (vedada seleção de riscos na contratação); NR-7 (ASO é ato médico).
2. **Diagnóstico, parecer, triagem automática ou prescrição.** Res. CFM 2.454/2026: art. 4º, I e § 2º (IA só como apoio; vedado delegar diagnóstico, prognóstico ou decisão terapêutica); art. 18, § 2º (ato médico é sempre do médico); art. 11 (uso de IA deve ser explicado ao paciente); Res. CFM 2.314/2022 (teleconsulta exige médico e consentimento); Res. CFM 2.327/2022 (procedimento não reconhecido é proibido).
3. **Emitir ASO/atestado e usar dado real de trabalhador.** Res. CFM 2.382/2024, art. 1º (Atesta CFM oficial e obrigatório, *inclusive para atestados de saúde ocupacional*; efeitos suspensos pelo TRF-1, Proc. 1087770-91.2024.4.01.3400) + LGPD art. 11 e 13 (dado sensível; base legal e ambiente controlado) + ANVISA RDC 751/2022, regra 11 (software que alimenta decisão diagnóstica = SaMD classe II, notificação obrigatória).

## Referências

- CFM Res. 2.454/2026 (IA na medicina) — https://sistemas.cfm.org.br/normas/arquivos/resolucoes/BR/2026/2454_2026.pdf — 27/02/2026
- CFM Res. 2.314/2022 (telemedicina) — https://sistemas.cfm.org.br/normas/arquivos/resolucoes/BR/2022/2314_2022.pdf — 05/05/2022
- CFM Res. 2.327/2022 (terapêuticas reconhecidas) — https://sistemas.cfm.org.br/normas/arquivos/resolucoes/BR/2022/2327_2022.pdf — 10/01/2023
- CFM Res. 2.382/2024 (Atesta CFM) — https://sistemas.cfm.org.br/normas/arquivos/resolucoes/BR/2024/2382_2024.pdf — 06/09/2024
- Portaria GM/MS 1.434/2020 (Conecte SUS, RNDS, padrões) — https://bvsms.saude.gov.br/bvs/saudelegis/gm/2020/prt1434_29_05_2020.html
- Portaria GM/MS 2.073/2011 (CPIISS: HL7, SNOMED-CT, TISS, DICOM, LOINC) — https://bvsms.saude.gov.br/bvs/saudelegis/gm/2011/prt2073_31_08_2011.html
- Decreto 12.560/2025 (RNDS e SUS Digital) — https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12560.htm
- Guia de Implementação RNDS (FHIR R4) — https://rnds-fhir.saude.gov.br/
- LGPD (Lei 13.709/2018, art. 11 e 13) — https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm
- ANVISA RDC 751/2022 (Anexo I, regra 11 — SaMD) — https://anvisalegis.datalegis.net/action/ActionDatalegis.php?acao=detalharAto&tipo=RDC&numeroAto=00000751&seqAto=000&valorAno=2022
- NR-7 (PCMSO) — https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-partitaria-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/nr-07-atualizada-2022-1.pdf
- NR-1 (GRO/PGR) — https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-partitaria-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/nr-01-atualizada-2025-i-1.pdf
- ANS dados abertos — https://dadosabertos.ans.gov.br/FTP/PDA/ — INSS CAT — https://dadosabertos.inss.gov.br/pt_PT/dataset/inss-comunicacao-de-acidente-de-trabalho-cat
- eSocial leiautes e XSD S-1.3 — https://www.gov.br/esocial/pt-br/documentacao-tecnica — Portal SUS — https://dadosabertos.saude.gov.br/ — TabNet — http://tabnet.datasus.gov.br
- VigIndústria Brasil 2026 — https://static.portaldaindustria.com.br/portaldaindustria/noticias/media/filer_public/fc/83/fc836c73-55b5-4ed7-9e4c-13a54a95786c/relatorio_vigindustria_-_conecta_saude_2026.pdf
