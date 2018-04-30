# coding=utf-8


from model.DBSession import DBsession
from model import ParsedUser
import json


f = open('../resource/user_corpus_list.json')
txt = f.readline()
user_list= json.loads(txt)
print len(user_list)
session = DBsession()
for index, _temp_user in enumerate(user_list):
    _temp_parsed_user = ParsedUser(word_list=_temp_user['word_list'].encode('utf-8'), user_token=_temp_user['user_token'].encode('utf-8'), agrees=_temp_user['agrees'], thanks=_temp_user['thanks'], asks=_temp_user['asks'], answers=_temp_user['answers'], posts=_temp_user['posts'], followees=_temp_user['followees'], followers=_temp_user['followers'], hashId=_temp_user['hashId'].encode('utf-8'))
    print '%d %s' % (index,  _temp_user['word_list'].encode('utf-8'))
    session.add(_temp_parsed_user)
    if index % 1000 == 0:
        session.flush()
session.commit()
session.close()
print 'ok'
