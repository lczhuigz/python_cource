import jieba
# 获取小说的全部内容
file = open(r"xiyouji.txt", "rb")
string = file.read()
file.close()
# 统计词语及数量
words = jieba.lcut(string)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "行者" or word == "大圣" or word == "老孙":
        rword = "悟空"
    elif word == "师父" or word == "三藏" or word == "长老":
        rword = "唐僧"
    elif word == "悟净" or word == "沙和尚":
        rword = "沙僧"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
# 删除无意义的词语
excludes = {"一个", "那里", "怎么", "我们", "不知", "两个", "甚么",
              "只见", "不是","原来", "不敢", "闻言", "如何", "什么", "\r\n"}
for word in excludes:
    del counts[word]
# 按中文词语的出现次数排序
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
# 输出前10个中文词语及数量
for i in range(10):
    word, count = items[i]
    print(f"{word}      {count}次")
