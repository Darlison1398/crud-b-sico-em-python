from bd import conn

cursor  = conn.cursor()

delete = """
  DELETE FROM cursos
        WHERE id = 5
    """

try:
    cursor.execute(delete)
    
    if cursor.rowcount > 0:
        print("Dado deletado com sucesso")
        
        conn.commit()

    else:
        print("Não foi possível deletar o dado")

except Exception as e:
    print("Erro ao deletar o dado:", e)

cursor.close()
conn.close()