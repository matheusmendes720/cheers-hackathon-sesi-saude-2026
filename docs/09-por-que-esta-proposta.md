# Por que esta proposta — a justificativa completa

**Equipe Cheers · 31/10/2026**
Este é o documento que responde *"por que isso e não outra coisa"*. Ele não substitui `docs/04-proposta.md` (o **o quê**); explica o **porquê**, e traz o detalhe que faltava: **qual a 7ª dimensão que vamos medir, como isso funciona na prática, e qual o impacto real esperado**.

Marca: `[fato]` verificável com fonte · `[hipótese]` leitura nossa.

---

## 0 · O resumo em 6 linhas

1. **O gap:** o SESI tem um instrumento oficial de saúde do trabalhador (o ASSTI) com **7 dimensões**. O relatório do SESI que saiu em setembro mediu **6** e **declarou a 7ª sem analisar**.
2. **A 7ª é "fatores de redução da produtividade"** — o presenteísmo: por que o trabalhador produz menos **sem faltar**. É a **4ª dimensão do Anexo I** (participação das pessoas) com outro nome.
3. **Ela está pronta e validada** (CR = 0,863; AVE = 0,581) — mas o questionário tem **zero** itens de autonomia, propósito ou segurança psicológica. Bateria pronta, instrumento sem item.
4. **A proposta:** operacionalizar a 7ª dimensão — 6 itens, no celular, offline, 90 s, opt-out; agregado anônimo com **k ≥ 10** por posto; cruza com a exposição prevista e vira **3 alavancas priorizadas** para a empresa.
5. **O impacto real não é R$ economizado.** É: a 4ª dimensão do Anexo I **passa a existir como número**, a empresa recebe **ação** em vez de 33 indicadores, e nasce um **antes/depois em dias expostos** — que hoje não existe.
6. **Por que não agrotech/IoT:** §7.2 torna o objeto obrigatório (*modelos assistenciais de saúde*), §6.3 exige responder a *um dos desafios propostos*, e a **seleção é julgada pelo formulário antes do desafio existir**. Não é preferência — é regra.

---

## 1 · O gap, em quatro camadas

### Gap 1 · De DIMENSÃO 🔴
O Anexo I pede **quatro** dimensões: *comportamento, ambiente, organização do trabalho, participação das pessoas*. O instrumento oficial cobre três.

| Evidência | Fonte |
|---|---|
| *"Os resultados focalizam em **seis das sete dimensões** do Sistema de Avaliação em Saúde e Segurança do Trabalhador da Indústria - ASSTI (SESI, 2023) […] **Não foram analisados, os fatores de redução da produtividade por não estarem alinhados ao propósito do presente estudo.**"* | VigIndústria Brasil 2026, **p. 16** `[fato]` |
| Busca literal no questionário completo (p. 110–119): **0** ocorrências de autonomia, autônomo, decisão, decidir, sugestão, engajamento, propósito, confiança, segurança psicológica. "Participação" aparece 2 vezes, e nenhuma sobre voz | VigIndústria, Anexo I `[fato]` |
| A 7ª dimensão é a **segunda mais bem validada** do instrumento: **CR = 0,863; AVE = 0,581** (validade convergente satisfatória) | VigIndústria, **p. 21** `[fato]` |
| O relatório **recomenda** *"fortalecer competências de liderança para promover uma comunicação aberta e um ambiente psicologicamente seguro"* — sem nenhum item que meça isso | VigIndústria, **p. 98** `[fato]` |

> **A fonte do desafio pede a coisa que o instrumento não mede.** Não é leitura nossa.

### Gap 2 · De CICLO 🔴
A cadeia de valor da saúde ocupacional tem **7 elos**: presenteísmo → exposição → evento → afastamento → incapacidade → saída → resultado. Instrumenta-se do **3 ao 6**. O **elo 1 (presenteísmo)** não existe em sistema nenhum — e é no 1 e no 2 que a predição funciona, antes do evento.

### Gap 3 · De DECISÃO 🟡
O VigIndústria entrega 33 indicadores com prevalência nacional para 57.952 trabalhadores em 825 empresas — mas:
- **não diz "aqui está o foco desta empresa"** (mede, mas não prioriza por recorte);
- **não mede se a intervenção funcionou**: é transversal, de um tempo só (jul–dez/2025).

