import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
       

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        

        # 将每艘新飞船放在屏幕的底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 在飞船的属性center中储存小数值
        self.center = float(self.rect.centerx)
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """依据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right< self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # 根据self.center更新rect对象
        self.rect.centerx = self.center
    

    def blitme(self):
        """在指定的位置重绘飞船"""
        self.screen.blit(self.image, self.rect)
        

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
