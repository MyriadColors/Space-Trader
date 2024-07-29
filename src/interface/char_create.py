"""
    Space Trader (PalmOS) | RPINerd, 2024

    Character creation screen
"""

import pygame

from ..constants import BKG_COLOR, CIRCLE_XY, FRG_COLOR, HALF_RES, INTERNAL_RES, GameStateID
from .renderer import Button, TextRender
from .state import State


class CharacterCreation(State):

    def __init__(self, game) -> None:
        self.game = game
        self.head_font: pygame.font.Font = game.font_sm_bold
        self.font: pygame.font.Font = game.font_sm
        super().__init__(game)

        self._curr_difficulty = 2
        self._curr_points = 16
        self._curr_pilot = 1
        self._curr_fighter = 1
        self._curr_trader = 1
        self._curr_engineer = 1

        self._inc_difficulty = Button("+", (HALF_RES + 40, 48), CIRCLE_XY, self.font)
        self._dec_difficulty = Button("-", (HALF_RES - 20, 48), CIRCLE_XY, self.font)

        self._inc_pilot = Button("+", (HALF_RES + 10, 80), CIRCLE_XY, self.font)
        self._dec_pilot = Button("-", (HALF_RES - 20, 80), CIRCLE_XY, self.font)
        self._inc_fighter = Button("+", (HALF_RES + 10, 92), CIRCLE_XY, self.font)
        self._dec_fighter = Button("-", (HALF_RES - 20, 92), CIRCLE_XY, self.font)
        self._inc_trader = Button("+", (HALF_RES + 10, 104), CIRCLE_XY, self.font)
        self._dec_trader = Button("-", (HALF_RES - 20, 104), CIRCLE_XY, self.font)
        self._inc_engineer = Button("+", (HALF_RES + 10, 116), CIRCLE_XY, self.font)
        self._dec_engineer = Button("-", (HALF_RES - 20, 116), CIRCLE_XY, self.font)

        self._buttons = [
            self._inc_difficulty,
            self._dec_difficulty,
            self._inc_pilot,
            self._dec_pilot,
            self._inc_fighter,
            self._dec_fighter,
            self._inc_trader,
            self._dec_trader,
            self._inc_engineer,
            self._dec_engineer,
        ]
        self._curr_values = [
            self._curr_points,
            self._curr_pilot,
            self._curr_fighter,
            self._curr_trader,
            self._curr_engineer,
        ]

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
        prompt_text.append(TextRender("Name:", (10, 20), self.font))
        prompt_text.append(TextRender("Difficulty:", (10, 40), self.font))
        prompt_text.append(TextRender("Skill Points:", (10, 65 + 14 * 0), self.font))
        prompt_text.append(TextRender("Pilot:", (10, 65 + 14 * 1), self.font))
        prompt_text.append(TextRender("Fighter:", (10, 65 + 14 * 2), self.font))
        prompt_text.append(TextRender("Trader:", (10, 65 + 14 * 3), self.font))
        prompt_text.append(TextRender("Engineer:", (10, 65 + 14 * 4), self.font))

        for text in prompt_text:
            text.draw(canvas)

        # Buttons
        for button in self._buttons:
            button.draw(canvas)

        # Draw the current values
        for idx, value in enumerate(self._curr_values):
            value_text = TextRender(str(value), (HALF_RES, 65 + (idx * 14)), self.font)
            value_text.draw(canvas)

        return canvas
