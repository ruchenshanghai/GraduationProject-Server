#coding=utf-8


from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_token = Column(VARCHAR(100), unique=True)
    location = Column(VARCHAR(255))
    business = Column(VARCHAR(255))
    sex = Column(VARCHAR(255))
    employment = Column(VARCHAR(255))
    education = Column(VARCHAR(255))
    username = Column(VARCHAR(255))
    url = Column(VARCHAR(255))
    agrees = Column(Integer)
    thanks = Column(Integer)
    asks = Column(Integer)
    answers = Column(Integer)
    posts = Column(Integer)
    followees = Column(Integer)
    followers = Column(Integer)
    hashId = Column(VARCHAR(255))

    def __getitem__(self, k):
        if k == 'location':
            return self.location
        elif k == 'business':
            return self.business
        elif k == 'sex':
            return self.sex
        elif k == 'employment':
            return self.employment
        elif k == 'education':
            return self.education
        elif k == 'username':
            return self.username
