from connection.bd import conn

cursor  = conn.cursor()

cursor.execute("SELECT * FROM alunos")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
