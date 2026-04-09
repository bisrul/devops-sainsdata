rule all:
    input: "reports/revenue_by_category.png"

rule download:
    output: "data/raw/sales.csv"
    script: "scripts/download_data.py"

rule process:
    input:  "data/raw/sales.csv"
    output: "data/processed/sales_clean.csv"
    script: "scripts/process_data.py"

rule analyze:
    input:  "data/processed/sales_clean.csv"
    output: "reports/revenue_by_category.png"
    script: "scripts/analyze.py"