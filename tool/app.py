# coding=utf-8

from model.DBSession import DBsession
import jieba
import jieba.analyse
import json

# session = DBsession()
# wordlList = []
# STOP_WORD_LIST = [line.rstrip() for line in open('./resource/stop_word.txt')]
# for user in session.query(User).all():
#     _temp_wordlist = []
#     _temp_after_word_list = []
#     for key in ['location', 'business', 'sex', 'employment', 'education', 'username']:
#         if user[key]:
#             content = user[key].strip().replace('\n', '').replace(' ', '').replace('\t', '').replace('\r', '')
#             seg_list = jieba.cut(content, cut_all=True)
#             for seg in seg_list:
#                 if seg not in STOP_WORD_LIST:
#                     _temp_after_word_list.append(seg)
#             _temp_wordlist.append(' '.join(_temp_after_word_list))
#     if len(_temp_wordlist) > 0:
#         for word in _temp_wordlist:
#             print word.encode('utf-8')
#         wordlList.append(_temp_wordlist)
# f = open('./resource/plain_corpus.txt', 'w')
# f.write(str(wordlList))
# f.close()
# new_url = Url(id=12343210, md5_url='测试中文test')
# session.add(new_url)
# session.commit()
# session.close()

# for url in session.query(Url).filter(Url.id == 12343210).all():
#     print(url.id)
#     if url.md5_url:
#         # seg_list = jieba.cut(url.md5_url, cut_all=True)
#         # for seg in seg_list:
#         #     print (seg)
#         print(url.md5_url.encode('utf-8'))

from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

# f = open('./resource/plain_corpus.txt')
# corpus_line = f.readline()
# f.close()
# temp_list = corpus_line[1:-1].split("'], [u'")
# corpus_list = []
# for list in temp_list:
#     words_lists = list.split("', u'")
#     user = []
#     for words in words_lists:
#         word_list = words.split(' ')
#         profile = []
#         for word in word_list:
#             profile.append(word.decode('unicode-escape').encode('utf-8'))
#             print word.decode('unicode-escape').encode('utf-8')
#         user.append(profile)
#     corpus_list.append(user)
# out_str = json.dumps(corpus_list, ensure_ascii=False)
# wf = open('./resource/corpus.json', 'w')
# wf.write(out_str)
# wf.close()


# f = open('./resource/corpus.json')
# txt = f.readline()
# corpus_list = json.loads(txt)
# word_list = []
# for user in corpus_list:
#     for profile in user:
#         for word in profile:
#             word_list.append(word)


