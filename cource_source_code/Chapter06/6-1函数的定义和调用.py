# ++++++++++   6.2.1 定义函数   ++++++++++
def add():
    result = 11 + 22
    print(result)
#
def add_modify(a, b):
    result = a + b
    print(result)


# ++++++++++  6.2.2 调用函数   ++++++++++
# add_modify(10, 20)

# def add_modify(a, b):
#     result = a + b
#     add()                    # 在add_modify()函数的内部调用add()函数
#     print(result)
# add_modify(10, 20)


# ++++++++++  多学一招：函数的嵌套定义   ++++++++++
# def add_modify(a, b):
#     result = a + b
#     print(result)
#     def test():                                 # 在add_modify()函数中定义函数test()
#         print("我是内层函数")
# add_modify(10, 20)

# def add_modify(a, b):
#     result = a + b
#     print(result)
#     def test():                                	# 在add_modify()函数中定义函数test()
#         print("我是内层函数")
#     test()                                      	# 在add_modify()函数中调用函数test()
# add_modify(10, 20)
