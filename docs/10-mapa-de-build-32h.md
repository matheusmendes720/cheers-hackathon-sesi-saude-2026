# O mapa de build — 32 h em 2 turnos

**Equipe Cheers · 31/10/2026 · o plano operacional de 14 e 15/11**
Quem executa: **Matheus + luquinhas** (TI). Quem sustenta: **Moisés, Esteves, Omena** (conteúdo, dado, design, pitch).

> **Este documento assume que o escopo travado em 13/11 (§ de `docs/08-plano-90min.md`) é o de `docs/04-proposta.md` §5.** Se o núcleo mudar, os **blocos** mudam (o que sai é sempre o mesmo: Export → Escuta → Plano → Exposição), mas a **grade de horários, os dois cortes e o freeze não mudam**.

---

## 0 · A conta primeiro — porque é ela que decide

| | |
|---|---|
| Janela total | 14/11 07h30 (check-in) → 15/11 15h30 (entrega) = **32 h de relógio** |
| Menos check-in e abertura | −1 h → **08h30** é o início real do build |
| Menos almoço (1 h) e jantar (1 h) | −2 h |
| Menos **dormo dos 2 devs** | −5 h |
| **Tempo de build dos devs** | **≈ 21 h de relógio, com 2 devs = 42 dev-h** |
| Desse total, **escopo puro** | **32 dev-h** (Motor 6 · Exposição 8 · Escuta 6 · Plano 8 · Export 4) |
| **Sobra para integração, teste, polimento e imprevisto** | **≈ 10 dev-h (31%)** |

> **A folga de 31% não é luxo — é o que absorve o imprevisto.** Ela é o motivo de o corte existir. Se às 23h30 a folga já acabou, o corte **não é opcional**.

⚠️ **Erro comum:** "cabe 32 h em 32 h". Não cabe. Cabe 32 h de **escopo** em **32 h de relógio com 2 devs, dormindo**. Quem planeja os 32 h de escopo como 32 h de relógio entrega 14 h atrasado.

---

## 1 · A grade dos dois turnos

```
14/11  07h30  ▓ check-in + abertura (todos)
       08h30  ┌─ TURNO 1 ─ devs construindo ─────────────────┐
       12h00  │  Motor de alavancas                          │
       13h00  │  almoço                                     │
       17h00  │  Exposição prevista                          │
       18h00  │  integração motor↔exposição + pausa          │
       19h00  │  jantar                                     │
       23h30  │  Escuta + Plano (parte 1)                   │
23/11  00h00  ╞══ 🔴 CORTE 1 — decisão de escopo ════════════╡
       05h00  ╞══ 💤 os 2 devs dormem (5 h) ═════════════════╡
       07h00  ├─ TURNO 2 ─ devs fechando ────────────────────┤
       11h00  │  Plano (parte 2) + Export                   │
       13h00  │  integração total + polimento + testes       │
15/11  13h00  ╞══ 🔴 CORTE 2 — FREEZE DE ESCOPO ═════════════╡
       14h30  │  só bug fix + teste do fluxo completo        │
       15h30  └  🧊 FREEZE DO CÓDIGO + backup + ensaio final ┘
       15h30  📦 ENTREGA DO PROTÓTIPO
       16h00  🎤 PITCH (3 min)
       19h00  🏁 encerramento
```

---

## 2 · Bloco a bloco — o que os devs fazem, e a hora do corte

