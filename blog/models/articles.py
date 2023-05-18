from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime, func
from sqlalchemy.orm import relationship

from blog.models.database import db
from .article_tag import article_tag_association_table


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship('Author', back_populates='article')
    title = Column(String(255), nullable=False, default='', server_default='')
    text = Column(Text, nullable=False, default='', server_default='')
    dt_created = Column(DateTime, default=datetime.utcnow(), server_default=func.now())
    tags = relationship(
        'Tag',
        secondary=article_tag_association_table,
        back_populates='articles'
    )
