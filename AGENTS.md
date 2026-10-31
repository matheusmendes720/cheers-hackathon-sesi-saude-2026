# AGENTS.md

Workspace da equipe **Cheers** para o **Hackathon+ SESI Saúde** (SESI Bahia + Grupo Rede+, Salvador, 14–15/11/2026). Tema: *"Desafios e soluções para a sustentabilidade dos modelos assistenciais de saúde"*.

**Até 12/11 o foco é pesquisa e roteiro de pitch. Nenhum código de produto antes do desafio ser revelado** — decisão do time em 27/10/2026, agora respaldada pelo regulamento (§7.3).

---

## Fontes de verdade

Ordem de precedência quando houver conflito:

1. **Regulamento 2026** — `Regulamento Hackathon SESI Saude 2026.pdf` (no repo). Data de 08/10/2026, assinado em Salvador. É o documento que rege. *Ressalva: o cabeçalho diz "Minuta" e o item 6.1 ressalva que a programação pode mudar.*
2. [Notícia oficial](https://www.sesibahia.com.br/detalhes-noticia?id=8312) — SESI Bahia, 09/10/2026
3. [Landing page oficial](https://materiais.sesibahia.com.br/hackathon-saude) — formulário, tamanho de equipe
4. [Formulário de inscrição](https://forms.cloud.microsoft/r/gzFVj3UiGX) — Microsoft Forms. **As 22 perguntas foram lidas na íntegra em 31/10/2026** (API de runtime do Forms) e estão mapeadas em `docs/05-inscricao-formulario.md` — **não há campo de ODS, e não há campo de "nome do produto"**
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

> ⚠️ **O calendário em dias da semana (verificado em 31/10):** **08/11 é domingo** — as inscrições precisam estar prontas **até sexta 06/11** (restam só **5 dias úteis**). 12/11 é quinta, **13/11 é sexta** (live de abertura à noite) e **o evento inteiro é um fim de semana: sábado 14 + domingo 15**, com check-in às 07h30 de sábado. Planejar como **plantão de ~30 h com revezamento**, não como dois dias de trabalho normal. E o §4.3 dá **24 h para confirmar a seleção** — o e-mail pode chegar entre 10/11 e 12/11 e a confirmação cair no fim de semana: definir **agora** quem responde.

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
   > **Leitura do §2.1 (verificada no PDF em 31/10):** os ODS são *"parâmetro"* do desafio, **não cardápio** — e **não há campo de ODS no formulário**, então **a banca não pontua ODS**. ODS é narrativa, não nota. O que a banca pontua é §8, e §8 não cita ODS. Ver `docs/07-alavancas-regulamento.md` §0.

2. **Prazo.** O grupo discute "jaja fecha" (25/10) e o print de 07/10 mostra 22/10 — mas 22/10 é o prazo do **Programa Aluno Empreendedor** (SENAI/CIMATEC/SEBRAE), outro programa. O prazo do hackathon é **08/11** (§3.1).

3. **Inscrição.** O formulário exige inscrição **individual de cada participante**, mesmo com time formado (§3.3.1, §5.2). Não basta um único envio do time.

4. **Duração.** O documento que o Moisés colou no grupo diz "três dias imersivos" — e o regulamento diz o mesmo em §2.4. Mas o cronograma (§6.2) e o §2.6 delimitam o presencial em **14 e 15/11** (2 dias), com 13/11 online. §6.1 ressalva que a programação é planejamento e pode mudar.

5. **Meta 3.8.** Até 31/10 este arquivo citava a meta 3.8 como *"Cobrir universalmente os serviços de saúde, incluindo atenção reabilitativa"*. **Não é o texto da ONU.** O oficial é *"Atingir a cobertura universal de saúde, incluindo a proteção do risco financeiro, o acesso a serviços de saúde essenciais de qualidade e o acesso a medicamentos e vacinas essenciais seguros, eficazes, de qualidade e a preços acessíveis para todos."* "Atenção reabilitativa" vem da **OMS** (Resolução WHA76.6, 2023), que define a reabilitação como componente essencial da meta 3.8 — é outra fonte. **Regra:** citar a meta pelo texto da ONU; "atenção reabilitativa" só com atribuição à OMS. Ver `docs/06-ods-metas.md` §2 e §5.

6. **A mensagem de ODS reenviada no grupo (31/10).** O resumo "🌾 ODS 2: Fome Zero… / 🏭 ODS 9… / 🔗 A Intersecção" do **Moisés** (já em `chat.md`, 25/10 23:15) **foi reenviado**. É útil em **um** ponto — a lista oficial das metas 9.4 e 9.5, verificadas — e perigoso em **dois**: (a) toda a metade "ODS 2 = agricultura" (agrotech, cadeia de frio, biotecnologia) é **material de outro domínio**; (b) a seção **"🔗 A Intersecção"** propõe que o projeto seja *Agrotechs + IoT + cadeia de frio + biotecnologia* — **é o caminho para construir a coisa errada**: domínio errado, o Anexo I rejeita "incorporação de novas tecnologias", e é o produto mais crowded que existe sem nenhum dos 12 dias de pesquisa já feitos no repo. **A interseção correta é ODS 9 → ODS 3**, não ODS 9 → ODS 2. Ver `docs/06-ods-metas.md` §4.

7. **"Agrotech + IoT + cadeia de frio + biotecnologia" está FORA do escopo por regulamento** — não por preferência. §7.2 é mandatório: *"As equipes deverão desenvolver soluções para **Desafios e soluções para a sustentabilidade dos modelos assistenciais de saúde** (Anexo I)"*. §2.1 fixa **dois** ODS como parâmetro (saúde + indústria) e §3.6 limita o ecossistema a saúde/TI/design/gestão; §2.3 diz que a ação **não tem caráter comercial**; §10.6 exige originalidade — e agrotech é o espaço mais crowded que existe. **Não existe "escolher qualquer ODS".** Se a proposta for reescrita, tem que ser reescrita *dentro* de saúde do trabalhador. Ver `docs/07-alvancas-regulamento.md` §1.

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
| D1 | Confirmar inscrição individual dos 5 e o vínculo ao time "Cheers" — **texto de cada campo pronto em `docs/05-inscricao-formulario.md`** (22 perguntas lidas na íntegra; os textos prontos estão em §3) | cada um | **08/11** |
| D2 | Nicho dentro de saúde corporativa para atacar — **PROPOSTA FECHADA 31/10**: saúde do trabalho na indústria, camada de **predição** (exposição) + **participação** (trabalhador com voz). Canônico em `docs/04-proposta.md` §1–4. *Validação do time: 10/11* | Esteves + Moisés + Omena | 10/11 |
| D2b | **Tese preditiva na cadeia de valor** — **PROPOSTA FECHADA 31/10**: a cadeia de 7 elos (presenteísmo → exposição → evento → afastamento → incapacidade → saída → resultado) fica como **enquadramento do pitch** (slide 2), com TAM/SAM/SOM; **não** como escopo de produto. MVP = **um elo** (exposição + presenteísmo). **Não chamar de "manutenção preditiva"** — a banca lê como IoT industrial e o Anexo I rejeita. Também **não atribuir os R$ 468 bi (4% do PIB) ao presenteísmo** — esse número é de doenças e acidentes de trabalho. Ver `docs/03-tese-preditiva.md` + `docs/04-proposta.md` §5 | Matheus + Moisés + Omena | 10/11 |
| D3 | 10 ideias → shortlist de 3 → 1, pela rubrica — **PROPOSTA FECHADA 31/10**: **A (Escuta + Alavanca)** com **C (Roda)** como camada que fecha o loop, **B (Aciona)** como expansão pós-hackathon. Escopo único de 32 h com **plano de corte declarado** em `docs/04-proposta.md` §5 | Matheus conduz | 11/11 |
| D4 | Speaker do pitch (Moisés se voluntariou) | time | 12/11 |
| D5 | Stack e arquitetura do protótipo | Matheus + luquinhas | **13/11**, na live de abertura |
| D6 | Perguntas para mentores (abaixo) | time | 13/11 |
| D7 | **Quem cobre o slot de designer** (§5.3) — **o formulário tem uma opção "Design"** no campo de perfil (pergunta 8). Recomendação: **Esteves assume o design** e marca "Design"; se ninguém marcar, a equipe aparece com 3 dos 4 perfis do §5.3 | time | **08/11** — vai no formulário |
| D8 | **Líder da equipe** para receber o prêmio (§9.5) + quem informa a conta | time | 10/11 |
| D9 | **Inventário de equipamento** — cada um leva note, carregador, extensão, mouse, hdmi (§11.2) | cada um | 12/11 |
| D10 | Onde dormir no local (sem dormitório, com chuveiro) (§11.3) | time | 12/11 |
| D11 | **Time de 5 ou 6?** — **resolvido pela leitura do formulário (31/10)**: a pergunta 20 diz *"Caso sua equipe seja selecionada e tenha menos de 6 pessoas, há a possibilidade de incluirmos mais pessoas"* — reconhecimento explícito do §5.4.2, não filtro. Responder **"Ciente"** e decidir internamente quem seria o 6º, se entrar | time | **08/11** |
| D12 | **Disponibilidade online em 13/11, 18h30** para a live de abertura | todos | 13/11 |
| D13 | **Nome do produto** — recomendação: **SINAL** (*o sinal que antecede a falta*); alternatas **Elo 1** e **Escuta**. Checar INPI e busca de marca antes de ir para o formulário. ⚠️ **§10.1: a cessão de imagem/voz/nome cobre "o nome, imagem e características da solução"** — o nome do produto vai para patrocinadores e parceiros. Decidir isso ANTES de escolher | Matheus + Omena | **08/11** |
| D14 | **Roteiro de 3 min** — `pitch/roteiro-3min.md` escrito (palavra por palavra, 2 ganchos, plano B de demo caída, 8 perguntas de banca, protocolo de 10 ensaios). Falta **ensaiar 10× em voz alta** | Moisés + time | 12/11 |
| D15 | **Texto do formulário** — `docs/05-inscricao-formulario.md` com os textos prontos por membro. Cada um **personaliza** (5 respostas iguais = spam; §4.1.2 avalia "conhecimento na temática") | cada um | **08/11** |
| D16 | **Metas ODS no formulário** — o formulário **não tem campo de ODS**; as metas (3.8, 3.d, 9.4, 9.5) entram nos campos de texto livre. Mapeamento verificado em `docs/06-ods-metas.md` | Matheus + Omena | **08/11** |
| D17 | **Quem responde o e-mail de confirmação em 24 h** (§4.3) — o aviso pode chegar entre 10/11 e 12/11 e a confirmação cair no **fim de semana**. Definir um substituto para cada membro | time | **10/11** |

---

## Escopo até 12/11

**Permitido:** pesquisa, análise, dados públicos, notas de pitch, mockups estáticos, ensaio oral, roteiro de demo.

**Proibido:** código do produto, arquitetura fechada, stack decidida, protótipo funcional. Motivo: §7.3 — o detalhamento do desafio **só é apresentado na abertura, às equipes**. Construir antes não bate com o tema real e quebra o nívelamento entre as 12 equipes.

**⚠️ E a consequência disso:** o que se leva ao dia 14 **não é uma solução pronta — é capacidade de absorver o desafio em 90 minutos.** Chegar com uma tese travada (O1+O3, por exemplo) incumpre exatamente o nivelamento que o §7.3 impõe, e as nossas 5 oportunidades podem não ser o desafio real. O ativo que construímos é o **kit de mapeamento**: grade das 4 dimensões do Anexo I · 33 indicadores com prevalência e CI · instrumento validado do VigIndústria · 9 datasets públicos · escudo regulatório (CFM 2.454/2026 Anexo II, I) · 5 armadilhas com evidência · mapa competitivo de 5 camadas. Ver `docs/02-cruzamento-whatsapp.md` §1.

**Métrica de sucesso em 12/11:** 1 problema definido com evidência ✅ (`docs/04-proposta.md` §2) · 3 hipóteses ranqueadas ✅ (A/B/C em `docs/01`) · 1 roteiro de 3 min **escrito** ✅ (`pitch/roteiro-3min.md`) — **falta ensaiar 10× em voz alta** (D14) · 1 slide único de impacto ✅ (`pitch/slide-impacto.html`) · 1 protocolo de 90 min para o reveal ✅ (`docs/08-plano-90min.md`) · 8 perguntas para os mentores ✅ (abaixo) · 1 entrada humana para o time ✅ (`README.md`) · 1 plano de build ✅ (`docs/10-mapa-de-build-32h.md`) · stack decidida no dia seguinte com o desafio real à vista.

**A proposta canônica do produto é `docs/04-proposta.md`** (31/10). Ela não substitui o §7.3: o desafio detalhado é revelado na abertura e pode reposicionar a tese — o §10 da proposta mapeia as **5 bifurcações** do kit para cada cenário, e o §5 traz o **plano de corte** que decide o que sai se o tempo apertar.

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
3. ~~**ODS 3 (metas 3.1–3.9) e ODS 9 (metas 9.1–9.5)**~~ ✅ **CONCLUÍDO 31/10** — `docs/06-ods-metas.md`: metas 3.8, 3.d, 9.4 e 9.5 com o **texto oficial verificado**, o mapeamento de cada uma para a proposta, a correção da citação da 3.8 e o que rejeitar da mensagem de ODS que circulou no grupo. **As metas entram no formulário como conhecimento demonstrado** — o formulário não tem campo de ODS.
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

- **A descrição do próprio formulário diz "modelos sustentáveis de *saúde suplementar*"**, enquanto o regulamento (§2.1) e o Anexo I falam em *modelos assistenciais de saúde*. São dois recortes: plano/operadora (RN 465, ANS) × saúde ocupacional (ASSTI, NR-7, SESI). **O desafio detalhado é de qual lado?** É a bifurcação mais consequente do §7.3. *(Pergunta nova, 31/10.)*
- **A demo do protótipo entra nos 3 minutos do pitch** ou o protótipo é julgado à parte, a partir do que foi entregue às 15h30?
- Quais são os **desafios concretos** que serão apresentados na abertura, e as empresas por trás de cada um?
- A organização libera algum **acesso a dados do SESI/ASSTI** para o protótipo, ou o time usa dados públicos?
- A composição §5.3 (gestor, designer, 2 TI, especialista) é **filtro de seleção** ou apenas recomendação?
- Como é definido o **líder da equipe** para fins do prêmio (§9.5)?
- **Equipes indicadas com menos de 6 integrantes são complementadas?** (§5.4.1 prioriza a equipe indicada; §5.4.2 completa equipes com menos de 6. Qual prevalece?)
- Há **rede para os participantes** e para as demonstrações no local?

---

## Estrutura do pitch (3 min — 60% da nota)

Roteiro palavra por palavra: **`pitch/roteiro-3min.md`** (31/10). O **Modo Pitch** do `demo.html` tem os mesmos 7 blocos, com cronômetro e nota de apresentador — o ensaio é feito nele.

| Tempo | Bloco | Conteúdo | Tela |
|---|---|---|---|
| 0:00–0:30 | Gancho | O problema em uma frase, com número. **2 versões** (A: o sinal invisível · B: a dimensão que não existe) — escolher no ensaio | Cadeia |
| 0:30–1:00 | Cadeia e solução | Os 7 elos, o elo 1 invisível, o ciclo em 3 passos | Cadeia → Exposição |
| 1:00–1:45 | Demo | Seletor → Exposição → "como o modelo funciona" → Escuta → 2 itens → "Ver meu plano" → Alavancas | Exposição → Escuta → Alavancas |
| 1:45–2:15 | Impacto | 106 mi dias · 4,1 mi afastamentos · o índice que não existe. **Não prometer economia** | Exposição |
| 2:15–2:40 | Viabilidade | Objetivo estratégico do PAO 2026 · 2,7 mi vidas na Viva+ · piloto BA + MES | Mercado |
| 2:40–2:52 | Equipe | Uma linha por pessoa, competência, não biografia | — |
| 2:52–3:00 | Fechamento | *"Mede-se em quantos dias a pessoa volta a produzir."* Parar. | — |

Regras: ensaiar em voz alta com cronômetro, **10 vezes** (protocolo em `pitch/roteiro-3min.md` §10); **a demo tem que rodar offline** (rede do local não é garantida e o §11.2 não dá equipamento) — cada um roda no próprio note; **plano B declarado** (§8 do roteiro) para o caso de a demo cair; slide único de impacto; ninguém fala mais de 3 minutos.

**Duas armadilhas de conteúdo, checadas contra a fonte:**
- **65,6%** dos trabalhadores diz que a comunicação sobre prevenção de acidentes é **suficiente** → portanto **34,4%** diz que **não** é. Em micro/pequenas empresas, só **56,2%** a acham suficiente. (VigIndústria, T36, p. 95.)
- **R$ 468 bi (4% do PIB)** é perda de produtividade por **doenças e acidentes de trabalho** — não é o presenteísmo. O presenteísmo (R$ 200–600 bi) é fonte secundária `[a confirmar]`.

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

Estado em 01/11/2026:

```
README.md                                              rosto público do repo (narrativa + dossiê + time + direitos) — o bloco operacional do time fica no fim
AGENTS.md                                              este arquivo
CONTRIBUTING.md                                        regras do repositório (6 regras, fluxo de PR, checklist de evidência)
.gitignore                                              o que não entra no repo
.github/PULL_REQUEST_TEMPLATE.md                       template de PR com checklist de evidência + regex de varredura
Regulamento Hackathon SESI Saude 2026.pdf              regulamento oficial (§N)
chat.md                                                export do WhatsApp em Markdown
chat.txt                                               mesmo export em texto puro
WhatsApp Image 2026-10-07 at 16.05.05.jpeg             Programa Aluno Empreendedor (SENAI/CIMATEC/SEBRAE)
WhatsApp Image 2026-10-13 at 11.27.18.jpeg             INTEGRA SENAI Regional 2026
docs/00-portfolio-oportunidades.md                     PORTFÓLIO DE OPORTUNIDADES (comece aqui)
docs/01-produtos-brainstorm.md                        10 conceitos de produto + shortlist de 3
docs/02-cruzamento-whatsapp.md                       pesquisa × histórico do grupo (kit de mapeamento)
docs/03-tese-preditiva.md                            cadeia de valor + TAM/SAM/SOM (direção D2b)
docs/04-proposta.md                                  A PROPOSTA — documento canônico do produto (D2/D2b/D3)
docs/05-inscricao-formulario.md                     as 22 perguntas do formulário + o texto de cada uma (D1/D7/D11/D15)
docs/06-ods-metas.md                                metas ODS 3 e 9 verificadas + mapeamento + o que rejeitar
docs/07-alvancas-regulamento.md                     alavancas de pontuação, restrições e o veredito de escopo (§2.1/§7.2)
pitch/demo.html                                      demo funcional offline (6 telas + Modo Pitch de 7 blocos)
pitch/roteiro-3min.md                                roteiro do pitch palavra por palavra (D14)
docs/08-plano-90min.md                               o protocolo de 13/11: grade de decisão e escopo travado em 90 min
docs/09-por-que-esta-proposta.md                     a justificativa completa: os 4 gaps, a 7ª dimensão operacionalizada, o impacto honesto e o veredito sobre o agro
pitch/slide-impacto.html                             slide único de impacto (A4 paisagem, imprimível, offline)
pitch/apresentacao-interna.md                        apresentação de 10 min para o time, sem contexto prévio
docs/10-mapa-de-build-32h.md                          plano de build hora a hora (2 turnos, CORTE 1/2, 3 trilhos, 8 riscos)
docs/11-perguntas-para-a-organizacao.md                one-pager imprimível das 8 perguntas para a live de 12/11 (P1/P2/P3)
docs/relatorios/                                       DOSSIÊ EM PDF (4 docs, 58 p.) — fonte HTML + PDF gerado
docs/relatorios/01-horizonte-de-trabalho               o horizonte explorado, o delta vs WhatsApp, decisões, calendário
docs/relatorios/02-nucleo-e-gaps                       a tese, a 7ª dimensão, os 4 gaps, o mecanismo, o impacto honesto
docs/relatorios/03-evidencia-mercado-regulacao         os 33 indicadores, a base científica, o mapa de preços, o escudo
docs/relatorios/04-kit-13-11-e-build                   o protocolo de 90 min, os 5 kernels, as 32 h, os 8 riscos
docs/README.md                                         índice da documentação por caminho de leitura (A/B/C/D/E)
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

**Onde entra o código do produto:** `prototype/` — **só depois de 14/11**, com a stack decidida com o desafio real à vista (D5). Até lá, `pitch/` guarda roteiro, ensaios e a demo de arquivo único.

**`docs/04-proposta.md`** é o documento canônico do produto: nome, problema com número, ciclo da solução, escopo único de 32 h com **plano de corte**, grade das 4 dimensões, armadilhas com evidência, impacto, viabilidade e os 5 riscos. Ele **funde** as duas listas de escopo que existiam separadas (`docs/00` §4 e `docs/03` §4). Qualquer proposta nova deve ser escrita e comparada **contra ele**.

**`pitch/demo.html`** já existe: mockup funcional de arquivo único, **sem CDN, sem fonte externa, sem chamada de rede** — abre offline na máquina de qualquer membro (§11.2). Seis telas (Cadeia · Exposição · Escuta · Alavancas · Mercado · Evidência) + **Modo Pitch** com cronômetro de 3:00, setas do teclado e nota de apresentador por slide — **7 blocos, na mesma divisão do roteiro**. Serve de ensaio cronometrado e de referência do que o protótipo final deve fazer. Modelo de exposição **transparente e auditável** (a soma das contribuições é o índice), com auto-verificação que acusa no console qualquer opção de seletor sem chave correspondente.

As seções de setup, lint e teste entram no AGENTS.md em **13/11**, quando a stack for decidida com o desafio real à vista. Sem stack fixa, elas seriam ficção.

---

## Git

- Branch a partir de `main`; `main` sempre espelha a pesquisa consolidada.
- Commits convencionais, corpo em pt-BR: `feat:`, `fix:`, `docs:`, `research:`, `pitch:`.
- Um tema de pesquisa por commit — o histórico é o log de raciocínio, e vai ser consultado durante a maratona.
- Não commitar segredos (`.env`) nem dado real de paciente.
- Manter os prints originais; não recomprimir.

### Remote e GitHub (publicado em 01/11/2026)

**`https://github.com/matheusmendes720/cheers-hackathon-sesi-saude-2026`** — repositório **público**, branch `main` como padrão, conta `matheusmendes720`.

- Topics: `hackathon` · `sesi` · `saude-do-trabalhador` · `saude-ocupacional` · `odp` · `dados-publicos` · `brasil` · `pesquisa`.
- 20 commits, 65 arquivos, ~29 MB (o grosso são os PDFs de terceiros em `docs/sources/`).
- O README raiz é o **rosto público**: narrativa, lacuna com número, proposta, dossiê, fontes, time, contribuir e direitos — com o bloco operacional do time preservado no fim. Dois diagramas em **Mermaid** (renderizado nativamente pelo GitHub; validado com o parser oficial do mermaid v11).
- **PR é obrigatório** — nada de commit direto na `main`. Convide os outros 4 como colaboradores: `gh api -X PUT repos/matheusmendes720/cheers-hackathon-sesi-saude-2026/collaborators/<usuario> -f permission=push` (precisa do username GitHub de cada um).

**Duas decisões que ficaram com o time (não são bloqueios de documentação):**

1. **Licença.** O repo foi criado **sem `LICENSE`** — padrão do GitHub é todos os direitos reservados, coerente com o §10.8 (os direitos autorais ficam com os criadores). Para liberar em MIT: botão **Add a license** do GitHub, ou `gh api -X PUT repos/matheusmendes720/cheers-hackathon-sesi-saude-2026/license -f license=mit`.
2. **Redistribuição dos PDFs de terceiros** (~25 MB em `docs/sources/` + o regulamento na raiz). Tudo é publicamente baixável na origem e `docs/sources/README.md` traz a URL pública de cada PDF. Decidir entre manter rastreado ou trocar por links + hashes. **Não removeu nada do disco.**

**Dado pessoal exposto:** `chat.md` / `chat.txt` (export do WhatsApp) e a tabela do time em `AGENTS.md` contêm **números de telefone dos membros da equipe**. Todos os 5 são colaboradores do repo, mas se o time preferir tirar do histórico público, ainda é possível (repo novo, sem forks) com `git filter-repo`.

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
