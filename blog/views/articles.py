from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

articles_app = Blueprint('articles_app', __name__)
ARTICLES = {
    1: {'name': 'Статья 1',
        'author': 1,
        'text': 'Пример текста',
        'rubric': 'Программирование'},
    2: {'name': 'Статья 2',
        'author': 2,
        'text': 'Пример текста',
        'rubric': 'Быт'},
    3: {'name': 'Статья 3',
        'author': 3,
        'text': 'Пример текста',
        'rubric': 'Рецепты'},
}


@articles_app.route('/', endpoint='list')
def articles_list():
    return render_template('articles/list.html', articles=ARTICLES)


@articles_app.route('/<int:articles_id>/', endpoint='detail')
def user_detail(articles_id: int):
    try:
        article_name = ARTICLES[articles_id]
    except KeyError:
        raise NotFound(f'Article #{articles_id} not found')
    return render_template('articles/details.html', articles_id=articles_id, articles=ARTICLES)
