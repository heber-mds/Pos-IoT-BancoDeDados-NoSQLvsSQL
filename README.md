# Pos-IoT-BancoDeDados-NoSQLvsSQL
Comparativo entre Banco de Dados Relacional (PostgreSQL) e Não Relacional (MongoDB)​  Estudo de Caso: Casos de COVID-19 no Brasil​  Linguagem de programação aplicada: Python

# Comparação entre PostgreSQL e MongoDB usando Dados da COVID-19 no Brasil

## 🎯 Objetivo da Apresentação

Este projeto tem como objetivo:

- Apresentar as principais **diferenças entre os paradigmas Relacional (SQL) e Não Relacional (NoSQL)**.
- Realizar uma **comparação prática entre PostgreSQL e MongoDB**, abordando:
  - Estrutura e **armazenamento de dados**;
  - Sintaxe e desempenho de **consultas**.
- Demonstrar consultas em **dados reais** da pandemia de COVID-19 no Brasil.

## 🗂️ Características do Dataset

- Fonte: [Brasil.IO – Datasets – COVID-19](https://brasil.io/dataset/covid19/caso/)
- Formato: Arquivos CSV
- Escopo: Registros por **estado** e **município**
- Volume de dados: Aproximadamente **3,9 milhões de registros**
- Total de atributos: **18 colunas**
- Exemplos de atributos:
  - `city` (Cidade)
  - `date` (Data)
  - `state` (UF)
  - `last_available_confirmed` (Casos confirmados)
  - `last_available_deaths` (Mortes)
  - `estimated_population_2019` (População estimada)

## 🛠️ Tecnologias Utilizadas

- **PostgreSQL** (Relacional)
- **MongoDB** (Não Relacional)
- **Python** para scripts de carga e consultas
- **Jupyter Notebook** para visualização dos resultados

## 📊 Estrutura do Projeto


