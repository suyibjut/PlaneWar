import pygame

pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))
pygame.display.update()

# 创建时间对象
colok = pygame.time.Clock()

hero_rect = pygame.Rect(150, 300, 102, 126)
while True:

    # 可以指定循环体内部的代码执行的频率
    colok.tick(60)
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)

    hero_rect.y -= 1
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    if hero_rect.y <= 0:
        hero_rect.y = 700

    pygame.display.update()

    pass

pygame.quit()