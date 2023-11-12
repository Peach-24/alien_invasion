import pygame
from settings import Settings

class Ship:
    """a class to manage the ship"""

    def __init__(self, invasion) -> None:
        self.screen = invasion.screen
        self.settings = invasion.settings
        self.screen_rect = invasion.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        
        # continous movement flags
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
       """Draw the ship at its current location."""
       self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x