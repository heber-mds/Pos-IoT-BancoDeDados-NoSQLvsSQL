
# 💾  Comparativo entre Banco de Dados SQL e NoSQL

Este repositório apresenta um passo a passo didático de como importar o dataset `caso_full` de COVID-19 do [Brasil.IO](https://brasil.io/dataset/covid19/caso_full/) em dois tipos de bancos de dados locais:

- 📦 **MongoDB** (NoSQL), usando **MongoDB Compass**
- 🐘 **PostgreSQL** (SQL), usando **PGAdmin 4**

---

## 📁 Dataset utilizado

- Dataset: `caso_full.csv`
- Fonte: [https://brasil.io/dataset/covid19/caso_full/](https://brasil.io/dataset/covid19/caso_full/)
- Tamanho: ~420 MB (varia com o tempo)

Faça o download do CSV diretamente em:  
👉 [`https://data.brasil.io/dataset/covid19/caso_full.csv.gz`](https://data.brasil.io/dataset/covid19/caso_full.csv.gz)

Descompacte o arquivo `.gz` para obter o `caso_full.csv`.

---

## 📦 Parte 1 — Importar o Dataset no MongoDB (NoSQL)

### 🛠️ Requisitos

- [MongoDB instalado localmente](https://www.mongodb.com/try/download/community)
- [MongoDB Compass](https://www.mongodb.com/products/compass)

### ✅ Passo a Passo

1. **Abra o MongoDB Compass.**
2. Clique em **"New Connection"** e use a URI padrão:
   ```
   mongodb://localhost:27017
   ```
3. Clique em **"Connect"**.
4. Clique em **"Create Database"**:
   - **Database Name**: `covid`
   - **Collection Name**: `caso_full`
5. Após criado, clique na coleção `caso_full`, depois em **"ADD DATA" > "Import File"**.
6. Selecione o arquivo `caso_full.csv`.
7. Selecione o tipo: **CSV**.
8. Clique em **"IMPORT"**.

### 🔍 Validando a Importação

Após a importação, clique na coleção `caso_full` e verifique:

- A presença de documentos (registros)
- A visualização dos campos como `date`, `city`, `state`, `confirmed`, `deaths`, etc.

Ou rode a seguinte consulta no painel aggregation do Compass:
```
[
  {
    "$match": {
      "city": "Foz do Iguaçu",
      "place_type": "city"
    }
  },
  {
    "$sort": {
      "date": -1
    }
  },
  {
    "$limit": 1
  },
  {
    "$project": {
      "_id": 0,
      "city": 1,
      "state": 1,
      "date": 1,
      "last_available_confirmed": 1
    }
  }
]
```
---
Resultado esperado:
```
{
  "city": "Foz do Iguaçu",
  "date": {
    "$date": "2022-03-27T00:00:00.000Z"
  },
  "last_available_confirmed": 45273,
  "state": "PR"
}
```
---

## 🐘 Parte 2 — Importar o Dataset no PostgreSQL (SQL)

### 🛠️ Requisitos

- [PostgreSQL](https://www.postgresql.org/download/)
- [PGAdmin 4](https://www.pgadmin.org/)

### ✅ Passo a Passo

1. Abra o **PGAdmin 4**.
2. No menu à esquerda, clique com o botão direito em **Servers > PostgreSQL** e escolha **Create > Database**.
   - **Database Name**: `covid`
3. Com o banco `covid` criado, vá até **Query Tool** (ferramenta de SQL).
4. Crie uma tabela com base nas colunas do CSV (exemplo simplificado):

```sql
CREATE TABLE caso_full (
    city TEXT,
    city_ibge_code BIGINT,
    date TEXT,
    epidemiological_week INT,
    estimated_population BIGINT,
    estimated_population_2019 BIGINT,
    is_last TEXT,
    is_repeated TEXT,
    last_available_confirmed INT,
    last_available_confirmed_per_100k_inhabitants REAL,
    last_available_date TEXT,
    last_available_death_rate REAL,
    last_available_deaths INT,
    order_for_place INT,
    place_type TEXT,
    state TEXT
);
```

5. Vá em **Tools > Import/Export**.
   - Selecione a **tabela**: `caso_full`
   - Escolha o **arquivo**: `caso_full.csv`
   - Tipo: **CSV**
   - Encoding: `UTF8`
   - Delimitador: `,`
   - Marque **Header** como `Yes`
   - Clique em **OK** para importar

> ⚠️ Ajuste os tipos e nomes das colunas conforme necessário com base no CSV real.

### 🔍 Validando a Importação

Abra o **Query Tool** e execute:

```sql
SELECT COUNT(*) FROM caso_full;
```

Ou visualize alguns dados com:

```sql
SELECT * FROM caso_full LIMIT 10;
```

---

## ✅ Conclusão

Com esses passos, você terá o mesmo dataset estruturado tanto em um banco de dados relacional (PostgreSQL) quanto em um banco de dados não relacional (MongoDB).

Esses bancos podem agora ser utilizados em consultas, comparações de desempenho e estrutura, análise de schema, e demonstrações práticas dos paradigmas SQL vs NoSQL.

---

## 📌 Referências

- [https://brasil.io/dataset/covid19/caso_full/](https://brasil.io/dataset/covid19/caso_full/)
- [MongoDB Compass Docs](https://www.mongodb.com/docs/compass/current/)
- [PGAdmin 4 Docs](https://www.pgadmin.org/docs/pgadmin4/latest/)

---

