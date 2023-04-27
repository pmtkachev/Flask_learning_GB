import os

from blog.app import app, db


@app.cli.command('create-admin')
def create_admin():
    from blog.models.user import User

    admin = User(username='admin', is_staff=True)
    admin.password = os.environ.get('ADMIN_PASSWORD') or 'adminpass'

    db.session.add(admin)
    db.session.commit()

    print('--- Done create admin ---')


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            debug=True,
            )
