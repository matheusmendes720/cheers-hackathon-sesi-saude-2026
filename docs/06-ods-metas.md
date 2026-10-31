# ODS — metas verificadas e mapeamento da tese

**Equipe Cheers · 31/10/2026 · fecha o item 3 da agenda de pesquisa**
Marca: `[fato]` verificável com fonte · `[hipótese]` leitura nossa.

---

## 1. A regra (não muda)

> Toda referência a ODS neste workspace é **ODS 3 (Saúde e Bem-Estar) + ODS 9 (Indústria, Inovação e Infraestrutura)**.

**Por que:** o SESI rotulou "ODS 2 – Saúde e Bem-Estar" na sua comunicação (página oficial e regulamento §2.1). Na Agenda 2030 da ONU, **Saúde e Bem-Estar é o ODS 3**; ODS 2 é Fome Zero e Agricultura Sustentável. O rótulo numérico do SESI está errado; o conteúdo que ele quer dizer está certo.

**Como escrever:** **"Saúde e Bem-Estar (ODS 3 na Agenda 2030)"** e **"ODS 9"**. Assim o texto bate com o rótulo do SESI *e* com a numeração oficial — e ninguém pode apontar erro. Citar "ODS 2" no formulário, hoje, seria citação errada por um número.

---

## 2. As metas que a proposta ataca — texto oficial, verificado

### ODS 3 — Saúde e Bem-Estar

**Meta 3.8** — *"Atingir a cobertura universal de saúde, incluindo a proteção do risco financeiro, o acesso a serviços de saúde essenciais de qualidade e o acesso a medicamentos e vacinas essenciais seguros, eficazes, de qualidade e a preços acessíveis para todos."*
Fonte: ONU / IPEA (adaptação brasileira); un.org/sustainabledevelopment/health

**Meta 3.d** — *"Reforçar a capacidade de todos os países, particularmente os países em desenvolvimento, para o alerta precoce, redução de riscos e gerenciamento de riscos nacionais e globais de saúde."*
Fonte: ONU, sdgs.un.org/goals/goal3

**Meta 3.5** — *"Melhorar a saúde mental e o bem-estar das pessoas."* *(relevante para a saúde mental no trabalho: 546.254 afastamentos por saúde mental em 2025, +15%)*

### ODS 9 — Indústria, Inovação e Infraestrutura

**Meta 9.4** — *"Até 2030, modernizar a infraestrutura e reabilitar as indústrias para torná-las sustentáveis, com eficiência aumentada no uso de recursos e maior adoção de tecnologias e processos industriais limpos e ambientalmente corretos; com todos os países atuando de acordo com suas respectivas capacidades."*
Fonte: ONU / gov.br (cartilha "Os cinco P's da Agenda 2030") / un.org/sustainabledevelopment/infrastructure-industrialization

**Meta 9.5** — *"Fortalecer a pesquisa científica, melhorar as capacidades tecnológicas de setores industriais em todos os países, particularmente os países em desenvolvimento, inclusive, até 2030, incentivando a inovação e aumentando substancialmente o número de trabalhadores de pesquisa e desenvolvimento por milhão de pessoas e os gastos público e privado em pesquisa e desenvolvimento."*
Fonte: idem

---

## 3. Por que estas quatro e não outras

| Meta | Onde a proposta encosta | Evidência no repo |
|---|---|---|
| **9.4** — eficiência no uso de recursos + reabilitar a indústria | A solução **não adiciona custo assistencial**: ela troca o assistido de indicador por decisão organizacional. E a meta fala em *modernizar a indústria* — a proposta moderniza **o trabalho**, que é a matéria-prima do setor | `docs/04-proposta.md` §5 · R$ 276,9 bi/ano em despesas assistenciais (ANS Panorama + DIOPS) |
| **9.5** — pesquisa, inovação, P&D, capacidade tecnológica industrial | É a meta do **método**: cruzar base pública (VigIndústria, CAT/INSS) com instrumento validado e publicar peso à vista. É o que o time constrói, não o que consome | `docs/04-proposta.md` §5 · CR = 0,863 na 7ª dimensão (VigIndústria, p. 16) |
| **3.8** — cobertura universal, proteção do risco financeiro, acesso a serviços essenciais de qualidade | O **fundo da fragmentação**: RN 465 art. 14 §2º tira o ASO da cobertura obrigatória do plano; o custo sai do bolso do employador/SESI e o dado não circula. Trazer o trabalhador para dentro do fluxo é cobertura, não compliance | `docs/00-portfolio-oportunidades.md` §1 · RN 465 · ANS Panorama |
| **3.d** — alerta precoce, redução de riscos | É literalmente o que a proposta faz: **antecipar** o desfecho em vez de medir o daño depois. E a saúde mental no trabalho é a frente que mais cresce (546.254 afastamentos, +15%) | `docs/04-proposta.md` §5 · O eixos do MES |

