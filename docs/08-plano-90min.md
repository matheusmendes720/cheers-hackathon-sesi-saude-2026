# O plano dos 90 minutos — 13/11, quando o desafio for revelado

**Equipe Cheers · 31/10/2026 · o artefato que decide o produto**
Por que existe: §7.3 diz que o detalhamento dos desafios *"será apresentado na abertura do evento, diretamente às equipes"*. **O que se leva ao dia 14 não é uma solução pronta — é capacidade de absorver o desafio em 90 minutos.** Este é o procedimento.

---

## 0 · O calendário real (com dia da semana — isso muda o urgency)

| Data | Dia | O quê | Custo |
|---|---|---|---|
| 31/10 | **sábado** | hoje | — |
| 02–06/11 | seg–sex | **5 dias úteis** | ⚠️ é o prazo real de tudo |
| 07/11 | sábado | último dia útil de verdade | — |
| 08/11 | **domingo** | **fim das inscrições** (o `EndTime` técnico é 09/11 00h15) | ⚠️ ninguém trabalha no domingo |
| 10/11 | terça | *"a partir de"* — divulgação dos selecionados | — |
| 12/11 | quinta | live de orientações **13h** + divulgação dos aprovados (§4.4) | — |
| 13/11 | **sexta** | **live de abertura 18h30** — o desafio é revelado | 🔴 **a noite que decide** |
| 14/11 | **sábado** | check-in **07h30** (sair de casa ~05h30) | ⚠️ dia de hackathon = fim de semana |
| 15/11 | **domingo** | entrega **15h30** · pitch **16h** · fim **19h** | ⚠️ o evento inteiro é um fim de semana |

**Duas consequências operacionais que ninguém tinha no radar:**

1. **As 5 inscrições precisam estar prontas até sexta 06/11.** O prazo oficial é domingo, mas é domingo — e o `EndTime` técnico dá só 15 min de margem depois da meia-noite.
2. **§4.3 dá 24 h para confirmar a seleção.** O e-mail pode chegar entre 10/11 e 12/11 — **e a confirmação pode cair no fim de semana.** Definir **agora** quem responde o e-mail de confirmação se o titular não puder (mesmo com a inscrição feita, o e-mail de confirmação tem que ter lido o e-mail no celular).

> **O check-in às 07h30 de um sábado, depois de uma live na sexta que termina às 20h30, com entrega às 15h30 de domingo.** Quem planejar 2 dias de trabalho normal vai quebrar na sexta à noite. Planejar como **um plantão de 30 h com revezamento** é o que funciona — e por isso o MVP de 32 h com plano de corte (D5/D3) importa mais do que nunca.

---

## 1 · O cronômetro de 90 minutos (13/11, 18h30 → 20h00)

> **Regra de ouro: às 20h00, o escopo está travado.** Não às 21h, não "amanhã". Quem decide às 20h decide com o cansaço do dia; quem decide às 21h decide sem dormir e sem protótipo.

| Tempo | Bloco | Quem | O que fazer | Saída |
|---|---|---|---|---|
| **0:00–0:15** | **Escuta sem falar** | os 5, em silêncio | Anotar as **falas literais** das empresas do Conecta Saúde 2026. Quais palavras se repetem? Quem falou de quê? **Ninguém discute ainda.** | 5 anotações brutas, uma por pessoa |
| **0:15–0:30** | **Mapear nas 4 dimensões** | Matheus | Para cada desafio anunciado: quais das 4 dimensões do Anexo I ele toca? | Challenge cards, uma por desafio, com as 4 dimensões marcadas |
| **0:30–0:45** | **Testar o kit** | Moisés + Omena | O desafio conecta a algum dos 5 eixos (O1–O5) ou aos 3 shortlisted (A/B/C)? Os dados públicos do kit respondem? | 1 ou 2 desafios com "atende" / "não atende" |
| **0:45–1:00** | **Decidir** | **time inteiro** | Aplicar a grade de decisão do §2 | **1 desafio escolhido** |
| **1:00–1:30** | **Travar o escopo** | Matheus escreve, os 5 revisam | Escrever o §3 (6 campos). Escolher 1–3 componentes do MVP. Escrever a frase de 10 s. | **1 página "escopo travado"** |

**Divisão de trabalho durante a live** (para ninguém ficar parado olhando):

