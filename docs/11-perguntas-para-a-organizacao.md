# 8 perguntas para a organização — live de 12/11, 13h

> **Equipe Cheers** · Hackathon+ SESI Saúde 2026 · Salvador, 14–15/11/2026
> **Imprimir 1 página (A4).** Gerar PDF com Ctrl+P → Save as PDF → margens "Padrão", escala 100%, sem cabeçalhos.

---

## Em 30 segundos

**Somos.** Equipe Cheers (5 pessoas: 2 TI, 1 gestor, 1 especialista em informática em saúde com doutorado em IA, 1 designer com parceiro médico). Inscrição individual já submetida, equipe indicada como "Cheers".

**O que vamos construir.** Um protótipo funcional que **dá voz ao trabalhador** sobre as condições que reduzem a capacidade de trabalhar, cruza isso (em agregado anônimo) com a exposição prevista e devolve **3 alavancas priorizadas** para a empresa. Roda **offline, no celular**, em 32 h de build.

**Por que isso é models assistencial.** O instrumento oficial do SESI (ASSTI, 7 dimensões) mede **risco** — mas a **7ª dimensão**, "fatores de redução da produtividade", foi **declarada e nunca analisada** (VigIndústria Brasil 2026, p. 16), e o questionário **não tem nenhum item** de autonomia, participação ou propósito (p. 110–119). Essa lacuna é exatamente a 4ª dimensão do Anexo I do desafio: *participação das pessoas*.

**O que precisamos.** 8 respostas. Três delas (P1) **destravam o escopo**; sem elas a gente constrói às cegas.

---

## P1 · Bloqueiam o escopo — perguntar primeiro

| # | Pergunta | Por que destrava |
|---|---|---|
| **1** | **"Modelos sustentáveis de saúde suplementar" ou "modelos assistenciais de saúde"?** A descrição do próprio formulário diz *saúde suplementar*; o regulamento (§2.1) e o Anexo I dizem *modelos assistenciais*. São dois recortes: plano/operadora (RN 465, ANS) × saúde ocupacional (ASSTI, NR-7, SESI). **O desafio detalhado de 13/11 é de qual lado?** | É a bifurcação mais consequente do §7.3. Define se a nossa proposta (saúde do trabalho, ASSTI) é **diretamente o desafio** ou precisa ser reposicionada. Ver o §10 de `docs/04-proposta.md` — as 5 bifurcações do kit já estão mapeadas para qualquer um dos dois lados. |
| **2** | **A demo do protótipo entra nos 3 minutos do pitch, ou o protótipo é julgado à parte** a partir do que foi entregue às 15h30 de domingo? | Se for à parte, a estratégia muda: o pitch pode ser mais conceitual e o protótipo precisa se sustentar sozinho. Se for dentro, cada segundo de demo tem que render nota de pitch (60% do total). Não está no §8. |
| **3** | **Quais são os desafios concretos que serão apresentados na abertura?** E as empresas por trás de cada um — alguma delas vai estar disponível para **validar o protótipo**? | O §7.3 só revela na abertura. Se a empresa que formulou o desafio estiver disponível, validamos com o cliente real em vez de hipótese. É o que separa um protótipo de uma maquete. |

## P2 · Mudam a forma do protótipo

| # | Pergunta | Por que destrava |
|---|---|---|
| **4** | **A organização libera acesso a dados do SESI/ASSTI** (anonimizados) para o protótipo, ou o time usa dados públicos? | Se houver dado real, o protótipo sai do terreno da simulação. Se não, usamos os 9 datasets públicos já mapeados (`docs/viabilidade-stack-dados-regulatorio.md`) e declaramos isso na tela — o que é honesto e pontuado por maturidade. |
| **5** | **A composição do §5.3 (gestor, designer, 2 TI, especialista) é filtro de seleção ou apenas recomendação?** | Se for filtro, a complementação do §5.4.2 pode ser um problema real. Como a equipe indicada tem prioridade (§5.4.1), queremos entender a ordem de prevalência. |
| **6** | **Equipes indicadas com menos de 6 integrantes são complementadas?** O §5.4.1 prioriza a equipe indicada; o §5.4.2 completa equipes com menos de 6. **Qual prevalece?** | Somos 5. Queremos saber se entramos com 5 ou se o sexto membro entra por indicação da Comissão — e quem seria, para não descobrir isso no meio do build. |

## P3 · Fecha a operação

| # | Pergunta | Por que destrava |
|---|---|---|
| **7** | **Como é definido o líder da equipe** para fins do prêmio? O §9.5 diz que a premiação cai na conta do membro indicado como líder; o §9.7 diz que a destinação é responsabilidade exclusiva da equipe. | Precisamos ter o líder designado e a conta informada **antes** de 14/11, e o combinado entre nós registrado — porque o SESI não media desacordo de equipe. |
| **8** | **Há rede para os participantes e para as demonstrações no local?** | O §11.2 não fornece equipamento: a demo roda na máquina de um de nós. Se o local tiver rede, dá para instalar dependências antes; se não, o protótipo é 100% offline por construção. |

---

## Se der só 5 minutos

Pergunte **1, 2 e 3**. As outras 5 a gente resolve por e-mail depois.

## Depois da live

- **12/11, à noite** → o time valida a tese e fecha o nome do produto e o líder da equipe.
- **13/11, 18h30** → abertura com o desafio real. O plano de 90 min para absorvê-lo está em `docs/08-plano-90min.md`.
- **As 8 perguntas para os mentores** são de outra live (13/11) e estão em `AGENTS.md` § "Perguntas para os mentores".
