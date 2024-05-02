from connection.bd import conn

def insert_into_cursos(id, nome_curso, duracao, descricao, nivel, aluno_id):
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO cursos(id, nome_curso, duracao, descricao, nivel, aluno_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    try:
        cursor.execute(insert_query, (id, nome_curso, duracao, descricao, nivel, aluno_id))
        if cursor.rowcount > 0:
            print("Dado criado com sucesso")
            conn.commit()
        else:
            print("Não foi possível criar o dado")
    except Exception as e:
        print("Erro ao inserir o dado:", e)
    finally:
        cursor.close()
