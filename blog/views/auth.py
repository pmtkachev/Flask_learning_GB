from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, LoginManager

from blog.models import User

auth_app = Blueprint('auth_app', __name__)

login_manager = LoginManager()


@auth_app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')

    username = request.form.get('username')
    if not username:
        return render_template('auth/login.html', error='username not passed')

    user = User.query.filter_by(username=username).first()
    if user is None:
        return render_template('auth/login.html', error=f'no user {username} found')

    login_user(user)
    return redirect(url_for('articles_app.list'))


@auth_app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_app.login'))
