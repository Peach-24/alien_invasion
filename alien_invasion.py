import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        # surface : The surface returned by display.set_mode() represents the entire game window.
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color
        self.background_colour = (240,230,220)

    def run_game(self):
        """Start the (main) game loop"""
        while True:
            # .tick() takes one arg - frame rate for the game
            self.clock.tick(60)
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    sys.exit()

            # recreate screen during each pass through of loop
            self.screen.fill(self.background_colour)
        
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, and run the game.
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
    