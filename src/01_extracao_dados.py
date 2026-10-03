"""
Data extraction from ESPN PDF files.

MBA in Data Science & Analytics - USP/Esalq
Project: Corinthians Performance Analysis (2021-2025)

This script extracts the textual content of the PDF files used
in the study and generates intermediate text files for subsequent
data treatment and structuring.
"""

import pdfplumber


for ano in range(2021, 2026):

    nome_pdf = f"Corinthians - Resultados - ESPN (BR) {ano}.pdf"
    texto = ""

    with pdfplumber.open(nome_pdf) as pdf:
        for pagina in pdf.pages:
            texto_pagina = pagina.extract_text()

            if texto_pagina:
                texto += texto_pagina + "\n"

    nome_saida = f"Corinthians_{ano}.txt"

    with open(
        nome_saida,
        "w",
        encoding="utf-8"
    ) as arquivo:
        arquivo.write(texto)


print("Arquivos de texto gerados com sucesso.")
