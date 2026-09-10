# ++++++++++   9.3.1 使用raise语句抛出异常	   ++++++++++
# raise IndexError
# raise IndexError()
# raise IndexError('索引超出范围')              	#抛出异常及其具体信息

# try:
#     raise IndexError('索引超出范围')
# except:
#     raise


# ++++++++++   9.3.2 使用assert语句抛出异常	   ++++++++++
# num_one = int(input("请输入被除数："))
# num_two = int(input("请输入除数："))
# assert num_two != 0, '除数不能为0'  	# assert语句判定num_two是否不等于0
# result = num_one / num_two
# print(num_one, '/', num_two, '=', result)


# ++++++++++   9.3.3 异常的传递	   ++++++++++
def get_width():             # 获取正方形边长
    print("get_width()开始执行")
    num = int(input("请输入除数："))
    width_len = 10 / num    # 此行代码在num为0时会出现异常
    print("get_width()执行结束")
    return width_len
def calc_area():             # 计算正方形的面积
    print("calc_area()开始执行")
    width_len = get_width()
    print("calc_area()执行结束")
    return width_len * width_len
def show_area():            # 输出正方形的面积
    try:
        print("show_area()开始执行")
        area_val = calc_area()
        print(f"正方形的面积是：{area_val}")
        print("show_area()执行结束")
    except ZeroDivisionError as e:
        print(f"捕获到异常:{e}")
show_area()

