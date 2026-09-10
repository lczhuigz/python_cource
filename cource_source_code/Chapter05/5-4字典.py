# ++++++++++   5.6.1 创建字典   ++++++++++
# d1 = {}										    # 创建空字典
# d2 = {'A': '123', 'B': '135', 'C': '680'}	    # 创建字典，键的类型都是字符串
# d3 = {'A': 123, 12: 'python'}                 	# 创建字典，键的类型不同
#
# d4 = dict()									# 创建空字典
# d5 = dict({'A': '123', 'B': '135'})			# 创建非空字典


# ++++++++++   5.6.2 字典的访问   ++++++++++
# print(d2['A'])
# print(d3[12])

# print(d2.get('A'))
# print(d3.get(12))

# dic = {'name': '小明', 'age':23, 'height':185}
# print(dic.keys())								# 利用keys()获取所有键
# print(dic.values())								# 利用values()获取所有值
# print(dic.items())								# 利用items()获取所有元素
# #
# for key in dic.keys():
#     print(key)


# ++++++++++   5.6.3 字典元素的添加和修改   ++++++++++
# add_dict = {'name': '小明', 'age':23, 'height':185}
# add_dict['sco'] = 98									# 添加元素
# print(add_dict)
#
# add_dict.update(weight=98)					# 添加一个元素
# print(add_dict)
# add_dict.update(stu_id=1, address='北京')	   	# 添加多个元素
# print(add_dict)

# modify_dict = {'stu1': '小明', 'stu2': '小刚', 'stu3': '小兰'}
# modify_dict.update(stu2='小强')   		#使用update()方法修改元素
# modify_dict['stu3'] = '小婷'       		# 通过指定键修改元素
# print(modify_dict)


# ++++++++++   5.6.4 字典元素的删除   ++++++++++
# per_info = {'001': '张三', '002': '李四',
#               '003': '王五', '004': '赵六'}
# print(per_info.pop('001'))            # 使用pop()删除指定键为001的元素
# print(per_info)

# per_info = {'001': '张三', '002': '李四',
#               '003': '王五', '004': '赵六'}
# print(per_info.popitem())             		#使用popitem()方法随机删除元素
# print(per_info)

# per_info = {'001': '张三', '002': '李四',
#               '003': '王五', '004': '赵六'}
# per_info.clear()                        # 使用clear()方法清空字典中的元素
# print(per_info)


# ++++++++++   5.6.5 字典推导式   ++++++++++
# old_dict = {'name': '小明', 'age':23, 'height':185}
# new_dict = {value:key for key, value in old_dict.items()}
# print(new_dict)

