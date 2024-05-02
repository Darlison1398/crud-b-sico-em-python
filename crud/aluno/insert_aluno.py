from connection.bd import conn

def insert_into_aluno(id, nome, data_nascimento, genero, endereco, email, telefone):
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO alunos(id, nome, data_nascimento, genero, endereco, email, telefone)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    try:
        cursor.execute(insert_query, (id, nome, data_nascimento, genero, endereco, email, telefone))
        if cursor.rowcount > 0:
            print("Dado criado com sucesso")
            conn.commit()
        else:
            print("Não foi possível criar o dado")
    except Exception as e:
        print("Erro ao inserir o dado:", e)
    finally:
        cursor.close()