O próprio relatório pede: *"a **continuidade do monitoramento sistemático** por meio do VigIndústria será fundamental para validar a efetividade das intervenções"* (p. 100). **Não existe antes/depois.**

### Gap 4 · De INCUMBENTE 🟡
| Quem | O que faz | Por que não fecha o gap |
|---|---|---|
| **ASSTI + Sesi Viva+** (o próprio SESI) | Avaliação populacional do trabalhador, 7 dimensões, desde 2018 | *"Empresa só recebe agregado"* — não recebe nada acionável |
| **SOC · SGG · WOTY** | Dashboard de SST + eSocial + PGR + COPSOQ | É o *"dashboard de SST"* — valor incremental zero frente ao que já é vendido |
| **bem.care, mywork, BlueService, Apdata** | Atestado → falta → folha | *"Atestado = ausência, não saúde"*. Contam a falta; ninguém cruza **falta ↔ saúde ↔ população** |
| **Onvida, Selven, DUO24h** | Telemedicina B2B | R$ 19,90–79,90/colaborador/mês. Commodity |
| **NRGuard, Benway, NR1Plus** | COPSOQ/HSE + relatório IA + PGR | R$ 0–1.297/mês. Diagnóstico comoditizado |
| **500+ consultorias credenciadas SESI BA** | NR-1, PGR, laudos | R$ 15–80 mil, 4–12 semanas. Entregam laudo — a intervenção não é delas |
| **MEUSOC (do SOC)** | App do trabalhador: 500 mil+ downloads | O canal existe, mas a reclamação mais frequente do líder é **não conseguir anexar atestado**. O trabalhador adota app *sobre ele*, não *dentro* do plano de cuidado |

---

## 2 · Qual a 7ª dimensão que vamos medir — e como, na prática

### 2.1 · A identidade da dimensão

| | |
|---|---|
| **Nome no ASSTI** | **Fatores de redução da produtividade** (7ª de 7) |
| **O que é, no fondo** | Os fatores que fazem o trabalhador **produzir menos sem faltar** — presenteísmo, carga, falta de autonomia, ausência de propósito |
| **Por que é a 4ª dimensão do Anexo I** | O Anexo I pede modelos que fortaleçam *"autonomia, participação, bem-estar e senso de propósito"*. Isso **é** o conjunto de fatores de redução da produtividade, medido na organização do trabalho |
| **Estado** | Construída, validada (CR 0,863 · AVE 0,581), **declarada e nunca analisada** (p. 16) |

### 2.2 · Como vamos operacionalizá-la: os 6 itens

O referencial de medição de risco psicossocial mais validado é o conjunto de **HSE Management Standards** (Health and Safety Executive, Reino Unido, 2000) — **seis fatores** que, medidos por escala Likert, formam o índice de contexto de trabalho. É esse referencial que usamos, adaptado ao português brasileiro.

| # | Item | Pergunta (como o trabalhador lê no celular) | O que mede |
|---|---|---|---|
| 1 | **Demanda** | *"A quantidade de trabalho que me é pedida cabe no meu tempo."* | Sobrecarga, ritmo, falta de recursos |
| 2 | **Controle** | *"Tenho margem para decidir como faço o meu trabalho."* | Autonomia sobre método e sequência |
| 3 | **Apoio** | *"Recebo apoio de colegas e chefia quando preciso."* | Capital social no posto |
| 4 | **Reconhecimento** | *"O meu trabalho é reconhecido."* | Retorno do esforço |
| 5 | **Propósito** | *"O meu trabalho faz sentido para mim."* | Sentido de propósito |
| 6 | **Segurança** | *"É seguro falar o que penso no trabalho."* | Segurança psicológica |

**Escala:** 1 (discordo) a 5 (concordo fortemente). **Tempo:** ~90 s. **Opt-out por bloco:** o trabalhador pode pular qualquer item — a ausência de resposta também é dado válido, e a recusa é garantida.

> **O ponto forte, e é o que a banca vai notar: a gente não inventa questionário.** A 7ª dimensão do ASSTI já existe como construto validado pelo próprio SESI. A nossa contribuição é **torná-la operacional** — dar voz ao trabalhador, agregar com privacidade, e converter em alavanca. É a diferença entre *"temos um relatório"* e *"temos a dimensão funcionando"*.

