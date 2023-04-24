import os
from flask import Flask, render_template
from flask_migrate import Migrate

from blog.models import User
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db
from blog.views.auth import login_manager, auth_app

migrate = Migrate()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(f'blog.configs.DevConfig')
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth_app.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app):
    app.register_blueprint(users_app, url_prefix='/users')
    app.register_blueprint(articles_app, url_prefix='/articles')
    app.register_blueprint(auth_app, url_prefix='/auth')
