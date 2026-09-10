# ++++++++++   7.5.1 基于维度的数据分类   ++++++++++
# 成都,重庆,杭州,西安,武汉,苏州,郑州,南京,天津,长沙,东莞,宁波,昆明,合肥,青岛

# "高三一班考试成绩":[
# 					    {"姓名": "小红",
# 					     "语文": "124",
# 					     "数学": "137",
# 					     "英语": "145",
# 					     "理综": "260" };
# 					    {"姓名": "小明",
# 					     "语文": "116",
# 					     "数学": "143",
# 					     "英语": "139",
# 					     "理综": "263" };
# 					     ……
# 				      ]


# ++++++++++   7.5.2 一维数据和二维数据的存储与读写   ++++++++++
# csv_file = open('score.csv')
# lines = []
# for line in csv_file:
#    line = line.replace('\n', '')
#    lines.append(line.split(','))
# print(lines)
# csv_file.close()


# csv_file = open('score.csv')
# file_new = open('count.csv', 'w+')
# lines = []
# for line in csv_file:
#     line = line.replace('\n', '')
#     lines.append(line.split(','))
# # 添加表头字段
# lines[0].append('总分')
# # 添加总分
# for i in range(len(lines) - 1):
#     idx = i + 1
#     sun_score = 0
#     for j in range(len(lines[idx])) :
#         if lines[idx][j].isnumeric():
#             sun_score += int(lines[idx][j])
#     lines[idx].append(str(sun_score))
# for line in lines:
#     print(line)
#     file_new.write(','.join(line) + '\n')
# csv_file.close()
# file_new.close()


# ++++++++++   7.5.3 多维数据的格式化   ++++++++++
# "高三一班考试成绩":[
# 					     {"姓名": "小红",
# 					      "语文": "124",
# 					      "数学": "137",
# 					      "英语": "145",
# 					      "理综": "260" };
# 					     {"姓名": "小明",
# 					      "语文": "116",
# 					      "数学": "143",
# 					      "英语": "139",
# 					      "理综": "263" };
# 					      ……
# 				      ]


# <高三一班考试成绩>
# 	<姓名>小红</姓名><语文>124</语文><数学>137<数学/><英语>145<英语/><理综>260<理综/>
# 	<姓名>小明</姓名><语文>116</语文><数学>143<数学/><英语>139<英语/><理综>263<理综/>
# 	……
# </高三一班考试成绩>
