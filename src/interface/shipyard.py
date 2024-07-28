"""
    Space Trader (PalmOS) | RPINerd, 2024

    Shipyard Screen
    Counterintuitively, not actually where you buy ships.
    Houses refuel, repair, escape pod purchase and then link to ship sales.
"""

import pygame

from ..constants import BKG_COLOR, GameStateID
from .renderer import Header, TextRender, TitleBar
from .state import State

FUEL_STATUS = "You have fuel to fly {0} parsecs."
FULL_TANK = "Your tank cannot hold more fuel."
HULL_STATUS = "Your hull strength is at {0}%."
FULL_HULL = "No repairs are needed."
SHIP_SALES = "No new ships are for sale."
ESCAPE_POD = "No escape pods are for sale."


class Shipyard(State):

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
        title = TitleBar("Shipyard", self.head_font, canvas)
        title.render()

        # Draw the text
        TextRender(FUEL_STATUS.format(0), (2, 30), self.font).draw(canvas)
        TextRender(FULL_TANK, (2, 50), self.font).draw(canvas)
        TextRender(HULL_STATUS.format(100), (2, 70), self.font).draw(canvas)
        TextRender(FULL_HULL, (2, 90), self.font).draw(canvas)
        TextRender(SHIP_SALES, (2, 110), self.font).draw(canvas)
        TextRender(ESCAPE_POD, (2, 130), self.font).draw(canvas)
        TextRender("Cash: {} cr.", (154, 158), self.font, ref="bottomright").draw(canvas)

        return canvas
