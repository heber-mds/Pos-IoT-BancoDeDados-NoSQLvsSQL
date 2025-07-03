# Pos-IoT-BancoDeDados-NoSQLvsSQL
Comparativo entre Banco de Dados Relacional (PostgreSQL) e Não Relacional (MongoDB)​  Estudo de Caso: Casos de COVID-19 no Brasil​  Linguagem de programação aplicada: Python
- Professor: Felippe Scheidt
- Aluno: Héber Miguel dos Santos

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
Pos-IoT-BancoDeDados-NoSQLvsSQL/
│
├── Apresentação/           → Slides da apresentação comparando bancos SQL e NoSQL
│
├── Dataset/                → Descritivo README.md para estruturar os bancos de dados foco do estudo, com dados reais da COVID-19 (extraídos do Brasil.IO)
│
├── Exemplo_Python/         → Códigos-fonte em Python para manipulação e consulta de dados usando:
│                              • MongoDB (NoSQL)
│                              • PostgreSQL (Relacional)
│
├── README.md               → Descrição geral do projeto, objetivos e instruções de uso
└── requirements.txt        → Lista de dependências Python necessárias para executar os exemplos

## 📚 Conclusão Esperada

Através dessa comparação prática, espera-se:

- Evidenciar **vantagens e limitações** de cada abordagem;
- Refletir sobre a **adequação de cada tecnologia** a diferentes cenários de uso;
- Demonstrar como bancos relacionais e não relacionais lidam com **grandes volumes de dados reais**.

## 🧾 Créditos e Referências

- Dados públicos: [Brasil.IO – Datasets – COVID-19](https://brasil.io/dataset/covid19/caso/)
- Artigos e Documentação:
  - [SQL vs. NoSQL: Diferenças, vantagens e casos de uso | Astera](https://www.astera.com/type/blog/sql-vs-nosql/)
  - [How to Use PostgreSQL in Python](https://www.psycopg.org/)
  - [Bancos De Dados NoSQL Versus SQL | MongoDB](https://www.mongodb.com/pt-br/nosql-explained/nosql-vs-sql)
  - [PostgreSQL: The world's most advanced open source database](https://www.postgresql.org/)
  - [Download MongoDB Community Server | MongoDB](https://www.mongodb.com/try/download/community)
  - [Instale o MongoDB Community Edition no Windows – MongoDB Docs](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/)
  - [O que é um banco de dados? – AWS](https://aws.amazon.com/pt/what-is/database/)
  - [What Is a Database? | Oracle](https://www.oracle.com/database/what-is-database/)
  - [SQL vs. NoSQL Databases: What's the Difference? | IBM](https://www.ibm.com/cloud/blog/sql-vs-nosql)

---
