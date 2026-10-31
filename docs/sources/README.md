# Fontes primárias

Todas verificadas no original em 27/10/2026.

> **Os PDFs não são versionados neste repositório.** São material de terceiros, publicado por outras instituições — redistribuir aqui não é o lugar certo. Cada um se baixa pela **URL pública** da coluna *Fonte*. O que **é** versionado é o **texto extraído** (`.txt`), que é o que sustenta a citação com página e linha dentro do repo.
>
> A regra está no `.gitignore` (`docs/sources/*.pdf`). Para quem for usar o material offline, basta baixar os 9 PDFs pelas URLs abaixo — e o `Regulamento Hackathon SESI Saude 2026.pdf`, na raiz do repo, continua versionado, porque é a fonte de verdade dos §N.

Os PDFs são a fonte; os `.txt` são o texto extraído (para busca e citação de linha).

| Arquivo | O que é | Por que importa | Fonte |
|---|---|---|---|
| `vigindustria-2026.pdf` | SESI + CN-SESI + MS. *VigIndústria Brasil 2026*, 119 p. | **O relatório-base do desafio.** 57.952 trabalhadores · 825 empresas · 33 indicadores · 6 das 7 dimensões do ASSTI. Curadoria página a página em `data/vigindustria-2026.md` | [PDF](https://static.portaldaindustria.com.br/portaldaindustria/noticias/media/filer_public/fc/83/fc836c73-55b5-4ed7-9e4c-13a54a95786c/relatorio_vigindustria_-_conecta_saude_2026.pdf) |
| `canpat_2025.pdf` + `.txt` | Auditores-Fiscais do Trabalho. *Acidentes do trabalho no Brasil 2016–2025* | 6,4 mi acidentes · 27.486 óbitos · **106 mi dias perdidos** · 249 mi dias debitados · 2025 recorde (806.011 acidentes / 3.644 óbitos) | [MTE/IGT](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao-do-trabalho/seguranca-e-saude-no-trabalho/canpat-2/canpat-2025/acidentes-de-trabalho-2016-a-2025.pdf/) |
| `ans_panorama_nov2025.pdf` + `.txt` | ANS. *Panorama Saúde Suplementar* ed. dez/2025 (3º tri 2025) | R$ 312,1 bi de receita → R$ 256,8 bi de despesas assistenciais · R$ 276,9 bi em 2025 · sinistralidade 78,0% | [ANS](https://www.gov.br/ans/pt-br/arquivos/acesso-a-informacao/perfil-do-setor/dados-e-indicadores-do-setor/publicacoes/Panorama_Saude_Suplementar_Ed_10_nov_2025_r06.pdf) |
| `iess_td118.pdf` + `.txt` | IESS. *TD nº 118/2026 — Contratantes e beneficiários de planos coletivos empresariais* | 37 mi beneficiários · 71% dos vínculos · **+48% de contratantes** (2020→2024) · razão 20→16 · mais coparticipação | [IESS](https://www.iess.org.br/sites/default/files/2026-03/TD%20118%20-%20Evoluc%CC%A7%CC%A3o%20dos%20Contratantes%20e%20Beneficia%CC%81rios%20de%20Planos%20Coletivos%20.pdf) |
| `iess-casos-sucesso.pdf` | IESS/SESI. *Promoção da saúde nas empresas: casos de sucesso* (2013) | Caso Brasil: readequação ergonômica estrutural, 295 trabalhadores / 24 meses — dor nas costas **53% → 33%**; estrutural −4,3 vs individual −2,1 | IESS |
| `cnsesi_absenteismo.pdf` + `.txt` | CN-SESI/SESI-DN. *Relatório de Gestão 2020* (136 p.) | Fonte do **Indicador de Absenteísmo** do SESI: 20,0% faltaram ≥1 dia/semana; 6,5% ≥3 dias; mulheres 22,5% | CN-SESI |
| `sesi_produtividade_2023.pdf` + `.txt` | CNI/SESI. *Estilo de Vida, Saúde e Produtividade de Trabalhadores da Indústria, pré e durante pandemia (2018–2021)* | Base do absenteísmo populacional (n = 123.355) e da relação saúde↔produtividade | CNI/SESI |
| `cni_sesi_saude_produtividade.pdf` + `cni_sesi.txt` | CNI/SESI. *Global Healthy Workplace Awards* — discurso de abertura (2015) | Enquadramento histórico: saúde do trabalhador como fator de negócios | CNI/SESI |
| `cfm_2454_2026.pdf` + `.txt` | CFM. **Res. nº 2.454/2026** — IA na medicina (DOU 27/02/2026, vigência 26/08/2026) | **O escudo regulatório.** Art. 4º I e §2º (IA só como apoio); art. 11 (explicar o uso ao paciente); art. 12-13 + **Anexo II, I**: *baixo risco* para IA sem influência decisória, em função administrativa/apoio | [CFM](https://sistemas.cfm.org.br/normas/arquivos/resolucoes/BR/2026/2454_2026.pdf) |

## Regra de uso

- **LGPD:** nada de dado individualizado de trabalhador. Todo uso é agregado (k ≥ 10) ou sintético.
- **Citação:** usar número, fonte e página. Os dados do VigIndústria já estão curados em `data/vigindustria-2026.md` — **cite dali, não do PDF bruto**, para não errar o recorte (global vs. porte da empresa vs. faixa etária).
- **Renomear a edição:** a capa do VigIndústria diz "2025" (ano do campo). Ao citar: *"VigIndústria Brasil 2026 (campo jul–dez/2025)"*.
- **Não usar:** o número "R$ 206 bilhões" atribuído à depressão pelo VigIndústria (p. 69) é implausível por ordem de grandeza e não foi corroborado. O verificável é **75,3 mil trabalhadores afastados** (INSS, 2016).
