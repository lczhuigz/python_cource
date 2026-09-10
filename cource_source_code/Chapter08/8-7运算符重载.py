# 定义一个表示计算器的类
class Calculator(object):
    def __init__(self, number):
        self.number = number                         	# 记录数值
    def __add__(self, other):       				# 重载运算符+
        self.number = self.number + other
        return self.number
    def __sub__(self, other):       				#重载运算符-
        self.number = self.number - other
        return self.number
    def __mul__(self, other):       				# 重载运算符*
        self.number = self.number * other
        return self.number
    def __truediv__(self, other):  				#重载运算符/
        self.number = self.number / other
        return self.number

calculator = Calculator(10)
print(calculator + 5)              		# calculator对象与数值5相加
print(calculator - 5)              		# calculator对象与数值5相减
print(calculator * 5)              		# calculator对象与数值5相乘
print(calculator / 5)              		# calculator对象与数值5相除

