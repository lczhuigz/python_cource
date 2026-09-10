import os


class WordBook:
    def __init__(self, filename):
        self.filename = filename  # 文件名
        self.words = []  # 单词列表，用于保存所有的单词及其翻译
        self.load_words()  # 从文件中加载所有的单词

    # 加载单词
    def load_words(self):
        # 判断当前目录下是否存在指定的文件
        if os.path.exists(self.filename) is not True:  # 不存在
            load_mode = 'w+'  # 指定打开文件的模式，该模式下会在没有文件时创建新文件
        else:  # 存在
            load_mode = 'r+'  # 指定打开文件的模式，该模式下会在有文件时保留原有内容
        with open(self.filename, load_mode, encoding='utf-8') as f:
            # 逐行读取文件中的内容
            all_data = f.readlines()
            for line_data in all_data:
                info_dict = dict()
                # 将每行内容转换为字典，字典的键为单词，值为翻译
                step_one = line_data.replace('{', '').replace('}', '')
                step_two = step_one.split(':')
                en = step_two[0].split(',')[0].replace("'", '').strip()
                zh = step_two[1].split(',')[0].replace("'", '').strip()
                info_dict[en] = zh
                # 将字典保存到列表中
                self.words.append(info_dict)

    # 保存单词
    def save_words(self):
        # 以w+模式打开指定文件，如果文件已经存在，则会清空文件的内容
        with open(self.filename, 'w+', encoding='utf-8') as f:
            # 将单词列表中的字典逐个写入文件中
            f.writelines(str(word) + '\n' for word in self.words)

    # 查看单词
    def view_words(self):
        if len(self.words) == 0:
            print('生词本内容为空')
        else:
            for word_tra in self.words:
                print(f'{word_tra}')

    # 背单词
    def memorize_word(self):
        if not self.words:
            print('生词本内容为空')
            return

        # 所有英文单词
        en_li = []
        for i in self.words:
            for j in i.keys():
                en_li.append(j)
        # 随机产生的英语单词
        for random_word in set(en_li):
            # 获取该单词在en_li中的索引
            random_word_index = en_li.index(random_word)
            # 获取该单词所对应的中文
            words_zh = self.words[random_word_index][random_word]
            in_words = input("请输入" + random_word + '翻译' + '：\n')
            # 判断翻译是否正确
            if in_words == words_zh:
                print('太棒了')
            else:
                print('再想想')

    # 添加新单词
    def add_word(self):
        word = input('请输入新单词：').strip()
        if word not in self.words:
            translate = input('请输入单词翻译：')
            word_dict = {word: translate}
            self.words.append(word_dict)
            print('添加成功')
        else:
            print('添加的单词已存在')

    # 删除单词
    def delete_word(self):
        if len(self.words) == 0:
            print("生词本内容为空")
        else:
            # 所有英文单词
            en_li = []
            for i in self.words:
                for j in i.keys():
                    en_li.append(j)
            del_words = input("请输入要删除的单词：\n")
            if del_words not in en_li:
                print('删除的单词不存在')
            else:
                # 获取要删除单词的索引
                del_words_index = en_li.index(del_words)
                # 删除单词
                self.words.pop(del_words_index)
                print('单词删除成功')

    # 清空生词本
    def clear_words(self):
        self.words.clear()
        print('清空成功')
        print(self.words)

    def show_menu(self):
        print('=' * 20)
        print('1.查看单词')
        print('2.背单词')
        print('3.添加新单词')
        print('4.删除单词')
        print('5.清空生词本')
        print('6.退出')
        print('=' * 20)

    def run(self):
        print('欢迎使用生词本！')
        while True:
            self.show_menu()
            choice = input('请输入功能选项: ')
            if choice == '1':
                self.view_words()  # 查看单词
            elif choice == '2':
                self.memorize_word()  # 背单词
            elif choice == '3':  # 添加新单词
                self.add_word()
            elif choice == '4':  # 删除单词
                self.delete_word()
            elif choice == '5':  # 清空生词本
                self.clear_words()
            elif choice == '6':  # 退出
                self.save_words()
                print('再见!')
                break
            else:
                print('无效选项')


word_book = WordBook('words.txt')
word_book.run()
