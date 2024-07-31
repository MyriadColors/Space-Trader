"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Universe Module
    This module houses the classes and functions for the game universe, which subsequently
    contains all the systems, their respective governments and traits.
"""

from random import choice, randint

from .constants import (
    GALAXYHEIGHT,
    GALAXYWIDTH,
    MIN_DISTANCE,
    PLANET_NAMES,
    SECTOR_DIAMETER,
    SocietalPressure,
    SpecialResource,
)
from .game_data import GOVERNMENTS
from .planet import Planet
from .utils import planet_distance, wormhole_exists


class Universe:
    """
    Responsible for managing the game world, including
    planets locations and attributes.
    """

    def __init__(self):
        self.planets: dict[int, Planet] = {}
        self.wormholes: list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.generate_planets()
        self.extra_planet_shuffle()

    def generate_planets(self):
        """
        Generate the planets for the game world.
        """

        for id, planet_name in PLANET_NAMES.items():

            planet_size = randint(0, 5)
            planet_govt = choice(GOVERNMENTS)

            # TODO can transition this to a choice of valid_tech_levels
            # print(planet_govt.minTech, planet_govt.maxTech)
            tech_level = randint(planet_govt.minTech, planet_govt.maxTech)

            # As per the original code, ~15% of planets have no societal pressure
            if randint(1, 100) >= 15:
                soci_pressure = SocietalPressure.NONE
            else:
                soci_pressure = randint(1, 7)

            # As per the original code, ~40% of planets have no special resource
            if randint(1, 5) < 3:
                special_resource = SpecialResource.NOTHING
            else:
                special_resource = randint(1, 12)

            # Generate system position
            x, y = self.pick_valid_xy(id)

            new_planet = Planet(
                planet_name, x, y, planet_size, planet_govt, tech_level, soci_pressure, special_resource
            )

            self.planets[id] = new_planet

    def pick_valid_xy(self, id: int) -> tuple[int, int]:
        """
        Pick a valid x, y coordinate for a new planet

        This first pass is as close a 1:1 translation as possible,
        there is likely a good way to refactor this, if nothing else as a
        good exercise in algorithm design!
        """

        x, y = 0, 0

        # Place the first planet somewhere in the center of the galaxy
        if id < len(self.wormholes):
            x = ((GALAXYWIDTH * (1 + 2 * (id % 3))) / 6) - randint(-SECTOR_DIAMETER + 1, SECTOR_DIAMETER)
            y = ((GALAXYHEIGHT * (1 if id < 3 else 3)) / 4) - randint(-SECTOR_DIAMETER + 1, SECTOR_DIAMETER)
            self.wormholes[id] = id

        else:
            valid = False
            while not valid:
                x = randint(1, GALAXYWIDTH)
                y = randint(1, GALAXYHEIGHT)

                close_found = False
                too_close = False
                j = 0
                while j < id and not too_close:

                    # Minimum distance between any two systems not to be accepted.
                    if planet_distance(self.planets[j].get_location(), x, y) < MIN_DISTANCE:
                        too_close = True

                    # There should be at least one system which is close enough.
                    if planet_distance(self.planets[j].get_location(), x, y) < SECTOR_DIAMETER:
                        close_found = True

                    j += 1

                valid = close_found and not too_close

        return (x, y)

    def extra_planet_shuffle(self):
        """
        This function is responsible for shuffling the planets around the universe.
        Apparently without this extra step, the planets with names at the beginning
        of the alphabet are all clustered in the center of the galaxy.
        """

        for planet in self.planets.values():
            i = randint(0, len(self.planets) - 1)
            if not wormhole_exists(self.wormholes, i, -1):
                planet.x, self.planets[i].x = self.planets[i].x, planet.x
                planet.y, self.planets[i].y = self.planets[i].y, planet.y
                hole = self.wormholes.index(i) if i in self.wormholes else -1
                if hole >= 0:
                    self.wormholes[hole] = i

        # Randomize wormhole order
        for wh in self.wormholes:
            new_index = randint(0, len(self.wormholes) - 1)
            wh, self.wormholes[new_index] = self.wormholes[new_index], wh
