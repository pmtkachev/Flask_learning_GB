from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Базовая вьюшка!'


@app.route('/users/')
def users():
    return 'Пользователи сайта'