| Bloco | Horário | Dev-h | Componente | Entregável verificável | Corta? |
|---|---|---|---|---|---|
| **A** | 14/11 08h30–12h00 | 7 | **Motor de alavancas** (6 h) | 3 alavancas priorizadas, cada uma com o indicador nacional que a justifica · **as regras à vista** | 🔴 **NUNCA CORTA** |
| — | 12h00–13h00 | — | almoço | — | — |
| **B** | 13h00–17h00 | 8 | **Exposição prevista** (8 h) | índice 0–100 + composição em waterfall + risco por causa, **todos os pesos visíveis** | 🟡 3º a cortar (vira tabela) |
| **C** | 17h00–18h00 | 2 | integração motor ↔ exposição | o par (exposição, contexto) produz as 3 alavancas | — |
| — | 18h00–19h00 | — | jantar | — | — |
| **D** | 19h00–22h00 | 6 | **Escuta** (6 h) | 6 itens no celular, offline, 90 s, opt-out por bloco | 🔴 1º a cortar (vira 4 itens) |
| **E** | 22h00–23h30 | 3 | **Plano do trabalhador** — parte 1 (8 h) | PWA instalável + agregação k ≥ 10 + devolve as 2 alavancas dele | 🟡 2º a cortar (devolve 1) |
| 🔴 | 23h30–00h00 | 1 | **CORTE 1** | o que roda às 23h30 fica; o que não roda, sai — **agora** | — |
| 💤 | 00h00–05h00 | — | **os 2 devs dormem** | o build está completo às 05h00 | — |
| **F** | 05h00–07h00 | 4 | **Plano** — parte 2 | tela final do trabalhador, contador de k, nota de privacidade | — |
| **G** | 07h00–11h00 | 8 | **Export** (4 h) + integração total | Bundle FHIR R4 (RNDS) + validador eSocial · **fluxo inteiro rodando** | 🔴 4º a cortar |
| **H** | 11h00–13h00 | 4 | polimento, ajuste de UX, testes | zero erro no console; fluxo testado em 2 máquinas | — |
| 🔴 | 13h00–13h30 | 1 | **CORTE 2 — freeze de escopo** | a partir daqui é **só bug fix**. Nenhum item novo | — |
| 🧊 | 13h30–15h30 | 4 | freeze do código, backup, ensaio final | protótipo em **2 notebooks** + pendrive + slide impresso | — |

### 2.1 · As regras do corte (escritas antes, aplicadas na hora)

| Corte | Ordem de sacrifício | O que sobra |
|---|---|---|
| **CORTE 1** — 14/11 23h30 | 1º **Export** → 2º **Escuta** (vira 4 itens) → 3º **Plano** (devolve 1 alavanca) → 4º **Exposição** (vira tabela) | **Motor de alavancas** — sempre. É o que entrega a promessa |
| **CORTE 2** — 15/11 13h00 | nada sai. **Nada novo entra.** | — |

> **Regra de ouro: depois das 23h30 de sábado, ninguém começa feature nova.** Se alguém começar uma tela nova, a tela nova morre.

---

## 3 · Os três trilhos paralelos (Moisés, Esteves, Omena)

> Os devs **não** podem atender mentoria (§6.2 — "Desenvolvimento e Mentorias"). Então o time de conteúdo fica livre para isso, que é exatamente o que precisa acontecer.

| Quem | 14/11 (08h30–23h30) | 15/11 (05h00–13h00) | 15/11 (13h00–15h30) |
|---|---|---|---|
| **Moisés** | **Mentorias** (2ª–4ª do dia) — extrair o que importa e o que é acionável. Tarde: **checar cada número que aparece na tela contra a fonte**. Noite: **ensaios 1–5** do roteiro (gancho sozinho, cronometrado) | **Ensaios 6–10** + **ensaio 9 com queda de demo simulada** (mata o processo e lê o plano B) | Revisão do roteiro com o que foi construído. **Ensaios 10–12** com o protótipo real |
| **Esteves** | **Design das telas** — o protótipo tem que parecer com o slide de impacto. **Validação clínica dos 6 itens** com o parceiro médico (a pergunta faz sentido pra um trabalhador real?). Tarde: **imprimir o slide** | Revisão visual do protótipo contra o slide. Foto do protótipo rodando | **Print/foto do protótipo** para o plano de Continuação (não é exigência, mas é o que o §10.8 valoriza) |
| **Omena** | **Dados institucionais**: Viva+ (2.738.306 vidas), PAO 2026 (objetivo estratégico), 10.800 empresas na BA, 76 empresas do MES, benchmark Salú (R$ 13,9/vida/mês). **Plano de piloto** com o SESI-BA | Conferir os números do slide contra a fonte, um por um. **Bloco de viabilidade** do pitch | Ensaios do bloco de viabilidade. Contato com a rede credenciada para o pós-hackathon |

**Regra do time de conteúdo:** **nenhum dev é interrompido** entre 08h30 e 23h30 por causa de dúvida de conteúdo — o dev responde no **intervalo das 18h** (1 h de pausa + integração).

---

## 4 · O checklist de cada dev às 23h30 (antes de dormir)

- [ ] O protótipo **abre offline** com o Wi-Fi desligado?
- [ ] O fluxo completo roda do início ao fim **em 90 s** (seletor → exposição → escuta → 2 itens → plano → alavancas)?
- [ ] **Zero erro no console**?
- [ ] Cada número na tela tem a fonte na mesma tela ou no slide?
- [ ] **Se meu partner dormir e o meu note morrer**, meu partner sabe rodar o meu? *(cada um roda o build do outro — isso é obrigatório, não opcional)*
- [ ] O build está **commitado** e com **tag** (`v1.0-corte1`), para dar pra voltar?