### 2.3 · Como funciona, na prática — uma terça-feira

| Momento | O que acontece |
|---|---|
| **07h40** | O trabalhador recebe o convite pelo canal que **já existe** (Sesi Viva+ / rede credenciada do SESI-BA, 500+ credenciadas e 15 carretas). Nenhuma conta nova, nenhuma instalação obrigatória. |
| **07h45** | Abre no celular. **Funciona offline** (é um PWA instalável, sem CDN, sem chamada de rede — §11.2 não dá equipamento e a rede do local não é garantida). Responde 6 itens em 90 s. Pode pular 2. |
| **07h47** | **Recebe de volta as 2 alavancas que são dele** — não um relatório. A tela diz: *"o que muda na sua rotina, e o que a empresa precisa ajustar no posto"*. É a devolução que ninguém faz hoje. |
| **Ao longo do dia** | A resposta fica **no aparelho dele**. Nada individual sai. Zero dado de saúde individual compartilhado (LGPD art. 11). |
| **Só quando o posto tem k ≥ 10** | O agregado anônimo do posto é liberado. Abaixo de 10, **não sai nada** — nem para o SESI, nem para a empresa. É uma trava de privacidade, não um parâmetro. |
| **Semana seguinte** | O **painel do SESI** mostra, por posto: **índice de contexto de trabalho** (0–100), **composição por item** e **dias expostos** pelo modelo de exposição — com **todos os pesos à vista** e um "como o modelo funciona" aberto. |
| **Segunda-feira seguinte** | O **RH da empresa** abre e vê **3 alavancas priorizadas**, cada uma com o indicador nacional que a justifica: *reduzir a demanda no posto* · *fortalecer o apoio* · *comunicar prevenção que chegue*. |
| **90 dias depois** | A mesma pergunta, de novo. É aí que nasce o **antes/depois** que o VigIndústria não tem (p. 100). |

### 2.4 · O que sai de cada ponta

| Ponta | Entrada | Saída |
|---|---|---|
| **Trabalhador** | 6 respostas (ou fewer) | As **2 alavancas dele**, em linguagem comum |
| **Posto (k ≥ 10)** | Respostas agregadas | **Índice de contexto de trabalho** 0–100 + composição por item |
| **Empresa** | Índice do posto + exposição prevista | **3 alavancas priorizadas**, com o número que as justifica |
| **SESI** | Agregados por posto e região | A **7ª dimensão finalmente analisada**, com antes/depois |
| **Ninguém** | — | Nada individual. Nenhum parecer. Nenhuma decisão de emprego |

---

## 3 · O impacto real esperado — honesto, e por isso defensável

### 3.1 · A cadeia causal que a proposta assume

```
alavanca no posto            contexto de trabalho        presenteísmo        exposição        desfecho
(3 alavancas priorizadas) → (índice por posto)     →   (dias improdutivos) → (dias expostos) → (afastamento)
```

### 3.2 · O que a gente **promete medir** (e é o que o Anexo I e a OIT pedem)

| Métrica | Como | Por que ela é nova |
|---|---|---|
| **Dias expostos por posto** | Modelo de exposição sobre VigIndústria + CAT, pesos à vista | É a unidade de intervenção: "quantos dias de exposição a mais este posto tem" |
| **Índice de contexto de trabalho** | Agregado k ≥ 10 dos 6 itens | **Não existe** — é a 7ª dimensão, declarada e nunca analisada |
| **Alavancas priorizadas** | Motor de regras, com o indicador nacional que justifica cada uma | Hoje a empresa recebe 33 indicadores e nenhuma priorização |
| **Mudança organizacional** | Duas ondas de 6 itens, 90 dias de intervalo | É o antes/depois que o relatório pede (p. 100) e que não existe |

### 3.3 · O que a gente **não** promete — e por que isso é uma força, não uma fraqueza

| Não prometemos | Por quê |
|---|---|
| Redução de absenteísmo em % | A meta-análise que sustenta os itens é **de estudos observacionais** — associa, não prova causal `[fato]` |
| ROI / economia em R$ | Em ensaio randomizado (n = 32.974), o retorno de programa de absenteísmo foi **−49%**. A literatura de "1 real economizado por 2 investidos" é artefato de desenho de estudo `[fato]` |
| "Manutenção preditiva" | O Anexo I rejeita a leitura de IoT industrial. É previsão de desfecho de saúde do trabalho |
| R$ 468 bi atribuído ao presenteísmo | Esse número é de **doenças e acidentes** de trabalho, não de presença improdutiva `[fato]` |

