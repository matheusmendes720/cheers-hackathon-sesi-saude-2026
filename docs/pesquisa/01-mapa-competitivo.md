# Mapa competitivo — saúde ocupacional e saúde corporativa no Brasil

*27/10/2026 · `[fato]` verificável · `[hipótese]` nossa · `[a confirmar]`. **Ocupacional ≠ wellness** (⚠️). URLs: `01-mapa-competitivo-fontes.md`.*

## Mapa competitivo

| Player (categoria) | O que faz | Receita / preço público | Fricção / dor do cliente | Fonte (credib.) |
|---|---|---|---|---|
| **SESI — ASSTI + Sesi Viva+** (a) | Avaliação populacional do trabalhador (7 dimensões, desde 2018); automatiza eSocial | Serviço institucional, sob consulta | Empresa só recebe agregado | [1][2][3] primária |
| **SESI Bahia** — 15 carretas, 500+ credenciadas (a) | SST e clínicas; Centro de Inovação em Prevenção da Incapacidade (WDP/SAW/RTW) | Serviço, sob consulta | Auto-diagnóstico de RTW "em breve" na VIVA+ | [2][3][4] primária |
| **SOC (Conplan)** (b,e) | Maior software integrado de SST: SIA/IA, eSocial, PGR; MEUSOC (500 mil+) | Licença+serviços, sob consulta | Falha ao anexar atestado; app instável | [6][7][8] vendor/RA |
| **SGG** (b) | SGGNet: SST, eSocial, PGR, IA, ISO 27001 | Licença+serviços, sob consulta | App do trabalhador: 1 mil+ downloads | [8] vendor |
| **WOTY** (e,f) | ERP de SST + eSocial + COPSOQ II | Licença, sob consulta | Sem continuidade clínica | [10] vendor |
| **Vixting / Sólides** (f) | 3.200+ / 1.200+ clínicas; eSocial S-2220/2240; NR-1 | Assinatura B2B→B2B, sob consulta | Não chegam ao trabalhador | [11] vendor |
| **Absenteísmo** — bem.care, mywork, BlueService, Apdata (d,f) | bem.care: atestado→falta por IA + eSocial; demais: atestados e ponto na folha | SaaS/assinatura, sob consulta | 14 reclamações/3 anos, 0% respondidas; atestado = ausência, não saúde | [9][12] RA/vendor |
| **Onvida / Selven / DUO24h** (c) | Telemedicina B2B per capita | Assinatura/colaborador, R$19,90–R$79,90/mês | Dor é preço e volume | [13] vendor |
| **NR-1 SaaS** (i) | COPSOQ/HSE + relatório IA + PGR (NRGuard, NR1Plus, Benway…) | Assinatura barata, R$79–R$1.297/mês; Benway R$0 | Diagnóstico comoditizado | [14] vendor |
| **Consultorias RH/SST** — 500+ credenciadas SESI BA (h) | NR-1, PGR, laudos: projeto, não operação | Fee, R$15–80 mil, 4–12 semanas | Entregam laudo; caro e lento | [14][15] vendor |
| ⚠️ **Wellhub / Benevity / Afya** (g) | Rede de bem-estar, benefícios, telemedicina | Corporate/empregado, sob consulta | Não toca SST/ASO/PGR/absenteísmo | [16] vendor |

*Categorias: a SESI · b plataformas SST · c telemedicina B2B · d absenteísmo · e prontuário/ASO · f eSocial · g wellness · h consultoria · i psicossocial.*
*Long tail:* eSocial/folha, coaching, corretoras e ~500 consultorias disputam o orçamento.

## Portas de entrada (barreiras)

| Barreira | Intensidade | Por quê |
|---|---|---|
| Dados populacionais do ASSTI | **Alta** | Único dataset longitudinal de saúde do trabalhador na indústria; gerou o VigIndústria. Indivíduo = dado sensível (LGPD) [1] |
| Canal SESI — 500+ credenciadas, 15 carretas, 26 DRs | **Alta** | Distribuição física e confiança institucional; entrada por edital [2][3] |
| Rede de clínicas (NR-7) + governança clínica | **Média** | Sem execução, o software não entrega cuidado; parecer simulado elimina a equipe (armadilha 4) |
| Prova de resultado em saúde | **Alta** | Resultado é lento; comprador exige ROI e demo de 3 min |

## Camadas descobertas (oportunidades que NINGUÉM resolve)

