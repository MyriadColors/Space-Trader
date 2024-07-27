"""
    Space Trader (PalmOS) | RPINerd, 2024

    Buy Cargo Screen
"""

import pygame

from ..constants import BKG_COLOR, GameStateID
from ..economy import TradeItemId
from .renderer import Header, TextRender, TitleBar
from .state import State


class BuyCargo(State):

    def __init__(self, game) -> None:
        self.game = game
        self.head_font: pygame.font.Font = game.font_sm_bold
        self.font: pygame.font.Font = game.font_sm
        super().__init__(game)

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

    def update(self, actions) -> None:
        pass

    def render(self, canvas: pygame.Surface) -> pygame.Surface:
        canvas.fill(BKG_COLOR)

        # Draw the header
        header = Header(canvas, self.font)
        header.render()
        title = TitleBar("Buy Cargo", self.head_font, canvas)
        title.render()

        # Draw the cargo list
        i = 0
        for good in TradeItemId.lst():
            TextRender(good, (30, 18 + i), self.font).draw(canvas)
            i += 13

        TextRender("Bays: {}/{}", (2, 158), self.font, ref="bottomleft").draw(canvas)
        TextRender("Cash: {} cr.", (154, 158), self.font, ref="bottomright").draw(canvas)

        return canvas
