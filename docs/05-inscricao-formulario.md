# O formulário de inscrição — as 22 perguntas e o texto de cada uma

**Equipe Cheers · 31/10/2026 · fecha a lacuna L1**
Fonte primária: formulário oficial (Microsoft Forms, "Inscrição Hackathon+ SESI Saúde 2026"), **lido na íntegra em 31/10/2026** pela API de runtime do Forms.

> **O formulário é o primeiro pitch da equipe.** Ele é lido e avaliado **antes** de qualquer pitch — e §4.1.2 diz que a seleção avalia *"conhecimento na temática proposta"*. Cinco respostas iguais = spam. Cada um escreve a **mesma estrutura** com a **sua** voz.

---

## 1 · Mapa do formulário (o que existe, na ordem)

Lido do formulário real. **22 perguntas, 14 obrigatórias.** A ordem tem ramificação: a pergunta *"Possui equipe já formada?"* decide o caminho.

| # | Pergunta (texto exato) | Tipo | Obrig. | O que colocar |
|---|---|---|---|---|
| 1 | Qual sua idade? | Texto | **sim** | sua idade (18+) |
| 2 | Nome Social | Texto | não | como quer ser chamado |
| 3 | Qual cidade você mora? | Texto | **sim** | sua cidade |
| 4 | Qual o seu Whatsapp? | Texto | **sim** | **com DDD** — "toda comunicação será enviada por este canal" |
| 5 | Tenho total aptidão, energia e disponibilidade para me dedicar de forma imersiva e presencial durante todo o período do hackathon, das **07h30 do dia 14/11 até às 19h do dia 15/11** | Escolha única: *"Sim, tenho total disponibilidade!"* | **sim** | única opção |
| 6 | **Por que você quer participar deste hackathon?** | Texto (1 linha) | **sim** | **campo da lacuna + das metas ODS** — §3.1 |
| 7 | Digite seu e-mail para receber a confirmação | Texto | **sim** | e-mail que você realmente lê |
| 8 | **Dentre os perfis abaixo, com qual deles você mais se enquadra?** | Lista suspensa: *Desenvolvimento de tecnologia · Design · Especialista (Profissionais, Pesquisadores e Estudantes da Saúde e Segurança do Trabalho) · Negócios/Gestão* | **sim** | **é o §5.3 — ver §3.3** |
| 9 | Qual sua formação? | Texto | **sim** | seu curso |
| 10 | **Quais as competências e conhecimentos técnicos que pode utilizar para ajudar a vencer o hackathon?** | Texto (multilinha) | **sim** | 3 blocos: ferramentas / metodologias / experiência — §3.2 |
| 11 | **Como você pode fazer a diferença e contribuir em uma equipe?** | Texto (1 linha) | **sim** | sua contribuição específica — §3.4 |
| 12 | Já participou de um hackathon antes? | Sim/Não | **sim** | honesto — luquinhas e Esteves: Sim |
| 13 | Como você ficou sabendo do Hackathon? | Lista suspensa (com "outro") | **sim** | Gabriel, Omena e Matheus: **Grupo no Whatsapp** · Moisés e luquinhas: o que for verdade |
| 14 | Qual gênero você se identifica? | Feminino/Masculino/Não-binário | não | o que for verdade |
| 15 | Você se identifica como parte da comunidade LGBTQ+? | Sim/Não | não | o que for verdade |
| 16 | É pessoa com deficiência | Sim/Não | não | o que for verdade |
| 17 | Se for pessoa com deficiência, alguma necessidade específica de apoio? | Texto | não | só se for o caso |
| 18 | Qual sua etnia/cor? | Lista suspensa | não | o que for verdade |
| 19 | **Possui equipe já formada?** | Sim/Não | **sim** | **Sim** — e abre a ramificação |
| — | → *"Identifique sua equipe"* → **Nome da equipe** | Texto | **sim** | **Cheers** — os 5, idêntico |
| 20 | Caso sua equipe seja selecionada e tenha menos de 6 pessoas, há a possibilidade de incluirmos mais pessoas | Escolha única: *"Ciente"* | **sim** | única opção — **é D11 respondida na cara** |
| 21 | Caso sua equipe não seja selecionada, e seu perfil seja selecionado, deseja participar como integrante em outra equipe? | Sim/Não | não | **decisão individual** — ver §3.5 |
| 22 | **Deseja compartilhar alguma informação complementar antes de finalizar sua inscrição?** | Texto | não | **a proposta em uma linha** — §3.6 |
| 23 | **DA CESSÃO DE DIREITO DE IMAGEM, VOZ E NOME** (5 cláusulas, LGPD) | Escolha única: *"Ciente"* | **sim** | única opção — **§10.1–10.3 do regulamento: leia antes de marcar** |

