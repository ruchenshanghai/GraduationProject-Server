# coding=utf-8

import sys
from sqlalchemy import desc
from model.DBSession import DBsession
from model.ParsedQuestion import ParsedQuestion

reload(sys)
sys.setdefaultencoding('utf8')


def search_question_by_keyword(keyword):
    session = DBsession()
    question_list = []
    for pq in session.query(ParsedQuestion).filter(ParsedQuestion.keywords.like('%' + keyword + '%')).order_by(
            desc(ParsedQuestion.followers)):
        question_list.append(pq.as_dict())
    return question_list
