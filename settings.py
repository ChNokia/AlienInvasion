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
