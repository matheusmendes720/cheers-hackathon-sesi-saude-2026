# VigIndústria Brasil 2026 — dataset curado

> Fonte primária extraída e conferida página a página. Toda cifra abaixo vem do PDF original, com página e tabela.
> PDF: https://static.portaldaindustria.com.br/portaldaindustria/noticias/media/filer_public/fc/83/fc836c73-55b5-4ed7-9e4c-13a54a95786c/relatorio_vigindustria_-_conecta_saude_2026.pdf
> Cópia local: `docs/sources/vigindustria-2026.pdf` · texto integral extraído: `data/vigindustria-2026-raw.txt` (119 p.)

**Produção:** SESI + CN-SESI + Ministério da Saúde. Execução analítica: Universidade de Pernambuco.
**Campo:** julho–dezembro de 2025 · **n = 57.952 trabalhadores** · 825 empresas · 33 indicadores · 6 dimensões.
**Desenho:** transversal, multicêntrico, com amostra por conglomerados (empresas).

> **Cuidado com a citação:** a capa do PDF diz "VIGINDÚSTRIA BRASIL **2025**" — a edição foi *lançada* em 2026 (Conecta Saúde, 01/09/2026) e cobre campo de 2025. Ao citar, use "VigIndústria Brasil 2026 (campo 2025)" e não "VigIndústria 2025".

---

## Metodologia (p. 16–23)

| Item | Valor |
|---|---|
| Tipo | Estudo transversal, estimativa de frequência e distribuição de indicadores |
| Dimensões analisadas | 6 das 7 do **ASSTI** (Sistema de Avaliação em Saúde e Segurança do Trabalhador da Indústria, SESI 2023) — a 7ª (fatores de redução da produtividade) ficou de fora |
| Amostragem | Aleatória por conglomerados (n = 3.910) + conveniência (n = 54.042) = **57.952** |
| Base amostral | Empresas contributoras e não do SESI, via CNI (TCTF) e dados extraídos do **eSocial** |
| Precisão | 95% de confiança, erro máximo de 2 p.p. (3 p.p. em subcategorias: ≥60 anos, viúvo/divorciado, 4+ filhos) |
| Desagregação | Por região geográfica e fatores demográficos — **não** por UF (logisticamente inviável nesta onda) |
| Coleta | Profissionais de saúde designados pelo Departamento Regional do SESI em cada estado |
| Identificação | **Anonimizada, sem identificação do trabalhador**; recusa individual garantida |

**Viés declarado pelo próprio relatório (p. 17):** a amostra de conveniência (recrutamento de empresas que *voluntariamente* demandaram serviços ao SESI) pode comprometer a representatividade. O relatório afirma que comparou as características demográficas das duas estratégias e optou pela combinação. **Este é o principal contra-argumento a usar contra nós mesmos se a banca pressionar a representatividade.**

### Instrumento (p. 18–21, Anexo I p. 110–119)

O questionário **foi administrado por chatbot** — ferramenta que simula conversa humana por texto — embarcado em plataforma digital com preenchimento **online e offline** (offline em tablets, conectados depois a um servidor). O sistema fazia *skip logic* automático, crítica imediata de respostas inválidas, cronometragem da duração da entrevista e alimentação direta e contínua no banco de dados do ASSTI.

Validação: 3 grupos focais → matriz analítica → painel de especialistas (TCC > 80% na validade de face; IVC > 80% na validade de conteúdo) → estudo piloto → teste-reteste (PABAK > 0,7) → AFE + AFC (CFI = 0,973 · TLI = 0,971 · RMSEA = 0,060 · SRMR = 0,130).

> **O SESI já usa chatbot para questionário de saúde ocupacional, com coleta offline.** É um padrão já validado dentro da operação — não é uma aposta de laboratório.

---

## Indicadores — prevalências (IC 95%)

### Fatores comportamentais de risco (p. 26–40)

