# 将输入的英文内容转换为小写
text = input("请输入英文内容：").lower()

# 将文本中的逗号和句号替换为空格
text = text.replace(",", " ").replace(".", " ")

# 根据空格将英文内容拆分为单独的单词，存储在一个列表中
words = text.split()

# 根据列表创建集合，以获取唯一单词
unique_words = set(words)

# 统计每个单词出现的次数，并将单词及其出现次数保存到字典中
word_count = {}
for word in unique_words:
    word_count[word] = words.count(word)

# word_count = {}
# for word in words:
#     if word not in word_count:
#         word_count[word] = 1
#     else:
#         word_count[word] += 1

print("--------------------")
# 遍历字典，输出每个单词出现的次数
for word in word_count:
    print(f"{word:10}: {word_count[word]}次")
