import turtle
import time

# 准备二十四节气用到的数据
solar_terms_24 = []
names = ["雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种",
         "夏至", "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露",
         "霜降", "立冬", "小雪", "大雪", "冬至", "小寒", "大寒", "立春"]
en_names = ["Rain Water", "Awakening of Insects", "Spring Equinox",
            "Pure Brightness", "Grain Rain", "Beginning of Summer",
            "Grain Buds", "Grain in Ear", "Summer Solstice", "Minor Heat",
            "Major Heat", "Beginning of Autumn", "End of Heat", "White Dew",
            "Autumn Equinox", "Cold Dew", "Frost's Descent",
            "Beginning of Winter", "Minor Snow", "Major Snow", "Winter Solstice",
            "Minor Cold", "Major Cold", "Beginning of Spring"]
poems = ["随风潜入夜 润物细无声", "春雷响 万物长", "春风如贵客 一到便繁华",
         "清明时节雨纷纷", "风吹雨洗一城花", "天地始交 万物并秀", "物至于此 小得盈满",
         "家家麦饭美 处处菱歌长", "绿筠尚含粉 圆荷始散芳", "荷风送香气 竹露滴清响",
         "桂轮开子夜 萤火照空时", "天阶夜色凉如水 坐看牵牛织女星",
         "春种一粒粟 秋收万颗子", "露从今夜白 月是故乡明", "晴空一鹤排云上",
         "千家风扫叶 万里雁随阳", "霜叶红于二月花", "寒夜客来茶当酒",
         "雪粉华 舞梨花", "大雪满弓刀", "冬至大如年", "凌寒独自开",
         "燕山雪花大如席", "万紫千红总是春"]
for name, en_name, poem in zip(names, en_names, poems):
    temp_dic = {}
    temp_dic["NAME"] = name
    temp_dic["EN_NAME"] = en_name
    temp_dic["POEM"] = poem
    solar_terms_24.append(temp_dic)

def draw_pic(secs):
    # 清除窗口
    turtle.clear()
    # 绘制圆形，作为背景装饰
    turtle.goto(0, -250)
    turtle.fillcolor("#b1352b")
    turtle.begin_fill()
    turtle.circle(250)
    turtle.end_fill()
    turtle.home()   # 画笔回到原点位置
    turtle.penup()  # 提起画笔，仍然可以写字，后面无需调用pendown()函数放下画笔
    turtle.pencolor("white") # 将画笔颜色修改为白色
    turtle.seth(-90)  # 画笔朝下
    # 写倒计时数字，即第一行文字
    turtle.backward(10)
    turtle.write(secs, align="center", font=("方正仿宋", 120, 'normal'))
    # 写节气的中文名称，即第二行文字
    turtle.forward(50)
    name = solar_terms_24[24-secs]["NAME"]
    turtle.write(name, align="center", font=("黑体", 30, 'normal'))
    # 写节气的英文名称，即第三行文字
    turtle.forward(50)
    en_name = solar_terms_24[24-secs]["EN_NAME"]
    turtle.write(en_name, align="center", font=("Arial", 25, 'normal'))
    # 写节气对应的古诗词，即第四行文字
    turtle.forward(50)
    poem = solar_terms_24[24-secs]["POEM"]
    turtle.write(poem, align="center", font=("隶书", 20, 'normal'))
    turtle.home()  # 画笔回到原点位置

def countdown(secs):
    while secs > 0:
        # 绘制倒计时画面
        draw_pic(secs)
        # 让程序睡眠一秒
        time.sleep(1)
        secs -= 1

turtle.speed(0)  # 设置画笔移动的速度
turtle.delay(0)  # 设置延迟时间，参数为0时表示绘图没有延迟
# 展示引导语
turtle.pencolor("black")  # 设置画笔颜色为黑色
turtle.penup()              # 提起画笔
turtle.setheading(-90)    # 画笔朝下
turtle.backward(30)        # 画笔移动到合适的位置
# 写中文引导语
turtle.write("让我们一起倒计时，迎接春的到来。", align="center",
               font=("黑体", 20, 'normal'))
turtle.forward(60)
# 写英文引导语
turtle.write("Let's greet the arrival of spring with a countdown",
                align="center", font=("Arial", 20, 'normal'))
turtle.home()  # 画笔回到原点位置
time.sleep(3)  # 暂停三秒钟，保证引导语画面能够正常显示
# 显示24秒倒计时
turtle.pencolor("white")  # 设置画笔颜色为白色
# 定义倒计时秒数
seconds = 24
# 启动倒计时
countdown(seconds)
# 关闭画布
turtle.done()
