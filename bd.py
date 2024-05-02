import psycopg2

try:
    conn = psycopg2.connect(
        dbname="Faculdade",
        user="postgres",
        password="darlin13",
        host="localhost"
    )
except psycopg2.Error as e:
    print("Erro ao conectar ao banco de dados:", e)