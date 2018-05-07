# coding=utf-8

from model.DBSession import DBsession
import jieba
import jieba.analyse
import json

session = DBsession()
userList = []
STOP_WORD_LIST = [line.rstrip() for line in open('../resource/stop_word.txt')]
# for user in session.query(User).all():
# session.commit()
session.close()
# f = open('./resource/user_corpus_list.json', 'w')


# with open('../resource/user_corpus_list.json', 'w') as f:
#     for chunk in json.JSONEncoder().iterencode(userList):
#         f.write(chunk)
#     f.close()

# for url in session.query(Url).filter(Url.id == 12343210).all():
#     print(url.id)
#     if url.md5_url:
#         # seg_list = jieba.cut(url.md5_url, cut_all=True)
#         # for seg in seg_list:
#         #     print (seg)
#         print(url.md5_url.encode('utf-8'))
