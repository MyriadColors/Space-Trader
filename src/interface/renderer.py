"""
    Space Trader (PalmOS) | RPINerd, 2024

    The renderer module contains classes for rendering text and UI elements to the screen.
    Elements like the header, and BSYW bar are universal elements for the game states and
    can be abstracted away here to keep the individual screens' classes clean.
"""

import pygame

from ..constants import BKG_COLOR, FRG_COLOR, INTERNAL_RES


class Button:

    def __init__(
        self, text: str, pos: tuple[int, int], size: tuple[int, int], font: pygame.font.Font, **options
    ) -> None:
        self.pos = pos
        self.width, self.height = size
        self.text = text
        self.font = font
        self.reference = options.get("ref", "topleft")
        self.render()

    def render(self) -> None:
        """Render the text into an image."""
        self.img = self.font.render(self.text, False, FRG_COLOR)
        self.rect = self.img.get_rect(center=(self.pos[0] + self.width // 2, self.pos[1] + self.height // 2))
        if self.reference == "center":
            self.rect.center = self.pos
        elif self.reference == "topright":
            self.rect.topright = self.pos
        elif self.reference == "bottomright":
            self.rect.bottomright = self.pos
        elif self.reference == "bottomleft":
            self.rect.bottomleft = self.pos
        else:
            self.rect.topleft = self.pos

    def draw(self, canvas: pygame.Surface) -> None:
        pygame.draw.rect(canvas, FRG_COLOR, (self.pos[0], self.pos[1], self.width, self.height), 1)
        canvas.blit(self.img, self.rect)


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

    def __init__(self, text: str, pos: tuple[int, int], font: pygame.font.Font, **options) -> None:
        self.text = text
        self.pos = pos
        self.font = font
        self.reference = options.get("ref", "topleft")
        self.fontcolor = options.get("fontcolor", FRG_COLOR)
        self.render()

    def render(self) -> None:
        """Render the text into an image."""
        self.img = self.font.render(self.text, False, self.fontcolor)
        self.rect = self.img.get_rect()
        if self.reference == "center":
            self.rect.center = self.pos
        elif self.reference == "topright":
            self.rect.topright = self.pos
        elif self.reference == "bottomright":
            self.rect.bottomright = self.pos
        elif self.reference == "bottomleft":
            self.rect.bottomleft = self.pos
        else:
            self.rect.topleft = self.pos

    def draw(self, canvas: pygame.Surface) -> None:
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

    def __init__(self, canvas: pygame.Surface, font: pygame.font.Font) -> None:
        self.canvas = canvas
        self.underline = pygame.Rect(1, 14, 158, 2)

        self.buttonB = Button("B", (INTERNAL_RES - 1, 1), (14, 13), font, reference="topright")
        self.buttonS = pygame.Rect(0, 0, 14, 13)
        self.buttonY = pygame.Rect(0, 0, 14, 13)
        self.buttonW = pygame.Rect(0, 0, 14, 13)
        self.buttonS.topright = (self.buttonB.rect.topleft[0] + 1, self.buttonB.rect.topleft[1])
        self.buttonY.topright = (self.buttonS.topleft[0] + 1, self.buttonS.topleft[1])
        self.buttonW.topright = (self.buttonY.topleft[0] + 1, self.buttonY.topleft[1])
        self.render()

    def render(self) -> None:
        pygame.draw.rect(self.canvas, FRG_COLOR, self.underline)
        # pygame.draw.rect(self.canvas, FRG_COLOR, self.buttonB, 1)
        self.buttonB.draw(self.canvas)
        pygame.draw.rect(self.canvas, FRG_COLOR, self.buttonS, 1)
        pygame.draw.rect(self.canvas, FRG_COLOR, self.buttonY, 1)
        pygame.draw.rect(self.canvas, FRG_COLOR, self.buttonW, 1)


class TitleBar:
    """
    Renders the title bar for the top of the screen (e.g. Sell Cargo, System Info, etc.)
    """

    def __init__(self, title: str, font: pygame.font.Font, canvas: pygame.Surface) -> None:
        self.canvas = canvas
        self.title = title
        self.font = font
        self.text = TextRender(title, (4, 3), font, fontcolor=BKG_COLOR)
        self.text_width = self.text.rect.size[0]
        self.bar = pygame.Rect(1, 2, self.text_width + 5, 14)
        self.top_bar = pygame.Rect(2, 1, self.text_width + 3, 1)
        self.render()

    def render(self) -> None:
        pygame.draw.rect(self.canvas, FRG_COLOR, self.bar)
        pygame.draw.rect(self.canvas, FRG_COLOR, self.top_bar)
        self.text.draw(self.canvas)


def divider(canvas: pygame.Surface, y: int) -> None:
    """
    Draws a horizontal divider line on the screen at the specified y position.
    """
    pygame.draw.line(canvas, FRG_COLOR, (1, y), (INTERNAL_RES - 1, y), 2)
