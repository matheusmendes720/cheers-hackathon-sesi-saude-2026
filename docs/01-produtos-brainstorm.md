# Brainstorm de produtos — 10 conceitos → 3 → 1

**Equipe Cheers · 27/10/2026 · insumo para D2 (nicho) e D3 (10 → 3 → 1)**
Base: `docs/00-portfolio-oportunidades.md` · `data/vigindustria-2026.md` · 9 fontes primárias em `docs/sources/`.

Marca: `[fato]` verificável · `[hipótese]` leitura nossa · `[a confirmar]`.

---

## O frame de design (o que a pesquisa impõe a qualquer produto)

Seis restrições que matam mais da metade das ideias antes de nascer:

| # | Restrição | Origem | Consequência |
|---|---|---|---|
| 1 | **Não é "incorporação de novas tecnologias"** — é redesenho do modelo assistencial | Anexo I do regulamento | App de atividade, telemedicina e dashboard de indicador estão fora |
| 2 | **Quatro dimensões obrigatórias**: comportamento, ambiente, organização do trabalho, participação | Anexo I | Produto que cobre uma só é incompleto |
| 3 | **O destino é autonomia, participação, bem-estar e senso de propósito** — não "redução de custo" | Anexo I | Não prometer ROI: em RCT o ROI de absenteísmo é **−49%** `[fato]` |
| 4 | **Demo offline, ~30 h, 2 devs** | §11.2 (não fornecem notebook) + §6.2 (2 dias imersivos) | PWA local, dados públicos, zero backend |
| 5 | **IA só em função administrativa/apoio** | Res. CFM 2.454/2026, Anexo II, I (baixo risco) | Sem diagnóstico, sem parecer, sem score individual que vire decisão de emprego |
| 6 | **Só agregado (k ≥ 10) ou sintético** | LGPD art. 11 §4º/§5º; NR-7 (ASO sigiloso) | Nada de dado individual de trabalhador |

**O ativo raro que a pesquisa revelou:** o ASSTI tem 7 dimensões, o VigIndústria analisou 6, e a 7ª (*fatores de redução da produtividade*) foi **declarada mas nunca analisada** `[fato, p. 16]`. Em paralelo, o instrumento de coleta tem **zero itens** para autonomia, decisão, propósito, confiança e segurança psicológica `[fato, verificado no Anexo I, p. 110–119]`.

> **As duas lacunas são o mesmo buraco visto de dois lados:** o sistema mede o risco que o trabalhador corre, mas não mede o poder que ele tem nem o trabalho que ele faz.

---

## As 10 ideias

| # | Conceito | O que faz, em uma linha | Âncora de evidência | 4 dimensões | 30 h | Demo em 3 min |
|---|---|---|---|---|---|---|
| 1 | **Aciona** | Converte um evento de ausência em plano de retorno ao trabalho com adaptação de posto | Cochrane 14 RCT: **−33,3 dias** de absenteísmo; intervenção dirigida ao trabalho: **89% vs 73%** de retorno `[fato]` | Org. do trabalho ★★★ | Média | Um atestado entra, sai um plano de retorno |
| 2 | **Escuta** | Micro-diagnóstico conversacional de 6 itens, offline, em que o trabalhador fica dono do plano e da própria voz | Instrumento atual: **0 itens** de autonomia/participação `[fato]` | Participação ★★★ | **Alta** | O trabalhador fala no celular e recebe a alavanca dele |
| 3 | **Roda** | Transforma o VigIndústria transversal (1 tempo só) em sinal mensal por empresa e detecta deriva | Relatório p. 100: *"a continuidade do monitoramento sistemático [...] será fundamental"* `[fato]` | Todas, por infraestrutura | Média | Duas ondas de dado, a curva, a deriva detectada |
| 4 | **Alavanca** | Do perfil da empresa (CNAE, porte, região, escolaridade) + perfil de ausência, sai o ranking de alavancas organizacionais | 8,1% insatisfação com condições de trabalho; 65,6% acha comunicação insuficiente `[fato]` | Org. do trabalho ★★★ | **Alta** | Slide: 5 alavancas, cada uma com o número que a justifica |
| 5 | **Prazo** | Orquestra os prazos da NR-7 (demissional 10 dias, retorno se afastamento ≥30 dias, periódico 1–2 anos) | NR-7; Salú entregou **+1 mi de agendamentos** `[fato]` | Ambiente (fraca) | **Muito alta** | Contagem regressiva para o prazo legal |
| 6 | **Linha DCNT** | Linha de cuidado para DCNT ocupacional (hipertensão 16,2%, diabetes 5,7%) com adaptação de jornada e de posto | Prevalências do VigIndústria; SESI/CE testando 4 linhas DCNT `[a confirmar]` | Org. do trabalho, comportamento | Baixa | Perfil de risco crônico → posto adapted |
| 7 | **Campanha** | Micro-campanha de literacia em saúde, segmentada por escolaridade, com medição de efeito | Relatório p. 99: *"campanhas direcionadas ao aumento da literacia"*; menor escolaridade → autocuidado frágil `[fato]` | Comportamento, participação | Média | Segmento → sequência de mensagens → indicador antes/depois |
| 8 | **Comunica** | Do dado de segurança da empresa, o que comunicar para qual turno, quando | 65,6% acha a comunicação suficiente; **59,5%** das micro-empresas recebeu treinamento `[fato]` | Ambiente, org. do trabalho | **Muito alta** | Um turno, uma mensagem, um porquê |
| 9 | **Coordenado** | Camada digital de cuidado SESI ↔ plano ↔ SUS, com trajectory longitudinal | Conecta Saúde 2026: *"conectar informações, acompanhar a trajetória do trabalhador"* `[fato]` | Todas, indireta | **Baixa** | Difícil — 3 integradores |
| 10 | **Catálogo de posto** | Catálogo estruturado de demandas por posto (PGR/NR-7 + CNAE) — a matéria-prima de RTW, absenteísmo e readequação | IESS/SESI: readequação estrutural, dor nas costas **53% → 33%** `[fato]` | Org. do trabalho, ambiente | Média | Um posto, suas demandas, o que pode ser adapted |

