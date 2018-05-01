#coding=utf-8


from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ParsedWord(Base):
    __tablename__ = 'parsed_word'
    id = Column(Integer, primary_key=True)
    word = Column(VARCHAR(100), unique=True)
    count = Column(Integer)

    def __getitem__(self, k):
        if k == 'id':
            return self.id
        elif k == 'word':
            return self.word
        elif k == 'count':
            return self.count