1. **Absenteísmo = 7ª dimensão do ASSTI, declarada e não analisada.** *Evidência:* o VigIndústria diz que "não foram analisados os fatores de redução da produtividade" (6 de 7 dimensões), com validade psicométrica (CR=0,863) [1]. *Por que:* único elo entre dado populacional e R$: contam a falta, ninguém cruza falta ↔ saúde ↔ população.
2. **RTW/SAW com job matching e task bank.** *Evidência:* o SESI/BA já tem WDP/SAW/RTW, mas o auto-diagnóstico está "em breve" na VIVA+ [2]; players BR não fazem RTW. No exterior: Bridges Health [17], Cority [18], ESIS/Chubb [19], getUBetter/NHS [20]. *Por que:* gatilho de compra obrigatório, alinhado a "organização do trabalho" (Anexo I).
3. **Co-participação do trabalhador no plano de cuidado.** *Evidência:* MEUSOC (500 mil+ downloads) mostra que o trabalhador adota app sobre ele — agendar exame, ver ASO, EPI [8]; a reclamação mais frequente do líder é **não conseguir anexar atestado** [7]. *Por que:* "participação das pessoas" é dimensão do Anexo I e o canal está quebrado.
4. **SESI como camada digital entre saúde ocupacional, saúde suplementar e SUS.** *Evidência:* o Conecta Saúde 2026 tratou da fragmentação do cuidado e de "conectar informações… acompanhar a trajetória do trabalhador" [21]; o SESI-SC pergunta como fazer da saúde "não apenas uma resposta a atestados" [22]; getUBetter (NHS) é o equivalente [20]. *Por que:* o MES é a base de clientes e o ASSTI já é a base.
5. **De diagnóstico a ação em psicossocial: o laudo é commodity, a intervenção não é.** *Evidência:* o questionário já custa de R$0 a R$1.297/mês [14]; a consultoria, R$15–80 mil e até 12 semanas [14][15]. *Por que:* o valor migra para fechar o ciclo risco → ação → retorno.

## Armadilhas — soluções que o Anexo I rejeita

1. **App de sedentarismo/atividade.** Anexo I: a resposta não é "mais tecnologia". A Centeni provou o contrário — R$ 5 mi captados, **encerrou jul/2026 devolvendo R$ 2,5 mi** [24].
2. **COPSOQ + relatório IA (NR-1).** Saturado, preço no chão (um player é gratuito) [14]. Conformidade, não redesenho do modelo assistencial.
3. **Telemedicina corporativa per capita.** Já vendida a R$19,90–R$79,90/colaborador/mês [13]. Dor de preço e volume; teleconsulta somada a app não é tese.
4. **IA que simula parecer médico.** Risco CFM + LGPD (§10.4); com 60% da nota no pitch, elimina a equipe.
5. **Dashboard/indicador de SST.** É o que SOC/SGG já vendem [6][8] e o ASSTI já produz [1]. Valor incremental zero.

## Fontes

1. **VigIndústria Brasil 2026** — `docs/sources/vigindustria-2026.pdf` — primária (01/09/2026)
2. **SESI/BA — Centro de Inovação em Prevenção da Incapacidade** — sesibahia.com.br/centro-inovacao — primária
3. **FIEB — SESI Bahia em SST** — fieb.org.br — institucional (data `[a confirmar]`)
4. **Correio 24h — SESI Bahia 75 anos** — correio24horas.com.br — imprensa (2023, `[a confirmar]`)
5. **FIEB — Hackathon+ SESI Saúde 2ª ed.** — institucional (29–30/11/2025)
6. **SOC** — soc.com.br — vendor (27/10/2026)
7. **Reclame Aqui — SOC** — reclameaqui.com.br/empresa/soc — dado primário (16 reclamações; 93,8% respondidas)
8. **Google Play — MEUSOC (500 mil+) / SGG (1 mil+)**; sgg.net.br — primária
9. **Reclame Aqui — bem.care** — reclameaqui.com.br/empresa/bem-care — dado primário (14 em 3 anos; 0% em 6 meses)
10. **WOTY** — woty.com.br — vendor
11. **Vixting** (3.200+ clínicas) · **Sólides** (1.200+) — vixting.com.br · solides.com.br — vendor
12. **mywork** · **BlueService** · **Apdata** — vendor
13. **Onvida** · **Selven** · **DUO24h** · **Telemedico** — vendor
14. **NR-1 SaaS** — nrguard.com.br (R$149,90/mês) · nr1plus.agilizabeneficios.com.br · indicepersona.com.br · empcsic.com.br · nr1flow.com.br · mindcompliance.org · benway.com.br/pesquisas/nr1 (R$0) — vendor
15. **Consultoria NR-1** (R$15–80 mil) + credenciados SESI BA 2025 — vendor+SESI
16. ⚠️ **Wellhub** · **Benevity** · **Afya** — vendor
17. **Bridges Health (Canadá)** — bridgeshealth.com — vendor (WorkWorld360 + ErgoWorks)
18. **Cority (Suécia)** — cority.com — vendor (RTW; STD 2,7→2,5 dias/ano)
19. **ESIS/Chubb — Integrated Absence Management** — esis.com — vendor
20. **getUBetter (NHS/UK)** — getubetter.com — vendor + sistema público
21. **Conecta Saúde 2026** — cnsesi.com.br/noticias/1975 e /1978 — primária (01/09/2026)
22. **SESI-SC — Conecta Saúde 2026** — sessc.org.br/conecta-saude — institucional (22/10/2026)
23. **SESI Ceará — Estação de Saúde Conectada** (4 linhas DCNT) — institucional
24. **PEGN — Centeni encerra** — revistapegn.globo.com — imprensa primária (jul/2026)
