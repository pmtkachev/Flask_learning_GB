from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from blog.models.database import db
from blog.models import Author, Article
from blog.forms.articles import CreateArticleForm

articles_app = Blueprint('articles_app', __name__)


@articles_app.route('/', endpoint='list')
@login_required
def articles_list():
    articles = Article.query.all()
    return render_template('articles/list.html', articles=articles)


@articles_app.route('/<int:articles_id>/', endpoint='details')
@login_required
def article_details(articles_id: int):
    article = Article.query.filter_by(id=articles_id).one_or_none()
    if article is None:
        raise NotFound
    return render_template('articles/details.html', articles_id=articles_id, article=article)


@articles_app.route('/create/', endpoint='create', methods=['GET', 'POST'])
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        article = Article(title=form.title.data.strip(),
                          text=form.text.data.strip())
        db.session.add(article)
        if current_user.author:
            article.author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author = author

        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception('Could not create new article!!!')
            error = 'Could not create article'
        else:
            return redirect(url_for('articles_app.details', articles_id=article.id))
    return render_template('articles/create.html', error=error, form=form)