### 3.4 · A base científica dos dois itens que sustentam as alavancas

| Fator | Efeito na ausência | Meta-análise |
|---|---|---|
| **Demanda** de trabalho | OR **1,57** (1,04–2,36) — aumenta | significativo |
| **Apoio** no trabalho | OR **0,58** (0,41–0,83) — **reduz** | significativo |
| *"Job strain"* (composto) | OR 1,20 (0,94–1,52) — **não** significativo | — |

> **Por que isso importa para a proposta:** a literatura mostra que **demanda e apoio funcionam; autonomia genérica não**. É por isso que o instrumento não pergunta "você se sente autônomo?" (que seria vago e não preditor) e pergunta **"a quantidade de trabalho que me é pedida cabe no meu tempo?"** e **"recebo apoio quando preciso?"** — duas perguntas específicas, com OR publicado. **A escolha dos itens não é estética — é a diferença entre um questionário e uma ferramenta.**

### 3.5 · O impacto real, em uma frase honesta

> **"A gente não promete reduzir absenteísmo. A gente promete instrumentar a dimensão que o Anexo I pede e que não existe, entregar 3 alavancas acionáveis por posto, e criar o antes/depois em dias expostos que hoje não existe — que é o pré-requisito de qualquer promessa de economia, e exatamente o que o relatório do SESI pede na p. 100."**

**E o tamanho esperado, em ordem de confiança:**
1. **Certeiro:** a lacuna de medição é preenchida (a 4ª dimensão vira número). Isso acontece no piloto.
2. **Certeiro:** a empresa recebe 3 alavancas priorizadas em vez de 33 indicadores soltos.
3. **Provável:** a exposição prevista fica **estimável no nível do posto** (hoje ela é só nacional).
4. **Hipótese a medir:** menos dias expostos após a alavanca.
5. **Não será afirmado:** economia em R$. Vira o **piloto** — e é o que separa uma proposta séria de um pitch.

---

## 4 · Por que não agrotech / IoT / cadeia de frio — a regra, não o gosto

| # | Teste | Texto do regulamento | Veredito |
|---|---|---|---|
| 1 | **Objeto** | §7.2 — *"As equipes deverão desenvolver soluções para **Desafios e soluções para a sustentabilidade dos modelos assistenciais de saúde** (Anexo I)"* | ❌ não é modelo assistencial de saúde |
| 2 | **Parâmetro** | §2.1 — *"tendo como parâmetro os **ODS 2 – Saúde e Bem-Estar** e **9 – Indústria, inovação e infraestrutura**"* | ❌ o ODS 2 real é agricultura; os dois parâmetros são saúde **e** indústria |
| 3 | **Natureza da ação** | §2.3 — *"A ação **não possui caráter comercial** nem objetiva resultados financeiros, tendo, portanto, finalidade cultural e social"* | ❌ um produto de logística alimentícia é comercial **por natureza** |
| 4 | **Ecossistema** | §3.6 — *"profissionais e ou acadêmicos atuantes no **ecossistema de saúde**, tecnologia da informação, designers, gestão"* | ❌ o evento é saúde |
| 5 | **Desafio real** | §6.3 — desenvolver solução para *"**um dos desafios propostos**"* (§7.3: apresentados na abertura) | ❌ só existe se estiver na lista |
| 6 | **Cronologia** | §4.1.2 — a seleção julga *"conhecimento na temática proposta"* pelo **formulário**; o desafio só aparece em **13/11** | ❌ **pode nem ser selecionado** |
| 7 | **Originalidade** | §10.6 — *"total responsabilidade pela solução apresentada, garantindo sua **originalidade** e titularidade"* (+ §10.7) | ❌ o espaço mais crowded que existe |

**O argumento decisivo, em uma frase:** *a seleção vem antes do desafio existir, e é julgada pelo formulário contra o §7.2 — o agro não "perde pontos", ele **perde a vaga** ou constrói contra um desafio que talvez nem exista.*

