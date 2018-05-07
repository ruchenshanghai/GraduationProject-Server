#coding=utf-8

from sqlalchemy import Column, Integer, VARCHAR, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ParsedUser(Base):
    __tablename__ = 'parsed_user'
    id = Column(VARCHAR(255), primary_key=True, unique=True)
    avatar_url = Column(VARCHAR(255))
    user_token = Column(VARCHAR(255), unique=True)
    name = Column(VARCHAR(255))
    headline = Column(VARCHAR(1024))
    following_count = Column(Integer)
    answer_count = Column(Integer)
    question_count = Column(Integer)
    voteup_count = Column(Integer)
    thanked_count = Column(Integer)
    follower_count = Column(Integer)
    articles_count = Column(Integer)
    identity = Column(VARCHAR(255))
    business_id = Column(Integer)
    locations = Column(Text)
    educations = Column(Text)
    best_answerer = Column(Text)
    employments = Column(Text)
    is_advertiser = Column(Boolean)
    is_org = Column(Boolean)
    gender = Column(Boolean)

    def __init__(self, id, avatar_url, user_token, name, headline, following_count, answer_count, question_count, voteup_count, thanked_count, follower_count, articles_count, identity, business_id, locations, educations, best_answerer, employments, is_advertiser, is_org, gender):
        self.id = id
        self.avatar_url = avatar_url
        self.user_token = user_token
        self.name = name
        self.headline = headline
        self.following_count = following_count
        self.answer_count = answer_count
        self.question_count = question_count
        self.voteup_count = voteup_count
        self.thanked_count = thanked_count
        self.follower_count = follower_count
        self.articles_count = articles_count
        self.identity = identity
        self.business_id = business_id
        self.locations = locations
        self.educations = educations
        self.best_answerer = best_answerer
        self.employments = employments
        self.is_advertiser = is_advertiser
        self.is_org = is_org
        self.gender = gender

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