| Indicador | Prevalência | IC 95% | Cuts que importam | Pág/tab |
|---|---|---|---|---|
| Consumo **episódico pesado** de álcool | **34,2%** | 32,4–36,0 | micro/pequenas **37,3%** | 29 · T5 |
| Inatividade física no lazer | **44,3%** | 42,4–46,1 | mulheres **49,4%** | 34 · T8 |
| Tempo prolongado de tela | **33,9%** | 32,0–35,8 | sem filhos 45,1%; com acesso a plano 29,4% | 38 · T10 |
| Baixa frequência de frutas/hortaliças | 75,0% homens / 65,6% mulheres | — | — | 30 · T6 |
| Consumo excessivo de refrigerantes/sucos artificiais | 22,2% (maior porte) | 20,2–24,4 | menor porte 21,9% | 33 · T7 |
| Tabagismo | 6,5% | 6,0–7,1 | — | 27 · T4 |
| Tempo prolongado de TV | 8,1% | — | — | 36 · T9 |

**Contraste com a população geral:** o consumo episódico pesado de álcool é **~68% maior** que o Vigitel 2024 para adultos brasileiros (20,4%) — declarado pelo próprio relatório (p. 98).

### Bem-estar mental (p. 41–53)

| Indicador | Prevalência | IC 95% | Cuts que importam | Pág/tab |
|---|---|---|---|---|
| Elevado nível de estresse | **20,3%** | 18,7–22,0 | mulheres **26,2%** / homens 16,2%; ensino sup. incompleto 26,3%; menor porte 20,9% | 42 · T11 |
| Dificuldade de relaxar e usufruir do lazer | **18,7%** | 17,0–20,5 | ensino fundamental **25,7%**; sem plano de saúde 21,2% | 49 · T15 |
| Percepção negativa da qualidade do sono | **16,5%** | 15,0–18,1 | mulheres 19,4% / homens 14,5% | 47 · T14 |
| Relacionamentos interpessoais de baixa qualidade | **12,4%** | 11,0–13,8 | Centro-Oeste 12,1% → Sul 13,7%; menor porte 14,8% | 45 · T13 |
| **Insatisfação com as condições de trabalho** | **8,1%** | 7,4–8,8 | mulheres 7,9% / homens 8,2%; menor porte 7,6% | 51 · T16 |
| Pensamentos negativos e pessimistas persistentes | 7,5% | 6,4–8,7 | mulheres 9,0% / homens 6,4% | 44 · T12 |

### Morbidade referida (p. 54–74)

| Indicador | Prevalência | IC 95% | Cuts | Pág/tab |
|---|---|---|---|---|
| **Obesidade** | **22,7%** | — | micro/pequenas 24,2% | 55 · T17 |
| Problema crônico de coluna | **19,3%** | 17,9–… | maior porte 19,9% | 73 · T26 |
| Colesterol alto referido | 17,1% | 15,7–18,6 | — | 61 · T20 |
| Hipertensão arterial referida | 16,2% | 14,8–17,7 | — | 57 · T18 |
| Depressão referida | **11,8%** | 10,4–13,3 | homens 5,9%; ensino fundamental 6,9% | 69 · T24 |
| Asma ou bronquite asmática | 8,5% | 7,3–9,7 | — | 67 · T23 |
| Diabetes referido | 5,7% | 4,7–6,9 | homens 4,3% / mulheres 7,6% | 59 · T19 |
| Artrite ou reumatismo | 4,3% | 3,6–5,0 | homens 2,3% / mulheres 7,2%; menor porte 5,2% | 65 · T22 |
| AVC referido | 2,6% (menor porte) | 0,8–8,5 | — | 63 · T21 |
| Câncer referido | 1,6% | — | menor porte 2,9% | 71 · T25 |

### Percepção de saúde e autocuidado (p. 75–83)

| Indicador | Prevalência | IC 95% | Cuts | Pág/tab |
|---|---|---|---|---|
| Baixa frequência de controle de condições crônicas | 32% | 30,0–34,0 | micro/pequenas 38,2% | 76 · T27 |
| Percepção de saúde negativa | **7,9%** | 6,6–9,5 | mulheres **10,6%** | 80 · T29 |
| Percepção de saúde bucal negativa | 7,1% | 5,9–8,5 | — | 82 · T30 |
| Atitude negativa para o autocuidado | 6,3% | 5,3–7,4 | — | 78 · T28 |

### Cultura de segurança (p. 84–97) — indicadores **positivos**

