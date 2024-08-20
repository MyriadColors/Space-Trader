"""
    Space Trader (PalmOS) | RPINerd, 2024

    The thought with this file is to have a universal file that contains all the
    actions that the user can take in the game.
    In theory we can then just tie any UI into the functions of the game and not
    have to worry about rewriting the game logic.
"""

from random import randint

import src.constants as c


# Disordered list of user interactions
def get_system_info():
    global current_system

    # Format system pressure
    #!pressure = current_system.pressure
    pressure = randint(0, 7)  # Placeholder
    pressure_str = f"System is {c.SocietalPressure.name(pressure)}"

    return pressure_str


def buy_fuel():
    pass


def buy_news():
    print("Buying news!")


def warp():
    pass


def attack():
    pass


def flee():
    pass


def ignore():
    pass


def orbit_trade():
    """This is when a trader encounter requests to trade with the player"""
    pass


def repair():
    pass


def buy_pod():
    pass


def buy_good():
    pass


def sell_good():
    pass


def buy_ship():
    pass


def buy_equipment():
    pass


def sell_equipment():
    pass


def hire_crew():
    pass


def fire_crew():
    pass


def buy_insurance():
    pass


def get_loan():
    pass
