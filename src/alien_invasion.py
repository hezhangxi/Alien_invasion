#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    #初始化程序并创建一个对象
    pygame.init()
    #将Settings类进行实例化
    ai_settings = Settings()
    #screen = pygame.display.set_mode((1200,800))
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #设置背景颜色
    #bg_color = (230,230,230)
    
    #将Ship类实例化
    ship  = Ship(screen)
    
    #开始程序的主循环
    while True:
        
        #监视键盘和鼠标事件
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                sys.exit()
                
        #每次循环都重新绘制屏幕
        #screen.fill(bg_color)
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #让最近绘制的图形可见
        pygame.display.flip()

run_game()