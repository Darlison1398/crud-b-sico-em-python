from connection.bd import conn

def update_cursos(id, novo_nome):
    cursor = conn.cursor()

    update_query = """
        UPDATE cursos
        SET nome = %s
        WHERE id = %s
    """

    try:
        cursor.execute(update_query, (novo_nome, id))
        if cursor.rowcount > 0:
            print("Dado atualizado com sucesso")
            conn.commit()
        else:
            print("Não foi possível atualizar o dado")
    except Exception as e:
        print("Erro ao atualizar o dado:", e)
    finally:
        cursor.close()