**Contagem do formulário:** 123 respostas até 31/10/2026. Formato **anônimo** (`IsAnonymous: true`).

**Prazo real:** a descrição diz *"até 8 de novembro"*, mas o `EndTime` técnico do formulário é **09/11/2026 00h15** (Brasília). São ~15 min de margem — **não usem o último minuto do dia 8.**

---

## 2 · O que mudou na nossa leitura (e era decisão do time)

| # | Antes | Agora | Por quê |
|---|---|---|---|
| **D7** — slot de designer | "ninguém está oficialmente no slot de design" (§5.3) | **O formulário tem uma opção "Design"** no campo de perfil (pergunta 8). **Alguém tem que marcar "Design"** — e a avaliação §4.1/§5.4.3 olha a equipe como um todo | O formulário **confirma** que os 4 perfis do §5.3 são o que eles esperam. Recomendação: **Esteves marca "Design"**, e ele **assume** o slot de design na proposta (`docs/04-proposta.md` §8) |
| **D11** — 5 ou 6 pessoas | "não está definido" | **Resolvido pela leitura do formulário:** a pergunta 20 diz, literalmente, *"Caso sua equipe seja selecionada e tenha menos de 6 pessoas, **há a possibilidade de incluirmos mais pessoas**"*. É **reconhecimento explícito**, não filtro | §5.4.2 é um fato. A pergunta 20 é a prova. Responde **"Ciente"** e **decida internamente** quem seria o 6º, se entrar |
| **L1** — texto do formulário | "ninguém redigiu o texto" | **Resolvido** — §3 deste documento | — |
| **ODS** | "escrever no formulário quais metas a equipe vai atacar" | **O formulário não tem campo de ODS.** As metas entram nos campos de texto livre, como conhecimento demonstrado (§4.1.2) | Verificado nas 22 perguntas |
| **Prazo** | "08/11" | **08/11**, com o formulário fechando tecnicamente às **00h15 de 09/11** | `EndTime` do Forms |
| **Tema** | "modelos assistenciais de saúde" (regulamento §2.1) | ⚠️ **A descrição do próprio formulário diz** *"modelos sustentáveis de **saúde suplementar**"* | **Nova pergunta para a organização** (12/11) — ver §5 |

---

## 3 · Os textos prontos para copiar

> **Regras que valem para os 5:**
> 1. **Não copie e cole igual.** A estrutura é a mesma; as frases são de cada um. A banca lê 5 respostas lado a lado.
> 2. **Toda afirmação com número leva a fonte.** É isso que separa "conhecimento da temática" de "interesse".
> 3. **Nunca prometer ROI.** Em ensaio randomizado o retorno de absenteísmo é **−49%**. Promete **medir**, não economizar.
> 4. **Nunca dizer "manutenção preditiva"** — a banca lê IoT industrial e desiste.
> 5. **Nunca atribuir os R$ 468 bi (4% do PIB) ao presenteísmo** — esse número é de doenças e acidentes de trabalho.

