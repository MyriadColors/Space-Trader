"""
    Space Trader (PalmOS) | RPINerd, 2024

    Character creation screen
"""

import pygame

from ..constants import BKG_COLOR, FRG_COLOR, INTERNAL_RES, GameStateID
from .renderer import TextRender
from .state import State


class CharacterCreation(State):

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
                self.game.running = False
            if event.key == pygame.K_ESCAPE:
                self.game.current_state = GameStateID.SPLASH
            if event.key == pygame.K_RETURN:
                self.game.current_state = GameStateID.SYSTEM_INFO

    def update(self, actions) -> None:
        pass

    def render(self, canvas: pygame.Surface) -> pygame.Surface:

        # Background
        canvas.fill(BKG_COLOR)

        # Border
        pygame.draw.rect(
            canvas,
            FRG_COLOR,
            pygame.Rect(1, 1, INTERNAL_RES - 2, INTERNAL_RES - 2),
            2,
            border_radius=3,
        )

        # Header
        pygame.draw.rect(
            canvas,
            FRG_COLOR,
            pygame.Rect(3, 1, INTERNAL_RES - 6, 14),
        )
        header_text = TextRender(
            "New Commander", (INTERNAL_RES // 2, 8), self.head_font, ref="center", fontcolor=BKG_COLOR
        )
        header_text.draw(canvas)

        prompt_text: list[TextRender] = []
        prompt_text.append(TextRender("Name:", (10, 28), self.font))
        prompt_text.append(TextRender("Difficulty:", (10, 48), self.font))
        prompt_text.append(TextRender("Skill Points:", (10, 68), self.font))
        prompt_text.append(TextRender("Pilot:", (10, 80), self.font))
        prompt_text.append(TextRender("Fighter:", (10, 92), self.font))
        prompt_text.append(TextRender("Trader:", (10, 104), self.font))
        prompt_text.append(TextRender("Engineer:", (10, 116), self.font))

        for text in prompt_text:
            text.draw(canvas)

        return canvas
