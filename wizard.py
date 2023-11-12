import pygame

class Wizard:
    """a class to manage the Wizard"""

    def __init__(self, ai_game) -> None:
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the Wizard image and get its rect.
        self.image = pygame.image.load('images/wizard.bmp')
        self.rect = self.image.get_rect()

        # Start each new Wizard at the bottom center of the screen.
        self.rect.center= self.screen_rect.center

    def blitme(self):
       """Draw the Wizard at its current location."""
       self.screen.blit(self.image, self.rect)