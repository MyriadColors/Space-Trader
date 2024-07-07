"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Universe Module
    This module houses the classes and functions for the game universe, which subsequently
    contains all the systems, their respective governments and traits.
"""

from random import randint

from constants import GOVT_NAMES, PLANET_NAMES, Government, PlanetId, SocietalPressure, TechLevel, TradeItemType
from planet import Planet


class Universe:
    """
    The Universe class is responsible for managing the game world, including
    planets locations and attributes.
    """

    def __init__(self):
        self.systems = {}
        self.generate_systems()

    def generate_systems(self):
        """
        Generate the star systems for the game world.
        """

        for id, system_name in PLANET_NAMES:

            system_size = randint(0, 5)
            system_govt = randint(0, len(GOVT_NAMES) - 1)
            tech_level = randint()
            system_pressure
            special_resource

            # Generate system position
            x, y = randint(0, 100), randint(0, 100)

            new_system = Planet(
                system_name,
                x,
                y,
                system_size,
                system_govt,
            )

            self.systems[id] = new_system
