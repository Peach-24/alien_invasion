import sys
import pygame
from ship import Ship
from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings() 
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the (main) game loop"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # recreate screen during each pass through of loop
        self.screen.fill(self.settings.background_colour)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance, and run the game.
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
