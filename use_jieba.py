import jieba
from jieba import analyse
import json
from snownlp import SnowNLP
from pyhanlp import *

with open('data/coreEntityEmotion_train.txt', 'r') as f:   
    data = f.readline()
    data = json.loads(data)
print(data["coreEntityEmotions"])

s = SnowNLP(data["content"])
print("snowNLP", s.keywords(10))
# print(s.summary(3))
# print(s.sentiments)


print("jieba", jieba.analyse.textrank(data["content"], topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')))

print("HanLP" ,HanLP.extractKeyword(data["content"], 2))

    # while(data):
    #     data = json.loads(data)
    #     print(data['newsId'], len(data['coreEntityEmotions']))
    #     data = f.readline()
    # print(data.keys())
    # print(data['coreEntityEmotions'][0].keys())
# print(data.keys())
# print(type(data))
# print(data)
# for key in data:
#     print(key)

# print(data.keys())
# print(data.values())

# new = data.values()
# print(new)