### 3.1 · Pergunta 6 — "Por que você quer participar deste hackathon?" (1 linha)

**Base — o mesmo núcleo, cada um fecha diferente:**

> *"Porque o SESI já mede o risco que o trabalhador corre — e não mede o trabalho que causa o risco: a 7ª dimensão do ASSTI foi declarada e nunca analisada (VigIndústria Brasil 2026, p. 16) e o instrumento de coleta tem zero itens de autonomia e participação. Quero construir essa camada: ODS 3 (metas 3.8 e 3.d) e ODS 9 (metas 9.4 e 9.5)."*

**Variações por membro:**

| Membro | Fecho da frase |
|---|---|
| **Moisés** | *"...Quero construir essa camada: ODS 3 (3.8 e 3.d) e ODS 9 (9.4 e 9.5). Sou da informática em saúde, com doutorado do orientador em IA no atendimento médico — quero um problema de campo com rigor de dado."* |
| **Matheus** | *"...Quero construir essa camada: ODS 3 (3.8 e 3.d) e ODS 9 (9.4 e 9.5). coordinatei um time no Programa Aluno Empreendedor e na Liga Jovem do SEBRAE: quero aplicar esse método aqui, com dado público e protótipo rodando offline."* |
| **Esteves** | *"...Quero construir essa camada: ODS 3 (3.8 e 3.d) e ODS 9 (9.4 e 9.5). Trago a validação clínica — o parceiro que cursa medicina já está no time — e a articulação com o ecossistema SESI/MES."* |
| **Omena** | *"...Quero construir essa camada: ODS 3 (3.8 e 3.d) e ODS 9 (9.4 e 9.5). Minha parte é de produto e negócio: transformar uma lacuna de medição em algo que o RH assina, com preço e canal."* |
| **luquinhas** | *"...Quero construir essa camada: ODS 3 (3.8 e 3.d) e ODS 9 (9.4 e 9.5). Já vim de hackathon anterior e sei o que cabe em 32 horas: quero provar que dá para construir um protótipo de arquivo único, offline, que roda na máquina de qualquer um."* |

### 3.2 · Pergunta 10 — "Quais as competências e conhecimentos técnicos…" (multilinha)

**Estrutura obrigatória em 3 blocos** (o enunciado pede exatamente isso):

| Membro | Ferramentas e Tecnologias | Metodologias e Processos | Experiência Prática |
|---|---|---|---|
| **Moisés** | Modelagem de dados em saúde; Python/R para análise de bases públicas; IA aplicada em functions administrativas (faixa de baixo risco, Res. CFM 2.454/2026) | Leitura crítica de fonte primária; validação de instrumento psicométrico (CFI, PABAK, AFC); desenho de estudo observacional | Informatização em saúde (doutorado do orientador, IA no atendimento médico); estágio e práticas reais em serviço de saúde |
| **Matheus** | Vite + React + TypeScript; PWA offline-first; SVG inline para gráficos sem dependência externa; Python para o modelo | Engenharia de produto; git e documentação como log de raciocínio; prototipagem sob prazo | Programa Aluno Empreendedor (SENAI/CIMATEC/SEBRAE) e Liga Jovem do SEBRAE 2026 — do zero ao protótipo com time |
| **Esteves** | Design de interface e comunicação visual; prototipação de fluxo de usuário; design de dados e informação | Design thinking aplicado a serviço de saúde; curadoria de evidência para décision | Articulação com o ecossistema SESI/MES; validação clínica com parceiro que cursa medicina |
| **Omena** | Modelagem de negócio e precificação por vida/ano; análise de mercado; CRM e funil B2B; painel de indicadores de adoção | Lean e testes de hipótese; dimensionamento de TAM/SAM/SOM com fonte; análise de benchmark (M&A e múltiplo de ARR) | Gestão de projeto do Programa Aluno Empreendedor; visão de produto em ambiente SENAI |
| **luquinhas** | Front-end (React/TS), empacotamento PWA, integração de dados e SVG; versionamento | Construção rápida de protótipo funcional sob prazo apertado; testes manuais e verificação em browser | Formation pelo SENAI; hackathons anteriores — do zero ao protótipo |

