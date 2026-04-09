# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install pandas matplotlib snakemake

CMD ["snakemake", "--cores", "1"]