---

## 5 · Os riscos da noite — e o plano de cada um

| # | Risco | Plano |
|---|---|---|
| **R1** | **Um dev dorme e o outro trava num bug** | Os dois dormem juntos (00h–05h). O CORTE 1 às 23h30 garante que o que estiver rodando às 05h00 está **completo**. Bug de madrugada só entra se for impeditivo (não abre tela / não carrega) |
| **R2** | **A demo não abre offline na máquina do local** | Zero recurso externo (sem CDN, sem fonte web). Testar em **2 notebooks** no dia 15. **Backup em pendrive** com o HTML + slide impresso. Plano B: o roteiro §8 lido do slide |
| **R3** | **Zoom, tela, brilho, fonte pequena no projetor do SESI** | Modo apresentação, zoom travado, brilho no máximo, **número grande**, slide único **impresso em A4** (2 cópias) |
| **R4** | **O build estoura** | Dois cortes com horário fixo. A folga de 10 dev-h é o amortecedor; se ela acabar antes das 23h30, o corte acontece mais cedo |
| **R5** | **Alguém do time adoece ou não aparece** | §9.7: o SESI **não media** desacordo entre membros. Por isso **cada componente tem 1 dono primário e 1 suplente**, e o pitch tem 5 linhas independentes (se um faltar, a linha dele é omitida, não improvisada) |
| **R6** | **A rede do local cai** | O protótipo não faz chamada de rede nenhuma. Testar com o Wi-Fi desligado às 13h30 |
| **R7** | **O número na tela está errado** | Todo número tem fonte. Revisão cruzada: Omena confere contra a fonte, Moisés contra o paper, Esteves contra o slide |
| **R8** | **O git trava ou o note perde o build** | Commit a cada bloco fechado + **tag** em cada corte + **cópia em pendrive** às 14h30 |

---

## 6 · O protocolo do freeze (15/11, 13h30 → 15h30)

| Hora | Ação |
|---|---|
| 13h30 | **Freeze de escopo.** A lista de features está fechada. Daqui em diante só entra bug |
| 13h30–14h15 | Bug fix + **teste do fluxo completo em 2 notebooks**, com o Wi-Fi desligado |
| 14h15–14h45 | **Backup duplo**: commit final + tag + **cópia em pendrive** + **slide impresso** (2 cópias) + **foto do protótipo** rodando |
| 14h45–15h15 | **Ensaio final do pitch com o protótipo real** — os 3 min, cronometrados, no modo apresentação |
| 15:15–15:30 | **Silêncio.** Ninguém mexe em mais nada. Todos no modo apresentação, tela travada, brilho no máximo |
| **15h30** | **📦 Entrega do protótipo** |

---

## 7 · O que o time precisa levar (cada um — §11.2 não dá equipamento)

- [ ] Notebook carregado, com o build **testado offline**
- [ ] **Carregador** (a tomada do local pode não ter lugar)
- [ ] **Extensão** (e cabo HDMI se o projetor for da sala)
- [ ] Mouse
- [ ] **Pendrive** com o build + o slide em PDF
- [ ] **Documento impresso**: slide de impacto (A4 paisagem) + o roteiro de 3 min
- [ ] Celular carregado (é por onde chega a confirmação de seleção)

> **E onde dormir (§11.3):** não há dormitório, mas há chuveiro. Dormir no local economiza 1 h de translado às 05h30 de sábado — **vale**. Decidir até 12/11.

---

## 8 · As 3 linhas que este plano protege

1. **Não começa feature nova depois das 23h30 de sábado.**
2. **O motor de alavancas nunca sai do corte** — é a promessa inteira.
3. **A entrega das 15h30 de domingo é sacred** — o corte existe para ela, não o contrário.

---

## Fontes

`docs/04-proposta.md` §5 (escopo de 32 h e ordem de corte) · `docs/08-plano-90min.md` (escopo travado em 13/11) · `pitch/roteiro-3min.md` §8 (plano B) e §10 (protocolo de ensaio) · Regulamento §6.2 (cronograma) · §9.7 (a organização não media) · §11.2 (sem equipamento) · §11.3 (sem dormitório)
