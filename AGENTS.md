# AGENTS.md

Workspace da equipe **Cheers** para o **Hackathon+ SESI Saúde** (SESI Bahia + Grupo Rede+, Salvador, 14–15/11/2026). Tema: *"Desafios e soluções para a sustentabilidade dos modelos assistenciais de saúde"*.

**Até 12/11 o foco é pesquisa e roteiro de pitch. Nenhum código de produto antes do desafio ser revelado** — decisão do time em 27/10/2026, agora respaldada pelo regulamento (§7.3).

---

## Fontes de verdade

Ordem de precedência quando houver conflito:

1. **Regulamento 2026** — `Regulamento Hackathon SESI Saude 2026.pdf` (no repo). Data de 08/10/2026, assinado em Salvador. É o documento que rege. *Ressalva: o cabeçalho diz "Minuta" e o item 6.1 ressalva que a programação pode mudar.*
2. [Notícia oficial](https://www.sesibahia.com.br/detalhes-noticia?id=8312) — SESI Bahia, 09/10/2026
3. [Landing page oficial](https://materiais.sesibahia.com.br/hackathon-saude) — formulário, tamanho de equipe
4. [Formulário de inscrição](https://forms.cloud.microsoft/r/gzFVj3UiGX) — Microsoft Forms
5. [VigIndústria Brasil 2026](https://static.portaldaindustria.com.br/portaldaindustria/noticias/media/filer_public/fc/83/fc836c73-55b5-4ed7-9e4c-13a54a95786c/relatorio_vigindustria_-_conecta_saude_2026.pdf) — relatório-base, ver [agenda](#agenda-de-pesquisa)
6. `chat.md` / `chat.txt` — contexto do time. **Contém erros factuais** — ver [Correções](#correções-pendentes)

Item citado como `§N` = item do regulamento. Item `[a confirmar]` = precisa de verificação com a organização.

---

## Cronograma (§6.2)

| Data | O quê |
|---|---|
| 09/10/2026 | Lançamento das inscrições |
| **08/11/2026** | **Encerramento das inscrições** (gratuito) |
| **12/11/2026** | Divulgação dos selecionados por e-mail + live de orientações às **13h** |
| **13/11/2026** | Live de abertura a partir das **18h30** — capacitações e formação das equipes (**online**) |
| **14/11/2026** | **Check-in às 07h30** — abertura, desenvolvimento e mentorias (presencial) |
| **15/11/2026** | Desenvolvimento e mentorias · **entrega do protótipo até 15h30** · **apresentação do pitch a partir das 16h** · avaliação e premiação, **encerramento às 19h** |

Em 27/10/2026 faltam **12 dias** para o fechamento das inscrições.

**O presencial são 2 dias (14 e 15).** O 13/11 é a live online. O próprio regulamento se contradiz: §2.4 fala em *"três dias imersivos"*, mas §2.6 diz *"presencialmente em Salvador, Bahia, nos dias 14 e 15 de novembro"* e §6.2 em *"duração de 02 dias imersivos"*. O cronograma (§6.2) é o operativo; as páginas de marketing dizem "13 a 15" e "três dias".

Duas consequências práticas: check-in às **07h30 no dia 14** significa sair de casa por volta das 5h30; e **13/11 à noite, todo mundo precisa estar online** para a live de abertura — se alguém contava com 13 dias de imersão presencial, está errado.

---

## Como a nota é calculada (§8) — a informação mais importante deste arquivo

Duas comissões julgadoras. Cada avaliador dá nota de **1 a 5** por critério; a nota de cada equipe é a média dos avaliadores.

```
Nota Final = (Nota do Pitch × 6) + (Nota do Protótipo × 4)
```

| Bloco | Critérios | Peso no total |
|---|---|---|
| **Pitch** (3 min) | Impacto · Inovação · Viabilidade | **60%** (20% cada) |
| **Protótipo** | Maturidade · Sofisticação técnica · Experiência do usuário | **40%** (13,3% cada) |

> **Cada critério do pitch vale 1,5× cada critério do protótipo.** Consequência direta: um protótipo excelente com pitch medíocre **perde** para um protótipo bom com pitch forte. A narrativa de 3 minutos é o ativo mais valioso da equipe — é onde a nota se decide.

Não está no regulamento: se a demo do protótipo entra dentro dos 3 minutos ou se o protótipo é julgado à parte, a partir do protótipo entregue às 15h30. **Levar essa pergunta à organização** (§8.3 não diz). A leitura conservadora: tratar os 3 minutos como se fossem a única chance de impressionar.

---

## O que o desafio realmente pede (Anexo I)

O Anexo I do regulamento é o texto que define a direção. Vale ler inteiro — ele **desafia a leitura óbvia** do tema.

> "A resposta, portanto, não está apenas na incorporação de novas tecnologias ou na ampliação da oferta de serviços, mas no **redesenho dos próprios modelos assistenciais**, tornando-os mais integrados, participativos e conectados às necessidades reais das pessoas e das organizações."

Pontos que moldam a solução:

- **Superar a lógica curativa e de controle de risco** → avançar para modelos que fortaleçam **autonomia, participação, bem-estar e senso de propósito** dos trabalhadores.
- **Quatro dimensões a articular** — *comportamento, ambiente, organização do trabalho, participação das pessoas*. Uma solução que cobre só uma delas está incompleta; a que articula as quatro é a que tem potencial de mudança duradoura.
- **Não olhar problemas isolados** — o desafio é a transformação do modelo, não um episódio de cuidado.
- **Contexto do SESI:** saúde do trabalhador como **fator estratégico** para competitividade, produtividade e sustentabilidade; crescimento de custos, doenças crônicas, necessidade de modelos mais eficientes.

**Armadilha a evitar:** um app que só rastreia atividade física ou entrega telemedicina é exatamente a "incorporação de novas tecnologias" que o Anexo I diz que *não* é a resposta. A tecnologia é meio, não tese.

**Os 3 eixos do MES para 2026–2027** (Lacerda, [*FIEB*](https://fiepb.com.br/fiep/noticia/movimento-empresarial-pela-saude-recebe-premio-por-boas-praticas-em-saude-sustentavel)) — o desafio é literalmente o eixo 3:

1. **Dados e Inteligência em Saúde** — reduzir fragmentação, fortalecer governança da informação
2. **Promoção da Saúde e Prevenção** — antecipar o cuidado reduz custos e pressões sobre o sistema
3. **Modelos Assistenciais Sustentáveis** — eficiência, qualidade e equilíbrio econômico ← *é o tema do hackathon*

**Origem dos desafios (§7.2, Anexo I):** as questões levantadas pelas empresas participantes do **Conecta Saúde 2026**. O Anexo I cita um encontro do MES **durante o Conecta Saúde em 15/10/2026** `[a confirmar]` — além do Conecta Saúde Nacional de 01/09 (FIESP/SP, 500+ pessoas). Os detalhes dos desafios são apresentados **na abertura, às equipes** (§7.3).

---

## O que a organização já define

- **Desafios:** das questões levantadas por empresas no Conecta Saúde 2026. Detalhamento revelado na abertura (§7.3).
- **Eixos temáticos:** IA aplicada à saúde, saúde mental, inovação e novos modelos de cuidado.
- **Entregável (§6.3):** protótipo funcional **+** apresentação em pitch de **3 minutos**.
- **Equipe (§5.1, §5.3):** **4 a 6 pessoas**, composição multidisciplinar preferencial:
  - 1 **gestor** — administração, comercial, financeiro, planejamento, estratégia
  - 1 **designer** — design gráfico, webdesign, comunicação
  - 2 **TI** — capacidade de desenvolvimento de produto tecnológico
  - 1 **especialista** na problemática do desafio
- **Vagas (§4.1):** 72 pessoas, 12 equipes. Seleção por qualidade do formulário + conhecimento do tema.
- **Público (§3.6):** 18+, profissionais e acadêmicos de saúde, TI, design, gestão.
- **Prêmios (§9):** R$ 9.000 / R$ 4.000 / R$ 2.000, por ranking de nota final.
- **Inscrição (§3.3):** cada integrante se inscreve **individualmente**, informando o nome do grupo. Nome do time: **"Cheers"**.
- **Certificado (§6.5):** PDF por e-mail, em até 30 dias após o encerramento. Só para quem submeteu o produto **em equipe**.
- **Prazo de resposta (§4.3):** confirmar a participação em até **24 h** após o e-mail, sob pena de perder a vaga.

### Restrições práticas que a equipe ainda não mapeou

- **§11.2 — não é fornecido material tecnológico.** *"Não será fornecido nenhum material tecnológico como notebooks e computadores para as equipes."* Cada um leva o próprio note, carregador, extensão, mouse, hdmi. **A demo vai rodar na máquina de um dos membros.**
- **§11.3 — sem dormitório**, mas todos podem dormir e usar os chuveiros no local. Planejar onde dormir.
- **§9.3 e §9.5 — o prêmio cai na conta do líder da equipe.** *"A premiação concedida será depositada exclusivamente na conta bancária do membro indicado como líder da equipe."* Precisa de líder designado e conta informada à organização. E §9.7 é explícito: *"A destinação da premiação é de responsabilidade exclusiva de cada equipe vencedora, não cabendo à Comissão Organizadora... qualquer envolvimento em questões ou desacordos entre os membros da equipe."* Ou seja: se o combinado entre vocês não for sólido, **a organização não media**. Isso é conversa de time antes do dia 14, não detalhe de secretaria.
- **§10.1–10.3 — cessão de imagem e voz:** gratuita, definitiva, irrevogável, sem limite territorial ou temporal, inclusive para o nome e as características da solução.
- **§10.8 — os direitos autorais continuam com os criadores.** A equipe vencedora *pode* ceder a PI ao SESI BA na submissão, se não quiser desenvolver o projeto. **Não assinar cessão de PI sem decisão explícita do time.**
- **§10.6 — os participantes assumem responsabilidade total pela originalidade** da solução. Não reempacotar produto existente.
- **§3.7 — vedada a participação** de quem tenha vínculo empregatício ou contratual com o SESI BA.
- **§11.11 — o formulário pode conter autorização de divulgação** do escopo e das funcionalidades do projeto. Ler antes de submeter.

---

## Correções pendentes

Erros que circulam no grupo do WhatsApp. **Nenhum agente deve propagá-los.**

1. **ODS.** A página oficial e o próprio regulamento (§2.1) dizem "ODS 2 – Saúde e Bem-Estar". É erro de numeração do SESI: na Agenda 2030, **Saúde e Bem-Estar é o ODS 3**; ODS 2 é Fome Zero e Agricultura Sustentável. O resumo do Gemini compartilhado em 25/10 (`chat.md` 23:15) descreve ODS 2 como agricultura — agrotech, cadeia de frio, biotecnologia. **Material de outro domínio, inservível aqui.** A lista dos 17 objetivos que o Gabriel mandou está correta; ela é que contradiz o rótulo numérico do SESI.
   > Regra: toda referência a ODS neste workspace é **ODS 3 (Saúde e Bem-Estar) + ODS 9 (Indústria, Inovação e Infraestrutura)**.

2. **Prazo.** O grupo discute "jaja fecha" (25/10) e o print de 07/10 mostra 22/10 — mas 22/10 é o prazo do **Programa Aluno Empreendedor** (SENAI/CIMATEC/SEBRAE), outro programa. O prazo do hackathon é **08/11** (§3.1).

3. **Inscrição.** O formulário exige inscrição **individual de cada participante**, mesmo com time formado (§3.3.1, §5.2). Não basta um único envio do time.

4. **Duração.** O documento que o Moisés colou no grupo diz "três dias imersivos" — e o regulamento diz o mesmo em §2.4. Mas o cronograma (§6.2) e o §2.6 delimitam o presencial em **14 e 15/11** (2 dias), com 13/11 online. §6.1 ressalva que a programação é planejamento e pode mudar.

---

## Equipe Cheers

| Membro | Contribuições | Papel proposto | Slot §5.3 |
|---|---|---|---|
| **Matheus Mendes** (`You`) | Programa Aluno Empreendedor (SENAI/CIMATEC/SEBRAE), Liga Jovem do SEBRAE 2026 | Coordenação do repo e do time; tech, front e UX do protótipo; **Product Owner** | TI (1/2) |
| **luquinhas** (`+55 71 9668-7060`) | Formado pelo SENAI; hackathons anteriores | Tech; velocidade de prototipação | TI (2/2) |
| **Omena** (`+55 71 9371-4666`) | SENAI; visão de produto | Visão de produto e de negócio; experiência do cliente | **Gestor** |
| **Moisés** (`+55 71 8739-0343`) | Informática em saúde; professor orientador com doutorado em IA no atendimento médico; estágio e práticas em saúde | Domínio técnico de IA em saúde; **se voluntariou para o pitch** | **Especialista** |
| **Gabriel Esteves** | Parceiro que cursa medicina | Articulação com o ecossistema SESI/MES; validação clínica | **Designer** ⚠️ |

**⚠️ Gap a resolver (§5.3):** a estrutura preferencial pede 1 designer. O time tem 5 pessoas e mapeia 4 slots claramente — **ninguém está oficialmente no slot de design.** É "preferencialmente", não obrigatória, mas §5.4.1 prioriza as equipes indicadas no formulário e §4.1 avalia a qualidade do preenchimento. Decidir explicitamente quem cobre design (e escrever no formulário) é mais forte do que deixar implícito.

**⚠️ Atenção ao tamanho (§5.4.2):** *"Equipes com menos de seis participantes serão complementadas a partir das demais inscrições individuais, a partir da indicação da Comissão Organizadora."* O time é 5. A leitura otimista é que §5.4.1 (equipes indicadas em campo específico são priorizadas) protege a formação; a pessimista é que um 6º membro é indicado pela organização e entra na equipe. **Isso não está definido.** Levar à organização (pergunta abaixo) e ter a resposta antes de 08/11 — decidir entre recrutar um 6º integrante deliberado ou arriscar a composição.

**Inscrição:** Omena e Moisés confirmaram inscrição em 25/10. **Esteves, luquinhas e Matheus — não confirmado.** Todos precisam se inscrever individualmente (§3.3.1) e informar o time "Cheers" (§5.2).

**Composição:** 5 pessoas — dentro do "4 a 6" (§5.1). Cobre saúde (Moisés, Esteves+medicina), tech (Matheus, luquinhas), produto/negócio (Omena).

### Decisões em aberto

| # | Decisão | Responsável | Prazo |
|---|---|---|---|
| D1 | Confirmar inscrição individual dos 5 e o vínculo ao time "Cheers" | cada um | **08/11** |
| D2 | Nicho dentro de saúde corporativa para atacar | Esteves + Moisés + Omena | 10/11 |
| D3 | 10 ideias → shortlist de 3 → 1, pela rubrica | Matheus conduz | 11/11 |
| D4 | Speaker do pitch (Moisés se voluntariou) | time | 12/11 |
| D5 | Stack e arquitetura do protótipo | Matheus + luquinhas | **13/11**, na live de abertura |
| D6 | Perguntas para mentores (abaixo) | time | 13/11 |
| D7 | Quem cobre o slot de **designer** (§5.3) | time | **08/11** — vai no formulário |
| D8 | **Líder da equipe** para receber o prêmio (§9.5) + quem informa a conta | time | 10/11 |
| D9 | **Inventário de equipamento** — cada um leva note, carregador, extensão, mouse, hdmi (§11.2) | cada um | 12/11 |
| D10 | Onde dormir no local (sem dormitório, com chuveiro) (§11.3) | time | 12/11 |
| D11 | **Time de 5 ou 6?** — §5.4.2 completa equipes com menos de 6; confirmar com a organização antes de fechar a inscrição | Matheus | **08/11** |
| D12 | **Disponibilidade online em 13/11, 18h30** para a live de abertura | todos | 13/11 |

---

## Escopo até 12/11

**Permitido:** pesquisa, análise, dados públicos, notas de pitch, mockups estáticos, ensaio oral, roteiro de demo.

**Proibido:** código do produto, arquitetura fechada, stack decidida, protótipo funcional. Motivo: §7.3 — o detalhamento do desafio **só é apresentado na abertura, às equipes**. Construir antes não bate com o tema real e quebra o nívelamento entre as 12 equipes.

**Métrica de sucesso em 12/11:** 1 problema definido com evidência, 3 hipóteses ranqueadas, 1 roteiro de 3 min ensaiado em voz alta, 8 perguntas para os mentores, stack decidida no dia seguinte com o desafio real à vista.

---

## Agenda de pesquisa

**Status em 27/10/2026 — itens 1, 2, 7 e 8 já concluídos.** Não refazê-los; ler os artefatos:

| Concluído | Onde está |
|---|---|
| 1 · VigIndústria Brasil 2026 | `data/vigindustria-2026.md` (indicadores com página e tabela) + `docs/sources/vigindustria-2026.pdf` |
| 2 · As 4 dimensões do Anexo I | `docs/00-portfolio-oportunidades.md` §2 · **a lacuna é a 4ª dimensão: 0 itens no instrumento para autonomia, participação, propósito, segurança psicológica** |
| 7 · Regulação e risco | `docs/viabilidade-stack-dados-regulatorio.md` — Res. CFM 2.454/2026 (IA em medicina, baixo risco no Anexo II, I), Res. 2.382/2024 (Atesta CFM cobre ASO), LGPD art. 11, NR-1/NR-7 |
| 8 · Benchmark | `docs/pesquisa/01-mapa-competitivo.md` — 11 players, 5 camadas descobertas, 5 armadilhas |

Pendentes, em ordem. Cada item vira um resumo de 1 página com link e data.

1. **Caderno técnico do ASSTI (SESI/DN, 2023, 107 p.)** — quais indicadores compõem a 7ª dimensão (fatores de redução da produtividade), declarada e não analisada no VigIndústria. **É o próximo passo crítico.**
2. **Os 3 eixos do MES 2026–2027** + os GTs (Promoção e Prevenção; Modelos Sustentáveis de Saúde Suplementar; Dados e Inteligência em Saúde). O MES tem **76 empresas-membro** (CN-SESI, 25/02/2026) — é a base de clientes potenciais e de validação. ⚠️ Circula "90 empresas"; a fonte primária diz 76.
3. **ODS 3 (metas 3.1–3.9) e ODS 9 (metas 9.1–9.5)** — mapear a solução para metas nominais. Conectar "sustentabilidade do modelo assistencial" às metas 9.4 (eficiência no uso de recursos) e 9.5 (inovação/P&D) dá munição para o júri.
4. **Modelos assistenciais** — SUS e atenção primária, RAPS, saúde suplementar (ANS), saúde ocupacional e saúde corporativa (MES), telemedicina, prontuário e interoperabilidade (HL7/FHIR, RNDS).
5. **A dor específica do SESI** — as edições 2025 focaram em *experiência do cliente indústria*. Mapear o funil real: agendamento, triagem, emissão de ASO, rastreio de exames, encaminhamento, retorno ao trabalho, absenteísmo, sinistralidade, custo.
6. **As edições de 2025** — ver o formato da demo vencedora e a dinâmica da maratona de 40 h.

### Perguntas para os mentores (levar ao 13/11)

- O desafio vem do Conecta Saúde — qual foi a pergunta mais concreta levantada por empresa?
- A empresa que formulou o desafio vai estar disponível para validar o protótipo?
- Que dado real podemos usar — e o que é proibido pela LGPD?
- O que a banca considera "protótipo funcional" mínimo?
- É esperado uso de IA com modelo próprio ou serviço existente?
- É esperado que a solução rode em celular?
- Como a equipe é pontuada: há planilha da banca?
- O que aconteceu com as soluções da edição 2025 depois? Rodaram?

### Perguntas para a organização (12/11, live de orientações)

- **A demo do protótipo entra nos 3 minutos do pitch** ou o protótipo é julgado à parte, a partir do que foi entregue às 15h30?
- Quais são os **desafios concretos** que serão apresentados na abertura, e as empresas por trás de cada um?
- A organização libera algum **acesso a dados do SESI/ASSTI** para o protótipo, ou o time usa dados públicos?
- A composição §5.3 (gestor, designer, 2 TI, especialista) é **filtro de seleção** ou apenas recomendação?
- Como é definido o **líder da equipe** para fins do prêmio (§9.5)?
- **Equipes indicadas com menos de 6 integrantes são complementadas?** (§5.4.1 prioriza a equipe indicada; §5.4.2 completa equipes com menos de 6. Qual prevalece?)
- Há **rede para os participantes** e para as demonstrações no local?

---

## Estrutura do pitch (3 min — 60% da nota)

| Tempo | Bloco | Conteúdo |
|---|---|---|
| 0:00–0:30 | Gancho | O problema em uma frase, com número |
| 0:30–1:15 | Solução | O que fazemos, para quem, como funciona (com a demo rodando) |
| 1:15–2:00 | Impacto | Métrica: R$, horas, %, vidas |
| 2:00–2:30 | Viabilidade | Quem usa, como é adotado, por que escala |
| 2:30–2:50 | Equipe | Uma linha por pessoa, competência, não biografia |
| 2:50–3:00 | Fechamento | Pedido + assinatura |

Regras: ensaiar em voz alta com cronômetro, **10 vezes**; **a demo tem que rodar offline** (rede do local não é garantida e o §11.2 não dá equipamento) — cada um roda no próprio note; slide único de impacto; ninguém fala mais de 3 minutos.

Como o pitch vale 6 e o protótipo 4, os 30 segundos de gancho e o bloco de viabilidade merecem mais tempo de ensaio que o común.

---

## Padrão de evidência

Toda afirmação neste workspace carrega uma marca:

- `[fato]` — verificável, com link e data
- `[hipótese]` — leitura nossa, sujeita a teste
- `[a confirmar]` — depende de confirmação da organização
- `§N` — vem do regulamento

Ao propor solução, sempre anexar: (1) a meta ODS específica, (2) o eixo do Conecta Saúde, (3) uma métrica de impacto mensurável extraída do VigIndústria quando possível, (4) a fonte do dado usado. Agente que não sabe **pesquisa e cita** — não chuta número clínico nem estatística de mercado.

---

## Estrutura do repositório

Estado em 27/10/2026:

```
AGENTS.md                                              este arquivo
Regulamento Hackathon SESI Saude 2026.pdf              regulamento oficial (§N)
chat.md                                                export do WhatsApp em Markdown
chat.txt                                               mesmo export em texto puro
WhatsApp Image 2026-10-07 at 16.05.05.jpeg             Programa Aluno Empreendedor (SENAI/CIMATEC/SEBRAE)
WhatsApp Image 2026-10-13 at 11.27.18.jpeg             INTEGRA SENAI Regional 2026
docs/00-portfolio-oportunidades.md                     PORTFÓLIO DE OPORTUNIDADES (comece aqui)
docs/01-produtos-brainstorm.md                        10 conceitos de produto + shortlist de 3
docs/pesquisa/01-mapa-competitivo.md                  mapa competitivo (11 players, 5 camadas)
docs/pesquisa/01-mapa-competitivo-fontes.md            bibliografia anotada do mapa
docs/pesquisa/02-dimensionamento-mercado.md            dimensionamento e funil de custo
docs/research/falhas-do-modelo-atual.md                falhas do modelo + contra-argumentos
docs/viabilidade-stack-dados-regulatorio.md           stack, datasets e escudo regulatório
docs/sources/                                          fontes primárias (PDF + texto extraído)
data/vigindustria-2026.md                              indicadores curados, com página e tabela
data/vigindustria-2026-raw.txt                         texto integral extraído do PDF (119 p.)
```

Os dois prints **não** são sobre o hackathon: são de outros dois programas. O de 07/10 é o Programa Aluno Empreendedor (inscrições até 22/10, CIMATEC Startups) e o de 13/10 é o INTEGRA SENAI Regional 2026 (3–5 integrantes, fase de prototipagem, prêmios R$ 600/400/300). O protótipo do hackathon pode servir de entrada no INTEGRA — trilha paralela, prazo do formulário a checar.

**Próxima estrutura** (a criar pelo time quando o escopo fechar, não por este bootstrap): `pitch/` (roteiro, slides, ensaios), `prototype/` (código — só depois de 14/11).

As seções de setup, lint e teste entram no AGENTS.md em **13/11**, quando a stack for decidida com o desafio real à vista. Sem stack fixa, elas seriam ficção.

---

## Git

- Branch a partir de `main`; `main` sempre espelha a pesquisa consolidada.
- Commits convencionais, corpo em pt-BR: `feat:`, `fix:`, `docs:`, `research:`, `pitch:`.
- Um tema de pesquisa por commit — o histórico é o log de raciocínio, e vai ser consultado durante a maratona.
- Não commitar segredos (`.env`) nem dado real de paciente.
- Manter os prints originais; não recomprimir.

**Apagar arquivo neste PC (Windows):** use `rm -- "<caminho-absoluto>"` como **único comando** do bash — sem `cd` antes, sem `echo`/`;` depois. `Remove-Item` é bloqueado pela política de segurança. Para diretório: `rm -r -- "<caminho-absoluto>"`. O runtime roteia para o launcher recuperável (lixeira).

---

## Segurança e dados

- Dado de saúde é **dado sensível** pela LGPD (Lei 13.709/2018), que o próprio regulamento cita (§10.4). Protótipo usa **dados sintéticos ou públicos** (VigIndústria, ANS, Vigitel), sempre com a fonte visível no repositório.
- Nada de dado real de paciente, mesmo anonimizado, neste repositório.
- Nenhuma saída de IA que simule parecer médico/diagnóstico sem o disclaimer visível na interface.
- Antes de usar API de IA: chave em variável de ambiente, nunca no código.
- O relatório do VigIndústria é de **dados agregados e autorrelatados** — usável. Já dados individualizados de trabalhadores não são.

---

## Trilhas paralelas

| Programa | Prazo | Premiação | Nota |
|---|---|---|---|
| Programa Aluno Empreendedor (SESI/CIMATEC/SEBRAE) | 22/10/2026 | — | Print de 07/10; verificar se o time se inscreveu |
| INTEGRA SENAI Regional 2026 | a checar | R$ 600 / 400 / 300 | Exige 3–5 integrantes, fase de prototipagem, demanda real; o protótipo do hackathon pode servir de entrada |
| Programa Regional de Incubação — Hub SESI/BA (Edital 001/2026) | edital fechado (17/07) | até 10 startups, 3 meses | Demo Day 18–20/11 — **imediatamente depois** do hackathon; procurar nova chamada |

---

## Links

- Regulamento 2026: `Regulamento Hackathon SESI Saude 2026.pdf` (no repo)
- Notícia oficial: https://www.sesibahia.com.br/detalhes-noticia?id=8312
- Landing page: https://materiais.sesibahia.com.br/hackathon-saude
- Formulário: https://forms.cloud.microsoft/r/gzFVj3UiGX
- SESI Saúde BA: https://www.sesisaudeba.com.br/
- Relatório VigIndústria Brasil 2026 (PDF): https://static.portaldaindustria.com.br/portaldaindustria/noticias/media/filer_public/fc/83/fc836c73-55b5-4ed7-9e4c-13a54a95786c/relatorio_vigindustria_-_conecta_saude_2026.pdf
- Conecta Saúde 2026 (CN-SESI): https://www.cnsesi.com.br/noticias/1975/ e https://www.cnsesi.com.br/noticias/1978/
- MES — Movimento Empresarial pela Saúde: https://www.sesi.portaldaindustria.com.br/institucional/atuacao-em-saude/mes
- Resultado da 2ª edição (vencedores): https://www.sesibahia.com.br/detalhes-noticia?id=8223
- Edital Incubação Hub SESI/BA: https://www.sesibahia.com.br/detalhes-noticia?id=8283
