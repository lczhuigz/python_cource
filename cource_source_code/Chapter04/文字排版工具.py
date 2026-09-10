print("欢迎使用文字排版工具！")
string = input(r"请输入要排版的文字（多段文字之间用\r\n标记）：")
print(f"排版前的文本：\n{string}")
while True:
    print('=========================')
    print('1.删除空格')
    print('2.英文标点替换')
    print('3.段落分割')
    print('4.字母大写')
    print('0.退出')
    print('=========================')
    option = input("请输入功能选项：")
    if option == '1':   # 删除空格
        string = string.replace(' ', '')
        print(f"删除空格后的文本：\n{string}")
    elif option == "2":  # 替换英文标点
        for i in string:
            if i == ',':
                string = string.replace(',', '，')
            elif i == '.':
                string = string.replace('.', '。')
            elif i == '?':
                string = string.replace('?', '？')
            elif i == '!':
                string = string.replace('!', '！')
            elif i == ':':
                string = string.replace(':', '：')
        print(f"替换标点后的文本：\n{string}")
    elif option == "3":  # 段落分割
        paragraphs = string.split(r"\r\n")
        temp_string = ''
        for paragraph in paragraphs:
            temp_string += f"{paragraph}\n"
        string = temp_string
        print(f"段落分割后的文本：\n{string}")
    elif option == "4":  # 字母大写
        string = string.upper()
        print(f"字母大写后的文本：\n{string}")
    elif option == "0":
        print("感谢使用文字排版工具，再见！")
        break
    else:
        print("无效的选项，请重新输入！")






