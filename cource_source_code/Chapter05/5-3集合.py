# ++++++++++   1.	创建集合   ++++++++++
# s1 = {1}									# 创建包含一个元素的集合
# s2 = {1, 'b', (2,5)}						# 创建包含多个元素的集合
# #
# s = set()
#
s1 = set([1, 2, 3])					# 根据列表创建集合
s2 = set((2, 3, 4))					# 根据元组创建集合
s3 = set('python')					# 根据字符串创建集合
s4 = set(range(5))                  # 根据range()函数返回的结果创建集合


# ++++++++++   2.	集合的常见操作   ++++++++++
# s1.add('s')							# 向集合s1中添加元素s
# print(s1)
# s2.remove(3)						     # 删除集合s2中的元素3
# print(s2)
# s3.discard('p')						# 删除集合s3中的元素p
# print(s3)
# data = s4.pop()						# 随机返回集合s4中的一个元素
# print(data)
# s3.clear()							# 清空集合s3
# print(s3)
# s5 = s2.copy()						# 复制集合s2并赋给s5
# print(s5)
# result = s4.isdisjoint(s2)			# 判断集合s4和s2是否有相同的元素
# print(result)


# ++++++++++   3.	集合推导式   ++++++++++
# ls = [1, 2, 3, 4, 5, 6, 7, 8]
# s = {data for data in ls if data%2==0}
# print(s)


