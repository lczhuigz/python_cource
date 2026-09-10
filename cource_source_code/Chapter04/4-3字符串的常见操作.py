# ++++++++++   4.4.1 字符串的查找与替换   ++++++++++
# words = '与其临渊羡鱼，不如退而结网。'
# result_one = words.find('鱼')      	# 从整个字符串中查找子串'鱼'
# print(result_one)
# result_two = words.find('鱼', 6)   	# 从索引6的位置开始查找子串'鱼'
# print(result_two)

# string = "All things Are difficult before they Are easy."
# new_string = string.replace("Are", "are")   		# 不指定替换次数
# print(new_string)
#
# new_string = string.replace('Are', 'are', 1)    # 指定替换次数
# print(new_string)


# ++++++++++   4.4.2 字符串的分割与拼接   ++++++++++
# string_example = "The more efforts you make, the more fortune you get."
# print(string_example.split())        	#根据空格分割字符串
# print(string_example.split('m'))	 	#根据字母m分割字符串
# print(string_example.split('e', 2)) 	#根据字母e分割字符串，并且分割两次

# symbol = '*'
# world = 'Python'
# print(symbol.join(world))

# start = 'Py'
# end = 'thon'
# print(start + end)


# ++++++++++   4.4.3 删除字符串的指定字符   ++++++++++
# old_string = '  Life is short, Use Python !  '
# strip_str = old_string.strip()              			# 删除字符串头部和尾部的空格
# lstrip_str = old_string.lstrip()            		# 删除字符串头部的空格
# rstrip_str = old_string.rstrip()                 	# 删除字符串尾部的空格
# print(f'strip()方法：{strip_str}】')
# print(f'lstrip()方法：{lstrip_str}】')
# print(f'rstrip()方法：{rstrip_str}】')


# ++++++++++   4.4.4 字符串大小写转换   ++++++++++
# old_string = 'hello woRld'
# upper_str = old_string.upper()          		# 将字符串的字母转换为大写字母
# lower_str = old_string.lower()          		# 将字符串的字母转换为小写字母
# cap_str = old_string.capitalize()      		# 将字符串的首字母转换为大写字母
# title_str = old_string.title()          		# 将每个单词的首字母转换为大写字母
# print(f'upper()方法：{upper_str}')
# print(f'lower()方法：{lower_str}')
# print(f'capitalize()方法：{cap_str}')
# print(f'title()方法：{title_str}')


# ++++++++++   4.4.5 字符串对齐   ++++++++++
# sentence = 'hello world'
# center_str = sentence.center(13,'-')  	#字符串的长度为13，居中显示，使用-填充
# ljust_str = sentence.ljust(13, '*')   		#字符串的长度为13，左对齐，使用*填充
# rjust_st = sentence.rjust(13, '%')    		#字符串的长度为13，右对齐，使用%填充
# print(f"居中显示：{center_str}")
# print(f"左对齐显示：{ljust_str}")
# print(f"右对齐显示：{rjust_st}")
