"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Economy Module
    This module contains the classes and functions for the game economy such as trade wares and prices.
"""

from .constants import Activity, Size, Skills, TechLevel


class PoliticalSystem:
    ANARCHY = 0
    CAPITALIST = 1
    COMMUNIST = 2
    CONFEDERACY = 3
    CORPORATE = 4
    CYBERNETIC = 5
    DEMOCRACY = 6
    DICTATORSHIP = 7
    FASCIST = 8
    FEUDAL = 9
    MILITARY = 10
    MONARCHY = 11
    PACIFIST = 12
    SOCIALIST = 13
    SATORI = 14
    TECHNOCRACY = 15
    THEOCRACY = 16

    def __init__(
        self,
        name: str,
        stability: int,
        law: int,
        crime: int,
        economy: int,
        minTech: int,
        maxTech: int,
        bribe_difficulty: int,
        drug_tolerance: bool,
        firearm_tolerance: bool,
        tradeItemId: int,
    ):
        self.name = name
        self.stability = stability
        self.law = law
        self.crime = crime
        self.economy = economy
        self.minTech = minTech
        self.maxTech = maxTech
        self.bribe_difficulty = bribe_difficulty
        self.drug_tolerance = drug_tolerance
        self.firearm_tolerance = firearm_tolerance
        self.tradeItemId = tradeItemId

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name} ({self.stability}, {self.law}, {self.crime}, {self.economy})"

    def firearms_ok(self) -> bool:
        return self.firearm_tolerance

    def drugs_ok(self) -> bool:
        return self.drug_tolerance


class Ware:
    """
    Class containing the trade wares and their respective attributes.

    params: name - Trade item name
    params: tech_level_prod - Tech level needed for production
    params: tech_level_min - Tech level needed to use
    params: tech_level_max - Tech level which produces this item the most
    params: max_price - Medium price at lowest tech level
    params: min_price - Price increase per tech level
    params: pressure_price - Max percentage above or below calculated price
    params: pressure - Price increases considerably when this event occurs
    params: special_resource_drop - When this resource is available, this trade item is cheap
    params: special_resource_hike - When this resource is available, this trade item is expensive
    params: min_prod - Minimum price to buy/sell in orbit
    params: max_prod - Maximum price to buy/sell in orbit
    params: quantity - Roundoff price for trade in orbit
    """

    WATER = 0
    FURS = 1
    FOOD = 2
    ORE = 3
    GAMES = 4
    FIREARMS = 5
    MEDICINE = 6
    MACHINERY = 7
    NARCOTICS = 8
    ROBOTS = 9
    NONE = 10

    @staticmethod
    def enum() -> list[int]:
        return range(10)

    @staticmethod
    def lst() -> list[str]:
        return [
            "Water",
            "Furs",
            "Food",
            "Ore",
            "Games",
            "Firearms",
            "Medicine",
            "Machinery",
            "Narcotics",
            "Robots",
        ]

    # TODO min and max price descriptions need to be checked against code
    # TODO min_prod and max_prod descriptions need to be checked against code, seem duplicated
    def __init__(
        self,
        name: str,
        tech_level_prod: int,
        tech_level_min: int,
        tech_level_max: int,
        max_price: int,
        min_price: int,
        pressure_price: int,
        pressure: int,
        special_resource_drop: int,
        special_resource_hike: int,
        min_prod: int,
        max_prod: int,
        quantity: int,
    ):
        self.name = name
        self.tech_level_prod = tech_level_prod
        self.tech_level_min = tech_level_min
        self.tech_level_max = tech_level_max
        self.max_price = max_price
        self.min_price = min_price
        self.pressure_price = pressure_price
        self.pressure = pressure
        self.special_resource_drop = special_resource_drop
        self.special_resource_hike = special_resource_hike
        self.min_prod = min_prod
        self.max_prod = max_prod
        self.quantity = quantity

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Equipment:
    WEAPON = 0
    SHIELD = 1
    GADGET = 2

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

    PULSELASER = 0
    BEAMLASER = 1
    MILITARYLASER = 2
    MORGANSLASER = 3
    PHOTONDISRUPTOR = 4
    QUANTUMDISRUPTOR = 5

    def __init__(self, id, damage, unk_bool, price, tech_level, unknown):
        super().__init__(id, price, tech_level)
        self.damage = damage
        self.unk_bool = unk_bool
        self.unknown = unknown


class Shield(Equipment):
    ENERGY = 0
    REFLECTIVE = 1
    LIGHTNING = 2

    # TODO what are points and unknown?
    def __init__(self, id, points, price, tech_level, unknown):
        super().__init__(id, price, tech_level)
        self.points = points
        self.unknown = unknown


class Gadget(Equipment):
    CARGOBAYS = 0
    AUTOREPAIR = 1
    NAVIGATION = 2
    TARGETING = 3
    CLOAKING = 4
    FUELCOMPACTOR = 5
    SMUGGLERHOLD = 6

    def __init__(self, id, skill, price, tech_level, unknown):
        super().__init__(id, price, tech_level)
        self.skill = skill
        self.unknown = unknown


class Ship:

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

    def get_value(self) -> int:
        return self.price


SHIPS = {
    Ship.FLEA: Ship(
        "Flea",
        Size.TINY,
        10,
        0,
        0,
        0,
        1,
        20,
        1,
        25,
        1,
        2000,
        2,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        Activity.ABSENT,
        TechLevel.EARLY_INDUSTRIAL,
    ),
    Ship.GNAT: Ship(
        "Gnat",
        Size.SMALL,
        15,
        1,
        0,
        1,
        1,
        14,
        1,
        100,
        2,
        10000,
        28,
        Activity.ABSENT,
        Activity.ABSENT,
        Activity.ABSENT,
        TechLevel.INDUSTRIAL,
    ),
    Ship.FIREFLY: Ship(
        "Firefly",
        Size.SMALL,
        20,
        1,
        1,
        1,
        1,
        17,
        1,
        100,
        3,
        25000,
        20,
        Activity.ABSENT,
        Activity.ABSENT,
        Activity.ABSENT,
        TechLevel.INDUSTRIAL,
    ),
    Ship.MOSQUITO: Ship(
        "Mosquito",
        Size.SMALL,
        15,
        2,
        1,
        1,
        1,
        13,
        1,
        100,
        5,
        30000,
        20,
        Activity.ABSENT,
        Activity.MINIMAL,
        Activity.ABSENT,
        TechLevel.INDUSTRIAL,
    ),
    Ship.BUMBLEBEE: Ship(
        "Bumblebee",
        Size.MEDIUM,
        25,
        1,
        2,
        2,
        2,
        15,
        1,
        100,
        7,
        60000,
        15,
        Activity.MINIMAL,
        Activity.MINIMAL,
        Activity.ABSENT,
        TechLevel.INDUSTRIAL,
    ),
    Ship.BEETLE: Ship(
        "Beetle",
        Size.MEDIUM,
        50,
        0,
        1,
        1,
        3,
        14,
        1,
        50,
        10,
        80000,
        3,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        Activity.ABSENT,
        TechLevel.INDUSTRIAL,
    ),
    Ship.HORNET: Ship(
        "Hornet",
        Size.LARGE,
        20,
        3,
        2,
        1,
        2,
        16,
        2,
        150,
        15,
        100000,
        6,
        Activity.FEW,
        Activity.SOME,
        Activity.MINIMAL,
        TechLevel.POST_INDUSTRIAL,
    ),
    Ship.GRASSHOPPER: Ship(
        "Grasshopper",
        Size.LARGE,
        30,
        2,
        2,
        3,
        3,
        15,
        3,
        150,
        15,
        150000,
        2,
        Activity.SOME,
        Activity.MODERATE,
        Activity.FEW,
        TechLevel.POST_INDUSTRIAL,
    ),
    Ship.TERMITE: Ship(
        "Termite",
        Size.HUGE,
        60,
        1,
        3,
        2,
        3,
        13,
        4,
        200,
        20,
        225000,
        2,
        Activity.MODERATE,
        Activity.MANY,
        Activity.SOME,
        TechLevel.HI_TECH,
    ),
    Ship.WASP: Ship(
        "Wasp",
        Size.HUGE,
        35,
        3,
        2,
        2,
        3,
        14,
        5,
        200,
        20,
        300000,
        2,
        Activity.MANY,
        Activity.ABUNDANT,
        Activity.MODERATE,
        TechLevel.HI_TECH,
    ),
    # The ships below can't be bought (mostly)
    Ship.SPACEMONSTER: Ship(
        "Space Monster",
        Size.HUGE,
        0,
        3,
        0,
        0,
        1,
        1,
        1,
        500,
        1,
        500000,
        0,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        TechLevel.UNAVAILABLE,
    ),
    Ship.DRAGONFLY: Ship(
        "Dragonfly",
        Size.SMALL,
        0,
        2,
        3,
        2,
        1,
        1,
        1,
        10,
        1,
        500000,
        0,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        TechLevel.UNAVAILABLE,
    ),
    Ship.MANTIS: Ship(
        "Mantis",
        Size.MEDIUM,
        0,
        3,
        1,
        3,
        3,
        1,
        1,
        300,
        1,
        500000,
        0,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        TechLevel.UNAVAILABLE,
    ),
    Ship.SCARAB: Ship(
        "Scarab",
        Size.LARGE,
        20,
        2,
        0,
        0,
        2,
        1,
        1,
        400,
        1,
        500000,
        0,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        TechLevel.UNAVAILABLE,
    ),
    Ship.SCORPION: Ship(
        "Scorpion",
        Size.HUGE,
        30,
        2,
        2,
        2,
        2,
        1,
        1,
        300,
        1,
        500000,
        0,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        TechLevel.UNAVAILABLE,
    ),
}

WEAPONS = {
    Weapon.PULSELASER: Weapon(Weapon.PULSELASER, 15, False, 2000, TechLevel.INDUSTRIAL, 50),
    Weapon.BEAMLASER: Weapon(Weapon.BEAMLASER, 25, False, 12500, TechLevel.POST_INDUSTRIAL, 35),
    Weapon.MILITARYLASER: Weapon(Weapon.MILITARYLASER, 35, False, 35000, TechLevel.HI_TECH, 15),
    Weapon.MORGANSLASER: Weapon(Weapon.MORGANSLASER, 85, False, 50000, TechLevel.UNAVAILABLE, 0),
    Weapon.PHOTONDISRUPTOR: Weapon(Weapon.PHOTONDISRUPTOR, 20, True, 15000, TechLevel.UNAVAILABLE, 0),
    Weapon.QUANTUMDISRUPTOR: Weapon(Weapon.QUANTUMDISRUPTOR, 60, True, 50000, TechLevel.UNAVAILABLE, 0),
}

SHIELDS = {
    Shield.ENERGY: Shield(Shield.ENERGY, 100, 5000, TechLevel.INDUSTRIAL, 70),
    Shield.REFLECTIVE: Shield(Shield.REFLECTIVE, 200, 20000, TechLevel.POST_INDUSTRIAL, 30),
    Shield.LIGHTNING: Shield(Shield.LIGHTNING, 350, 45000, TechLevel.UNAVAILABLE, 0),
}

GADGETS = {
    Gadget.CARGOBAYS: Gadget(Gadget.CARGOBAYS, Skills.NONE, 2500, TechLevel.EARLY_INDUSTRIAL, 35),
    Gadget.AUTOREPAIR: Gadget(Gadget.AUTOREPAIR, Skills.ENGINEER, 7500, TechLevel.INDUSTRIAL, 20),
    Gadget.NAVIGATION: Gadget(Gadget.NAVIGATION, Skills.PILOT, 15000, TechLevel.POST_INDUSTRIAL, 20),
    Gadget.TARGETING: Gadget(Gadget.TARGETING, Skills.FIGHTER, 2500, TechLevel.POST_INDUSTRIAL, 20),
    Gadget.CLOAKING: Gadget(Gadget.CLOAKING, Skills.PILOT, 100000, TechLevel.HI_TECH, 5),
    # Gadgets below can't be bought
    Gadget.FUELCOMPACTOR: Gadget(Gadget.FUELCOMPACTOR, Skills.NONE, 30000, TechLevel.UNAVAILABLE, 0),
    Gadget.SMUGGLERHOLD: Gadget(Gadget.SMUGGLERHOLD, Skills.NONE, 60000, TechLevel.UNAVAILABLE, 0),
}
