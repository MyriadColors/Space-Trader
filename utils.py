"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Utils Module
    The utils module has a couple of functions that were separated in the original codebase.
    Likely could refactor these into the respective modules, but for now they are here.
"""


# TODO placeholder till I figure out what this function does
def array_index_of(x, y):
    """"""
    return x + y * 10


def distance(x1, y1, x2, y2):
    """
    Calculate the distance between two points.

    params: x1 - x coordinate of point 1
    params: y1 - y coordinate of point 1
    params: x2 - x coordinate of point 2
    params: y2 - y coordinate of point 2

    returns: distance between the two points
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def wormhole_exists(wormholes, x, y):
    """
    Check if a wormhole exists at the given coordinates.

    params: wormholes - list of wormholes
    params: x - x coordinate
    params: y - y coordinate

    returns: True if wormhole exists, False otherwise
    """
    return wormholes[x + y * 10] == 1