| Pessoa | Papel na live | Por quê |
|---|---|---|
| **Moisés** | escuta e anota as falas literais | é o especialista; conhece o vocabulário do SESI |
| **Matheus** | mapeia nas 4 dimensões e escreve o escopo travado | Product Owner |
| **Omena** | testa o kit contra viabilidade e canal | é quem fecha a venda |
| **Esteves** | testa o kit contra o DESAFIO (a pergunta da empresa) e a validação clínica | é a ponte com o cliente real |
| **luquinhas** | testa o kit contra o **tempo de build** — "isso é 32 h ou 60 h?" | quem vai ter que construir na madrugada |

---

## 2 · A grade de decisão (4 testes, nesta ordem)

O desafio escolhido é o que passa em **≥3 dos 4**:

| # | Teste | Pergunta | Por que |
|---|---|---|---|
| **T1** | **Integração** | O desafio cobre **≥3 das 4 dimensões** do Anexo I? | O Anexo I: *"soluções integradas, capazes de articular dimensões como comportamento, ambiente, organização do trabalho e participação das pessoas"*. Se cobre 1, é dashboard — e o Anexo I rejeita dashboard |
| **T2** | **Dado** | Existe **dado público** que responde à pergunta? | Sem dado = sem protótipo em 32 h. O kit tem 9 datasets (VigIndústria, CAT, eSocial, ANS, CN-SESI, CANPAT, INSS, PIB setorial, IPEA) — só funciona se a pergunta cair neles |
| **T3** | **Mensurabilidade** | Existe um indicador de **antes e depois**? | Se não dá para medir, não dá para prometer — e §8.1.2 (Impacto) é 20% da nota |
| **T4** | **Nossa evidência** | A nossa evidência forte (**7ª dimensão morta · 0 itens · 65,6%**) é a **resposta direta** ao desafio? | É o que nos torna verificáveis em 10 segundos na frente de uma banca que lê o relatório do SESI |

**Regra de desempate:** se dois desafios passarem em 3/4, escolhe o que **a empresa do Conecta Saúde pagaria para resolver** — o §Anexo I diz que os desafios vêm das empresas, e quem tem dor paga.

**Se nenhum passar em 3/4:** não é motivo de pânico — é motivo para ler o §3.3.

---

## 3 · Os 5 kernels (o que fica em cada cenário)

O kit não tem uma tese só. Tem **cinco kernels**, e o §10 de `docs/04-proposta.md` mapeia o resto. O que muda é **qual é o núcleo**:

| Se o desafio for sobre… | **Núcleo (obrigatório)** | Corte imediato | O que fica como camada |
|---|---|---|---|
| **Participação / autonomia / propósito** | **Escuta** (6 itens) + **Motor de alavancas** | Export FHIR · Plano do trabalhador | Exposição prevista vira a camada de contexto |
| **Ausenteísmo / custo / previsão de desfecho** | **Modelo de exposição prevista** + **Motor de alavancas** | Escuta vira 4 itens · Plano vira 1 alavanca | Escuta entra se sobrar tempo |
| **Risco / exposição / prevenção / laudo** | **Exposição prevista** + **Motor de alavancas** + orquestração de prazo | Escuta inteira | — |
| **Retorno ao trabalho / incapacidade / readaptação** | **Catálogo de demandas por posto** + plano de retorno | Exposição prevista vira tabela | Export FHIR vira o entregável institucional |
| **Fragmentação / interoperabilidade / SUS-plano** | **Export FHIR R4 (RNDS) + eSocial** + trajectory | Escuta vira acessória | — |

### 3.1 · O pior cenário, e o que se faz nele

**Desafio sobre "dashboard / BI / dados".** É o cenário em que o Anexo I é acionado contra a gente: *"a resposta não está apenas na incorporação de novas tecnologias"*.

**A saída:** reancorar nas 4 dimensões e dizer, na primeira frase do pitch, que dashboard sem participação não é modelo assistencial. O kernel vira **Escuta + Motor de alavancas**, e o dashboard é o **veículo** (o painel de exposição vira a tela que a empresa abre na segunda-feira). Isso é o que já está construído — e é por isso que o MVP não é "um dashboard".

### 3.2 · A armadilha do "sexy"

