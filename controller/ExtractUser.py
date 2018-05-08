# coding=utf-8

import sys
from sqlalchemy import desc
from model.DBSession import DBsession
from model.ParsedUser import ParsedUser

reload(sys)
sys.setdefaultencoding('utf8')


def get_best_answer_user_list_by_topic(topic_list):
    session = DBsession()
    user_list = []
    result_list = []
    for pt in topic_list:
        for pu in session.query(ParsedUser).filter(ParsedUser.best_answerer.like('%' + bytes(pt['id']) + '%')).order_by(
                desc(ParsedUser.follower_count)):
            user_list.append(pu.as_dict())
    id_list = []
    for user in user_list:
        if user['id'] not in id_list:
            id_list.append(user['id'])
            result_list.append(user)
    return sorted(result_list, key=lambda k: (k['answer_count'] + (k['articles_count'] * 100) + k['follower_count'] + k['following_count'] + k['question_count'] + k['thanked_count'] + k['voteup_count']), reverse=True)