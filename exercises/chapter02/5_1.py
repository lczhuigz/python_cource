PI = 3.14

while True:

    r = float(input("请输入圆的半径："))

    if r > 0.0:
        print(f"圆的直径:{2 * r}")
        print(f"圆的面积:{PI * r * r}")
    else:
        print("输入错误！请重新输入")