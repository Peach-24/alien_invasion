import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """a class to manage the bullet"""

    def __init__(self, invasion):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = invasion.screen
        self.settings = invasion.settings
        self.colour = self.settings.bullet_colour

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = invasion.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
       self.y -= self.settings.bullet_speed
       self.rect.y = self.y

    def draw_bullet(self):
       pygame.draw.rect(self.screen, self.colour, self.rect)
