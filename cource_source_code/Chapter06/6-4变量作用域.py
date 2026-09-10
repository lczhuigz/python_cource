# ++++++++++   6.5.1 局部变量和全局变量   ++++++++++
# def test_one():
#     number = 10    	                  	# 局部变量
#     print(number) 	                 	# 在函数内部访问局部变量
# test_one()
# print(number)


# def test_one():
#     number = 10
#     print(number)  						# 访问test_one()函数的局部变量number
# def test_two():
#     number = 20
#     print(number)  						# 访问test_two()函数的局部变量number
# test_one()
# test_two()


# number = 10         							# 定义全局变量
# def test_one():
#     print(number)   							# 在函数内部访问全局变量
# test_one()
# print(number)       							# 在函数外部访问全局变量


# number = 10                                    	# 定义全局变量
# def test_one():
#     print(number)  						# 在函数内部访问全局变量
#     number += 1  							# 在函数内部直接修改全局变量
# test_one()
# print(number)


# ++++++++++   6.5.2 global和nonlocal关键字   ++++++++++
# number = 10                    			# 定义全局变量
# def test_one():
#     global number              			# 使用global声明变量number为全局变量
#     number += 1
#     print(number)
# test_one()
# print(number)


# def test():
#     number = 10                    	# 定义变量
#     def test_in():
#         nonlocal number           	# 使用nonlocal声明变量number
#         number = 20                 	# 在内部函数中修改变量number
#     test_in()
#     print(number)
# test()

