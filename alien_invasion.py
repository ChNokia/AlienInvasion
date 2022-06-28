import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

from pygame.sprite import Sprite

class AlienInvasion:
    """Загальний клас, що керує ресурсами та поведінкою гри."""
    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
        self.is_fullscreen = False
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
    
    def _switch_on_fullscreen(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_heigth = self.screen.get_rect().height
        self.is_fullscreen = True
    
    def _switch_off_fullscreen(self):
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
        self.is_fullscreen = False

    def _check_events(self):
        """Слідкувати за подіями миші та клавіатури."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагувати на натискання клавіш."""
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_f:
            if self.is_fullscreen:
                self._switch_off_fullscreen()
            else:
                self._switch_on_fullscreen()
            # ????????????? update ship position
            self.ship.update()
            self._update_screen()
    
    def _check_keyup_events(self, event):
        """Реагувати, коли клавіша не натиснута."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Оновити зображення на екрані та перемкнути на новий екран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        """Показати останній намальований екран."""
        pygame.display.flip()

    def _fire_bullet(self):
        """Створити нову кулю на екрані та додати її до групи куль"""
        new_bullet = Bullet(self)
        print('new_bullet', self.bullets, new_bullet)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Оновити позицію куль тп позбавитись старих куль."""
        # Оновити позиції куль.
        self.bullets.update()

        # Позбавитись куль, що зникли
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Реакція на зіткнення куль з прибульцями."""
        # Видалити всі кулі та прибульців, що зіткнулися.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            # Знищити наявні кулі та створити новий флот.
            self.bullets.empty()
            self._create_fleet()
    
    def _update_aliens(self):
        """
        Перевірити чи флот знаходиться на краю,
        тоді оновити позиції всіх прибульців флоту.
        """
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """Стврити флот прибульців."""
        # Створити прибульців та визначити кількість прибульців у ряду.
        # Відстань між прибульцями дорівнює ширині одного прибульця.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Визначити, яка кількість рядків прибульців поміщається на екрані.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_heigth - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Створити повний флот прибульців.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        """ Створити прибульця та поставити його до ряду."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        """
        Реагує відповідно до того, чи досяг котррийсь із прибульців краю екрана.
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Спуск всього флоту та зміна його напрямку"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    def run_game(self):
        """Розпочати головний цикл гри."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            """Наново намалювати екран на кожній ітерації циклу."""
            self._update_screen()
            

if __name__ == '__main__':
    """Створити екземпляр гри та запустити гру."""
    ai = AlienInvasion()
    ai.run_game()