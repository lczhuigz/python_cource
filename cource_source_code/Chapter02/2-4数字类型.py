# ++++++++++   2.5.1整数类型   ++++++++++
# 5      									   				# 十进制数
# 0b101  									   				# 二进制数
# 0o5    									   				# 八进制数
# 0x5    									   				# 十六进制数

# decimal = 10  		 				# 十进制数
# bin_num = 0b1010                       	# 二进制数
# print(bin(decimal))  					# 将十进制数10转换为二进制数
# print(oct(decimal))  					# 将十进制数10转换为八进制数
# print(int(bin_num))                   	#将二进制数0b1010转换为十进制数
# print(hex(decimal))  					# 将十进制数10转换为十六进制数


# ++++++++++   2.5.2浮点型   ++++++++++
# 1.09999              1.2021                 314.15926
# -2.36                -10.0632               -100.03

# -3.14e10							# 相当于-3.14×10的10次方，结果为-31400000000
# 3.14e-10							# 相当于3.14×10的-10次方，结果为0.000000000314

# print(3.14e500)
# print(-3.14e500)


# ++++++++++   2.5.3复数类型   ++++++++++
# complex_one = 1 + 2j               	# 实部为1，虚部为2
# complex_two = 2j                    # 虚部为2

# complex_one = complex(3, 2)     # 创建复数，分别传入实部和虚部
# print(complex_one)
# complex_two = complex(5)         # 创建复数，只传入实部
# print(complex_two)
#
# complex_one = 1 + 2j
# print(complex_one.real)  							# 获取复数的实部
# print(complex_one.imag)  							# 获取复数的虚部


# ++++++++++   2.5.4布尔类型   ++++++++++
# print(bool(None))                     	# 检测None的布尔值
# print(bool(0))                         	# 检测整型数据0的布尔值
# print(bool(3.1415))                   	# 检测浮点型数据3.1415的布尔值
# print(bool(0j))                        	# 检测复数类型数据0j的布尔值
# print(bool('hello'))                  	# 检测字符串'hello'的布尔值
# print(bool(1))                         	# 检测整型数据1的布尔值


# ++++++++++   2.5.5数字类型转换   ++++++++++
# num_one = 2.0
# print(int(num_one)) 					#将浮点型数据转换为整型数据
# num_two = 5
# print(float(num_two)) 	 	 		#将整型数据转换为浮点型数据
# print(complex(num_one)) 	 	 	 	#将浮点型数据转换为复数类型的数据
# words_one = '10.01'
# print(float(words_one))               	# 将字符串类型的数据转换为浮点型数据
# words_two = '10'
# print(int(words_two))                 	# 将字符串类型的数据转换为整型数据
# words_three = '1+2j'
# print(complex(words_three))          	# 将字符串类型的数据转换为复数类型的数据

words_four = '0b1010'         	# 字符串中包含二进制数
print(int(words_four, base=2))	# 将字符串转换为整型数据时，通过base指定要转换为二进制数据



