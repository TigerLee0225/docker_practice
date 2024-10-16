from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='mysql',
        user='root',
        password='password',
        database='mydb'
    )
    return connection

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS visits (count INT)')
    cursor.execute('SELECT count FROM visits')
    row = cursor.fetchone()
    if row:
        count = row[0] + 1
        cursor.execute('UPDATE visits SET count = %s', (count,))
    else:
        count = 1
        cursor.execute('INSERT INTO visits (count) VALUES (%s)', (count,))
    conn.commit()
    cursor.close()
    conn.close()
    return f'Hello, World! This page has been visited {count} times.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
