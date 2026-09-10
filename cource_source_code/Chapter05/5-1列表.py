# ++++++++++   5.2.1 创建列表   ++++++++++
# list_one = []      					           # 创建空列表，没有任何元素
#
# list_two = ['p', 'y', 't', 'h', 'o', 'n'] 		# 列表中的元素类型均为字符串
# list_three = [1, 'a', '&', 2.3]  		   		    # 列表中的元素类型不同
# list_four = [1, 'a', '&', 2.3, list_three]		# 列表中嵌套了另一个列表
#
# # 创建空列表，结果为[]
# li_one = list()
# # 根据字符串创建列表，结果为['p', 'y', 't', 'h', 'o', 'n']
# li_two = list('python')
# # 根据另一个列表创建列表，结果为[1, 'python']
# li_three = list([1, 'python'])


# ++++++++++   多学一招：可迭代对象   ++++++++++
# 从collections.abc模块中导入Iterable类
# from collections.abc import Iterable
# ls = [3, 4, 5]
# print(isinstance(ls, Iterable))


# ++++++++++   5.2.2 访问列表元素   ++++++++++
# list_demo01 = ["Java", "C#", "Python", "PHP"]
# print(list_demo01[1])   					# 通过正向索引访问列表元素
# print(list_demo01[-3])  					# 通过反向索引访问列表元素

# li_one = ['p', 'y', 't', 'h', 'o', 'n']
# print(li_one[1:4:2]) 		# 按步长2获取li_one中索引1～3对应的元素
# print(li_one[2:])     	# 获取li_one中索引2到末尾对应的元素
# print(li_one[:3])     	# 获取li_one中索引0～2对应的元素
# print(li_one[:])      	# 获取li_one中的所有元素

# li_one = ['p', 'y', 't', 'h', 'o', 'n']
# for li in li_one:
#     print(li, end=' ')


# ++++++++++   5.2.3 添加列表元素   ++++++++++
# list_one = [1, 2, 3, 4]
# list_one.append(5)                    	# 在列表末尾添加元素5
# print(list_one)
# list_one.append(['论语', '诗经'])    	# 继续在列表末尾添加另一个列表
# print(list_one)

# list_str = ['a', 'b', 'c']
# list_num = [1, 2, 3]
# list_str.extend(list_num)       # 将list_num的所有元素添加到list_str的末尾
# print(list_num)
# print(list_str)

# names = ['小明', '小红', '小兰']
# # 在列表names中索引为2的位置插入新元素'小白'
# names.insert(2, '小白')
# print(names)
# # 在列表names中索引为1的位置插入新元素('张三', '李四')
# names.insert(1, ('张三', '李四'))
# print(names)
# names.insert(10, '王五')      # 在列表names的末尾插入新元素'王五'
# print(names)
# names.insert(-10, '王五')     # 在列表names的开头插入新元素'王五'
# print(names)


# ++++++++++   5.2.4 列表元素排序   ++++++++++
# li_one = [6, 2, 5, 3]
# li_two = [7, 3, 5, 4]
# li_three = ['python', 'java', 'php']
# li_one.sort()                			# 采用升序的方式对列表中的元素进行排序
# li_two.sort(reverse=True)  			# 采用降序的方式对列表中的元素进行排序
# li_three.sort(key=len)                	# 按照元素的长度对列表中的字符串进行排序
# print(li_one)
# print(li_two)
# print(li_three)

# li_one = [4, 3, 2, 1]
# li_two = sorted(li_one)         # 采用升序的方式对列表li_one的元素进行排序
# print(li_one)
# print(li_two)

# li_one = ['a', 'b', 'c', 'd']
# li_one.reverse()
# print(li_one)


# ++++++++++   5.2.5 删除列表元素   ++++++++++
names = ['小明', '小红', '小兰']
# del names[0]       							# 从列表中删除索引为0的元素
# print(names)

# del names             # 删除列表names
# print(names)

# chars = ['h', 'e', 'l', 'l', 'e']
# chars.remove('e')           					# 删除匹配到的第一个'e'
# print(chars)

# numbers = [1, 2, 3, 4, 5]
# print(numbers.pop())        # 删除列表中的最后一个元素
# print(numbers.pop(1))       # 删除列表中索引为1的元素
# print(numbers)

# names = [1, 2, 3]
# names.clear()                # 清空列表中的所有元素
# print(names)


# ++++++++++   5.2.6 列表推导式   ++++++++++
ls = [1, 2, 3, 4, 5, 6, 7, 8]
ls = [data * data for data in ls]
# print(ls)

# new_ls = [temp for temp in ls if temp > 4]
# print(new_ls)

# new_ls = [temp if temp % 2 == 0 else temp + 1 for temp in ls]
# print(new_ls)

# ls_one = [1, 2, 3]
# ls_two = [3, 4, 5]
# ls_three = [x + y for x in ls_one for y in ls_two]
# print(ls_three)

