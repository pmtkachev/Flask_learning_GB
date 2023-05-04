import flask_bcrypt
from flask_login import UserMixin

from sqlalchemy import Column, String, Integer, Boolean, LargeBinary
from sqlalchemy.orm import relationship

from blog.models.database import db


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False, default='', server_default='')
    last_name = Column(String(100), nullable=False, default='', server_default='')
    email = Column(String(255), nullable=False, default='', server_default='', unique=True)
    is_staff = Column(Boolean, nullable=False, default=False)
    _password = Column(LargeBinary, nullable=True)
    author = relationship('Author', uselist=False, back_populates='user')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt.check_password_hash(self._password, password)

    def __repr__(self):
        return f'<User #{self.id} {self.username!r}>'
