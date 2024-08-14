"""
    Space Trader (PalmOS) | RPINerd, 2024

    Basic system information screen
"""

import pygame

from ..constants import BKG_COLOR, GameStateID
from .renderer import Header, TextRender, TitleBar
from .state import State


class SystemInfo(State):

    def __init__(self, game) -> None:
        self.game = game
        self.head_font: pygame.font.Font = game.font_sm_bold
        self.font: pygame.font.Font = game.font_sm
        super().__init__(game)

        self.header = Header(self.game.canvas, self.font)
        self.buttonB, self.buttonS, self.buttonY, self.buttonW = self.header.get_buttons()

    def handle_events(self, event: pygame.event) -> None:
        if event.type == pygame.QUIT:
            self.game.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.current_state = GameStateID.SPLASH
            if event.key == pygame.K_b:
                self.game.current_state = GameStateID.B_CARGO
            if event.key == pygame.K_s:
                self.game.current_state = GameStateID.S_CARGO
            if event.key == pygame.K_y:
                self.game.current_state = GameStateID.Y_SHIPYARD
            if event.key == pygame.K_e:
                self.game.current_state = GameStateID.BUY_EQUIPMENT
            if event.key == pygame.K_q:
                self.game.current_state = GameStateID.SELL_EQUIPMENT
            if event.key == pygame.K_p:
                self.game.current_state = GameStateID.PERSONNEL
            if event.key == pygame.K_k:
                self.game.current_state = GameStateID.BANK
            if event.key == pygame.K_i:
                self.game.current_state = GameStateID.SYSTEM_INFO
            if event.key == pygame.K_c:
                self.game.current_state = GameStateID.STATUS
            if event.key == pygame.K_g:
                self.game.current_state = GameStateID.GALACTIC_CHART
            if event.key == pygame.K_w:
                self.game.current_state = GameStateID.W_SHORTRANGE
            if event.key == pygame.K_o:
                NotImplemented
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.buttonB.is_clicked(event.pos):
                print("Clicked B")
                self.game.current_state = GameStateID.B_CARGO
            if self.buttonS.is_clicked(event.pos):
                print("Clicked S")
                self.game.current_state = GameStateID.S_CARGO
            if self.buttonY.is_clicked(event.pos):
                print("Clicked Y")
                self.game.current_state = GameStateID.Y_SHIPYARD
            if self.buttonW.is_clicked(event.pos):
                print("Clicked W")
                self.game.current_state = GameStateID.W_SHORTRANGE

    def update(self, actions) -> None:
        pass

    def render(self, canvas: pygame.Surface) -> pygame.Surface:
        canvas.fill(BKG_COLOR)

        # Draw the header
        # Header(canvas, self.font)
        self.header.render()
        TitleBar("System Info", self.head_font, canvas)

        # Category headers
        categories: list[TextRender] = []
        categories.append(TextRender("Name:", (1, 18), self.head_font))
        categories.append(TextRender("Size:", (1, 38), self.head_font))
        categories.append(TextRender("Tech Level:", (1, 58), self.head_font))
        categories.append(TextRender("Government:", (1, 78), self.head_font))
        categories.append(TextRender("Resources:", (1, 98), self.head_font))
        categories.append(TextRender("Police:", (1, 118), self.head_font))
        categories.append(TextRender("Pirates:", (1, 138), self.head_font))

        for category in categories:
            category.draw(canvas)

        return canvas
