"""
    Space Trader (PalmOS) | RPINerd, 2024

    Game class (core)

    This is the main game class that handles the game loop, event handling, and rendering for each frame.
"""

import configparser
import os

import pygame

from .constants import INTERNAL_RES, GameStateID
from .interface.average_prices import AvgPrices
from .interface.bank import Bank
from .interface.buy_cargo import BuyCargo
from .interface.buy_equip import BuyEquipment
from .interface.buy_ship import BuyShip
from .interface.char_create import CharacterCreation
from .interface.char_status import CharInfo
from .interface.longrange import LongRange
from .interface.personnel import Personnel
from .interface.quests import Quests
from .interface.sell_cargo import SellCargo
from .interface.sell_equip import SellEquipment
from .interface.ship_info import ShipInfo
from .interface.shipyard import Shipyard
from .interface.shortrange import ShortRange
from .interface.special_cargo import SpecialCargo
from .interface.splash import Splash
from .interface.state import State
from .interface.system_info import SystemInfo
from .interface.target_system import TargetSystem


class Game:
    """
    Class to represent the core game object.

    Handles the game loop, event handling, and rendering for each frame.

    Attributes:
        canvas (pygame.Surface): The surface to draw the game on.
        screen (pygame.Surface): The game window.
        running (bool): Flag to indicate if the game is running.
    """

    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Load game assets
        self.load_assets()

        # Set up the game window
        self.screen_res = INTERNAL_RES * 5
        self.canvas = pygame.Surface((INTERNAL_RES, INTERNAL_RES))
        self.screen = pygame.display.set_mode((self.screen_res, self.screen_res))
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
                self.get_state().handle_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_event = event
                mouse_event.pos = (mouse_event.pos[0] // 5, mouse_event.pos[1] // 5)
                self.get_state().handle_events(mouse_event)

    def update(self):
        pass

    def render(self):
        """
        Transforms the current canvas to the desired resolution and then
        renders it to the screen.
        """

        self.canvas = self.get_state().render(self.canvas)
        transform = pygame.transform.scale_by(self.canvas, 5)
        self.screen.blit(transform, (0, 0))
        pygame.display.flip()
        self.clock.tick(10)

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
        self.font_sm = pygame.font.Font("assets/fonts/palm-pilot-small.ttf", 16)
        self.font_sm_bold = pygame.font.Font("assets/fonts/palm-pilot-bold.ttf", 16)
        self.font_lg = pygame.font.Font("assets/fonts/palm-pilot-large.ttf", 24)
        self.font_lg_bold = pygame.font.Font("assets/fonts/palm-pilot-large-bold.ttf", 24)

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
            GameStateID.SYSTEM_INFO: SystemInfo(self),
            GameStateID.TARGET_SYSTEM: TargetSystem(self),
            GameStateID.AVG_PRICES: AvgPrices(self),
            GameStateID.BANK: Bank(self),
            GameStateID.QUESTS: Quests(self),
            GameStateID.Y_SHIPYARD: Shipyard(self),
            GameStateID.B_CARGO: BuyCargo(self),
            GameStateID.S_CARGO: SellCargo(self),
            GameStateID.BUY_EQUIPMENT: BuyEquipment(self),
            GameStateID.SELL_EQUIPMENT: SellEquipment(self),
            GameStateID.W_SHORTRANGE: ShortRange(self),
            GameStateID.GALACTIC_CHART: LongRange(self),
            GameStateID.PERSONNEL: Personnel(self),
            GameStateID.STATUS: CharInfo(self),
            GameStateID.BUY_SHIP: BuyShip(self),
            GameStateID.SHIP_INFO: ShipInfo(self),
            GameStateID.SPECIAL_CARGO: SpecialCargo(self),
        }
