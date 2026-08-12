from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

def connect_db():
    time.sleep(5)  # wait for MySQL to start
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="testdb",
        port=3306
    )

@app.route('/')
def home():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        result = cursor.fetchone()
        return f"Now i have completely setup CICD pipeline via Github Actions and now i want to see the live updates on push event: {result}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
