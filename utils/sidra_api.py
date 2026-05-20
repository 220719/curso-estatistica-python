"""
Módulo utilitário para coleta de dados da API SIDRA (IBGE).

A API SIDRA é pública, não requer chave e expõe milhares de tabelas do IBGE.
Documentação oficial: https://apisidra.ibge.gov.br/

Formato genérico da URL:
    https://apisidra.ibge.gov.br/values/t/{tabela}/n/{nivel}/v/{variavel}/p/{periodo}/...

Onde:
    t/{tabela}      → ID da tabela no SIDRA
    n{X}/{cod}      → Nível geográfico (n1=Brasil, n3=UF, n6=município)
    v/{variavel}    → ID da variável
    p/{periodo}     → Período (ex: "all", "last 12", "202001-202012")
    c{classif}/{cod}→ Classificação opcional
"""

import requests
import pandas as pd
from typing import Optional


SIDRA_BASE = "https://apisidra.ibge.gov.br/values"


def consultar_sidra(url_path: str, timeout: int = 60) -> pd.DataFrame:
    """
    Consulta a API SIDRA e devolve um DataFrame limpo.

    Parameters
    ----------
    url_path : str
        Trecho da URL após /values/ (ex.: "t/1737/n1/all/v/63/p/all").
    timeout : int
        Tempo máximo de espera em segundos.

    Returns
    -------
    pd.DataFrame
        Dados com colunas renomeadas e valores numéricos convertidos.
    """
    url = f"{SIDRA_BASE}/{url_path}"
    resp = requests.get(url, timeout=timeout)
    resp.raise_for_status()
    raw = resp.json()

    # A primeira linha é o cabeçalho com nomes "humanos" das colunas.
    header = raw[0]
    rows = raw[1:]
    df = pd.DataFrame(rows)
    df = df.rename(columns=header)

    # Converte a coluna de valor para numérico (vem como string no SIDRA).
    if "Valor" in df.columns:
        df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")

    return df


def obter_ipca_mensal(n_ultimos: int = 60) -> pd.DataFrame:
    """
    Coleta a variação mensal do IPCA (Índice Nacional de Preços ao
    Consumidor Amplo) — Tabela 1737, variável 63.

    Parameters
    ----------
    n_ultimos : int
        Quantidade de meses mais recentes (padrão = 60 = 5 anos).

    Returns
    -------
    pd.DataFrame
        Colunas: data (datetime), variacao_mensal (float, em %).
    """
    url_path = f"t/1737/n1/all/v/63/p/last%20{n_ultimos}"
    df = consultar_sidra(url_path)

    # Mantém somente as colunas relevantes e renomeia.
    df = df[["Mês (Código)", "Mês", "Valor"]].copy()
    df.columns = ["periodo_cod", "periodo", "variacao_mensal"]

    # Converte AAAAMM -> datetime (primeiro dia do mês).
    df["data"] = pd.to_datetime(df["periodo_cod"], format="%Y%m")
    df = df[["data", "variacao_mensal"]].sort_values("data").reset_index(drop=True)

    return df


def obter_pib_per_capita_uf(ano: Optional[int] = None) -> pd.DataFrame:
    """
    Coleta o PIB per capita por UF — Tabela 5938, variável 6577.

    Parameters
    ----------
    ano : int, opcional
        Ano de referência. Se None, traz o último disponível.

    Returns
    -------
    pd.DataFrame
        Colunas: uf, pib_per_capita (R$).
    """
    periodo = "last%201" if ano is None else str(ano)
    url_path = f"t/5938/n3/all/v/6577/p/{periodo}"
    df = consultar_sidra(url_path)

    df = df[["Unidade da Federação", "Ano", "Valor"]].copy()
    df.columns = ["uf", "ano", "pib_per_capita"]

    return df


def obter_populacao_uf(ano: int = 2022) -> pd.DataFrame:
    """
    População residente por UF — Censo 2022 (tabela 4709, variável 93).

    Returns
    -------
    pd.DataFrame
        Colunas: uf, populacao.
    """
    url_path = f"t/4709/n3/all/v/93/p/{ano}"
    df = consultar_sidra(url_path)
    df = df[["Unidade da Federação", "Valor"]].copy()
    df.columns = ["uf", "populacao"]
    return df
