"""
    Space Trader (PalmOS) | RPINerd, 2024

    The renderer module contains classes for rendering text and UI elements to the screen.
    Elements like the header, and BSYW bar are fairly universal elements and
    can be abstracted away here to keep the individual screens' classes clean.
"""

import pygame
from pygame.locals import Color

from ..constants import INTERNAL_RES


class TextRender:
    """
    A self aware object that can render itself to the screen.

    Attributes:
        text (str): The text to render.
        pos (tuple[int, int]): The position to render the text.
        font (pygame.font.Font): The font to render the text in.
        pos_center (bool): Flag to center the text on the position.
        fontcolor (pygame.Color): The color of the text.
        img (pygame.Surface): The rendered text image.
        rect (pygame.Rect): The bounding rectangle
    """

    def __init__(self, text, pos, font, **options):
        self.text: str = text
        self.pos: tuple[int, int] = pos
        self.font: pygame.font.Font = font
        self.pos_center = options.get("center", False)
        self.fontcolor = options.get("fontcolor", Color("black"))
        self.render()

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, False, self.fontcolor)
        self.rect = self.img.get_rect()
        if self.pos_center:
            self.rect.center = self.pos
        else:
            self.rect.topleft = self.pos

    def draw(self, canvas: pygame.Surface):
        """Draw the text to the screen."""
        canvas.blit(self.img, self.rect)


class Header:
    """
    Renders the core header for vast majority of screens in the game.
    This includes the underline, as well as the BSYW button
    outlines for the top right.

    Underline - 2px thick, starts 14px from the top of the screen
    BSYW Button - 14px by 13px squares, 1px from the top right corner
    """

    def __init__(self, canvas):
        self.canvas: pygame.Surface = canvas
        self.underline = pygame.Rect(1, 14, 158, 2)
        self.buttonB = pygame.Rect(0, 0, 14, 13)
        self.buttonS = pygame.Rect(0, 0, 14, 13)
        self.buttonY = pygame.Rect(0, 0, 14, 13)
        self.buttonW = pygame.Rect(0, 0, 14, 13)
        self.buttonB.topright = (INTERNAL_RES - 1, 1)
        self.buttonS.topright = (self.buttonB.topleft[0] + 1, self.buttonB.topleft[1])
        self.buttonY.topright = (self.buttonS.topleft[0] + 1, self.buttonS.topleft[1])
        self.buttonW.topright = (self.buttonY.topleft[0] + 1, self.buttonY.topleft[1])
        self.render()

    def render(self):
        pygame.draw.rect(self.canvas, Color("black"), self.underline)
        pygame.draw.rect(self.canvas, Color("black"), self.buttonB, 1)
        pygame.draw.rect(self.canvas, Color("black"), self.buttonS, 1)
        pygame.draw.rect(self.canvas, Color("black"), self.buttonY, 1)
        pygame.draw.rect(self.canvas, Color("black"), self.buttonW, 1)


class TitleBar:
    """
    Renders the title bar for the top of the screen (e.g. Sell Cargo, System Info, etc.)
    """

    def __init__(self, title: str, font: pygame.font.Font, canvas: pygame.Surface):
        self.canvas = canvas
        self.title = title
        self.font = font
        self.text = TextRender(title, (4, 3), font, fontcolor=(240, 240, 240))
        self.text_width = self.text.rect.size[0]
        self.bar = pygame.Rect(1, 2, self.text_width + 5, 14)
        self.top_bar = pygame.Rect(2, 1, self.text_width + 3, 1)
        self.render()

    def render(self):
        pygame.draw.rect(self.canvas, Color("black"), self.bar)
        pygame.draw.rect(self.canvas, Color("black"), self.top_bar)
        self.text.draw(self.canvas)
