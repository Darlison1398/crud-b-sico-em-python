from connection.bd import conn

def delete_cursos_por_id(id):
    cursor = conn.cursor()

    delete_query = """
        DELETE FROM cursos
        WHERE id = %s
    """

    try:
        cursor.execute(delete_query, (id,))
        if cursor.rowcount > 0:
            print("Dado deletado com sucesso")
            conn.commit()
        else:
            print("Não foi possível deletar o dado")
    except Exception as e:
        print("Erro ao deletar o dado:", e)
    finally:
        cursor.close()
