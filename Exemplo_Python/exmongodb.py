# ================================
# Bibliotecas importadas
# ================================
import sys        # Permite acesso aos argumentos passados via linha de comando
import time       # Usado para medir o tempo de execução das consultas
from pymongo import MongoClient       # Biblioteca para conectar com o MongoDB
from datetime import datetime         # Utilizado para manipular datas

# Conexão com o MongoDB (localhost, porta padrão 27017)
client = MongoClient("mongodb://localhost:27017/")

# Seleciona o banco de dados chamado "covid"
db = client["covid"]

# Seleciona a coleção chamada "covidcasos"
collection = db["covidcasos"]

# ================================
# Função 1: Buscar o dado mais recente de uma cidade específica
# ================================
def buscar_casos_por_cidade(cidade_nome):
    inicio = time.time()  # Início da contagem de tempo

    # Busca um documento que tenha a cidade informada,
    # ordenando pela data mais recente (ordem decrescente)
    doc = collection.find_one(
        {"city": cidade_nome},
        sort=[("date", -1)]
    )

    fim = time.time()  # Fim da contagem de tempo

    # Exibe os dados, se encontrados
    if doc:
        print(f"{cidade_nome} - {doc['date'].date()} - Casos confirmados: {doc.get('last_available_confirmed', 'N/A')}")
        print("Total de documentos retornados: 1")
    else:
        print(f"Nenhum dado encontrado para a cidade: {cidade_nome}")
        print("Total de documentos retornados: 0")

    print(f"Tempo da consulta: {fim - inicio:.4f} segundos")

# ================================
# Função 2: Buscar registros por estado e mês específico
# ================================
def buscar_registros_por_estado_e_mes(estado_sigla, ano, mes):
    # Define o intervalo de datas: do primeiro dia do mês até o próximo mês
    inicio_data = datetime(ano, mes, 1)
    fim_data = datetime(ano + 1, 1, 1) if mes == 12 else datetime(ano, mes + 1, 1)

    inicio = time.time()  # Início da contagem de tempo

    # Consulta todos os registros de um estado, dentro do mês especificado
    resultado = collection.find({
        "state": estado_sigla.upper(),
        "date": {"$gte": inicio_data, "$lt": fim_data}
    })

    docs = list(resultado)  # Converte o cursor em uma lista de documentos
    fim = time.time()       # Fim da contagem de tempo

    # Exibe os registros encontrados
    print(f"\nRegistros do estado {estado_sigla.upper()} em {mes:02d}/{ano}:")
    for doc in docs:
        cidade = doc.get("city", "[Sem cidade]")
        data = doc["date"].date()
        casos = doc.get("last_available_confirmed", "N/A")
        print(f"{cidade} - {data} - Casos: {casos}")
    
    # Exibe a contagem de registros encontrados e tempo da consulta
    print(f"Total de documentos retornados: {len(docs)}")
    print(f"Tempo da consulta: {fim - inicio:.4f} segundos")

# ================================
# Função 3: Total de casos confirmados por estado
# ================================
def total_casos_por_estado():
    # Pipeline de agregação:
    pipeline = [
        {"$match": {"place_type": "state"}},  # Considera apenas registros do tipo "estado"
        {"$group": {
            "_id": "$state",  # Agrupa por sigla do estado
            "total_confirmados": {"$max": "$last_available_confirmed"}  # Pega o valor máximo de casos confirmados
        }},
        {"$sort": {"total_confirmados": -1}}  # Ordena do maior para o menor
    ]

    inicio = time.time()
    resultado = list(collection.aggregate(pipeline))  # Executa o pipeline e converte em lista
    fim = time.time()

    # Exibe o total de casos por estado
    print("\nTotal de casos confirmados por estado:")
    for doc in resultado:
        print(f"Estado: {doc['_id']} - Casos: {doc['total_confirmados']}")

    print(f"Total de documentos retornados: {len(resultado)}")
    print(f"Tempo da consulta: {fim - inicio:.4f} segundos")

# ================================
# Função 4: Top 5 estados com mais mortes
# ================================
def top_5_mortes_por_estado():
    pipeline = [
        {"$match": {"place_type": "state"}},  # Filtra apenas os documentos que representam estados
        {"$group": {
            "_id": "$state",
            "total_obitos": {"$max": "$last_available_deaths"}  # Pega o maior número de mortes registrado por estado
        }},
        {"$sort": {"total_obitos": -1}},  # Ordena em ordem decrescente
        {"$limit": 5}                     # Limita aos 5 maiores resultados
    ]

    inicio = time.time()
    resultado = list(collection.aggregate(pipeline))
    fim = time.time()

    # Exibe o top 5 estados com mais óbitos
    print("\nTop 5 estados com mais mortes:")
    for doc in resultado:
        print(f"Estado: {doc['_id']} - Óbitos: {doc['total_obitos']}")
    
    print(f"Total de documentos retornados: {len(resultado)}")
    print(f"Tempo da consulta: {fim - inicio:.4f} segundos")

# ================================
# Bloco principal de execução
# ================================
if __name__ == "__main__":
    # Verifica se foi passado algum argumento via terminal
    if len(sys.argv) < 2:
        print("Uso: python exmongodb.py <funcao> [parametros]")
        sys.exit(1)

    # Recupera o nome da função (primeiro argumento)
    comando = sys.argv[1]

    # Mapeia o comando para a função correspondente
    if comando == "buscar_casos_por_cidade":
        cidade = sys.argv[2]
        buscar_casos_por_cidade(cidade)

    elif comando == "buscar_registros_por_estado_e_mes":
        estado = sys.argv[2]
        ano = int(sys.argv[3])
        mes = int(sys.argv[4])
        buscar_registros_por_estado_e_mes(estado, ano, mes)

    elif comando == "total_casos_por_estado":
        total_casos_por_estado()

    elif comando == "top_5_mortes_por_estado":
        top_5_mortes_por_estado()

    else:
        print(f"Comando desconhecido: {comando}")

# ================================
# Exemplos de uso no terminal:
# ================================
# python exmongodb.py buscar_casos_por_cidade Curitiba
# python exmongodb.py buscar_registros_por_estado_e_mes PR 2020 4
# python exmongodb.py total_casos_por_estado
# python exmongodb.py top_5_mortes_por_estado
