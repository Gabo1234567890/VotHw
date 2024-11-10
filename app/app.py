# Главният Flask app file, който се грижи за HTTP заявки и отговори. Той дефинира структурата и държанието на web app.
# В този случай се дефинира простичък Flask app, който се свързва с PostgreSQL DB и взима съобщение, което се връща като HTML response

from flask import Flask
import psycopg2
from psycopg2.extras import RealDictCursor # Toва е dictionary cursor - това прави резултатите от заявките (query) към БД като dict, а не като tuple

app = Flask(__name__) # Създава се инстанция на Flask app

def get_db_connection(): # Taзи функция установява връзка с БД
    conn = psycopg2.connect(
        host="db",  # Специфицира host-а за връзката с БД. В случая това съвпада с посоченото в docker-compose.yml
        database="exampledb", # Специфицира името на БД, с която да се свърже
        user="exampleuser", # Задава потребителското име за аутентикация в БД
        password="examplepass", # Задава паролата за аутентикация в БД
        cursor_factory=RealDictCursor # Задава типа на курсора да бъде RealDictCursor, за да бъдат връщани резултатите от заявките като dictonary
    )
    return conn # Връща врзката към БД като обект, като чрез него може да се взаимодейства с нея

@app.route('/') # Дефинира пътя за root URL като /, това означава, че когато бъде посетен URL на app-a (например localhost:5000), index функцията ще се изпълни
def index(): # Тази функция обработва заявки към root URL
    conn = get_db_connection() # Създава връзка с БД като вика горната функция
    cursor = conn.cursor() # Създава курсорен обект, чрез който ще бъдат изпълнявани SQL заявки към БД
    cursor.execute('SELECT message FROM messages LIMIT 1;') # Изпълнява заявка, която да вземе 'message' колоната от първия ред на 'messages' таблицата
    message = cursor.fetchone() # Взима единствено и само първия ред от резултата от заявката и го съхранява в message променливата. Тук тя е dictionary заради RealDictCursor
    cursor.close() # Затваря курсора, за да освободи ресурси
    conn.close() # Затваря връзката с БД, за да освбоди ресурси
    return f"<h1>{message['message']}</h1>" # Извлича message ключа от dictionary-то message и го връща в HTML формат, като текст

if __name__ == '__main__': # Подсигурява, че Flask server-a се изпълнява само ако този файл е изпълнен, а не ако е import-нат като модул
    app.run(host='0.0.0.0', port=5000) # Стартира Flask web server-a на 0.0.0.0, за да може да се достъпи и извън контейнера и на порт 5000
