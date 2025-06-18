class Settings():
    """储存《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.scree_width = 1200
        self.scree_height = 800
        self.bg_color = (20, 230, 230)
        

        # 飞船的速度
        self.ship_speed_factor = 1.5