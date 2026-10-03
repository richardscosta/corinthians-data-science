/*
Corinthians Performance Analysis (2021-2025)
MBA in Data Science & Analytics - USP/Esalq

SQL query used to aggregate individual match records
by season and competition.

The analysis uses an equivalent-points criterion:
3 points for a win, 1 for a draw and 0 for a loss.
This allows comparison across competitions with
different tournament formats.
*/

SELECT
    Temporada,
    Competicao,

    COUNT(*) AS Jogos,

    SUM(
        CASE
            WHEN Resultado = 'Vitória' THEN 1
            ELSE 0
        END
    ) AS Vitorias,

    SUM(
        CASE
            WHEN Resultado = 'Empate' THEN 1
            ELSE 0
        END
    ) AS Empates,

    SUM(
        CASE
            WHEN Resultado = 'Derrota' THEN 1
            ELSE 0
        END
    ) AS Derrotas,

    SUM(GM) AS Gols_Marcados,
    SUM(GC) AS Gols_Sofridos,

    SUM(
        CASE
            WHEN Resultado = 'Vitória' THEN 3
            WHEN Resultado = 'Empate' THEN 1
            ELSE 0
        END
    ) AS Pontos_Equivalentes,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN Resultado = 'Vitória' THEN 3
                WHEN Resultado = 'Empate' THEN 1
                ELSE 0
            END
        ) / (COUNT(*) * 3),
        2
    ) AS Aproveitamento

FROM Partidas

GROUP BY
    Temporada,
    Competicao

ORDER BY
    Temporada,
    Competicao;
