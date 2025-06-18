import sys

import pygame

def check_keydown_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
            
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def updata_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # 让最近重绘的屏幕可见
    pygame.display.flip()