O §7.2 e o Anexo I delimitam o escopo. **Se um desafio anunciado parecer "mais sexy" e estiver fora do §7.2, ele é distração** — é exatamente a armadilha da mensagem de ODS. A pergunta que substitui o instinto:

> *"Se a empresa do Conecta Saúde pagasse para resolver isto, ela pagaria?"*

Se a resposta for não, não é o desafio deles, e a banca (recrutada pelo SESI, §1.2) vai saber.

---

## 4 · O template de 6 campos (preencher na hora, 13/11)

```
DESAFIO ANUNCIADO (literal, 1 frase):
_______________________________________________
DIMENSÕES DO ANEXO I COBERTAS:   [ ] comporta  [ ] ambiente  [ ] org. do trab.  [ ] participação
EIXO DO KIT QUE ATENDE:          O__   TESTES PASSADOS: T1 __ T2 __ T3 __ T4 __
NÚCLEO DO MVP (1–3 componentes):
  1. ______________________________  h
  2. ______________________________  h
  3. ______________________________  h
PLANO DE CORTE (o que sai se apertar): ______________
FRASE DE 10 S QUE ABRE O PITCH:
  "_______________________________________________"
```

**Conferência antes de dormir (13/11, 20h00):**
- [ ] O escopo fecha em **≤ 32 h** de build com 2 devs?
- [ ] Existe **dado público** para cada número que vai aparecer no slide?
- [ ] A frase de 10 s **não contém** "manutenção preditiva" nem promessa de ROI?
- [ ] O pitch continua **3 minutos**?

---

## 5 · O produto da noite (o que precisa estar pronto às 20h de 13/11)

| # | Artefato | Quem | Prazo |
|---|---|---|---|
| 1 | **1 página "escopo travado"** (o §4 acima, preenchido) | Matheus | 20h00 de 13/11 |
| 2 | **Slide único de impacto atualizado** (`pitch/slide-impacto.html`) com os números do desafio real | Matheus | 22h de 13/11 |
| 3 | **Roteiro de 3 min reescrito** — só o gancho (0:00–0:30) e a frase de 10 s mudam; os outros 6 blocos são estáveis | Moisés | 23h de 13/11 |
| 4 | **Mapa do protótipo** — o que entra em cada tela, com o plano de corte | luquinhas | 23h de 13/11 |
| 5 | **Dúvidas para os mentores** — atualizadas com o desafio real | Matheus | manhã de 14/11 |

> **Só o gancho e a frase mudam.** O resto do roteiro (`pitch/roteiro-3min.md`) foi escrito para sobreviver à mudança de domínio — ele é sobre o **método** (escuta → alavanca → medição), não sobre o setor. É por isso que ele está pronto antes do reveal: **para não ser reescrito às 23h de uma sexta-feira.**

---

## 6 · As 4 armadilhas do momento

| # | Armadilha | Como evitar |
|---|---|---|
| **A1** | **Travar a tese antes de ouvir.** Chegar com "nós já temos a solução pronta" | §7.3 é nivelamento. Chegar com **kit**, não com_vertex. Se alguém do time defender a tese atual antes do bloco 0:15, é porque está com medo de refazer — e refazer é mais barato que construir errado |
| **A2** | **Ficar 90 minutos discutindo.** A discussão mais VIT (viável) é a que mata a noite | Cronômetro de 15 em 15. **Às 20h00 decide, ponto.** O registro das decisões é no template de 6 campos, não na conversa |
| **A3** | **Aceitar o desafio "sexy" fora do §7.2** | §2 + a pergunta "a empresa pagaria?" |
| **A4** | **Construir antes de travar o escopo.** Às 22h alguém começa a codar | O §4 do roteiro (`pitch/roteiro-3min.md` §5) tem a ordem de sacrifício. **Ninguém toca em código antes do escopo travado.** §11.8: vantagem indevida desclassifica o grupo |

---

## Fontes

Regulamento 2026 §2.1 · §2.3 · §6.2 · §7.2 · §7.3 · §8.1.2 · §10 · §11.2 · §11.8 · Anexo I (íntegro) · Formulário oficial (`EndTime` técnico: 09/11/2026 00h15) · `docs/02-cruzamento-whatsapp.md` (kit de mapeamento) · `docs/04-proposta.md` §5 e §10 · `docs/07-alavancas-regulamento.md` §2 (ALAVANCA 5)
