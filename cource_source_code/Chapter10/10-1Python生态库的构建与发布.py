# ++++++++++   10.2.1 模块的构建与使用   ++++++++++
# import test                             # 导入模块
# result = test.add(11, 22)            # 使用模块中定义的函数
# print(result)


# import test
# result = test.add(11, 22)
# print(result)


# ++++++++++   10.2.2 包的构建与导入   ++++++++++
# import package_a

# import package_a.module							# 方式一
# from package_a import module					    # 方式二

# import package.package_a.module_a				    # 方式一
# from package.package_a import module_a			# 方式二


# ++++++++++   10.2.3 库的发布   ++++++++++
# from distutils.core import setup
# setup(
#     name = 'lib_test',
#     version = '1.0',
#     description = 'function package',
#     author = 'itcast',
#     py_modules = ['package.module','package.package_a.module_a',
#                     'package.package_b.module_b']
# )
