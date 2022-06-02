import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Загальний клас, що керує ресурсами та поведінкою гри."""
    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
    
    def _check_events(self):
        """Слідкувати за подіями миші та клавіатури."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    
    def _update_screen(self):
        """Оновити зображення на екрані та перемкнути на новий екран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        """Показати останній намальований екран."""
        pygame.display.flip()

    def run_game(self):
        """Розпочати головний цикл гри."""
        while True:
            self._check_events()
            self.ship.update()
            """Наново намалювати екран на кожній ітерації циклу."""
            self._update_screen()
            

if __name__ == '__main__':
    """Створити екземпляр гри та запустити гру."""
    ai = AlienInvasion()
    ai.run_game()