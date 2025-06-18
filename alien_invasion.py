import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    
    # 初始化游戏并创建一个屏幕对
    pygame.init()
    ai_settings = Settings()
    width = ai_settings.scree_width
    height = ai_settings.scree_height
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Alien Invasion")
    
    
    # 创建一艘飞船
    ship = Ship(ai_settings,screen) 
    
    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ship)
        
        ship.update()
                
        gf.updata_screen(ai_settings, screen, ship)



run_game()