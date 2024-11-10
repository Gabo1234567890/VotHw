# Този файл създава PostgreSQL БД, създава message таблицата и слага съобщение в таблицата

import psycopg2

conn = psycopg2.connect( # Установява връзка с PostgreSQL БД, използвайки същите параметри като app.py
    host="db",
    database="exampledb",
    user="exampleuser",
    password="examplepass"
)
cursor = conn.cursor() # Създава курсорен обект, чрез който се изпълняват SQL заявки

# Това създава таблицата messages в БД, ако не съществува вече и я създава с 2 колони - id, която е с автоматично нарастващи цели числа с единица, които са ключ и message, която самото съобщение
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id SERIAL PRIMARY KEY,
        message TEXT NOT NULL
    )
''')

# Това записва в message колоната от messages таблицата съобщението в скобите
cursor.execute('INSERT INTO messages (message) VALUES (%s) ON CONFLICT DO NOTHING', ('Example message',))

conn.commit() # Запазва промените в БД
cursor.close()
conn.close()
