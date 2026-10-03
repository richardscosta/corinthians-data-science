"""
Descriptive statistics for sporting performance indicators.

MBA in Data Science & Analytics - USP/Esalq
Project: Corinthians Performance Analysis (2021-2025)

This script calculates descriptive statistics and the
coefficient of variation for the main sporting performance
indicators consolidated by season.
"""

import pandas as pd


# Descriptive statistics
estatisticas = tabela_final[
    [
        "Aproveitamento",
        "Gols_Marcados",
        "Gols_Sofridos",
        "Saldo_Gols",
        "GM_por_Jogo",
        "GC_por_Jogo",
        "Saldo_por_Jogo"
    ]
].describe().T


# Coefficient of variation (%)
estatisticas["Coef_Variacao_%"] = (
    estatisticas["std"]
    / estatisticas["mean"].abs()
    * 100
)


# Round results
estatisticas = estatisticas.round(2)


print(
    "\nESTATÍSTICAS DESCRITIVAS "
    "DOS INDICADORES ESPORTIVOS"
)

print(estatisticas)
