from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    db_host = os.getenv('DB_HOST', 'localhost')
    return f"Aplikasi berhasil terhubung dan berjalan! (DB Host: {db_host})"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
