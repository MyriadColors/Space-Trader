"""
    Space Trader (PalmOS) | RPINerd, 06/27/24

    An early strategy RPG game for PalmOS, Space Trader is a game where you are a
    freelance captain, buying and selling goods to make a profit, fending off pirates,
    dealing with sector police, and occasionally ending up on intergalactic quests.

    You can travel to different planets, each with their own economy for trade. You can
    also upgrade your ship, hire crew, and take on missions to make money.

    The game is over when you run out of money, your ship is destroyed or you
    retire with the spoils of your adventures.
"""

import configparser
import os

import pygame

from src.constants import INTERNAL_RES, GameStateID
from src.interface.char_create import CharacterCreation
from src.interface.splash import Splash
from src.interface.state import State


class Game:
    """
    Class to represent the core game object.

    Handles the game loop, event handling, and rendering for each frame.

    Attributes:
        screen_width (int): The width of the game window.
        screen_height (int): The height of the game window.
        canvas (pygame.Surface): The surface to draw the game on.
        screen (pygame.Surface): The game window surface.
        config (configparser.ConfigParser): The configuration file for the game.
        running (bool): Flag to indicate if the game is running.
    """

    def __init__(self):

        # Initialize pygame
        pygame.init()

        # Load game assets
        self.load_assets()

        # Set up the game window
        self.screen_width = int(self.config["graphics"]["screen_width"])
        self.screen_height = int(self.config["graphics"]["screen_height"])
        self.canvas = pygame.Surface((INTERNAL_RES, INTERNAL_RES))
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Space Trader")
        pygame.display.set_icon(pygame.image.load("assets/images/App.ico"))

        # Establish the state management
        self.current_state = GameStateID.SPLASH
        self.previous_state = None
        self.build_states()

        self.running = True

    # Core Loop
    def run(self):
        """
        Main game loop.
        """

        while self.running:
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        """
        Handles all events in the event queue.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                self.get_state().handle_events(event)

    def update(self):
        pass

    def render(self):
        """
        Transforms the current canvas to the desired resolution and then
        renders it to the screen.
        """

        self.canvas = self.get_state().render(self.canvas)
        transform = pygame.transform.scale(self.canvas, (self.screen_width, self.screen_height))
        self.screen.blit(transform, (0, 0))
        pygame.display.flip()
        self.clock.tick(30)

    # Asset Management
    def load_assets(self):
        """
        Loads all game assets, currently just pointers to directories
        """

        # Load the configuration file
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join("src/config", "config.ini"))

        # Load the directories for the game assets
        self.images = os.path.join("assets/images/")
        self.resources = os.path.join("assets/resources/")
        # self.data = os.path.join("data")
        self.font_sm = pygame.font.Font("assets/fonts/palm-pilot-small.ttf", 8)
        self.font_sm_bold = pygame.font.Font("assets/fonts/palm-pilot-bold.ttf", 8)
        self.font_lg = pygame.font.Font("assets/fonts/palm-pilot-large.ttf", 8)
        self.font_lg_bold = pygame.font.Font("assets/fonts/palm-pilot-large-bold.ttf", 8)

    # State Management
    def get_state(self) -> State:
        """
        Returns the current gamestate
        """
        return self.__states[self.current_state]

    def get_previous_state(self) -> State:
        """
        Returns the previous gamestate
        """
        return self.__states[self.previous_state]

    def set_state(self, new_state) -> None:
        """
        Sets the new gamestate
        """
        self.previous_state = self.current_state
        self.current_state = new_state

    def build_states(self):
        """
        Builds the states for the game.
        """

        self.__states = {
            GameStateID.SPLASH: Splash(self),
            GameStateID.CHAR_CREATE: CharacterCreation(self),
        }


def main():
    """ """

    space_trader = Game()
    while space_trader.running:
        space_trader.run()
    pygame.quit()


if __name__ == "__main__":

    main()