| Indicador | Proporção | IC 95% | Cuts | Pág/tab |
|---|---|---|---|---|
| Segurança e prevenção são importantes para a empresa | 79,7% | 75,1–83,7 | — | 85 · T31 |
| **Percepção de ambiente de trabalho seguro** | **71,4%** | 69,6–73,1 | <30 anos **67,7%** / ≥60 80,1%; menor porte 69,8% | 87 · T32 |
| **Liderança obedece e encoraja a obediência às normas de segurança** | **72,6%** | 70,7–74,4 | — | 89 · T33 |
| Empresa prioriza esforços suficientes para prevenção de acidentes | 70,2% | 66,6–73,6 | — | 91 · T34 |
| **Recebe treinamento para emergências e prevenção de acidentes** | **69,8%** | 68,1–71,5 | **micro/pequeno 59,5%** vs médio/grande **72,9%** | 93 · T35 |
| **Comunicação suficiente e adequada sobre prevenção de acidentes** | **65,6%** | 63,8–67,3 | homens 67,7% / mulheres 62,4% | 95 · T36 |

---

## A grade do Anexo I → o que o VigIndústria mede (e o que não mede)

O Anexo I do regulamento do hackathon pede **quatro dimensões**: *comportamento, ambiente, organização do trabalho, participação das pessoas*, com destino em *autonomia, participação, bem-estar e senso de propósito*.

| Dimensão do Anexo I | Onde o VigIndústria mede | Lacuna |
|---|---|---|
| **Comportamento** | Bloco comportamental completo (álcool 34,2%, sedentarismo 44,3%, tela 33,9%, tabaco 6,5%) | Mede, mas não **prioriza por recorte**: nada no sistema diz "aqui está o foco desta empresa" |
| **Ambiente** | Percepção de ambiente seguro 71,4% · Insatisfação com condições de trabalho 8,1% | Dois indicadores, nenhum ligando ambiente → desfecho de saúde |
| **Organização do trabalho** | Liderança 72,6% · Prevenção 70,2% · Treinamento 69,8% · Comunicação 65,6% · Estresse 20,3% | Indicadores de **cultura**, nenhum de **organização** (jornada, autonomia, carga, apoio social) |
| **Participação das pessoas** | **NENHUM INDICADOR** | O instrumento não mede participação, autonomia, decisão, sugestão, propósito, confiança ou segurança psicológica |

### Verificação no instrumento (Anexo I do relatório, p. 110–119)

Busca literal no questionário completo:

| Termo | Ocorrências |
|---|---|
| autonomia / autônomo | **0** |
| decisão / decidir | **0** |
| sugestão | **0** |
| engajamento | **0** |
| voz do trabalhador | **0** |
| propósito | **0** |
| confiança | **0** |
| segurança psicológica | **0** |
| participação | 2 — (a) "participou de atividade de promoção da saúde?", (b) tempo de tela em redes sociais |

> **Achado central.** O relatório *recomenda* (p. 98): *"fortalecimento das competências de liderança para promover uma comunicação aberta e um ambiente psicologicamente seguro"*. Mas o instrumento **não tem nenhum item que meça ambiente psicologicamente seguro, autonomia ou participação**. A medição cobre risco, bem-estar, morbidade, autocuidado e cultura de segurança — e para no limite do que a empresa oferece. **Não mede o que o trabalhador exerce.**
>
> É exatamente a lacuna que o Anexo I nomeia como direção do desafio: **autonomia, participação, bem-estar e senso de propósito.**

---

## As recomendações do relatório (p. 98–101) — onde está o software

Citações literais que definem o espaço de oportunidade:

