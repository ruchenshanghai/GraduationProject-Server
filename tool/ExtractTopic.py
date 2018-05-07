# coding=utf-8

import sys
import operator
import json
import jieba
import jieba.analyse
from sqlalchemy import desc
from model.DBSession import DBsession
from model.ParsedTopic import ParsedTopic
from model.ParsedUser import ParsedUser

reload(sys)
sys.setdefaultencoding('utf8')


def _get_topic_list_by_tags(tag_list):
    session = DBsession()
    topic_list = []
    for pt in session.query(ParsedTopic).filter(ParsedTopic.name.in_(tag_list)).order_by(desc(ParsedTopic.location)):
        topic_list.append(pt.as_dict())
    return topic_list


def _get_best_answer_user_list_by_topic(topic_list):
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
    # return result_list.sort(key=lambda k: (k.get('follower_count', 0)))



def extract_topic(txt, keyword_count):
    _result = {}
    _result['word_list'] = []
    _result['topic_list'] = []

    tags = jieba.analyse.extract_tags(txt, topK=keyword_count, withWeight=True)
    for tag in tags:
        _result['word_list'].append({
            'word': tag[0],
            'weight': tag[1]
        })

    stop_list = {}.fromkeys([line.strip() for line in open("../resource/stop_word.txt")])
    tag_list = []
    tag_list = jieba.cut(txt, cut_all=True)
    tag_list = [word.encode('utf-8') for word in list(tag_list)]
    tag_list = [word for word in list(tag_list) if word not in stop_list]

    # print json.dumps(result['word_list'], ensure_ascii=False)
    _result['topic_list'] = _get_topic_list_by_tags(tag_list)
    _result['user_list'] = _get_best_answer_user_list_by_topic(_result['topic_list'])
    # print json.dumps(result['topic_list'], ensure_ascii=False)
    return _result
