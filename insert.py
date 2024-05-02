from bd import conn

cursor  = conn.cursor()

insert = """
        INSERT INTO cursos(id, nome_curso, duracao, descricao, nivel)
        VALUES (5, 'DIreito', 5, 'Curso bacharel em direito', 'Superior')
    """

try:
    cursor.execute(insert)
    
    if cursor.rowcount > 0:
        print("Dado criado com sucesso")
        
        conn.commit()

    else:
        print("Não foi possível criar o dado")

except Exception as e:
    print("Erro ao inserir o dado:", e)

cursor.close()