# ++++++++++   8.3.1 属性   ++++++++++
# class Car:
#     wheels = 4  								# 定义类属性
# car = Car()
# print(Car.wheels)   	           				# 通过类Car访问类属性
# print(car.wheels)   	           				# 通过对象car访问类属性
# Car.wheels = 3    	                			# 通过类Car修改类属性
# print(Car.wheels)
# print(car.wheels)
# car.wheels = 4                      				# 通过对象car修改类属性
# print(Car.wheels)
# print(car.wheels)


# class Car:
#     def drive(self):
#         self.wheels = 4                    			# 定义实例属性
# car = Car()                                 			# 创建对象car
# car.drive()
# print(car.wheels)                          			# 通过对象car访问实例属性
# print(Car.wheels)                          			# 通过类Car访问实例属性


# class Car:
#     def drive(self):
#         self.wheels = 4                   			# 定义实例属性
# car = Car()                                			# 创建对象car
# car.drive()
# car.wheels = 6                         			# 修改实例属性
# # print(car.wheels)                         		# 通过对象car访问实例属性
#
# car.color = "红色"                     # 动态地添加实例属性
# # print(car.color)
#
# car2 = Car()                            # 创建另一个对象
# print(car2.color)                      # 尝试用另一个对象访问动态添加的实例属性


# ++++++++++   8.3.2 方法   ++++++++++
class Car:
    def drive(self):                           		# 定义实例方法
        print("我是实例方法")
car = Car()
car.drive()                                     	# 通过对象调用实例方法
Car.drive()                                     	# 通过类调用实例方法


# class Car:
#     def create_arr(self):              			# 定义另一个实例方法
#         self.color = "红色"            			# 定义实例属性
#     def drive(self):                    			# 定义实例方法
#         print("我是实例方法")
#         self.create_arr()              		# 通过self调用另一个实例方法
#         print(self.color)              		# 通过self访问实例属性
# car = Car()
# car.drive()                             		# 通过对象调用实例方法


# class Car:
#     @classmethod
#     def stop(cls):  						      	# 定义类方法
#         print("我是类方法")
# car = Car()
# car.stop()   							     		# 通过对象调用类方法
# Car.stop()   										# 通过类调用类方法


# class Car:
#     wheels = 3               						# 定义类属性
#     @classmethod
#     def stop(cls):           						# 定义类方法
#         print(cls.wheels)   						# 使用cls访问类属性
#         cls.wheels = 4       						# 使用cls修改类属性
#         print(cls.wheels)
# car = Car()
# car.stop()


# class Car:
#     @staticmethod
#     def test():                                		# 定义静态方法
#         print("我是静态方法")
# Car.test()                                      		# 通过类调用静态方法


# class Car:
#     wheels = 3                                 		# 定义类属性
#     @staticmethod
#     def test():
#         print("我是静态方法")
#         print(f"类属性的值为{Car.wheels}")  		# 在静态方法中访问类属性
# Car.test()


# ++++++++++  8.3.3 私有成员   ++++++++++
# class Car:
#     __wheels = 4         							# 私有属性
#     def __drive(self):  							# 私有方法
#         print("开车")


# class Car:
#     __wheels = 4        							# 私有属性
#     def __drive(self): 							# 私有方法
#         print("行驶")
#     def test(self):
#         print(f"汽车有{self.__wheels}个车轮") 		# 在公有方法中访问私有属性
#         self.__drive()                          		# 在公有方法中调用私有方法
# car = Car()
# # print(car.__wheels)  								# 在类外部访问私有属性
# # car.__drive()         								# 在类外部调用私有方法
# car.test()

