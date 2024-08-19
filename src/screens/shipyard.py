"""
    Space Trader (PalmOS) | RPINerd, 2024

    Shipyard Screen
    Counterintuitively, not actually where you buy ships.
    Houses refuel, repair, escape pod purchase and then link to ship sales.
"""

import pygame

from ..constants import BKG_COLOR
from ..game_data import ShipID
from .screens import Screen

FUEL_STATUS = "You have fuel to fly {0} parsecs."
FULL_TANK = "Your tank cannot hold more fuel."
HULL_STATUS = "Your hull strength is at {0}%."
FULL_HULL = "No repairs are needed."
SHIP_SALES = "No new ships are for sale."
ESCAPE_POD = "No escape pods are for sale."


class Shipyard(Screen):

    def __init__(self, game) -> None:
        self.game = game
        self.head_font: pygame.font.Font = game.font_sm_bold
        self.font: pygame.font.Font = game.font_sm
        super().__init__(game)

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


class BuyShip(Screen):

    def __init__(self, game) -> None:
        self.game = game
        self.head_font: pygame.font.Font = game.font_sm_bold
        self.font: pygame.font.Font = game.font_sm
        super().__init__(game)

    def render(self, canvas: pygame.Surface) -> pygame.Surface:
        canvas.fill(BKG_COLOR)

        # Draw the header
        header = Header(canvas, self.font)
        header.render()
        title = TitleBar("Buy Ship", self.head_font, canvas)
        title.render()

        # Draw avaialble ships
        i = 0
        for ship in ShipID.sale_lst():
            TextRender(ship, (35, 18 + i), self.font).draw(canvas)
            i += 13

        TextRender("Cash: {0} cr.", (154, 158), self.font, ref="bottomleft").draw(canvas)

        return canvas
