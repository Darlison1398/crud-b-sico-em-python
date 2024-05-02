from bd import conn


cursor = conn.cursor()

update = """
        UPDATE cursos
        SET nome_curso = 'Agronomia'
        WHERE id = 5
    """

try:
    cursor.execute(update)
    
    if cursor.rowcount > 0:
        print("Dado atualizado com sucesso")
        
        conn.commit()

    else:
        print("Não foi possível atualizar o dado")

except Exception as e:
    print("Erro ao atualizar o dado:", e)

cursor.close()
