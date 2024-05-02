from bd import conn

cursor  = conn.cursor()

cursor.execute("SELECT * FROM cursos WHERE nome_curso = 'Medicina'")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
