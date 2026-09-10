# ++++++++++   6.3.1 位置参数的传递   ++++++++++
# def get_max(a, b):
#     if a > b:
#         print(a, "是较大的值！")
#     elif a < b:
#         print(b, "是较大的值！")
#     else:
#         print("两个值一样大！")
# get_max(8, 5)


# ++++++++++   6.3.2 关键字参数的传递   ++++++++++
# def connect(ip, port):
#     print(f"设备{ip}:{port}连接！")
# connect(ip="127.0.0.1", port=8080)


# ++++++++++   多学一招：仅限位置   ++++++++++
def func(a, b, /, c):  			# 使用“/”限制其前面的形参a、b
    print(a, b, c)

# 错误的调用方式
# func(a=10, 20, 30)
# func(10, b=20, 30)
# # 正确的调用方式
# func(10, 20, c=30)


# ++++++++++   6.3.3 默认参数的传递   ++++++++++
# def connect(ip, port=8080):
#     print(f"设备{ip}:{port}连接！")
# connect(ip="127.0.0.1")
# connect(ip="127.0.0.1", port=3306)


# ++++++++++   6.3.4 参数的打包与解包   ++++++++++
# def test(*args):
#     print(args)
# test(11, 22, 33, 44, 55)

# def test(**kwargs):
#     print(kwargs)
# test(a=11, b=22, c=33, d=44, e=55)

# def test(a, b, c, d, e):
#     print(a, b, c, d, e)
# nums = (11, 22, 33, 44, 55)
# test(*nums)

# nums = {"a":11, "b":22, "c":33, "d":44, "e":55}
# test(**nums)


# ++++++++++   6.3.5 混合传递   ++++++++++
# def test(a, b, c=33, *args, **kwargs):
#     print(a, b, c, args, kwargs)
#
# test(1, 2)
# test(1, 2, 3)
# test(1, 2, 3, 4)
# test(1, 2, 3, 4, e=5)


