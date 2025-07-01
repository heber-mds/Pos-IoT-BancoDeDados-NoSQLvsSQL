
# 📊 Execução de Exemplos com MongoDB e PostgreSQL

Este repositório contém dois scripts Python que demonstram como acessar e consultar dados do dataset COVID-19, armazenado em dois bancos diferentes:

- `exmongodb.py`: acessa o banco **MongoDB** (`covid.covidcasos`)
- `expostgredb.py`: acessa o banco **PostgreSQL** (`covidcasos.caso_covid`)

Ambos os scripts usam consultas parametrizadas para buscar dados de forma segura e eficiente.

---

## 📦 Instalação dos requisitos

Antes de executar os scripts, instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## 🔌 Configuração dos bancos

### MongoDB

- A base de dados deve estar no `localhost:27017`
- Nome do banco: `covid`
- Nome da coleção: `covidcasos`

### PostgreSQL

- O banco deve estar disponível localmente (porta padrão: 5432)
- Parâmetros definidos no script:
  - `host`: `localhost`
  - `dbname`: `covidcasos`
  - `user`: `postgres`
  - `password`: `posiot`
- Nome da tabela: `caso_covid`

---

## ▶️ Como executar os scripts

Os dois scripts seguem a mesma lógica: o primeiro argumento indica a função, e os demais são os parâmetros.

### 🔷 MongoDB (`exmongodb.py`)

```bash
python exmongodb.py buscar_casos_por_cidade Foz do Iguaçu
python exmongodb.py buscar_registros_por_estado_e_mes PR 2021 5
python exmongodb.py total_casos_por_estado
python exmongodb.py top_5_mortes_por_estado
```

### 🔶 PostgreSQL (`expostgredb.py`)

```bash
python expostgredb.py buscar_casos_por_cidade Foz do Iguaçu
python expostgredb.py buscar_registros_por_estado_e_mes PR 2021 5
python expostgredb.py total_casos_por_estado
python expostgredb.py top_5_mortes_por_estado
```

---

## 📄 O que cada função faz?

| Função                           | Descrição                                                                 |
|----------------------------------|---------------------------------------------------------------------------|
| `buscar_casos_por_cidade`       | Retorna os casos mais recentes para uma cidade específica                 |
| `buscar_registros_por_estado_e_mes` | Lista os registros de um estado em um mês/ano                            |
| `total_casos_por_estado`        | Mostra o total acumulado de casos por estado                              |
| `top_5_mortes_por_estado`       | Lista os 5 estados com maior número de óbitos registrados                 |

---

## ✅ Resultado esperado

Ao rodar qualquer script, o terminal exibirá:

- Resultado da consulta (cidade, data, casos, etc.)
- Número de documentos ou registros retornados
- Tempo de execução da consulta

---

## 📌 Observações

- Certifique-se de que o dataset do Brasil.IO foi corretamente importado para os dois bancos.
- Os nomes dos campos no MongoDB e PostgreSQL devem estar compatíveis com os scripts.
- Use Python 3.9+ para compatibilidade total.

---

## 📁 Arquivos do repositório

- `exmongodb.py`: consultas usando MongoDB e `pymongo`
- `expostgredb.py`: consultas usando PostgreSQL e `psycopg2`
- `requirements.txt`: lista de bibliotecas utilizadas

---

Desenvolvido para fins educacionais — aula prática de comparação entre bancos SQL e NoSQL.

