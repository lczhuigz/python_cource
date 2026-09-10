# ++++++++++   10.3.1 time库   ++++++++++
# import time
# print(time.time())                                   # 获取时间戳

# import time
# print(time.localtime())          	# 获取结构化时间，默认使用当前时间戳
# print(time.localtime(34.54))     	# 获取结构化时间，使用指定的时间戳

# import time
# print(time.gmtime())        	 	# 获取结构化时间，默认使用当前时间戳
# print(time.gmtime(34.54))    		# 获取结构化时间，使用指定的时间戳

# import time
# now_string = time.strftime("%Y-%m-%d %H:%M:%S")
# print(now_string)

# import time
# print(time.strftime('%H:%M:%S'))                   # 格式化部分时间信息

# import time
# now_string = time.asctime()  	# 将本地时间对应的时间对象转换为时间字符串
# print(now_string)
# gmtime = time.gmtime()        	# 将协调世界时对应的时间对象转换为时间字符串
# print(time.asctime(gmtime))

# import time
# print(time.ctime())        	# 将当前时间戳转换为时间字符串
# print(time.ctime(36.36))  	# 将指定的时间戳转换为时间字符串

# import time
# print(time.strptime('Sat,11 Apr 2023 11:54:42', '%a,%d %b %Y %H:%M:%S'))
# print(time.strptime('11:54:42', '%H:%M:%S'))

# import time
# print('开始')
# time.sleep(3)
# print('结束')

# import time
# time_a = time.time()
# time.sleep(3.5)
# time_b = time.time()
# print(time_a + time_b)
# print(time_b - time_a)


# ++++++++++   10.3.2 random库   ++++++++++
# import random
# print(random.random())					#生成[0.0,1.0)范围内的随机浮点数
# print(random.uniform(3, 5))				#生成[3.0,5.0]范围内的随机浮点数
# print(random.randint(2, 8))				#生成[2,8]范围内的随机整数
# print(random.randrange(10))				#生成[0,10)范围内的随机整数
# print(random.randrange(1, 10, 2))			# 随机返回1、3、5、7、9中的一个元素
# # 随机返回序列中的一个元素
# print(random.choice(['Python', 'C', 'PHP', 'Java']))
# ls = ['Python', 'C', 'PHP', 'Java']
# # 将序列ls的元素随机排列
# random.shuffle(ls)
# print(ls)
# # 从序列中获取长度为3的片段，随机排序后返回新的序列
# print(random.sample(('Python', 'C', 'PHP', 'Java'), k=3))


# ++++++++++   10.3.3 Turtle库   ++++++++++
# import turtle
# turtle.setup(800, 600)

# import turtle
# turtle.setup(800, 600)     	# 创建图形窗口
# turtle.done()               	# 绘制结束

# import turtle
# turtle.color('pink')
# turtle.color('#A22A2A')
# turtle.done()

# import turtle
# turtle.colormode(1.0)							# 使用RGB小数颜色值
# turtle.color((1, 1, 0))
# turtle.colormode(255)							# 使用RGB整数颜色值
# turtle.color((165, 42, 42))
# turtle.done()

# import turtle
# turtle.penup()						# 提起画笔
# turtle.pendown()						# 放下画笔
# turtle.done()

# import turtle
# turtle.forward(200)	    # 向前移动200px
# turtle.seth(-90)		# 调整画笔朝向，使其朝向-90°方向
# turtle.forward(200) 	# 向前移动200px
# turtle.right(90)		# 调整画笔朝向，使其向右转动90°
# turtle.forward(200) 	# 向前移动200px
# turtle.left(-90)		# 调整画笔朝向，使其向左转动-90°，即向右转动90°
# turtle.forward(200) 	# 向前移动200px
# turtle.right(90)		# 调整画笔朝向，使其向右转动90°
# turtle.done()

# import turtle
# turtle.fillcolor("blue")         				# 设置填充颜色为蓝色
# turtle.begin_fill()             				# 开始填充
# turtle.circle(150)
# turtle.end_fill()               				# 填充结束
# turtle.done()




