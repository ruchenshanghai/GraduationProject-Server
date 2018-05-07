# coding=utf-8

from sqlalchemy import Column, Integer, VARCHAR, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ParsedTopic(Base):
    __tablename__ = 'parsed_topic'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(VARCHAR(255), unique=True)
    avatar_url = Column(VARCHAR(255))
    introduction = Column(Text)
    location = Column(Integer)
    school = Column(Integer)
    major = Column(Integer)
    company = Column(Integer)
    business = Column(Integer)
    job = Column(Integer)

    def __init__(self, id, name, avatar_url, introduction, location, school, major, company, business, job):
        self.id = id
        self.name = name
        self.avatar_url = avatar_url
        self.introduction = introduction
        self.location = location
        self.school = school
        self.major = major
        self.company = company
        self.business = business
        self.job = job

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
