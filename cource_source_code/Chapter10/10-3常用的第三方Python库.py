# ++++++++++   10.5.1 jieba库   ++++++++++
import jieba
# seg_list = jieba.cut("我打算到中国教育科学研究院图书馆学习", cut_all=True)
# print("【全模式】: " + "/ ".join(seg_list))                  # 全模式
# seg_list = jieba.lcut("我打算到中国教育科学研究院图书馆学习")
# print("【精确模式】: " + "/ ".join(seg_list))                # 精确模式
# # 搜索引擎模式
# seg_list = jieba.cut_for_search("我打算到中国教育科学研究院图书馆学习")
# print("【搜索引擎模式】: " + ", ".join(seg_list))


# jieba.add_word("好天气")
# result = jieba.lcut("今天真是个好天气")
# print(result)


# ++++++++++   10.5.2 wordcloud库   ++++++++++
# import wordcloud
# # 创建词云对象
# w = wordcloud.WordCloud(font_path='AdobeHeitiStd-Regular.otf',
#      max_words=500, max_font_size=40, background_color='white')
# # 加载词云图使用的文本
# file = open(r'xiyouji.txt', encoding='utf-8')
# string = file.read()
# file.close()
# w.generate(string)
# # 生成词云图
# w.to_file('xiyou.jpg')


# import wordcloud
# import numpy as np
# from PIL import Image
# picture = Image.open("wukong.png") 	# 加载图片，返回一个图片对象
# mk = np.array(picture)              	# 将图片对象转换成数组
# # 创建词云对象
# w = wordcloud.WordCloud(font_path='AdobeHeitiStd-Regular.otf', mask=mk,
#                                    max_words=500, background_color='white')
# file = open(r'xiyouji.txt', encoding='utf-8')
# string = file.read()
# file.close()
# # 加载词云图使用的文本
# w.generate(string)
# # 生成词云图
# w.to_file('xiyou.jpg')


# ++++++++++   10.5.3 Pygame库   ++++++++++
# 1. Pygame的初始化和退出
# import pygame                           # 导入pygame
# def main():
#     pygame.init()                       # 初始化所有模块
#     pygame.quit()                       # 卸载所有模块
# if __name__ == '__main__':
#     main()


# 2. 创建游戏窗口
# import pygame  # 导入pygame
#
# WINWIDTH = 640  # 窗口宽度
# WINHEIGHT = 206  # 窗口高度
# BGCOLOR = (125, 125, 0)  # 预设颜色为橄榄色
#
# FPS = 60								# 预设频率
# def main():
#     pygame.init()  # 初始化所有模块
#
#     FPSCLOCK = pygame.time.Clock()  # 创建Clock类的对象
#
#     # 创建图形窗口
#     WINSET = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
#     WINSET.fill(BGCOLOR)  # 填充背景颜色
#
#     pygame.display.set_caption('小游戏')  # 设置窗口标题
#
#     image = pygame.image.load('bg.jpg')  # 加载图片
#     WINSET.blit(image, (0, 0))  # 绘制图片
#
#     pygame.display.update()  # 刷新窗口
#     i = 0  # 临时变量，记录循环的执行次数
#     while True:
#         i = i + 1
#         # print(i)
#         FPSCLOCK.tick(FPS)  # 控制帧率
#
#     pygame.quit()  # 卸载所有模块
#
# if __name__ == '__main__':
#     main()


import pygame, time  # 导入pygame
from pygame.locals import *

WINWIDTH = 640  # 窗口宽度
WINHEIGHT = 206  # 窗口高度
# ------颜色变量----
BGCOLOR = (125, 125, 0)  # 预设背景颜色
MSGCOLOR = (95, 200, 255)  # 设置字体颜色
MSGBGCOLOR = (23, 78, 20)  # 按钮背景颜色

FPS = 60


def main():
    pygame.init()  # 初始化所有模块

    FPSCLOCK = pygame.time.Clock()  # 创建Clock类的对象

    # 创建图形窗口
    WINSET = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    WINSET.fill(BGCOLOR)  # 填充背景颜色
    pygame.display.set_caption('小游戏')
    image = pygame.image.load('bg.jpg')  # 加载背景图片
    WINSET.blit(image, (0, 0))  # 绘制背景图片
    BASICFONT = pygame.font.Font('STKaiti.ttf', 25)  # 创建字体对象
    msg_surf = BASICFONT.render('初始化', True, MSGCOLOR, MSGBGCOLOR)  # 渲染
    WINSET.blit(msg_surf, (0, 0))

    # 准备背景
    # base_surf = WINSET.copy()

    # 渲染字体
    auto_surf = BASICFONT.render('自  动', True, MSGCOLOR, MSGBGCOLOR)
    auto_rect = auto_surf.get_rect()  # 获取矩形属性
    auto_rect.x = WINWIDTH - auto_rect.width - 10  # 重设横坐标
    auto_rect.y = WINHEIGHT - auto_rect.height - 10  # 重设纵坐标
    WINSET.blit(auto_surf, auto_rect)  # 绘制字体

    # # 在背景的不同位置绘制方块，制造移动效果。方块向左移动BLOCKSIZE-2
    # for i in range(0, WINHEIGHT, 2):
    #     FPSCLOCK.tick(FPS)
    #     WINSET.blit(auto_surf, auto_rect)  # 绘制字体
    #     pygame.display.update()
    #     auto_rect.x -= 10  # 修改“自动”按钮的横坐标
    #     if i + 2 < WINHEIGHT:
    #         WINSET.blit(base_surf, (0, 0))  # 使用备份base_surf覆盖WINSET

    pygame.display.update()
    # time.sleep(5)

    while True:
        FPSCLOCK.tick(FPS)
        # 获取点击事件
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:  # 如果有鼠标放开事件
                # 检查某个点是否在矩形区域内
                if auto_rect.collidepoint(event.pos):
                    print('点击了按钮')
                else:
                    print('点击了空白区域')
            elif event.type == KEYUP:  # 如果有按键放开事件
                if event.key in (K_LEFT, K_a):
                    print('←')
                elif event.key in (K_RIGHT, K_d):
                    print('→')
                elif event.key in (K_UP, K_w):
                    print('↑')
                elif event.key in (K_DOWN, K_s):
                    print('↓')
        if pygame.key.get_pressed()[K_ESCAPE]:  # 如果按下Esc键
            print('退出游戏')
            pygame.quit()
            break
    pygame.quit()  # 卸载所有模块


if __name__ == '__main__':
    main()