### Wildcards — três ângulos fora do domínio

| # | Wildcard | Por que pode vencer |
|---|---|---|
| **W1** | **A empresa como paciente.** Em vez de medir o trabalhador, o SESI mede a **organização** e entrega um índice de saúde do trabalho (demanda, controle, apoio, reconhecimento). O trabalhador deixa de ser ativo de risco e vira cliente com voz. | Inverte o objeto do modelo assistencial — é literalmente "redesenhar o modelo". Se a banca perguntar "o que é novo aqui?", a resposta é "quem é o paciente". |
| **W2** | **O eSocial como espelho do trabalho.** Cruzar eSocial (demanda, jornada, rotação) com saúde agregada produz "custo do absenteísmo por desenho de turno" — sem tocar em dado de saúde individual. | Dá a **organização do trabalho** uma métrica nova e é 100% público. Complementa o VigIndústria em vez de repetir. |
| **W3** | **Prontuário de voz.** Registro estruturado, anonimizado e agregado das falas dos trabalhadores sobre o próprio trabalho, virado em item de medição (o que 0 instrumento mede hoje). | É a camada que torna a 4ª dimensão do Anexo I auditável. Alto risco de parecer "pesquisa" se não tiver productização. |

---

## Shortlist — as 3 que valem o ensaio de pitch

### 🥇 A — **Escuta + Alavanca** (fuso: participação instrumentada → alavanca organizacional)

> **Hook:** *"O VigIndústria mede o risco que o trabalhador corre. Não mede o poder que ele tem, nem o trabalho que ele faz. A gente instrumenta as duas coisas que faltam."*

| | |
|---|---|
| **O que é** | PWA instalável e offline. O trabalhador responde 6 itens (demanda, controle, apoio, reconhecimento, propósito, segurança — derivados do HSE) numa conversa. Recebe **as alavancas dele**, não um relatório. O agregado (k ≥ 10) volta para a empresa como 3 alavancas organizacionais priorizadas. |
| **Números** | 0 itens no instrumento atual `[fato]` · 20,0% dos trabalhadores faltaram ≥1 dia/semana; 6,5% ≥3 dias `[fato]` · **34,2%** com consumo álcool episodico pesado, 68% acima da população geral `[fato]` · 44,3% sedentarismo no lazer `[fato]` |
| **Por que não é a armadilha** | Não é app de atividade (mede contexto, não movimento), não é telemedicina, não é dashboard. Devolve poder ao trabalhador e devolve **ação** à empresa. Cobre as 4 dimensões: comportamento (o que o trabalhador já faz), ambiente, organização do trabalho (as 6 perguntas são exatamente isso) e participação (é o canal). |
| **Demo (90 s)** | 1) Um trabalhador no celular, offline, responde as 6 perguntas. 2) Ele recebe: *"suas 2 alavancas: seu turno e seu posto de trabalho"*. 3) Corte para a visão da empresa: 3 alavancas, cada uma com o indicador do VigIndústria que a justifica e o custo em dias. |
| **Risco** | O motor de alavancas precisa ser crível no pitch. Mitigação: as 6 perguntas **são** as alavancas — não há motor de IA, há lógica de regra explicável. Isso é mais forte, não mais fraco. |
| **Viabilidade** | 6 h (itens + diálogo) · 10 h (PWA offline + agregação) · 8 h (motor de alavancas) · 6 h (export FHIR/eSocial) |

