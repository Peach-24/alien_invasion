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

    def at_edge_of_screen(self):
        """Return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