**E o ponto honesto a favor do agro (que é real):** o "sexy" dele é uma variável de **craft**, não de domínio. O regulamento paga **Inovação (20%)** e **Maturidade + Sofisticação técnica + Experiência do usuário (40%)**. Transpondo o mesmo energia:

| Agro | Equivalente no domínio certo |
|---|---|
| Sensores IoT e dashboard | **Modelo transparente com pesos à vista** — auditoria vale mais que caixa-preta, e **ninguém** no mercado de SST faz isso |
| Drones e agricultura de precisão | **PWA offline de verdade, 90 s, na máquina de qualquer um** — tecnologia que respeita o chão de fábrica |
| Cadeia de frio inteligente | **A cadeia da saúde ocupacional com o elo 1 iluminado** — mesma lógica, domínio certo |

---

## 5 · As cinco bifurcações — o que acontece quando o tema real aparecer em 13/11

O §7.3 diz que o detalhamento dos desafios será apresentado **na abertura, dia 13/11 às 18h30**. Por isso a proposta **não é uma solução travada**: é um núcleo com 5 componentes.

| Se o desafio for sobre… | **Núcleo (obrigatório)** | Corte imediato | Fica como camada |
|---|---|---|---|
| **Participação / autonomia / propósito** | **Escuta** (6 itens) + **Motor de alavancas** | Export FHIR · Plano do trabalhador | Exposição prevista vira contexto |
| **Absenteísmo / custo / previsão de desfecho** | **Exposição prevista** + **Motor de alavancas** | Escuta vira 4 itens · Plano vira 1 alavanca | Escuta entra se sobrar tempo |
| **Risco / exposição / prevenção / laudo** | **Exposição** + **Motor** + orquestração de prazo | Escuta inteira | — |
| **Retorno ao trabalho / incapacidade** | **Catálogo de demandas por posto** + plano de retorno | Exposição vira tabela | Export FHIR vira o entregável institucional |
| **Fragmentação / interoperabilidade / SUS-plano** | **Export FHIR R4 (RNDS) + eSocial** + trajectory | Escuta vira acessória | — |

**A grade de decisão (4 testes, 90 minutos, escopo travado às 20h de 13/11):**
1. **Integração** — cobre ≥3 das 4 dimensões do Anexo I?
2. **Dado** — existe dado público que responde?
3. **Mensurabilidade** — existe antes/depois?
4. **Nossa evidência** — a 7ª dimensão morta e o zero de itens são a resposta direta?

Passa em ≥3 → **vai**. Detalhe operacional em `docs/08-plano-90min.md`.

---

## 6 · O veredito final

> **A nossa proposta não é "mais uma solução de saúde ocupacional". É a ativação da única dimensão do instrumento oficial do SESI que foi declarada e nunca analisada — que é exatamente a dimensão que o Anexo I do desafio pede.**
>
> O que o mercado já faz: conta a falta, vende laudo, vende telemedicina, vende dashboard.
> **O que ninguém faz:** dá voz ao trabalhador e devolve, à empresa, a alavanca que muda o trabalho — com a evidência do número e sem identificar ninguém.
>
> E é a única proposta que **não pode ser invalidada pelo reveal**, porque nasce de uma lacuna que a própria fonte do desafio declara.

---

## Fontes

VigIndústria Brasil 2026 (SESI/CN-SESI/Ministério da Saúde, 119 p.) — p. 16 (as 7 dimensões e a frase da 7ª) · p. 21 (CR 0,863 / AVE 0,581) · p. 98 (recomendação) · p. 100 (monitoramento contínuo) · Anexo I p. 110–119 (o instrumento) · SESI/ASSTI *Estilo de Vida, Saúde e Produtividade* (n = 123.355) · CANPAT · INSS · meta-análise de job strain × ausência · RCT de absenteísmo (ROI −49%) · Regulamento 2026 §2.1, §2.3, §3.6, §4.1.2, §6.3, §7.2, §7.3, §10.6, §11.2 · `docs/01` · `docs/04-proposta.md` · `docs/07-alavancas-regulamento.md` · `docs/08-plano-90min.md` · `docs/pesquisa/01-mapa-competitivo.md` · `pitch/demo.html` · `pitch/roteiro-3min.md`
