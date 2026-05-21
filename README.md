# 📊 Curso de Estatística com Python e dados públicos do IBGE

Curso prático em **10 aulas** que ensina **Estatística Básica e Intermediária com Python**
usando dados reais da **API SIDRA do IBGE** — gratuita, pública e sem chave.

Cada aula é um Jupyter Notebook autocontido com:
- ✅ **Teoria explicada em detalhe** dentro do próprio notebook
- ✅ **Código Python comentado linha a linha**
- ✅ **Dados reais** coletados ao vivo da API IBGE/SIDRA
- ✅ **Gráficos salvos automaticamente** na pasta `graficos/`
- ✅ **Pronto para Google Colab** — funciona ao clonar o repositório

---

## 🚀 Como usar

### Opção 1 — Google Colab (recomendado)

Clique no badge em qualquer notebook e ele abre direto no Colab:

```
https://colab.research.google.com/github/220719/curso-estatistica-python/blob/main/notebooks/01_introducao_e_coleta_sidra.ipynb
```

> ⚠️ **Antes de subir ao GitHub**, edite a variável `REPO_URL` na célula de SETUP de cada
> notebook substituindo `220719` pelo seu usuário do GitHub.

A primeira célula de cada notebook:
1. Instala as dependências automaticamente
2. Clona o repositório se ainda não existir
3. Configura o `sys.path` para importar o módulo `utils/sidra_api.py`
4. Cria a pasta de gráficos

### Opção 2 — Ambiente local

```bash
git clone https://github.com/220719/curso-estatistica-python.git
cd curso-estatistica-python
pip install -r requirements.txt
jupyter notebook notebooks/
```

---

## 📚 Estrutura das aulas

| # | Aula | Tópicos | Dados |
|---|------|---------|-------|
| 01 | **Introdução + API SIDRA** | Visão geral, primeira coleta, inspeção de DataFrame | IPCA mensal |
| 02 | **Estatística Descritiva** | Média, mediana, variância, desvio, quantis, IQR, CV | IPCA + PIB per capita |
| 03 | **Visualização Exploratória** | Histograma, KDE, boxplot, skewness, kurtosis, pairplot | IPCA + PIB per capita |
| 04 | **Probabilidade e Distribuições** | Bernoulli, Binomial, Poisson, Uniforme, Exponencial | IPCA (probabilidades empíricas) |
| 05 | **Normal e TCL** | Distribuição Normal, regra 68-95-99,7, Teorema Central do Limite, Q-Q plot, Shapiro-Wilk | IPCA |
| 06 | **Intervalos de Confiança** | IC para média (t e z), IC para proporção, simulação de cobertura | IPCA |
| 07 | **Testes de Hipótese (z, t)** | $H_0$ vs $H_1$, p-valor, testes bi/unilateral, poder do teste | IPCA vs meta BCB |
| 08 | **Duas Amostras + χ²** | Welch, t pareado, qui-quadrado de independência e aderência | IPCA, PIB UF |
| 09 | **Correlação e Regressão** | Pearson, Spearman, MQO, $R^2$, diagnóstico de resíduos | PIB per capita × População |
| 10 | **Análise Integrada + Plotly** | Dashboard, choropleth, relatório completo | Tudo |

---

## 🗂️ Estrutura do repositório

```
curso-estatistica-python/
├── notebooks/                          # 10 aulas em .ipynb
│   ├── 01_introducao_e_coleta_sidra.ipynb
│   ├── 02_estatistica_descritiva.ipynb
│   ├── 03_visualizacao_exploratoria.ipynb
│   ├── 04_probabilidade_e_distribuicoes.ipynb
│   ├── 05_normal_e_tcl.ipynb
│   ├── 06_intervalos_de_confianca.ipynb
│   ├── 07_testes_de_hipotese.ipynb
│   ├── 08_duas_amostras_e_qui_quadrado.ipynb
│   ├── 09_correlacao_e_regressao.ipynb
│   └── 10_analise_integrada_plotly.ipynb
├── utils/
│   └── sidra_api.py                    # Funções de coleta da API IBGE/SIDRA
├── graficos/                           # Gráficos PNG + dashboards HTML
├── data/                               # (opcional) cache de dados
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🌐 Sobre a API SIDRA (IBGE)

A [API SIDRA](https://apisidra.ibge.gov.br/) expõe milhares de tabelas do IBGE:
- IPCA, IPC, INPC (inflação)
- PIB (nacional, estadual, municipal, per capita)
- Censo Demográfico 2022
- PNAD Contínua
- Cadastro de Empresas, e muito mais

**Sem autenticação**, **sem limites práticos** para uso educacional. As funções em
`utils/sidra_api.py` cobrem os endpoints usados no curso:

```python
from utils.sidra_api import (
    obter_ipca_mensal,
    obter_pib_per_capita_uf,
    obter_populacao_uf,
    consultar_sidra,   # função genérica para qualquer tabela
)
```

---

## 📋 Pré-requisitos

- Python ≥ 3.10
- Conhecimento básico de Python (variáveis, funções, listas)
- Vontade de aprender estatística com dados reais 🇧🇷

Bibliotecas (instaladas automaticamente):
`numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`, `plotly`, `requests`.

---

## 🎯 Para quem é este curso?

- Estudantes de graduação/pós em qualquer área quantitativa
- Profissionais de dados começando em estatística
- Pesquisadores que precisam analisar dados públicos brasileiros
- Autodidatas que querem **teoria + prática + dados reais** num só lugar

---

## 📝 Como referenciar

Se este material for útil em algum trabalho:

```
Curso de Estatística com Python e dados do IBGE. Disponível em:
https://github.com/220719/curso-estatistica-python
```

---

## 📄 Licença

MIT — veja [LICENSE](LICENSE).

---

