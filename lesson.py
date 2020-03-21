from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Привет!</h1>'


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run('0.0.0.0', port)