### 🥈 B — **Aciona** (volta ao trabalho com plano, não com advice)

> **Hook:** *"A empresa não tem um problema de saúde do trabalhador. Tem um problema de projeto de trabalho. A gente entrega o plano de volta."*

| | |
|---|---|
| **O que é** | Recebe o evento de ausência e devolve: (a) plano de retorno com prazo, (b) **adaptação de posto** a partir de um catálogo de demandas, (c) o que muda no trabalho para a próxima vítima do mesmo posto. Opera no **posto**, não na pessoa. |
| **Números** | −33,3 dias de absenteísmo cumulativo (Cochrane, 14 RCT, n = 1.897) `[fato]` · 89% vs 73% de retorno para intervenção dirigida ao local de trabalho `[fato]` · dor nas costas 53% → 33% com abordagem estrutural; −4,3 vs −2,1 pontos `[fato]` · **SESI/BA já tem** a metodologia WDP/SAW/RTW, com auto-diagnóstico *"em breve"* na VIVA+ `[fato]` |
| **Por que não é a armadilha** | É readequação de trabalho, não tratamento. Ataca a **organização do trabalho**, que é a dimensão com mais evidência de efeito. E tem contraparte institucional pronta. |
| **Demo (90 s)** | 1) Um registro de ausência (sintético) entra. 2) Sai: "volta em 15 dias, 3 tarefas do posto adaptadas, 1 mudança no turno". 3) O custo evitado em dias, com a fonte do número. |
| **Risco** | **Alto na fronteira regulatória** se individualizar. Mitigação: o motor trabalha com **demandas do posto**, não com diagnóstico. Revisão CFM obrigatória antes de codar. |
| **Viabilidade** | 20 h · exige o **Catálogo de posto** (ideia 10) como insumo — o que aumenta o escopo, mas também a exclusividade |

### 🥉 C — **Roda** (monitoramento contínuo + comunicação dirigida)

> **Hook:** *"O relatório que o SESI acabou de publicar pede, na própria página 100, que o monitoramento continue. Ele é transversal — uma fotografia. Ninguém tira a segunda foto."*

| | |
|---|---|
| **O que é** | Camada de sinal mensal por empresa/unidade: combina o corte transversal (VigIndústria) com série sintética mensal e **detecta deriva** (estresse ↑ + relaxar ↓ + comunicação ↓ = alerta), apontando a alavanca. Fecha o ciclo: a intervenção vira hipótese verificável. |
| **Números** | p. 100 do relatório: *"a continuidade do monitoramento sistemático por meio do VigIndústria será fundamental para validar a efetividade das intervenções"* `[fato]` · p. 98–99: 5 recomendações de ação que hoje não têm como ser validadas `[fato]` |
| **Por que não é a armadilha** | Não é dashboard de indicador (camada saturada: SOC, SGG, WOTY, ASSTI). É **detecção de deriva + ação recomendada + medição de efeito**. E a "continuidade" é o que o Anexo I pede (transformação, não episódio). |
| **Demo (90 s)** | 1) Duas ondas de dado. 2) A curva que foge. 3) O alerta: "comunicação e liderança caíram — a alavanca é X". 4) O que acontece depois. |
| **Risco** | Efetividade leva tempo para aparecer → no pitch, vender o **loop de medição**, não o resultado. Mitigação: mostrar a lógica de detecção, não o efeito. |
| **Viabilidade** | 16 h · é a **infraestrutura que torna A e B verificáveis** |

### Menção honrosa — **Prazo** (ideia 5)

A mais rápida de construir (8 h), a mais fácil de demonstrar (contagem regressiva para os 10 dias do demissional) e com valor de mercado comprovado pelo playbook da Salú (+1 mi de agendamentos, +300 mil horas devolvidas ao RH). **Mas** é a camada de compliance, que é a mais saturada do mercado, e tem a história mais fraca para o Anexo I. Serve de **fallback** se o time escolher pragmatismo sobre tese.

---

## Matriz de decisão

