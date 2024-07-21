"""
    Space Trader (PalmOS) | RPINerd, 2024
    
    Character creation screen
"""

import pygame

from ..constants import INTERNAL_RES, GameStateID
from .renderer import TextRender
from .state import State


class CharacterCreation(State):

    def __init__(self, game) -> None:
        self.game = game
        super().__init__(game)

    def handle_events(self, event: pygame.event) -> None:
        if event.type == pygame.QUIT:
            self.game.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.game.running = False

    def update(self, actions) -> None:
        pass

    def render(self, canvas: pygame.Surface) -> pygame.Surface:
        canvas.fill((240, 240, 240))
        pygame.draw.rect(
            canvas,
            (0, 0, 0),
            pygame.Rect(1, 1, INTERNAL_RES - 2, INTERNAL_RES - 2),
            2,
            border_radius=3,
        )
        pygame.draw.rect(canvas, TextRender("Character Creation", (10, 10), self.game.font_sm))
        return canvas