1. **p. 98** — *"aproximadamente um em cada cinco trabalhadores(as) são obesos"*; *"elevada prevalência de consumo episódico pesado de bebidas alcoólicas… 34,2%"*, *"~68% maior que o observado em adultos brasileiros (20,4%)"*.
2. **p. 98** — *"no âmbito organizacional, orienta-se o fortalecimento das competências de liderança para promover uma comunicação aberta e um ambiente psicologicamente seguro"*.
3. **p. 99** — *"trabalhadores com menor escolaridade apresentaram indicadores de autocuidado e percepção de saúde mais frágeis, o que sugere uma **barreira informacional** e, possivelmente, de acesso a serviços de saúde"*.
4. **p. 99** — *"recomenda-se a implementação de **campanhas direcionadas ao aumento da literacia em saúde**"*.
5. **p. 99** — *"orienta-se que as **empresas integrem o apoio ao autocuidado na cultura organizacional**"*.
6. **p. 99–100** — *"há espaço para implementação de intervenções, em especial no tocante à realização de treinamentos para emergências… e na **melhoria das ações de comunicação**"*.
7. **p. 100** — *"A continuidade do **monitoramento sistemático por meio do VigIndústria será fundamental para validar a efetividade das intervenções** em andamento e, por conseguinte, a eventual necessidade de reorientá-las"*.
8. **p. 100** — *"a utilização dos dados do sistema **ASSTI pode auxiliar na customização** das ações de acordo com as necessidades específicas de cada região e dos diferentes setores de produção industrial"*.
9. **p. 100** — *"é imperativo que as indústrias adotem **modelos de intervenção baseados em evidências**"*.
10. **p. 100** — referência ao **Plano DANT 2021–2030** do Ministério da Saúde como marco de política pública.

### O que essas recomendações implicam

| Recomendação | O que falta hoje | Lacuna de software |
|---|---|---|
| Monitoramento sistemático e **contínuo** (p. 100) | O VigIndústria é **transversal, de um tempo só** (jul–dez/2025) | Nada mede se a intervenção funcionou — não há antes/depois |
| **Customização por região e setor de produção** via ASSTI (p. 100) | A customização é "auxiliar", não é produto | Nenhum sistema transforma dado de ASSTI em plano de ação por empresa |
| **Campanhas de literacia em saúde** (p. 99) | Campanhas são genéricas | Nenhuma camada que segmente por escolaridade, que é o fator que mais prediz fragilidade de autocuidado |
| **Ambiente psicologicamente seguro e liderança** (p. 98) | Recomendado mas **não medido** | Não há indicador de autonomia/participação para pilotar nem demonstrar efeito |
| **Empresas integrarem autocuidado na cultura organizacional** (p. 99) | Sem ferramenta, depende de advise manual | Nenhum fluxo que entregue campanha → adesão → retorno medido |

---

## Como este dataset pode virar protótipo (e o que ele NÃO é)

**O que dá para usar agora, offline:**
- O **instrumento validado** (Anexo I do relatório, p. 110–119) — 10 páginas de questionário pronto, com skip logic e domínios já mapeados.
- Os **33 indicadores com prevalência nacional e CIs** — dataset sintético de agregação com recorte por região, porte, sexo, idade, escolaridade, estado civil, nº de filhos, acesso a plano de saúde.
- As **6 dimensões do ASSTI** e os **critérios de validação** (CFI 0,973; PABAK > 0,7) — dá para replicar a validação do nosso instrumento no protótipo, o que é sinal fortíssimo de sofisticação técnica para a banca.

**O que este dataset NÃO é:**
- Não é dado individualizado — é **agregado e autorrelatado**. Nada de nível de trabalhador.
- Não é dado de absenteísmo, custo, sinistralidade ou ASO. Não há números de afastamento aqui.
- Não substitui acesso ao ASSTI: o sistema real é do SESI e não está liberado (pergunta pendente para a organização).

---

## Referência completa

- **Relatório:** SESI, CN-SESI, Ministério da Saúde. *VigIndústria Brasil 2026* — 119 p. fieldwork jul–dez/2025.
- **PDF:** https://static.portaldaindustria.com.br/portaldaindustria/noticias/media/filer_public/fc/83/fc836c73-55b5-4ed7-9e4c-13a54a95786c/relatorio_vigindustria_-_conecta_saude_2026.pdf
- **Lançamento:** Conecta Saúde 2026, FIESP/SP, 01/09/2026.
- **SESI/ASSTI:** sistema de avaliação em saúde e segurança do trabalhador da indústria (SESI, 2023) — 7 dimensões, 6 analisadas aqui.
- **Contexto de política:** Plano DANT 2021–2030 (Ministério da Saúde); Guia de Atividade Física; Guia Alimentar; Cadernos de Atenção Básica.
- **Contraste populacional:** Vigitel 2024 — adultos brasileiros, consumo episódico pesado 20,4%.
