class Settings():
    """储存《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 230, 230)
        

        # 飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        # fleed_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1