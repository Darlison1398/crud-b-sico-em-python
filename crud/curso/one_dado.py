from connection.bd import conn

def select_cursos_por_nome(nome_curso):
    cursor = conn.cursor()

    select_query = """
        SELECT * FROM cursos WHERE nome_curso = %s
    """

    try:
        cursor.execute(select_query, (nome_curso,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Erro ao executar consulta:", e)
    finally:
        cursor.close()
