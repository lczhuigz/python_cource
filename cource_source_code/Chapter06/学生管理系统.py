# 保存所有的学生信息
stu_info = []

# 输出功能菜单
def print_menu():
    print('=' * 30)
    print('学生管理系统 V10.0')
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.查询所有学生信息')
    print('0.退出系统')
    print('=' * 30)


# 添加学生信息
def add_stu_info():
    # 提示并获取学生的姓名
    new_name = input('请输入新学生的姓名:')
    # 提示并获取学生的性别
    new_sex = input('请输入新学生的性别:')
    # 提示并获取学生的手机号
    new_phone = input('请输入新学生的手机号码:')
    new_info = dict()
    new_info['name'] = new_name
    new_info['sex'] = new_sex
    new_info['phone'] = new_phone
    stu_info.append(new_info)
    print("添加成功！")


# 删除学生信息
def del_stu_info(student):
    del_num = int(input('请输入要删除的序号：')) - 1
    del student[del_num]
    print("删除成功！")


# 修改学生信息
def modify_stu_info():
    if len(stu_info) != 0:
        stu_id = int(input('请输入要修改学生的序号:'))
        new_name = input('请输入要修改学生的姓名:')
        new_sex = input('请输入要修改学生的性别:(男/女)')
        new_phone = input('请输入要修改学生的手机号码:')
        stu_info[stu_id - 1]['name'] = new_name
        stu_info[stu_id - 1]['sex'] = new_sex
        stu_info[stu_id - 1]['phone'] = new_phone
    else:
        print('学生信息表为空')

# 显示所有的学生信息
def show_stu_info():
    print('学生的信息如下：')
    print('=' * 30)
    print('序号    姓名    性别    手机号码')
    i = 1
    for tempInfo in stu_info:
        print("%d    %s    %s    %s" % (i, tempInfo['name'],
               tempInfo['sex'], tempInfo['phone']))
        i += 1


# 在main函数中执行不同的功能
def main():
    while True:
        print_menu()      # 输出功能菜单
        key = input("请输入功能对应的数字：")  # 获取用户输入的序号
        if key == '1':    # 添加学生信息
            add_stu_info()
        elif key == '2':  # 删除学生信息
            del_stu_info(stu_info)
        elif key == '3':  # 修改学生信息
            modify_stu_info()
        elif key == '4':  # 查询所有学生信息
            show_stu_info()
        elif key == '0':
            quit_confirm = input('亲，真的要退出么？(Yes or No):').lower()
            if quit_confirm == 'yes':
                print("谢谢使用！")
                break  # 跳出循环
            elif quit_confirm == 'no':
                continue
            else:
                print('输入有误!')

main()