**Texto pronto (modelo para o Matheus):**
> *Ferramentas e Tecnologias: Vite + React + TypeScript, PWA offline-first, SVG inline para gráficos sem dependência externa, Python para o modelo preditivo.*
> *Metodologias e Processos: engenharia de produto sob prazo, prototipagem incremental, git e documentação como log de raciocínio.*
> *Experiência Prática: Programa Aluno Empreendedor (SENAI/CIMATEC/SEBRAE) e Liga Jovem do SEBRAE 2026 — do zero ao protótipo com equipe.*

### 3.3 · Pergunta 8 — "Dentre os perfis abaixo…" (a decisão de D7)

| Membro | Opção a marcar | Justificativa na proposta (`docs/04-proposta.md` §8) |
|---|---|---|
| **Moisés** | **Especialista** (Profissionais, Pesquisadores e Estudantes da Saúde e Segurança do Trabalho) | Informatização em saúde + prática em saúde. É o slot §5.3 "especialista" |
| **Esteves** | **Design** | ⚠️ **D7 — precisa de decisão do time até 08/11.** Se ele assume design, os 4 perfis do §5.3 ficam cobertos. Se não, o time fica com 3 dos 4 perfis e a composição é questionada |
| **Omena** | **Negócios/Gestão** | Slot §5.3 "gestor" |
| **Matheus** | **Desenvolvimento de tecnologia** | Slot §5.3 "TI 1" |
| **luquinhas** | **Desenvolvimento de tecnologia** | Slot §5.3 "TI 2" |

> ⚠️ **Se ninguém marcar "Design", a equipe aparece com 3 dos 4 perfis.** O §5.4.3 trata a equipe como multidisciplinar e a banca lê isso. **Decidir em 08/11.**

### 3.4 · Pergunta 11 — "Como você pode fazer a diferença e contribuir em uma equipe?" (1 linha)

| Membro | Texto |
|---|---|
| **Moisés** | *"Levo o rigor da saúde: transformar dado de saúde ocupacional em decisão organizacional sem virar parecer médico — a fronteira do que a IA pode fazer aqui é o ponto que mais importa acertar."* |
| **Matheus** | *"Sustento o time de ponta a ponta — do roteiro à entrega — e garanto que o protótipo rode offline na máquina de qualquer um, sem depender de rede do local."* |
| **Esteves** | *"Conecto a solução a quem valida: a linguagem dos itens com a medicina, a interface com o trabalhador, e a solução com o ecossistema SESI/MES."* |
| **Omena** | *"Fecho a viabilidade: quem paga, por que adota, em que prazo. Transformo a lacuna em alavanca de negócio que o RH assina."* |
| **luquinhas** | *"Entrego o protótipo funcionando dentro do tempo: é o que prova que a ideia vira produto."* |

### 3.5 · Pergunta 21 — "Caso sua equipe não seja selecionada… deseja participar em outra equipe?"

Decisão **individual** de cada um. Recommendation: **Sim** — mantém a pessoa na competition se a equipe não for selecionada, e a inscrição não custa nada. Mas: quem responder "Sim" deve avisar o time no WhatsApp, para ninguém achar que há um 6º integrating de surprise (e o §9.7 diz que a organização **não media** desacordo entre membros).

### 3.6 · Pergunta 22 — "Deseja compartilhar alguma informação complementar…" (opcional) — **a proposta em uma linha**

