from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",  # Matches the service name in docker-compose.yml
        database="exampledb",
        user="exampleuser",
        password="examplepass",
        cursor_factory=RealDictCursor
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT message FROM messages LIMIT 1;')
    message = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(message=message['message'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
