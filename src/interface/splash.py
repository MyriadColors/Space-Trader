"""
    Space Trader (PalmOS) | RPINerd, 2024

    The splash screen is the inital screen that is displayed when the game is started.
"""

import pygame

from ..constants import BKG_COLOR, GameStateID
from .state import State


class Splash(State):

    def __init__(self, game) -> None:
        self.game = game
        super().__init__(game)
        self.background_image = pygame.image.load(self.game.images + "/splash.jpg")

    def handle_events(self, event: pygame.event) -> None:
        if event.type == pygame.QUIT:
            self.game.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.game.set_state(GameStateID.CHAR_CREATE)

    def update(self, actions) -> None:
        pass

    def render(self, canvas: pygame.Surface) -> pygame.Surface:
        canvas.blit(self.background_image, (0, 0))
        return canvas
