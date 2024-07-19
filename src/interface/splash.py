"""
    Space Trader (PalmOS) | RPINerd, 2024
    
    The splash screen is the inital screen that is displayed when the game is started.
"""

import pygame

from .state import State


class Splash(State):

    def __init__(self, game) -> None:
        super().__init__(game)
        self.background_image = pygame.image.load("assets/splash.png")

    def update(self, actions) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.manager.set_state(1)

    def render(self, canvas):
        self.canvas.blit(self.background_image, (0, 0))
        transform = pygame.transform.scale(self.canvas, (self.screen_width, self.screen_height))
        self.screen.blit(transform, (0, 0))
        pygame.display.flip()
        self.clock.tick(30)