| Critério (peso) | A · Escuta+Alavanca | B · Aciona | C · Roda | Prazo |
|---|---|---|---|---|
| Impacto — clareza do número no pitch (25%) | 5 | 5 | 3 | 4 |
| Inovação — "isso não existe" (25%) | **5** | 4 | 4 | 2 |
| Viabilidade — 30 h, offline, 2 devs (25%) | **4** | 2 | 4 | **5** |
| Aderência ao Anexo I (15%) | **5** | 4 | 4 | 2 |
| Blindagem regulatória (10%) | 4 | 2 | **5** | 3 |
| **Total ponderado /100** | **91** | 70 | 78 | 63 |

*Escala 1–5. A aderência ao Anexo I entra com peso alto de propósito: um produto tecnicamente perfeito que a banca lê como "mais um app" perde austainability, mesmo com nota alta em maturidade.*

---

## Recomendação

**Construir A (Escuta + Alavanca), com C (Roda) como a camada que fecha o loop dentro do próprio demo, e B (Aciona) como a expansão pós-hackathon.**

Por quê:

1. **A é a única que ocupa a lacuna declarada na fonte do desafio.** Não é inferência da nossa parte: o instrumento não mede participação, o ASSTI não analisou a 7ª dimensão, e o Anexo I pede exatamente as duas coisas.
2. **A é a mais demonstrável em 3 minutos** — e o pitch vale 60% da nota (§8.2.4).
3. **A + C juntas têm a forma que a banca premiou duas vezes** (integração de dados + experiência do cliente) e a forma que o relatório pede (monitoramento contínuo).
4. **A tem o menor risco regulatório** das três — IA em função administrativa, agregação k ≥ 10, nada de parecer.
5. **B fica como plano de expansão**, o que mostra visão de longo prazo sem inflar o MVP — e B tem a melhor história institucional (SESI/BA já tem WDP/SAW/RTW).

**O pitch em 3 frases:**
1. *"O SESI mede, em 57.952 trabalhadores, o risco que a indústria corre — mas não mede o trabalho que causa o risco."*
2. *"A 7ª dimensão do ASSTI, os fatores de redução da produtividade, foi declarada e nunca analisada. Nenhuma empresa no mercado cruza saúde com absenteísmo."*
3. *"A gente entrega a camada que falta: o trabalhador fala, a empresa recebe a alavanca, e o absenteísmo é a consequência — não a promessa."*

---

## Mecânica para a sessão de brainstorm (D3)

Rodar **60 min**, em grupo, com estas 5 provocações. Cada uma força um ângulo que a lista não cobre.

1. **"Qual é o paciente?"** — Se o objeto do modelo assistencial é o trabalhador (ativo de risco), o que muda se for a **organização**? (→ W1)
2. **"O que o trabalho faz com a saúde, e não o que a saúde faz com o trabalhador?"** — Onde, no turno, na escala, na rotação, no layout da linha, a organização produz o dano? (→ W2)
3. **"O que a pessoa faz quando o sistema a trata como número?"** — A ausência é o momento exato em que o trabalhador sai do processo. O que o produto devolve naquele instante?
4. **"Qual é a menor coisa que ainda é uma tese?"** — Não a menor demo: a menor *tese*. Se só couber um componente, qual?
5. **"O que a organização vai comprar no dia 30?"** — Não o que impressiona a banca: o que o gestor de RH assina.

**Critérios de kill** (qualquer um elimina o conceito):
- Precisa de dado individual de trabalhador → eliminada
- Depende de API externa para funcionar offline → eliminada
- É um dashboard de indicador → eliminada
- Promete economia/ROI na demo → eliminada (evidência é contra)
- Não cabe em 30 h de 2 devs **com** o demo offline → eliminada

**Regra de saída:** shortlist de 3, uma escolha, e **decisão registrada no `AGENTS.md` (D2/D3)** com o número que ancora o gancho do pitch.

---

## Fontes

Todas em `docs/sources/` (verificadas no original, 27/10/2026). Ver `docs/sources/README.md` para o índice e as regras de citação.

- `docs/00-portfolio-oportunidades.md` — 5 oportunidades ranqueadas, armadilhas com evidência, escudo regulatório, MVP de 30 h
- `data/vigindustria-2026.md` — 33 indicadores com página e tabela; grade das 4 dimensões; verificação do instrumento
- `docs/pesquisa/01-mapa-competitivo.md` — 11 players, 5 barreiras, 5 camadas descobertas, 5 armadilhas
- `docs/research/falhas-do-modelo-atual.md` — 8 falhas do modelo, 5 casos de sucesso, contra-argumentos
- `docs/viabilidade-stack-dados-regulatorio.md` — stack vs. critérios da banca, datasets, interoperabilidade, tarefas de IA defensáveis
- `docs/pesquisa/02-dimensionamento-mercado.md` — dimensionamento e funil de custo
