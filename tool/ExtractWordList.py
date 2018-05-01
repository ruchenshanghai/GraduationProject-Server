# coding=utf-8

import json
from model.DBSession import DBsession
from model import ParsedWord


# f = open('../resource/user_corpus_list.json')
# txt = f.readline()
# user_list= json.loads(txt)
# word_dict = {}
# for i, u in enumerate(user_list):
#     _word_list = json.loads(u['word_list'])
#     for w in _word_list:
#         print i, w[0].encode('utf-8'), w[1]
#         if word_dict.has_key(w[0].encode('utf-8')):
#             word_dict[w[0].encode('utf-8')] += w[1]
#         else:
#             word_dict[w[0].encode('utf-8')] = w[1]
#
# with open('../resource/word_list_simple_plus.json', 'w') as f:
#     for chunk in json.JSONEncoder(ensure_ascii=False).iterencode(word_dict):
#         f.write(chunk)
#     f.close()

f = open('../resource/word_list_recount.json')
txt = f.readline()
word_list= json.loads(txt)
session = DBsession()
for index, word in enumerate(word_list):
    _temp_key = word.encode('utf-8')
    print '%d %s  %d' % (index, _temp_key, word_list[word])
    _temp_parsed_word = ParsedWord(word=_temp_key, count=word_list[word])
    session.add(_temp_parsed_word)
session.commit()
session.close()
f.close()
print 'ok'