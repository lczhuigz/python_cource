# ++++++++++   8.7.1 单继承   ++++++++++
# class Cat(object):
#     def __init__(self, color):
#         self.color = color
#     def walk(self):
#         print("走猫步～")
# # 定义继承Cat的ScottishFold类
# class ScottishFold(Cat):
#     pass
# fold = ScottishFold("灰色")  					# 创建子类的对象
# print(f"{fold.color}的折耳猫")  					# 子类访问从父类继承的属性
# fold.walk()  									# 子类调用从父类继承的方法


# class Cat(object):
#     def __init__(self, color):
#         self.color = color
#         self.__age = 1                        # 增加私有属性
#     def walk(self):
#         print("走猫步～")
#     def __test(self):						# 增加私有方法
#         print("我是私有方法")
# # 定义继承Cat的ScottishFold类
# class ScottishFold(Cat):
#     pass
# fold = ScottishFold("灰色")  					# 创建子类的对象
# print(f"{fold.color}的折耳猫")  					# 子类访问从父类继承的属性
# fold.walk()  									# 子类调用从父类继承的方法
# print(fold.__age)     					# 子类访问父类的私有属性
# fold.__test()          					# 子类调用父类的私有方法



# ++++++++++   8.7.2 多继承   ++++++++++
# 定义一个表示房屋的类House
# class House(object):
#     def live(self):   							# 居住
#         print("供人居住")
# # 定义一个表示汽车的类Car
# class Car(object):
#     def drive(self):  						# 行驶
#         print("行驶")
# # 定义一个表示房车的类，继承House和Car类
# class TouringCar(House, Car):
#     pass
# tour_car = TouringCar()
# tour_car.live()   							# 子类对象调用父类House的方法
# tour_car.drive()  							# 子类对象调用父类Car的方法


# 定义一个表示房屋的类House
# class House(object):
#     def live(self):   							# 居住
#         print("供人居住")
#
#     def test(self):
#         print("House类测试")
#
# # 定义一个表示汽车的类Car
# class Car(object):
#     def drive(self):  						# 行驶
#         print("行驶")
# # 定义一个表示房车的类，继承House和Car类
# class TouringCar(House, Car):
#     pass
# tour_car = TouringCar()
# tour_car.live()   							# 子类对象调用父类House的方法
# tour_car.drive()  							# 子类对象调用父类Car的方法
# tour_car.test()       # 子类对象调用两个父类的同名方法


# ++++++++++   8.7.3 重写   ++++++++++
# # 定义一个表示人的类
# class Person(object):
#     def say_hello(self):
#         print("打招呼！")
# # 定义一个表示中国人的类
# class Chinese(Person):
#     def say_hello(self):  						# 重写的方法
#         print("吃了吗？")
# chinese = Chinese()
# chinese.say_hello()       						# 子类调用重写的方法


# # 定义一个表示人的类
# class Person(object):
#     def say_hello(self):
#         print("打招呼！")
# # 定义一个表示中国人的类
# class Chinese(Person):
#     def say_hello(self):
#         super().say_hello()                			# 调用父类中被重写的方法
#         print("吃了吗？")
# chinese = Chinese()
# chinese.say_hello()       						# 子类调用重写的方法
