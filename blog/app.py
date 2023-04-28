from flask import Flask
from flask_migrate import Migrate

from blog.security import flask_bcrypt
from blog.models import User
from blog.models.database import db
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.views.auth import login_manager, auth_app


def register_blueprints(app):
    app.register_blueprint(users_app, url_prefix='/users')
    app.register_blueprint(articles_app, url_prefix='/articles')
    app.register_blueprint(auth_app, url_prefix='/auth')


app = Flask(__name__)
app.config.from_object(f'blog.configs.DevConfig')
db.init_app(app)

migrate = Migrate(app, db)
flask_bcrypt.init_app(app)

register_blueprints(app)

login_manager.login_view = 'auth_app.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
