import sys

import pygame

from hero import Hero

class BlueSky:
    """Overall class to manage the blue sky."""

    def __init__(self):
        """Initialize the game and create the sky."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Sky")
        self.bg_colour = (0, 0, 230)
        self.hero = Hero(self)

    def run_sky(self):
        """Start the loop to run the sky."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_colour)
            self.hero.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    bs = BlueSky()
    bs.run_sky()