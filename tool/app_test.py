# coding=utf-8

from model.DBSession import DBsession
from model.User import User
from model.ParsedUser import ParsedUser
import jieba
import jieba.analyse
import json

session = DBsession()
userList = []
STOP_WORD_LIST = [line.rstrip() for line in open('./resource/stop_word.txt')]
# for user in session.query(User).all():
for index, user in enumerate(session.query(User).all()):
    _temp_user = {}
    _temp_wordlist = []
    for key in ['location', 'business', 'sex', 'employment', 'education', 'username']:
        if user[key]:
            content = user[key].strip().replace('\n', '').replace(' ', '').replace('\t', '').replace('\r', '')
            seg_list = jieba.analyse.extract_tags(content, topK=20, withWeight=True)
            for seg in seg_list:
                _temp_wordlist.append(seg)
                # if seg[0] not in STOP_WORD_LIST:
                #     _temp_wordlist.append(seg)
    if len(_temp_wordlist) > 0:
        for word in _temp_wordlist:
            print '%d %s' % (index, word[0].encode('utf-8'))
        _temp_user['word_list'] = json.dumps(_temp_wordlist, ensure_ascii=False)
        _temp_user['user_token'] = user.user_token
        _temp_user['agrees'] = user.agrees
        _temp_user['thanks'] = user.thanks
        _temp_user['asks'] = user.asks
        _temp_user['answers'] = user.answers
        _temp_user['posts'] = user.posts
        _temp_user['followees'] = user.followees
        _temp_user['followers'] = user.followers
        _temp_user['hashId'] = user.hashId
        userList.append(_temp_user)
        # _temp_parsed_user = ParsedUser(word_list=_temp_user['word_list'], user_token=_temp_user['user_token'], agrees=_temp_user['agrees'], thanks=_temp_user['thanks'], asks=_temp_user['asks'], answers=_temp_user['answers'], posts=_temp_user['posts'], followees=_temp_user['followees'], followers=_temp_user['followers'], hashId=_temp_user['hashId'])
        # session.add(_temp_parsed_user)
# session.commit()
session.close()
# f = open('./resource/user_corpus_list.json', 'w')


with open('./resource/user_corpus_list.json', 'w') as f:
    for chunk in json.JSONEncoder().iterencode(userList):
        f.write(chunk)
    f.close()

# for url in session.query(Url).filter(Url.id == 12343210).all():
#     print(url.id)
#     if url.md5_url:
#         # seg_list = jieba.cut(url.md5_url, cut_all=True)
#         # for seg in seg_list:
#         #     print (seg)
#         print(url.md5_url.encode('utf-8'))
