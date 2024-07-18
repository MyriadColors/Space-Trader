"""
    Space Trader (PalmOS) | RPINerd, 2024
    
    The splash screen is the inital screen that is displayed when the game is started.
"""

import pygame


def run():
    NotImplemented


def render(canvas):
    self.canvas.blit(self.background_image, (0, 0))
    transform = pygame.transform.scale(self.canvas, (self.screen_width, self.screen_height))
    self.screen.blit(transform, (0, 0))
    pygame.display.flip()
    self.clock.tick(30)
