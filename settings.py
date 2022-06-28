class Settings:
    """Клас для збереження всіх налаштувань гри."""

    def __init__(self):
        """Ініціалізувати налаштування гри"""
        # Screen settings
        self.screen_width = 1200
        self.screen_heigth = 800
        self.bg_color = (230, 230, 230)
        # Налаштування корабля
        self.ship_speed = 0.5
        # Налаштування кулі
        self.bullet_speed = 0.4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # Налаштування прибульця
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # fleet_direction 1 означає напрямок руху праворуч; -- ліворуч.
        self.fleet_direction = 1
