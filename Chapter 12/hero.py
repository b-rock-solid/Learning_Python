import pygame

class Hero:
    """A class to manage the hero."""


    def __init__(self, bs_game):
        """Initialize the hero and set its starting position."""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        self.image = pygame.image.load('images/super-man.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw hero at its current location."""
        self.screen.blit(self.image, self.rect)