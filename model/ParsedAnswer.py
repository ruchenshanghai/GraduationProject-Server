# coding=utf-8

from sqlalchemy import Column, Integer, VARCHAR, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ParsedAnswer(Base):
    __tablename__ = 'parsed_answer'
    id = Column(Integer, primary_key=True, unique=True)
    question_id = Column(Integer)
    user_id = Column(VARCHAR(255))
    voteup_count = Column(Integer)
    comment_count = Column(Integer)
    content = Column(Text)

    def __init__(self, id, question_id, user_id, voteup_count, comment_count, content):
        self.id = id
        self.question_id = question_id
        self.user_id = user_id
        self.voteup_count = voteup_count
        self.comment_count = comment_count
        self.content = content

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
