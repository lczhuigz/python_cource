# ++++++++++   7.2.1 文件的打开与关闭   ++++++++++
# file1 = open('E:\\a.txt')			# 以只读的方式打开E盘的文本文件a.txt
# file2 = open('b.txt', 'w')		# 以只写的方式打开当前目录的文本文件b.txt
# file3 = open('c.txt', 'w+')		#以读写的方式打开文本文件c.txt
# file4 = open('d.txt', 'wb+')		# 以二进制读写的方式打开文本文件d.txt

# file.close()

# with open('a.txt', 'w+') as file:
#     print('我是with语句')


# ++++++++++   7.2.2 文件的读写   ++++++++++
# with open('test.txt') as file:
#     result = file.read(3)              	# 读取3个字符
#     print(result)
#     result = file.read(3)              	# 继续读取3个字符
#     print(result)
#     result = file.read()               	# 继续读取剩余的全部数据
#     print(result)

#
# with open('test.txt') as file:
#     result = file.readline()  # 第1次读取，读取第1行数据
#     print(result)
#     result = file.readline()  # 第2次读取，读取第2行数据
#     print(result)
#     result = file.readline()  # 第3次读取，读取第3行数据
#     print(result)
#     result = file.readline()  # 第4次读取，读取第4行数据
#     print(result)

#
# with open('test.txt') as file:
#     print(file.readlines())      # 使用 readlines() 方法读取所有的数据


# string = "Nothing in the world is difficult " \
#            "for one who sets his mind to it."
# with open('write_file.txt', mode='w') as file:
#     size = file.write(string)                  # 向文件中写入数据
#     print(size)                                   # 输出字符数


# string_list = ["Interest is the best teacher!\n",
#                   "Interest is the best teacher!\n",
#                   "Interest is the best teacher!"]
# with open('write_file.txt', mode='w') as file:
#     file.writelines(string_list)


# ++++++++++   7.2.3 文件的定位读写   ++++++++++
# with open('write_file.txt') as file:
#     read_location = file.tell()    # 获取文件读写位置
#     print(read_location)
#     file.read(5)                      # 通过read()方法读取数据，移动文件读写位置
#     read_location = file.tell()    # 再次获取文件读写位置
#     print(read_location)


# with open('write_file.txt') as file:
#     read_location = file.seek(5, 0)     	# 从文件开头移动5个字节
#     print(read_location)                   	# 输出当前的文件读写位置
#     result = file.read(3)                   	# 读取3个字符
#     print(result)


# with open('write_file.txt') as file:        	# 打开文本文件
#     read_location = file.seek(5, 0)         	# 从文件开头移动5个字节
#     print(read_location)
#     read_location = file.seek(-3, 2)        	# 从文件末尾向前移动3个字节
#     print(read_location)


# with open('write_file.txt', 'rb') as file:  	# 以二进制读取的方式打开文件
#     read_location = file.seek(5, 0)           	# 从文件开头移动5个字节
#     print(read_location)
#     read_location = file.seek(-3, 2)           	# 从文件末尾向前移动3个字节
#     print(read_location)


