# ++++++++++   2.1.1注释   ++++++++++
# 我是单行注释
# print('志当存高远')                   # 我也是单行注释


"""
Prints the values to a stream, or to sys.stdout by default.
  sep
    string inserted between values, default a space.
  end
    string appended after the last value, default a newline.
  file
    a file-like object (stream); defaults to the current sys.stdout.
  flush
    whether to forcibly flush the stream.
"""


# ++++++++++   2.1.2缩进   ++++++++++
# if True:
#     print("True")
# else:
#     print("False")

# if True:
#     print("Answer")
#     print("True")
# else:
#     print("Answer")
#   print("False")                          			# 缩进量不一致，会导致运行错误


# ++++++++++   2.1.3语句换行   ++++++++++
# side_01 = 3; side_02 = 4; side_03 = 5
# # 使用“\”进行换行
# result = side_01 + side_02 > side_03 or \
#            side_02 + side_03 > side_01 or \
#            side_01 + side_03 > side_02

# side_01 = 3; side_02 = 4; side_03 = 5
# # 使用小括号进行换行
# result = (side_01 + side_02 > side_03 or
#             side_02 + side_03 > side_01 or
#             side_01 + side_03 > side_02)

# 小括号包裹的内容进行换行显示
demo_one = ('one', 'two', 'three', 'four', 'five',
               'six', 'seven', 'eight', 'nine', 'ten')
# 中括号包裹的内容进行换行显示
demo_two = ['one', 'two', 'three', 'four', 'five',
              'six', 'seven', 'eight', 'nine', 'ten']
# 大括号包裹的内容进行换行显示
demo_thr = {'one': '壹', 'two': '贰', 'three': '叁', 'four': '肆',
               'five': '伍', 'six': '陆', 'seven': '柒', 'eight': '捌',
               'nine': '玖', 'ten': '拾'}