**Conector extra para a banca:** a saúde do trabalhador é **fator estratégico** para competitividade, produtividade e sustentabilidade da indústria — é o eixo 3 do MES (*Modelos Assistenciais Sustentáveis*), que é literalmente o tema do hackathon.

---

## 4. ⚠️ O que **rejeitar** da mensagem que circulou no grupo

A mensagem do **Moisés (+55 71 8739-0343)** com "🌾 ODS 2: Fome Zero e Agricultura Sustentável" + "🏭 ODS 9" + "🔗 A Intersecção" **já está no `chat.md`** (25/10, 23:15) e **foi reenviada**. Ela é útil em **um ponto** e perigosa em **três**.

### ✅ O que serve

A **lista oficial dos 17 objetivos** que o Gabriel mandou está correta — e é ela que contradiz o rótulo numérico do SESI, não o contrário. As metas 9.4 e 9.5 (agora verificadas com o texto oficial, §2) são exatamente as duas que a proposta ataca.

### ❌ O que não serve

| # | Trecho | Por que rejeitar |
|---|---|---|
| 1 | Toda a metade **"ODS 2: Fome Zero"** (metas 2.1–2.5, solo, cadeia de frio, biotecnologia) | **Material de outro domínio.** A inservibilidade do "ODS 2 = agricultura" já está registrada no `AGENTS.md` (Correções pendentes #1). Não é insumo de produto aqui |
| 2 | **"🔗 A Intersecção"** — a proposta de que o projeto seja *Agrotechs + Sensores IoT (agricultura de precisão)*, *Cadeias de Frio Inteligentes* e *Biotecnologia Sustentável* | **É o caminho para construir a coisa errada.** Três motivos: (a) é **domínio errado** — o tema é saúde na indústria; (b) o **Anexo I do regulamento rejeita explicitamente** a "incorporação de novas tecnologias" como resposta; (c) é o **produto mais crowded que existe**, sem nenhum dos 12 dias de pesquisa que já estão no repo |
| 3 | **"Indústria 4.0"** e a leitura de "inovação tecnológica digital" no diagnóstico do ODS 9 | A banca mapeia mentalmente para IoT industrial + dashboard — exatamente a armadilha R1 do `AGENTS.md`. É a mesma leitura que faz o time ser confundido com "manutenção preditiva" |

> **A correção que precisa circular no grupo, em uma frase:**
> *"A interseção não é ODS 9 → ODS 2. É ODS 9 → ODS 3: a tecnologia do SESI (dado público + modelo transparente) a serviço da saúde do trabalhador, dentro da indústria."*

---

## 5. Correção de citação — meta 3.8

O `AGENTS.md` (até 31/10) citava a meta 3.8 como *"Cobrir universalmente os serviços de saúde, incluindo atenção reabilitativa"*. **Esse não é o texto da ONU.**

- **Texto oficial da ONU:** *"Atingir a cobertura universal de saúde, incluindo a proteção do risco financeiro, o acesso a serviços de saúde essenciais de qualidade e o acesso a medicamentos e vacinas essenciais seguros, eficazes, de qualidade e a preços acessíveis para todos."*
- **De onde veio "atenção reabilitativa":** da **OMS** — a Resolução WHA76.6 (2023) define a reabilitação como componente essencial da **meta 3.8**. É uma fonte legítima, **mas de outro documento** (OMS, não ONU).

**Regra:** citar a meta pelo texto da ONU; se usar "atenção reabilitativa", atribuir à **OMS/WHA76.6**. Nunca misturar as duas fontes na mesma citação.

---

## 6. Como as metas entram no formulário

**O formulário não tem campo de ODS.** (Verificação: `docs/05-inscricao-formulario.md` §1 — as 22 perguntas do formulário foram lidas na íntegra.) As metas entram como **conhecimento demonstrado**, nos campos de texto livre:

| Campo do formulário | O que colocar |
|---|---|
| "Por que você quer participar deste hackathon?" (obrigatório) | A lacuna + **as metas nominais** — é onde §4.1.2 ("conhecimento na temática proposta") é avaliado |
| "Quais as competências e conhecimentos técnicos…" (obrigatório, multilinha) | As ferramentas, os métodos e a experiência que **viabilizam** as metas |
| "Deseja compartilhar alguma informação complementar…" (opcional) | A proposta em uma linha + o nome do time + o link do repositório |

---

## Fontes

- ONU — Goal 3: un.org/sustainabledevelopment/health · sdgs.un.org/goals/goal3
- ONU — Goal 9: un.org/sustainabledevelopment/infrastructure-industrialization
- IPEA — ODS 3 (adaptação brasileira): ipea.gov.br/ods/ods3.html
- gov.br — "Os cinco P's da Agenda 2030" (cartilha, metas 9.1–9.5): gov.br/culturaviva
- OMS — Resolução WHA76.6 (2023), reabilitação e a meta 3.8: resolutionsportal.who.int
- Formulário oficial (22 perguntas lidas em 31/10/2026) · Regulamento 2026 §2.1, §4.1.2, §8.2.4