> *"Time **Cheers** (5 pessoas: saúde, TI, produto, canal SESI/MES). Nossa direção: **SINAL** — o trabalhador responde 6 itens offline no celular; o agregado anônimo do posto (k≥10) vira um índice de contexto de trabalho; um modelo transparente cruza esse índice com a exposição prevista (VigIndústria + CAT) e devolve à empresa 3 alavancas priorizadas, cada uma com o indicador nacional que a justifica. Não prometemos economia — prometemos medir dias expostos antes e depois. Repositório com a pesquisa, a proposta e o roteiro do pitch: github.com/[org]/hackaton"*

*(trocar a URL pelo repositório real antes de enviar — ou remover se não for público)*

### 3.7 · Pergunta 9 — "Qual sua formação?"

Cada um escreve o próprio curso. **Moisés e Matheus**: áreas de saúde/informática, que somadas ao estágio de Moisés e ao doutorado do orientador atendem ao §3.6 ("profissionais e acadêmicos de saúde, TI, design, gestão") e ao §4.1.2.

---

## 4 · Checklist antes de enviar (cada um)

- [ ] **WhatsApp com DDD** (é por onde vai toda a comunicação, inclusive a confirmação de seleção)
- [ ] **E-mail que você realmente lê** — a confirmação e o aviso de 24 h (D1) vão por lá (§4.3)
- [ ] Idade, cidade, nome social
- [ ] Questão 5 marcada ("Sim, tenho total disponibilidade!") — ela é bindente: **das 07h30 de 14/11 às 19h de 15/11**
- [ ] Questão 19 = **Sim** → nome da equipe = **Cheers** (idêntico nos 5)
- [ ] Questão 20 = **Ciente**
- [ ] Questão 23 (cessão de imagem, voz e nome) — **ler as 5 cláusulas antes de marcar "Ciente"**: é gratuita, definitiva, irrevogável, sem limite territorial ou temporal, e **inclui o nome e as características da solução** (§10.1–10.3)
- [ ] Texto 6 (por que participar) **personalizado** — não igual ao do colega
- [ ] Texto 10 (competências) com os 3 blocos preenchidos
- [ ] Texto 11 (contribuição na equipe) **personalizado**
- [ ] Questão 22 (complementar) com a proposta em uma linha
- [ ] Nenhum número sem fonte; nenhuma promessa de ROI; nenhuma palavra "manutenção preditiva"

⚠️ **§11.11 do regulamento:** o formulário pode conter autorização de divulgação do escopo e das funcionalidades do projeto. **Ler antes de submeter.**

---

## 5 · Nova pergunta para a organização (live de 12/11)

> **A descrição do próprio formulário diz** *"soluções inovadoras e tecnológicas para o tema relacionado a **modelos sustentáveis de saúde suplementar**"*, enquanto o regulamento (§2.1) e o Anexo I falam em **modelos assistenciais de saúde**. São dois recortes diferentes: saúde suplementar (plano, operadora, RN 465, ANS) × saúde ocupacional (ASSTI, NR-7, SESI).
> **Pergunta:** o desafio detalhado vai ser do lado do **plano/operadora** (o custo que sai do bolso do empregador e não circula — RN 465 art. 14 §2º) ou do lado do **SESI ocupacional** (a rede, o ASSTI, a Plataforma Viva+)? Isso define se a proposta se ancora na ANS ou no ASSTI — e é a bifurcação mais consequente do §7.3.

*(pergunta nova, somada às 7 que já estão no `AGENTS.md`)*

---

## Fontes

Formulário oficial "Inscrição Hackathon+ SESI Saúde 2026" — 22 perguntas lidas em 31/10/2026 via API de runtime do Forms · Regulamento 2026 §3.3.1 · §3.6 · §3.7 · §4.1.2 · §4.3 · §5.3 · §5.4.1 · §5.4.2 · §5.4.3 · §6.5 · §9.7 · §10.1–10.3 · §11.11 · `docs/04-proposta.md` · `docs/06-ods-metas.md` · `data/vigindustria-2026.md` · `docs/00-portfolio-oportunidades.md`
