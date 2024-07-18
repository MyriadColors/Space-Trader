"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Utils Module
    The utils module has a couple of functions that were separated in the original codebase.
    Likely could refactor these into the respective modules, but for now they are here.
"""

from constants import MAX_WORMHOLES


def planet_distance(planet: tuple[int, int], x2: int, y2: int) -> float:
    """
    Calculate the distance between a planet and a point.

    params: planet - tuple containing the x and y coordinates of the planet
    params: x2 - x coordinate of point 2
    params: y2 - y coordinate of point 2

    returns: distance between the planet and the point
    """
    return distance(planet[0], planet[1], x2, y2)


def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """
    Calculate the distance between two points.

    params: x1 - x coordinate of point 1
    params: y1 - y coordinate of point 1
    params: x2 - x coordinate of point 2
    params: y2 - y coordinate of point 2

    returns: distance between the two points
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def wormhole_exists(wormholes: list[int], a: int, b: int) -> bool:
    """
    Check if a wormhole exists at the given coordinates.

    params: wormholes - list of wormholes
    params: a - first wormhole
    params: b - second wormhole, or -1 if only checking for any wormhole at a

    returns: True if wormhole exists, False otherwise
    """

    # TODO bit of a mess, probably should have small separate functions for each check
    if a in wormholes:

        if b < 0:
            return True

        index = wormholes.index(a)
        if index < MAX_WORMHOLES - 1:
            if wormholes[index + 1] == b:
                return True
        elif wormholes[0] == b:
            return True

    return False
