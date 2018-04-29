#coding=utf-8


from sqlalchemy import Column, Integer, VARCHAR, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ParsedUser(Base):
    __tablename__ = 'parsed_user'
    id = Column(Integer, primary_key=True)
    user_token = Column(VARCHAR(100), unique=True)
    word_list = Column(Text)
    agrees = Column(Integer)
    thanks = Column(Integer)
    asks = Column(Integer)
    answers = Column(Integer)
    posts = Column(Integer)
    followees = Column(Integer)
    followers = Column(Integer)
    hashId = Column(VARCHAR(255))

    def __getitem__(self, k):
        if k == 'id':
            return self.id
        elif k == 'word_list':
            return self.word_list
        elif k == 'user_token':
            return self.user_token
        elif k == 'agrees':
            return self.agrees
        elif k == 'thanks':
            return self.thanks
        elif k == 'asks':
            return self.asks
        elif k == 'posts':
            return self.posts
        elif k == 'answers':
            return self.answers
        elif k == 'followees':
            return self.followees
        elif k == 'followers':
            return self.followers
        elif k == 'hashId':
            return self.hashId
