# Corinthians Performance Analysis | Data Science

Data Science and Sports Analytics project developed as part of the **MBA in Data Science & Analytics at USP/Esalq**, analyzing the sporting performance of **Sport Club Corinthians Paulista from 2021 to 2025**.

The project integrates match, competition, squad, coaching staff, transfer, and financial data to investigate the club's performance over five seasons using data analysis techniques.

## Project Overview

Professional football performance is influenced by multiple dimensions that go beyond match results. This project structures and analyzes data from different sources to provide a longitudinal view of Corinthians' sporting performance between 2021 and 2025.

The study covers **353 matches** and combines sporting indicators with information about squad utilization, coaching changes, player transfers, and financial context.

The analysis is primarily descriptive and exploratory. Its purpose is to identify patterns and associations in the club's performance rather than establish causal relationships.

## Technologies

- **Python**
- **Pandas**
- **NumPy**
- **SQL**
- **SQLite**
- **Excel**
- **Power BI**
- **Matplotlib**
- **pdfplumber**

## Data Analysis Workflow

The project follows a structured analytical workflow:

**Data Extraction → Data Cleaning → Data Validation → Data Structuring → SQL Aggregation → Exploratory Data Analysis → Statistical Analysis → Data Visualization**

### 1. Data Extraction

Match information from the 2021–2025 seasons was extracted from PDF files using Python and `pdfplumber`, generating intermediate text files for subsequent processing.

### 2. Data Cleaning and Validation

The datasets were standardized and validated before analysis. The process included checks for:

- missing values;
- duplicate records;
- inconsistent match results;
- variable formats;
- competition and team naming;
- consistency between match-level and aggregated records.

### 3. SQL and Data Aggregation

SQLite was used within Python to query and aggregate match-level records by season, competition, and other analytical dimensions.

For comparisons across competitions with different formats, an equivalent-points criterion was adopted:

- Win = 3 points
- Draw = 1 point
- Loss = 0 points

This criterion was used only as a standardized analytical measure and does not represent official points in knockout competitions.

### 4. Exploratory and Statistical Analysis

The project includes:

- descriptive statistics;
- coefficient of variation;
- year-over-year performance analysis;
- home vs. away performance;
- performance by competition;
- squad utilization;
- coaching staff analysis;
- transfer activity;
- financial context;
- Pearson correlation analysis.

Because the longitudinal analysis covers five seasons, correlation results are interpreted as exploratory rather than causal evidence.

## Repository Structure

```text
corinthians-data-science/
│
├── README.md
│
└── src/
    ├── 01_extracao_dados.py
    ├── 02_consultas_sql.sql
    ├── 03_estatisticas_descritivas.py
    └── 04_analise_temporal_correlacoes.py
```

## Code

The `src` directory contains selected code used in the analytical workflow:

- `01_extracao_dados.py` — PDF text extraction for the 2021–2025 seasons
- `02_consultas_sql.sql` — SQL aggregation of match records by season and competition
- `03_estatisticas_descritivas.py` — descriptive statistics and coefficient of variation
- `04_analise_temporal_correlacoes.py` — temporal evolution and Pearson correlation analysis

The repository focuses on the main computational procedures used in the study rather than reproducing all intermediate diagnostic scripts.

## Main Analytical Dimensions

The analysis integrates six main dimensions:

1. **Sporting performance** — results, goals, goal difference and performance percentage
2. **Competitions** — comparison across tournaments
3. **Home and away performance** — differences according to match location
4. **Squad utilization** — player usage and concentration of minutes
5. **Coaching and transfers** — coaching changes and squad movement
6. **Financial context** — revenue, debt and squad market value

## Data Sources

The study combines publicly available information from multiple sources, including:

- ESPN
- FBref
- SofaScore
- Transfermarkt
- Sport Club Corinthians Paulista financial statements and public reports

The datasets themselves are not redistributed in this repository. The repository contains selected analytical code developed for the project.

## Academic Context

This project was developed as the final project for the **MBA in Data Science & Analytics — USP/Esalq (2026)**.

**Study period:** 2021–2025  
**Club analyzed:** Sport Club Corinthians Paulista  
**Field:** Data Science / Sports Analytics

## Author

**Richard Costa**

MBA in Data Science & Analytics — USP/Esalq

Interests: Data Analytics | Data Science | Sports Analytics | Data Quality | Data Governance
