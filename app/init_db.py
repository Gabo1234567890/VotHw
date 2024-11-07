import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="db",
    database="exampledb",
    user="exampleuser",
    password="examplepass"
)
cursor = conn.cursor()

# Create the messages table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id SERIAL PRIMARY KEY,
        message TEXT NOT NULL
    )
''')

# Insert a sample message
cursor.execute('INSERT INTO messages (message) VALUES (%s) ON CONFLICT DO NOTHING', ('Hello, Docker with PostgreSQL!',))

# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()
