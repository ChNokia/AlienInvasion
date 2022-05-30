import pygame

class Ship:
    """Клас для керування кораблем."""

    def __init__(self, ai_game):
        """Ініціалізувати корабель та задати його початкову позицію."""
        self.screen = ai_game.screen
        self.screen_rec = ai_game.screen.get_rect()

        # Завантажити зображення корабля та отримати його rect.
        self.image = pygame.image.load('images/ship.bmp') #ship.png
        self.rect = self.image.get_rect()
        # Створювати кожен новий корабель внизу екрана, по центру.
        self.rect.midbottom = self.screen_rec.midbottom
    
    def blitme(self):
        """Намалювати корабель у його поточному розташуванні."""
        self.screen.blit(self.image, self.rect)