from blog.app import create_app, db

app = create_app()


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('--- Done ---')


@app.cli.command('create-users')
def create_users():
    from blog.models.user import User

    admin = User(username='admin', is_staff=True)
    pavel = User(username='pavel')
    pmtkachev = User(username='pmtkachev')

    db.session.add(admin)
    db.session.add(pavel)
    db.session.add(pmtkachev)

    db.session.commit()

    print('--- Done create users ---')


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            debug=True,
            )
