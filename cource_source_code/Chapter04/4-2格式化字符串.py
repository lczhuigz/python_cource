# ++++++++++   4.2.1 使用%格式化字符串   ++++++++++
# value = 10
# format = '我今年%d岁。'
# print(format % value)

# value = '10'
# format = '我今年%d岁。'          	# 在字符串中插入用于格式化十进制数的格式符%d
# print(format % value)           	# 将%d替换为变量value的值

# name = '小明'
# age = 27
# address = '北京市昌平区'
# print('我叫%s，今年%d岁了，来自%s。' % (name, age, address))


# ++++++++++   4.2.2 使用format()方法格式化字符串   ++++++++++
# name = '小明'
# string = '我叫{}'
# print(string.format(name))

# name = '小明'
# age = 27
# # 字符串中插入了两个符号{}
# string = '我叫{}，今年{}岁了'
# # 使用format()方法格式化字符串，并指定两个真实数据
# print(string.format(name, age))

# name = '小明'
# age = 27
# # 字符串中插入两个符号{}，并在{}中指定编号
# string = '我叫{1}，今年{0}岁了'
# # 使用format()方法格式化字符串
# print(string.format(age, name))

# name = '小明'
# age = 27
# # 字符串中插入两个符号{}，并在{}中指定变量名
# string = '我叫{arg_one}，今年{arg_two}岁了'
# # 使用format()方法格式化字符串
# print(string.format(arg_one=name, arg_two=age))

# value = 3.141592653589793
# # 字符串中插入一个符号{}，并在{}中指定保留两位小数
# string = 'π的值为：{:.2f}'
# result = string.format(value)
# print(result)


# ++++++++++   4.2.3 使用f-string格式化字符串   ++++++++++
# name = '小明'
# age = 27
# string = f'我叫{name}，今年{age}岁了'
# print(string)

# num1 = 9
# num2 = 9
# string = f"{num1}×{num2}={num1 * num2}"
# print(string)

value = 3.141592653589793
print(f'π的值为：{value:.2f}.')

