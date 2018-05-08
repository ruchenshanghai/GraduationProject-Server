# coding=utf-8

import sys
import json
from sqlalchemy import desc
from model.DBSession import DBsession
from model.ParsedUser import ParsedUser
from model.ParsedAnswer import ParsedAnswer
from model.ParsedTopic import ParsedTopic

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


def _get_topic_list_by_id_list(id_list):
    session = DBsession()
    _topic_list = []
    for pt in session.query(ParsedTopic).filter(ParsedTopic.id.in_(id_list)).order_by(desc(ParsedTopic.location)):
        _topic_list.append(pt.as_dict())
    return _topic_list


def parse_user_by_id(id):
    session = DBsession()
    _parsed_user = session.query(ParsedUser).filter(ParsedUser.id == id).first()
    _parsed_user = _parsed_user.as_dict()
    _parsed_answers = []
    for pa in session.query(ParsedAnswer).filter(ParsedAnswer.user_id == id).order_by(desc(ParsedAnswer.voteup_count)):
        _parsed_answers.append(pa.as_dict())
    _parsed_user['answer_list'] = _parsed_answers

    if _parsed_user['business_id']:
        _business = _get_topic_list_by_id_list([_parsed_user['business_id']])
        if len(_business) == 1:
            _parsed_user['business'] = _business[0]

    if _parsed_user['best_answerer']:
        _best_id_list = json.loads(_parsed_user['best_answerer'])
        _topic_list = _get_topic_list_by_id_list(_best_id_list)
        _parsed_user['best_list'] = _topic_list
    else:
        _parsed_user['best_answerer'] = []

    if _parsed_user['locations']:
        _location_id_list = json.loads(_parsed_user['locations'])
        _topic_list = _get_topic_list_by_id_list(_location_id_list)
        _parsed_user['location_list'] = _topic_list
    else:
        _parsed_user['location_list'] = []

    if _parsed_user['educations']:
        _major_id_list = []
        _school_id_list = []
        _education_list = json.loads(_parsed_user['educations'])
        for education in _education_list:
            if education['major_id'] != 0 and education['major_id'] not in _major_id_list:
                _major_id_list.append(education['major_id'])
            if education['school_id'] != 0 and education['school_id'] not in _school_id_list:
                _school_id_list.append(education['school_id'])
        _topic_list = _get_topic_list_by_id_list(_major_id_list)
        _parsed_user['major_list'] = _topic_list
        _topic_list = _get_topic_list_by_id_list(_school_id_list)
        _parsed_user['school_list'] = _topic_list
    else:
        _parsed_user['major_list'] = []
        _parsed_user['school_list'] = []

    if _parsed_user['employments']:
        _company_id_list = []
        _job_id_list = []
        _employment_list = json.loads(_parsed_user['employments'])
        for employment in _employment_list:
            if employment['company_id'] != 0 and employment['company_id'] not in _company_id_list:
                _company_id_list.append(employment['company_id'])
            if employment['job_id'] != 0 and employment['job_id'] not in _job_id_list:
                _job_id_list.append(employment['job_id'])
        _topic_list = _get_topic_list_by_id_list(_company_id_list)
        _parsed_user['company_list'] = _topic_list
        _topic_list = _get_topic_list_by_id_list(_job_id_list)
        _parsed_user['job_list'] = _topic_list
    else:
        _parsed_user['company_list'] = []
        _parsed_user['job_list'] = []

    return _parsed_user