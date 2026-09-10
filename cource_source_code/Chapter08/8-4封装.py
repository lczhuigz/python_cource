class Person:
    def __init__(self, name):
        self.name = name             				# 姓名
        self.__age = 1               				# 年龄，默认为1岁，私有属性
    # 设置私有属性值的方法
    def set_age(self, new_age):
        if 0 < new_age <= 120:      			# 判断年龄是否合法
            self.__age = new_age
    # 获取私有属性值的方法
    def get_age(self):
        return self.__age

# person = Person("小明")
# person.set_age(20)
# print(f"年龄为{person.get_age()}岁")


# person = Person("小明")
# person.set_age(-10)
# print(f"年龄为{person.get_age()}岁")
