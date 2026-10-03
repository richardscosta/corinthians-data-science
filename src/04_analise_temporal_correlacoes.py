"""
Temporal evolution and correlation analysis.

MBA in Data Science & Analytics - USP/Esalq
Project: Corinthians Performance Analysis (2021-2025)

This script evaluates year-over-year changes in sporting
performance indicators and calculates Pearson correlations
between selected variables.
"""

import pandas as pd


# ============================================================
# 1. TEMPORAL EVOLUTION
# ============================================================

evolucao_temporal = tabela_final[
    [
        "Temporada",
        "Aproveitamento",
        "Gols_Marcados",
        "Gols_Sofridos",
        "Saldo_Gols"
    ]
].copy()


# Year-over-year absolute change in performance
evolucao_temporal["Variacao_Aproveitamento_pp"] = (
    evolucao_temporal["Aproveitamento"].diff()
)


# Year-over-year percentage changes
evolucao_temporal["Variacao_GM_%"] = (
    evolucao_temporal["Gols_Marcados"]
    .pct_change()
    .mul(100)
)

evolucao_temporal["Variacao_GC_%"] = (
    evolucao_temporal["Gols_Sofridos"]
    .pct_change()
    .mul(100)
)


evolucao_temporal = evolucao_temporal.round(2)


print("\nEVOLUÇÃO TEMPORAL")
print(evolucao_temporal)


# ============================================================
# 2. CORRELATION ANALYSIS
# ============================================================

variaveis_correlacao = [
    "Vitorias",
    "Aproveitamento",
    "Gols_Marcados",
    "Gols_Sofridos",
    "Saldo_Gols",
    "GM_por_Jogo",
    "GC_por_Jogo",
    "Saldo_por_Jogo"
]


matriz_correlacao = (
    tabela_final[variaveis_correlacao]
    .corr(method="pearson")
    .round(2)
)


print("\nMATRIZ DE CORRELAÇÃO DE PEARSON")
print(matriz_correlacao)
