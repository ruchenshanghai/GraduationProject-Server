# coding=utf-8

from sqlalchemy import Column, Integer, VARCHAR, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ParsedQuestion(Base):
    __tablename__ = 'parsed_question'
    id = Column(Integer, primary_key=True, unique=True)
    content = Column(Text)
    followers = Column(Integer)
    viewers = Column(Integer)
    comments = Column(Integer)
    answers = Column(Integer)
    keywords = Column(VARCHAR(1024))

    def __init__(self, id, content, followers, viewers, coments, answers, keywords):
        self.id = id
        self.content = content
        self.followers = followers
        self.viewers = viewers
        self.comments = coments
        self.answers = answers
        self.keywords = keywords

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
