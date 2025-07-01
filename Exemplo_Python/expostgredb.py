# ================================
# Bibliotecas importadas
# ================================
import sys                 # Permite acessar argumentos passados pela linha de comando (ex: nome da função e parâmetros)
import time                # Usado para medir o tempo de execução das consultas
import psycopg2            # Biblioteca oficial para conectar Python com o banco de dados PostgreSQL
from psycopg2.extras import RealDictCursor  # Faz com que os resultados sejam retornados como dicionários (ao invés de tuplas)

# ================================
# Parâmetros de conexão com o banco de dados PostgreSQL
# ================================
conn_params = {
    "host": "localhost",        # Endereço onde o banco está rodando (localhost = máquina local)
    "dbname": "covidcasos",     # Nome do banco de dados que será acessado
    "user": "postgres",         # Nome de usuário do PostgreSQL
    "password": "posiot"        # Senha correspondente ao usuário acima
}

# ================================
# Função de conexão com o banco de dados
# ================================
def conectar():
    # Cria e retorna uma conexão com o banco usando os parâmetros definidos
    return psycopg2.connect(**conn_params)

# ================================
# Função 1 - Buscar o caso mais recente de uma cidade
# ================================
def buscar_casos_por_cidade(cidade_nome):
    # Consulta SQL que busca os casos de uma cidade específica, ordenando pela data mais recente
    query = """
        SELECT city, date, last_available_confirmed
        FROM caso_covid
        WHERE city = %s
        ORDER BY date DESC
        LIMIT 1;
    """
    # Abre conexão e executa a consulta
    with conectar() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            inicio = time.time()  # Marca o tempo de início da execução
            cur.execute(query, (cidade_nome,))  # Executa a consulta com o nome da cidade como parâmetro
            resultado = cur.fetchone()  # Retorna o primeiro (e único) registro encontrado
            fim = time.time()  # Marca o tempo final da execução

            # Exibe o resultado da consulta
            if resultado:
                print(f"{resultado['city']} - {resultado['date']} - Casos confirmados: {resultado['last_available_confirmed']}")
                print("Total de registros retornados: 1")
            else:
                print(f"Nenhum dado encontrado para a cidade: {cidade_nome}")
                print("Total de registros retornados: 0")

            print(f"Tempo da consulta: {fim - inicio:.4f} segundos")  # Tempo total da operação

# ================================
# Função 2 - Buscar todos os registros de um estado em um mês/ano específico
# ================================
def buscar_registros_por_estado_e_mes(estado_sigla, ano, mes):
    # Cria as datas de início e fim com base no mês informado
    inicio_data = f"{ano}-{mes:02d}-01"
    fim_data = f"{ano + 1}-01-01" if mes == 12 else f"{ano}-{mes + 1:02d}-01"

    # Consulta SQL que retorna todas as cidades do estado com dados dentro do intervalo de datas
    query = """
        SELECT city, date, last_available_confirmed
        FROM caso_covid
        WHERE state = %s
          AND date >= %s
          AND date < %s
        ORDER BY date;
    """
    with conectar() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            inicio = time.time()
            # Executa a consulta com os parâmetros: estado, data inicial e data final
            cur.execute(query, (estado_sigla.upper(), inicio_data, fim_data))
            resultados = cur.fetchall()  # Retorna todos os registros encontrados
            fim = time.time()

            print(f"\nRegistros do estado {estado_sigla.upper()} em {mes:02d}/{ano}:")
            for r in resultados:
                cidade = r["city"] or "[Sem cidade]"  # Trata caso o campo cidade esteja nulo
                data = r["date"]
                casos = r["last_available_confirmed"] if r["last_available_confirmed"] is not None else "N/A"
                print(f"{cidade} - {data} - Casos: {casos}")
            print(f"Total de registros retornados: {len(resultados)}")
            print(f"Tempo da consulta: {fim - inicio:.4f} segundos")

# ================================
# Função 3 - Total de casos confirmados por estado (último valor registrado)
# ================================
def total_casos_por_estado():
    # Consulta SQL que agrupa os dados por estado e retorna o maior número de casos confirmados registrados
    query = """
        SELECT state, MAX(last_available_confirmed) AS total_confirmados
        FROM caso_covid
        WHERE place_type = 'state'
        GROUP BY state
        ORDER BY total_confirmados DESC;
    """
    with conectar() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            inicio = time.time()
            cur.execute(query)  # Executa a consulta sem parâmetros
            resultados = cur.fetchall()
            fim = time.time()

            print("\nTotal de casos confirmados por estado:")
            for r in resultados:
                print(f"Estado: {r['state']} - Casos: {r['total_confirmados']}")
            print(f"Total de registros retornados: {len(resultados)}")
            print(f"Tempo da consulta: {fim - inicio:.4f} segundos")

# ================================
# Função 4 - Top 5 estados com maior número de óbitos
# ================================
def top_5_mortes_por_estado():
    # Consulta SQL semelhante à anterior, mas agrupando e ordenando pelo número de mortes (óbitos)
    query = """
        SELECT state, MAX(last_available_deaths) AS total_obitos
        FROM caso_covid
        WHERE place_type = 'state'
        GROUP BY state
        ORDER BY total_obitos DESC
        LIMIT 5;
    """
    with conectar() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            inicio = time.time()
            cur.execute(query)  # Executa a consulta sem parâmetros
            resultados = cur.fetchall()
            fim = time.time()

            print("\nTop 5 estados com mais mortes:")
            for r in resultados:
                print(f"Estado: {r['state']} - Óbitos: {r['total_obitos']}")
            print(f"Total de registros retornados: {len(resultados)}")
            print(f"Tempo da consulta: {fim - inicio:.4f} segundos")

# ================================
# Bloco principal - ponto de entrada quando o script é executado
# ================================
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python expsql.py <funcao> [parametros]")
        sys.exit(1)

    # Captura o nome da função passada como argumento
    comando = sys.argv[1]

    # Chamada da função correspondente com seus parâmetros
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
# python expostgredb.py buscar_casos_por_cidade Curitiba
# python expostgredb.py buscar_registros_por_estado_e_mes PR 2020 4
# python expostgredb.py total_casos_por_estado
# python expostgredb.py top_5_mortes_por_estado