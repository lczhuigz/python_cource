import turtle

# 定义绘制半圆形的函数，具有动态半径和颜色
def semi_circle(col, rad, val):
    turtle.color(col)  # 设置半圆的填充颜色
    turtle.penup()  # 提起画笔，移动时不绘制
    turtle.goto(val, 0)  # 移动到指定位置
    turtle.pendown()  # 放下画笔，开始绘制
    turtle.setheading(-90)  # 设置朝向，以绘制半圆
    turtle.circle(rad, -180)  # 绘制半圆
    turtle.setheading(0)  # 重置朝向为默认方向

# 创建图形窗口
turtle.setup(600, 400)
# 设置背景颜色
turtle.bgcolor('black')
# 设置标题
turtle.title('彩虹')
# 设置画笔特性
turtle.pensize(10)  # 设置画笔尺寸
turtle.speed(5)   # 设置绘制速度
# 设置绘制用的颜色
col = ['purple', 'blue', 'cyan', 'green', 'yellow', 'orange', 'red']
# 循环绘制7个半圆
for i in range(7):
    semi_circle(col[i], 10 * (i + 8), -10 * (i + 1))
# 绘制结束
turtle.done()