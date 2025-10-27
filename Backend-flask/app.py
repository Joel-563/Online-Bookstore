from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from psycopg2 import OperationalError
from celery import Celery
import os
import time

app = Flask(__name__)
CORS(app)

# Celery config
celery = Celery('worker', broker='redis://broker:6379/0')

# DB connection
while True:
    try:
        conn = psycopg2.connect(
            host="db",
            database="bookstore",
            user="postgres",
            password="postgres"
        )
        print("Database connected!")
        break
    except OperationalError:
        print("Database not ready, retrying in 2s...")
        time.sleep(2)

@app.route('/books', methods=['GET'])
def get_books():
    cur = conn.cursor()
    cur.execute("SELECT id, title, author FROM books")
    rows = cur.fetchall()
    cur.close()
    books = [{"id": r[0], "title": r[1], "author": r[2]} for r in rows]
    return jsonify(books)

@app.route('/order', methods=['POST'])
def place_order():
    data = request.json
    process_order.delay(data)
    return jsonify({"status": "Order received"}), 202

@celery.task
def process_order(order):
    # Here you would update DB inventory, etc.
    print(f"Processing order: {order}")
    return True

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
