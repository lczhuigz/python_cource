# ++++++++++   8.4.1 构造方法   ++++++++++
# class Car:
#     def __init__(self):      							# 无参构造方法
#         self.color = "红色"
#     def drive(self):
#         print(f"车的颜色为：{self.color}")
# car_one = Car()   									# 创建对象并初始化
# car_one.drive()
# car_two = Car()   									# 创建对象并初始化
# car_two.drive()


# class Car:
#     def __init__(self, color):  				# 有参构造方法
#         self.color = color        				# 将形参color赋给属性
#     def drive(self):
#         print(f"车的颜色为：{self.color}")
# car_one = Car("红色")   						# 创建对象，并根据实参初始化属性
# car_one.drive()
# car_two = Car("蓝色")   						# 创建对象，并根据实参初始化属性
# car_two.drive()


# ++++++++++   8.4.2 析构方法   ++++++++++
# class Car:
#     def __init__(self):
#         self.color = "蓝色"
#         print("对象被创建")
#     def __del__(self):   							# 析构方法
#         print("对象被销毁")
# car = Car()
# print(car.color)
# del car  										# 使用del语句删除对象
# print(car.color)
