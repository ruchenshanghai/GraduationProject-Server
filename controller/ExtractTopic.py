# coding=utf-8

import sys
import jieba
import jieba.analyse
from sqlalchemy import desc
from model.DBSession import DBsession
from model.ParsedTopic import ParsedTopic
from ExtractUser import get_best_answer_user_list_by_topic

reload(sys)
sys.setdefaultencoding('utf8')


def _get_topic_list_by_tags(tag_list):
    session = DBsession()
    topic_list = []
    for pt in session.query(ParsedTopic).filter(ParsedTopic.name.in_(tag_list)).order_by(desc(ParsedTopic.location)):
        topic_list.append(pt.as_dict())
    return topic_list


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
    tag_list = jieba.cut(txt, cut_all=True)
    tag_list = [word.encode('utf-8') for word in list(tag_list)]
    tag_list = [word for word in list(tag_list) if word not in stop_list]

    _result['topic_list'] = _get_topic_list_by_tags(tag_list)
    _result['user_list'] = get_best_answer_user_list_by_topic(_result['topic_list'])
    return _result


def get_topic_by_id(id):
    session = DBsession()
    target_topic = session.query(ParsedTopic).filter(ParsedTopic.id == id).first()
    if target_topic:
        return target_topic.as_dict()
    return None

