from connection.bd import conn

def get_alunos_e_cursos():
    cursor = conn.cursor()

    select_query = """
        SELECT a.nome, c.nome_curso
        FROM alunos a
        INNER JOIN cursos c ON a.id = c.aluno_id
    """
    
    try:
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Erro ao executar consulta:", e)
    finally:
        cursor.close()
