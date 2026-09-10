def main():
    print('1.反诈查询 2.举报 3.退出')
    while True:
        options = input('请选择功能选项：')
        # 1.反诈查询
        if options == '1':
            flag = '1' # 标识参数
            print('1.手机号查询 2.网址查询')
            search_options = input('请输入选项:')
            if search_options == '1':
                search_options = '手机号'
                phone = input('请输入查询的手机号：')
                # 查询的时候标出已有多少人标记
                search_report(search_options, phone, flag)
            elif search_options == '2':
                search_options = '网址'
                website = input('请输入查询的网址：')
                # 读取文件查询,定义一个查询方法
                search_report(search_options, website, flag)
        # 2.举报
        elif options == '2':
            flag = '2'
            print('1.手机号举报 2.网址举报')
            search_options = input('请输入选项：')
            if search_options == '1':
                search_options = '手机号'
                phone = input('请输入举报的手机号：')
                search_report(search_options, phone, flag)
            elif search_options == '2':
                search_options = '网址'
                website = input('请输入举报的网址：')
                # 读取文件查询,定义一个查询方法
                search_report(search_options, website, flag)
        elif options == '3':
            break

def search_report(_type, data, flag):
    try:
        file = open('info.txt', 'r+', encoding='utf-8')
        try:
            # 转换为字典类型
            file_data = eval(file.read())
        except FileNotFoundError as error:
            print(error)  # 抛出异常
        else:
            keys_li = []  # 保存所有key值
            for info_dict in file_data[_type]:
                for k, v in info_dict.items():
                    # 将_type类型所有key值保存到列表keys_li
                    keys_li.append(k)
            if flag == '1':  # 查询逻辑
                # 判断查询举报的内容是否在keys_li列表中
                if data in keys_li:
                    # 获取查询内容在keys_li对应的索引
                    index = keys_li.index(data)
                    # 查询内容在keys_li与_type类型对应的索引值相同
                    for k, v in file_data[_type][index].items():
                        print(f'您查询的内容：{k},已被标记{v}次.')
                else:
                    print('查询内容不存在')
            elif flag == '2':  # 举报逻辑
                if data in keys_li:
                    # 获取举报内容在keys_li对应的索引
                    index = keys_li.index(data)
                    # 举报内容在keys_li与_type类型对应的索引相同
                    for k, v in file_data[_type][index].items():
                        file_data[_type][index].update({data: v + 1})
                else:
                    file_data[_type].append({data: 1})
                # 读取文件之后的读写位置在末尾，后续重新写入，所以读写位置设置为0,0
                file.seek(0, 0)
                file.write(str(file_data))
                print('举报成功')
        finally:
            file.close()
    except FileNotFoundError as error:
        print(error)
if __name__ == '__main__':
    main()
