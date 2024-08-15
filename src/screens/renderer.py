"""
    Space Trader (PalmOS) | RPINerd, 2024

    The renderer module contains classes for rendering text and UI elements to the screen.
    Elements like the header, and BSYW bar are universal elements for the game states and
    can be abstracted away here to keep the individual screens' classes clean.
"""

import pygame

from ..constants import FRG_COLOR, INTERNAL_RES


class Button:
    def __init__(
        self,
        text: str,
        pos: tuple[int, int],
        size: tuple[int, int],
        font: pygame.font.Font,
        **options,
    ) -> None:
        self.pos = pos
        self.width, self.height = size
        self.text = text
        self.font = font
        self.reference = options.get("reference", "topleft")
        self.render()

    def render(self) -> None:
        """Render the text into an image."""
        self.border = pygame.Rect(0, 0, self.width, self.height)
        self.img = self.font.render(self.text, False, FRG_COLOR)
        self.txtarea = self.img.get_rect()

        # Set the position of the button based on the reference point. For the text area, we need to center
        # it within the button so the position is adjusted based on the half-width and height of the border position.
        if self.reference == "center":
            self.border.center = self.pos
            self.txtarea.center = (self.pos[0], self.pos[1])
        elif self.reference == "topright":
            self.border.topright = self.pos
            self.txtarea.center = (
                self.pos[0] - self.width // 2,
                self.pos[1] + self.height // 2,
            )
        elif self.reference == "bottomright":
            self.border.bottomright = self.pos
            self.txtarea.center = (
                self.pos[0] + self.width // 2,
                self.pos[1] - self.height // 2,
            )
        elif self.reference == "bottomleft":
            self.border.bottomleft = self.pos
            self.txtarea.center = (
                self.pos[0] + self.width // 2,
                self.pos[1] - self.height // 2,
            )
        else:
            self.border.topleft = self.pos
            self.txtarea.center = (
                self.pos[0] + self.width // 2,
                self.pos[1] + self.height // 2,
            )

    def draw(self, canvas: pygame.Surface) -> None:
        pygame.draw.rect(canvas, FRG_COLOR, self.border, 1)
        canvas.blit(self.img, self.txtarea)

    def is_clicked(self, pos: tuple[int, int]) -> bool:
        #! Debugging print statements
        # print(self.border.topleft, self.border.bottomright)
        # print(pos)
        # print(self.border.collidepoint(pos))

        return self.border.collidepoint(pos)


class TextRender:
    """
    A self aware object that can render itself to the screen.

    Attributes:
        text (str): The text to render.
        pos (tuple[int, int]): The position to render the text.
        font (pygame.font.Font): The font to render the text in.
        pos_center (bool): Flag to center the text on the position.
        fontcolor (pygame.Color or RGB tuple): The color of the text.
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


class TextInput(pygame.sprite.Sprite):
    """A text input box for the player to enter a custom value"""

    def __init__(self, x, y, w, font: pygame.font.Font):
        super().__init__()
        self.color = (0, 0, 0)
        self.backcolor = None
        self.pos = (x, y)
        self.width = w
        self.font = font
        self.active = False
        self.text = ""
        self.render_text()

    def render_text(self):
        t_surf = self.font.render(self.text, False, self.color, self.backcolor)
        self.image = pygame.Surface(
            (max(self.width, t_surf.get_width() + 10), t_surf.get_height() + 10), pygame.SRCALPHA
        )
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (5, 5))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.render_text()


def divider(canvas: pygame.Surface, y: int) -> None:
    """
    Draws a horizontal divider line on the screen at the specified y position.
    """
    pygame.draw.line(canvas, FRG_COLOR, (1, y), (INTERNAL_RES - 2, y), 2)
