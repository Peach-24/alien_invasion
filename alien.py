import pygame
from settings import Settings
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class for a single alien"""

    def __init__(self, invasion):
        """Initialise the alien and set its starting position."""
        super().__init__()
        self.screen = invasion.screen
        self.settings = invasion.settings

        # load alien image and set rect attrib
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alient near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x
