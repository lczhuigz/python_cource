# ++++++++++   3.1.1 if语句   ++++++++++
# score = 88
# if score >= 60:
#     print("考试及格！")


# ++++++++++   3.1.2 if-else语句   ++++++++++
# score = 88
# if score >= 60:
#     print("考试及格！")
# else:
#     print("考试不及格！")

# score = 55
# if score >= 60:
#     print("考试及格！")
# else:
#     print("考试不及格！")


# ++++++++++   3.1.3 if-elif-else语句   ++++++++++
# score = 88
# if score >= 85:
#     print("优秀")
# elif 75 <= score < 85:
#     print("良好")
# elif 60 <= score < 75:
#     print("中等")
# else:
#     print("差")


# ++++++++++   3.1.4 if 嵌套   ++++++++++
# year = 2024      # 年份
# month = 2         # 月份
# if month in  [1, 3, 5, 7, 8, 10, 12]: 	# 判断月份是否为1、3、5、7、8、10、12
#     print("%d月有 31 天 " % month)
# elif month in [4, 6, 9, 11]:          	# 判断月份是否为4、6、9、11
#     print("%d月有 30 天 " % month)
# elif month == 2:                        	# 判断月份是否为2月
#     # 判断年份是否为闰年
#     if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#         print("%d年%d月有29天" % (year, month))
#     else:
#         print("%d年%d月有28天" % (year, month))