test_str = "《新龙门客栈》里，金镶玉出场时，100分钟的电影已近1/4了。一出场，便是个性感的俯卧姿势，以及一句简单的笛声：先下行，再上撩，这是她的主题曲。电影前1/4，金戈铁马，关山万里，兵甲铿锵；唯独她出场，是清越的管乐。以及，张曼玉发丝纠缠、脖颈间香汗淋漓的背影；一个故作矜持的回首；以及，被按倒后，本电影最性感的一幕：汗水淋漓。张曼玉的娃娃脸面相，演金镶玉恰好：带点娇憨，带点天真，所以之后杀人不眨眼，才显出对比来。刚还软玉温香，忽然相思柳叶镖杀人翻脸无情，这就是金镶玉的出场。惊艳而急促，捉摸不透。然而也没那么难以捉摸。之后，金镶玉便显出她的一点执念：林青霞的邱莫言来了，金镶玉一句“不正眼看我的，都不是男人”；这是她的自信，也是对男人的鄙夷；之后她去窥看邱莫言洗澡，二人打将起来，也是她的心思：金镶玉讨厌伪装，非得揭穿了才好。所以她得意对邱莫言说：“可是我看你比你看我看得通透啊！”之后又自鸣得意：“是不是连蜡烛都没点过啊？”上了房顶，听见周淮安的笑声，金镶玉大怒，就光着身子站起来指：“哪里来的蜡烛啊！？”金镶玉对男性的态度，从她骂人就听得出来，“去你爹的！”她性子刚硬，而且总要坐得比男性高，没事就桌子上叠起椅子来，俯视男人们。金镶玉讨厌伪装，讨厌男性权威。于是用妖娆多变或粗直凶恶对待男性权威——她不是不知道男人不会把她的话当真，她无所谓，她的许多妖娆，只是不屑罢了。所以在她不动情时，曲子是“喝碗酒嘞撒泡尿嘞，大漠里的汉子爱美酒！”就这么粗直，就这么不屑。周淮安来找她谈事，讨好她说是上房，金镶玉很直白地：“什么上房？土房子罢了。”周淮安再讨好她，问她“这是什么花？很精致。”金镶玉恶声恶气道：“萝卜花啊！还能是雪莲花？”她是不相信世上有纯洁无瑕之事的，样样摆起的架势都要揭穿。但她到底对周淮安心动了，于是故作柔弱地划伤了手，眼珠一转，哎呀一声。就在她故意划伤手的一瞬间（张曼玉眼神与手势的配合精妙绝伦），那缕清越的笛音又响了。东厂三大档头到来后，金镶玉方显出其为本片第一重要角色的价值。如果没有她的摇摆、莫测与斡旋，东厂与周淮安一伙早已开打；就是忌惮着她这点摇摆，双方还得场面上你来我往；金镶玉也就虚与委蛇，未语先笑；说些桃花运、割羊肉之类不相干的话。终于周淮安发现了她的地下屠宰坊，图穷匕见，黑店本质揭露了。金镶玉望着周淮安。这是她本片第一次没有表情的瞬间。大概因为这一刻，彼此坦诚相见，没有秘密了，不用假装了吧？我觉得那一刻，张曼玉美极了，丰富极了。这个没有表情的瞬间，凝聚了一切。信任，不信任；爱，恨；贪欢，利益，她自己过往的经历，自怜。她看着周淮安，不需要任何矫饰了。可以谈条件了——真的要谈条件吗？之后是著名的婚宴对打。金镶玉在听见黑子说东厂动手杀人后，瞳孔连续缩放两次，愤怒出手，杀了陆小川，又合力杀了贾廷。已经撕破脸皮，不用假装柔情蜜意了。周淮安旁若无人地跟邱莫言谈情说爱。金镶玉继续冷笑：看惯人情，她是不相信这些所谓真情的。只到听见周淮安说笛子身外之物时，她才恼了，说了句戳心的话：“你们这些过客，达到目的就走，我们都一样，无情无义！”这句话说来狠辣，又何尝不是她的自我保护？她长久以来对虚伪的不齿，也就出于此。但嘴硬心软，生死之际，乱箭如雨而来，她还是要将周淮安的笛子还给邱莫言，而且倔强地：“你的笛子，别人施舍的东西，我不要！”最后大战曹少钦，尘埃落定。曹少钦一死，金镶玉第一句话是：“周淮安？”而周淮安在昏迷中，咳了一声，道：“莫言！”金镶玉放下了心，倒了地；与此同时，怅然若失地，咬了一下牙。她是爱周淮安的，也再次确认，周淮安并不怎么爱她。电影最后，周淮安走了。还说了，“下一批过客来时，你自会忘记我的。”本来到此结束，也就可以了。的确，金镶玉可以继续做她的老板娘，继续戴着巧笑嫣然的面具，杀人越货，勾引自己喜欢的人，继续下去。然而金镶玉回去，将客栈烧了，去找周淮安了。她何尝不知道周淮安爱的依然是邱莫言，她最后怅然地一咬牙时已经知道了；她何尝不知道这么去追着周淮安未必有好结果，她是最懂得用面具来自我保护，同时揭穿他人虚伪的女人啊。但她去了。因为这是她自己的选择。她在无情无义的沙漠里玩弄人情左右逢源揭穿虚伪，是因为她不相信世上还有真东西；但一旦发现还有点真的，她就义无反顾地去了。就像那一缕清越的笛声，其实无遮无拦，纯粹之极。张曼玉的金镶玉演得，真是好。她的娃娃脸带点娇憨与天真，让她笑得甜又迷人；她是全电影唯一一个摇摆不定，但又有所成长的人物——曹少钦要杀人，三大档头要捉人，周淮安和邱莫言一出场就生死相许了真爱，只有她在变化，在摇摆，在成长，在怒骂，在欢笑，在揭穿了一切虚伪后，做了自己愿意做的选择。在其他人布衣缓带城府深藏的轻柔姿态下，张曼玉那些夸张又迷人的肢体语言，是这部电影里最动人的时刻。她制造一切悬念，制造一切戏剧性，而且本人的情绪，从开头的自以为是自得其乐，到中间的动荡，到末尾重新平和。本片其实也就是由她情绪主导的。她的变幻又纯粹，是本片真正的灵魂：一个最纯粹的女人，仿佛她自己就是变幻不定的沙漠本身。龙门客栈在哪里？金镶玉的身上，就是龙门客栈。"

tags = jieba.analyse.extract_tags(test_str, topK=10, withWeight=True)
for tag in tags:
    print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))


# seg_list = jieba.lcut(test_str, cut_all=False)
# for seg in seg_list:
#     print (seg)
# vectorizer = CountVectorizer()
# transformer = TfidfTransformer()
# tfidf = transformer.fit_transform(vectorizer.fit_transform(seg_list))
# words = vectorizer.get_feature_names()  # 所有文本的关键字
# weight = tfidf.toarray()
#
# n = 5  # 前五位
# for (title, w) in zip(word_list, weight):
#     # print u'{}:'.format(title)
#     # 排序
#     loc = np.argsort(-w)
#     for i in range(n):
#         print u'-{}: {} {}'.format(str(i + 1), words[loc[i]], w[loc[i]])
