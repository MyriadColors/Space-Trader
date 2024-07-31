"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Ships Module
    This module contains the classes and functions for the game ships, weapons, shields and gadgets.
"""


class ShipID:
    # ESCAPEPOD = 0 #? Not in source
    FLEA = 0
    GNAT = 1
    FIREFLY = 2
    MOSQUITO = 3
    BUMBLEBEE = 4
    BEETLE = 5
    HORNET = 6
    GRASSHOPPER = 7
    TERMITE = 8
    WASP = 9
    SPACEMONSTER = 10
    DRAGONFLY = 11
    MANTIS = 12
    SCARAB = 13
    BOTTLE = 14
    CUSTOM = 15
    SCORPION = 16

    @staticmethod
    def enum() -> list[int]:
        return range(17)

    @staticmethod
    def lst() -> list[str]:
        return [
            "Flea",
            "Gnat",
            "Firefly",
            "Mosquito",
            "Bumblebee",
            "Beetle",
            "Hornet",
            "Grasshopper",
            "Termite",
            "Wasp",
            "Space Monster",
            "Dragonfly",
            "Mantis",
            "Scarab",
            "Bottle",
            "Custom",
            "Scorpion",
        ]

    @staticmethod
    def sale_lst() -> list[str]:
        return [
            "Flea",
            "Gnat",
            "Firefly",
            "Mosquito",
            "Bumblebee",
            "Beetle",
            "Hornet",
            "Grasshopper",
            "Termite",
            "Wasp",
        ]


class EquipmentType:
    WEAPON = 0
    SHIELD = 1
    GADGET = 2


class GadgetID:
    CARGOBAYS = 0
    AUTOREPAIR = 1
    NAVIGATION = 2
    TARGETING = 3
    CLOAKING = 4
    FUELCOMPACTOR = 5
    SMUGGLERHOLD = 6


class WeaponID:
    PULSELASER = 0
    BEAMLASER = 1
    MILITARYLASER = 2
    MORGANSLASER = 3
    PHOTONDISRUPTOR = 4
    QUANTUMDISRUPTOR = 5


class SheildID:
    ENERGY = 0
    REFLECTIVE = 1
    LIGHTNING = 2


class Equipment:

    def __init__(self, id, price, tech_level):
        self.id = id
        self.price = price
        self.tech_level = tech_level

    @staticmethod
    def sale_list() -> list[str]:
        return [
            "Pulse laser",
            "Beam laser",
            "Military laser",
            "Energy shield",
            "Reflective shield",
            "5 extra cargo bays",
            "Auto-repair system",
            "Navigation system",
            "Targeting system",
            "Cloaking device",
        ]


class Weapon(Equipment):

    def __init__(self, id, damage, unk_bool, price, tech_level, unknown):
        super().__init__(id, price, tech_level)
        self.damage = damage
        self.unk_bool = unk_bool
        self.unknown = unknown


class Shield(Equipment):

    # TODO what are points and unknown?
    def __init__(self, id, points, price, tech_level, unknown):
        super().__init__(id, price, tech_level)
        self.points = points
        self.unknown = unknown


class Gadget(Equipment):

    def __init__(self, id, skill, price, tech_level, unknown):
        super().__init__(id, price, tech_level)
        self.skill = skill
        self.unknown = unknown


class Ship:

    def __init__(
        self,
        name: str,
        size: int,
        cargo: int,
        weapon_slots: int,
        shield_slots: int,
        gadget_slots: int,
        crew: int,
        fuel: int,
        fuel_cost: int,
        hull: int,
        repair_cost: int,
        price: int,
        unknown_percent: int,
        police_use: int,
        pirate_use: int,
        trader_use: int,
        tech_level: int,
    ):
        self.name = name
        self.size = size
        self.cargo = cargo
        self.weapon_slots = weapon_slots
        self.shield_slots = shield_slots
        self.gadget_slots = gadget_slots
        self.crew = crew
        self.fuel = fuel
        self.fuel_cost = fuel_cost
        self.hull = hull
        self.repair_cost = repair_cost
        self.price = price
        self.unknown_percent = unknown_percent
        self.police_use = police_use
        self.pirate_use = pirate_use
        self.trader_use = trader_use
        self.tech_level = tech_level
