# 保存所有的饮品信息
goods = {"可口可乐": 2.5, "百事可乐": 2.5, "冰红茶": 3, "脉动": 3.5,
         "果缤纷": 3, "绿茶": 3, "茉莉花茶": 3, "尖叫": 2.5}

# 展示饮品菜单
def show_goods():
    print("--------------------")
    for x, y in goods.items():
        print(x, ":", str(y) + "元")
    print("--------------------")


# 计算总金额
def total(goods_dict):
    count = 0
    for name, num in goods_dict.items():
        total_money = goods[name] * num
        # 总金额
        count += total_money
    print("需要支付金额：", count, "元")


def main():
    print("欢迎使用饮品自动售货机！")
    show_goods()
    goods_dict = {}
    while True:
        goods_name = input("请输入您要购买的商品（按q完成选择）：")
        if goods_name == 'q':
            break
        if goods_name in [g_name for g_name in goods.keys()]:
            goods_num = input("请输入购物数量：")
            if goods_num.isdigit():
                goods_dict[goods_name] = float(goods_num)
            else:
                print('商品数量不合法！')
        else:
            print('请输入正确的商品名称！')
    total(goods_dict)
    print("完成支付！期待下次惠顾!")

main()
