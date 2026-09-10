# ++++++++++   9.2.1 使用try-except语句捕获异常   ++++++++++
# num_one = int(input("请输入被除数："))
# num_two = int(input("请输入除数："))
# try:
#     print("结果为", num_one / num_two)
# except ZeroDivisionError:
#     print("出错了")


# num_one = int(input("请输入被除数："))
# num_two = int(input("请输入除数："))
# try:
#     print("结果为", num_one / num_two)
# except ZeroDivisionError as error:
#     print("出错了，原因：", error)


# try:
#     num_one = int(input("请输入被除数："))
#     num_two = int(input("请输入除数："))
#     print("结果为", num_one / num_two)
# except (ZeroDivisionError, ValueError) as error:
#     print("出错了，原因：", error)


# try:
#     num_one = int(input("请输入被除数："))
#     num_two = int(input("请输入除数："))
#     print("结果为", num_one / num_two)
# except Exception as error:
#     print("出错了，原因：", error)


# ++++++++++   9.2.2 异常结构中的else	子句   ++++++++++
# first_num = int(input("请输入被除数："))
# second_num = int(input("请输入除数："))
# try:
#     res = first_num / second_num
# except ZeroDivisionError as error:
#     print('异常原因：', error)
# else:
#     print(res)


# ++++++++++   9.2.3 异常结构中的finally子句   ++++++++++
# file = open('test.txt', mode='r', encoding='utf-8')
# try:
#     file.write("人生苦短，我用Python")
# except Exception as error:
#     print("写入文件失败", error)
# finally:
#     file.close()
#     print('文件已关闭')
