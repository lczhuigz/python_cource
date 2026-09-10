import random
from sys import exit
import pygame
from pygame.locals import *
pygame.init()
# 屏幕宽度
SCREEN_WIDTH = 450
# 屏幕高度
SCREEN_HEIGHT = 560
# 香蕉下落速度
BANANA_SPEED = 1
def game_start():
    # 绘制图形窗口
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    # 设置窗口标题
    pygame.display.set_caption("猴子接香蕉")
    # 分数字体，字号
    run_time_font = pygame.font.SysFont('simhei', 48)
    # 加载图片
    game_background = pygame.image.load('background.jpg')
    monkey = pygame.image.load('monkey.png')
    banana = pygame.image.load('banana.png')
    # 游戏初始分数
    score = 0
    # 猴子初始位置信息
    monkey_x = 200
    monkey_y = 470
    # 设置猴子的移动速度
    monkey_x_speed = 1
    monkey_move = {K_LEFT: 0, K_RIGHT: 0}
    # 香蕉初始位置列表
    pos_list = []
    for i in range(7):
        x = random.randint(0, 390)
        y = random.randint(0, 560)
        pos_list.append([x, y])
    # 帧率控制Clock对象
    clock = pygame.time.Clock()
    while True:
        # 绘制背景图片
        screen.blit(game_background, (0, 0))
        # 事件处理
        for event in pygame.event.get():
            if event.type == QUIT:   # 退出事件
                exit()
            if event.type == KEYDOWN:  # 按键按下事件
                # 判断事件类型是否为左右键
                if event.key in monkey_move:
                    monkey_move[event.key] = 1
            elif event.type == KEYUP:  # 按键松开事件
                if event.key in monkey_move:
                    monkey_move[event.key] = 0
        # 距上次调用clock对象时间
        second_time_passed = clock.tick(60)
        # 定位猴子移动后坐标
        monkey_x -= monkey_move[K_LEFT] * \
                    monkey_x_speed * second_time_passed
        monkey_x += monkey_move[K_RIGHT] * \
                    monkey_x_speed * second_time_passed
        # 判断猴子边界条件
        if monkey_x > 450 - monkey.get_width():
            monkey_x = 450 - monkey.get_width()
        elif monkey_x < 0:
            monkey_x = 0
        screen.blit(monkey, (monkey_x, monkey_y))
        for y in pos_list:  # 坐标循环，从y轴的上限往下限方向飘落
            y[1] = y[1] + BANANA_SPEED
            screen.blit(banana, (y[0], y[1]))
            if y[1] >= 560:
                y[1] = -banana.get_height()
            # 碰撞检测
            if monkey_x < y[0] < monkey_x + monkey.get_width() and \
                    monkey_y - banana.get_height() < y[1] < monkey_y:
                score += 10
                pos_list.remove([y[0], y[1]])
                x, y = random.randint(0, 390), random.randint(0, 560)
                if len(pos_list) <= 6:
                    pos_list.append([x, -y])
        screen_score = run_time_font.render('分数：' + str(score), True, (255, 0, 0))
        screen.blit(screen_score, (0, 0))
        # 刷新显示
        pygame.display.update()
if __name__ == '__main__':
    game_start()




