#coding=utf-8


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql

engine = create_engine('mysql+pymysql://root:@localhost:3306/graduation?charset=utf8')
# engine = create_engine('mysql+pymysql://root:@localhost:3306/zhihu?charset=utf')
DBsession = sessionmaker(bind=engine)

