class Settings:
    """A class to store game settings"""

    def __init__(self):
        """Initialise game settings"""
        # Screen settins:
        self.screen_width = 1200
        self.screen_height = 800
        self.background_colour = (230,230,230)
        self.ship_speed = 10.0

        # bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction being 1 means moving right, -1 means moving left
        self.fleet_direction = 1