"""
    Space Trader (PalmOS) | RPINerd, 2024

    
"""

import pygame

from ..constants import INTERNAL_RES, GameStateID
from .renderer import Header, TextRender, TitleBar
from .state import State


class <state>(State):

    def __init__(self, game) -> None:
        self.game = game
        self.head_font: pygame.font.Font = game.font_sm_bold
        self.font: pygame.font.Font = game.font_sm
        super().__init__(game)

    def handle_events(self, event: pygame.event) -> None:
        if event.type == pygame.QUIT:
            self.game.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.game.current_state = GameStateID.SPLASH
            if event.key == pygame.K_ESCAPE:
                self.game.current_state = GameStateID.SPLASH

    def update(self, actions) -> None:
        pass

    def render(self, canvas: pygame.Surface) -> pygame.Surface:
        canvas.fill((240, 240, 240))

        # Draw the header
        header = Header(canvas)
        header.render()
        title = TitleBar("<state>", self.head_font, canvas)
        title.render()

        return canvas
