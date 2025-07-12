"""
    Space Trader (PalmOS) | RPINerd, 2024

    The thought with this file is to have a universal file that contains all the
    actions that the user can take in the game.
    In theory we can then just tie any UI into the functions of the game and not
    have to worry about rewriting the game logic.
"""

import src.constants as c
import src.economy as e


# Disordered list of user interactions
def get_system_info() -> tuple[list[str], str]:
    """"""
    current_planet = c.GAME["universe"].planets[c.GAME["commander"].currentSystem]

    sys_info = current_planet.system_info()

    # Format system pressure
    pressure = current_planet.get_pressure()
    pressure_str = f"System is {c.SocietalPressure.name(pressure)}"

    return sys_info, pressure_str


def get_commander_info() -> dict:
    """
    Returns a dictionary of the commander's information
    """
    commander = c.GAME["commander"]
    return {
        "name": commander.name,
        "pilot": (commander.pilotSkill, commander.pilotSkill),
        "fighter": (commander.fighterSkill, commander.fighterSkill),
        "trader": (commander.traderSkill, commander.traderSkill),
        "engineer": (commander.engineerSkill, commander.engineerSkill),
        "kills": commander.kills,
        "time": commander.timePlayed,
        "cash": commander.credits,
        "debt": commander.debt,
        "net_worth": commander.get_net_worth(),
        "rep": commander.get_reputation(),
        "record": commander.get_police_record(),
        "difficulty": c.GAME["difficulty"],
    }


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


def get_debt() -> str:
    return f"{c.GAME["commander"].debt} cr."


def get_max_loan() -> str:
    # TODO this is a placeholder, figure out how this is calculated in soruce
    return f"{c.GAME["commander"].get_net_worth()} cr."


def repair():
    pass


def buy_pod():
    pass


def get_ware_list() -> list[str]:
    return e.Ware.lst()


def get_bays() -> str:
    # TODO placeholder value, not currently tracked
    # return f"{c.GAME["commander"].ship.bays} bays"
    return "Bays: 3/25"


def buy_good():
    pass


def sell_good():
    pass


def buy_ship():
    pass


def get_equip_sold() -> list[str]:
    # Make an list of equipment sold by the current system, with 'x' for ones not sold
    current_system_tech = c.GAME["universe"].planets[c.GAME["commander"].currentSystem].tech_level
    sold_equipment: list[tuple[str, str, str]] = []
    for equips in [e.WEAPONS, e.SHIELDS, e.GADGETS]:
        for _, equip in equips.items():
            if equip.tech_level == e.TechLevel.UNAVAILABLE:
                continue
            if equip.tech_level <= current_system_tech:
                sold_equipment.append(("", equip.name, f"{equip.price} cr."))
            else:
                sold_equipment.append(("x", equip.name, "not sold"))
    return sold_equipment


def buy_equipment():
    pass


def sell_equipment():
    pass


def hire_crew():
    pass


def fire_crew():
    pass


def get_credits() -> str:
    current_balance = c.GAME["commander"].credits
    print(f"Current balance: {current_balance}")
    return f"Cash: {current_balance} cr."


def get_formatted_credits() -> str:
    """Return just the credit amount with currency suffix"""
    return f"{c.GAME['commander'].credits} cr."


def get_formatted_debt() -> str:
    """Return just the debt amount with currency suffix"""
    return f"{c.GAME['commander'].debt} cr."


def get_financial_status() -> dict:
    """Return complete financial status for comprehensive display"""
    commander = c.GAME["commander"]
    return {
        "credits": commander.credits,
        "debt": commander.debt,
        "net_worth": commander.get_net_worth(),
        "credits_text": f"Cash: {commander.credits} cr.",
        "debt_text": f"Debt: {commander.debt} cr.",
        "net_worth_text": f"Net Worth: {commander.get_net_worth()} cr."
    }


def get_ship_value() -> str:
    return f"{c.GAME["commander"].ship.get_value()} cr."


def get_no_claim() -> str:
    # TODO placeholder until I figure out how this is calculated in source
    return "0%"


def get_insurance_rate() -> str:
    return f"{c.INSURANCE_RATE * c.GAME["commander"].ship.get_value()} cr. daily"


def buy_insurance():
    # TODO
    print("Buying insurance!")


def get_loan():
    # TODO
    print("Getting a loan!")
