from constants import Activity, GadgetID, SheildID, ShipID, Size, Skills, TechLevel, WeaponID


class Weapon:

    def __init__(self, id, damage, unk_bool, price, tech_level, unknown):
        self.id = id
        self.damage = damage
        self.unk_bool = unk_bool
        self.price = price
        self.tech_level = tech_level
        self.unknown = unknown


class Shield:

    # TODO what are points and unknown?
    def __init__(self, id, points, price, tech_level, unknown):
        self.id = id
        self.points = points
        self.price = price
        self.tech_level = tech_level
        self.unknown = unknown


class Gadget:

    def __init__(self, id, skill, price, tech_level, unknown):
        self.id = id
        self.skill = skill
        self.price = price
        self.tech_level = tech_level
        self.unknown = unknown


class Ship:

    def __init__(
        self,
        id,
        size,
        cargo,
        weapon_slots,
        shield_slots,
        gadget_slots,
        crew,
        fuel,
        fuel_cost,
        hull,
        repair_cost,
        price,
        unknown_percent,
        police_use,
        pirate_use,
        trader_use,
        tech_level,
    ):
        self.id = id
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


WEAPONS = {
    WeaponID.PULSELASER: Weapon(WeaponID.PULSELASER, 15, False, 2000, TechLevel.INDUSTRIAL, 50),
    WeaponID.BEAMLASER: Weapon(WeaponID.BEAMLASER, 25, False, 12500, TechLevel.POST_INDUSTRIAL, 35),
    WeaponID.MILITARYLASER: Weapon(WeaponID.MILITARYLASER, 35, False, 35000, TechLevel.HI_TECH, 15),
    WeaponID.MORGANSLASER: Weapon(WeaponID.MORGANSLASER, 85, False, 50000, TechLevel.UNAVAILABLE, 0),
    WeaponID.PHOTONDISRUPTOR: Weapon(WeaponID.PHOTONDISRUPTOR, 20, True, 15000, TechLevel.UNAVAILABLE, 0),
    WeaponID.QUANTUMDISRUPTOR: Weapon(WeaponID.QUANTUMDISRUPTOR, 60, True, 50000, TechLevel.UNAVAILABLE, 0),
}
SHIELDS = {
    SheildID.ENERGY: Shield(SheildID.ENERGY, 100, 5000, TechLevel.INDUSTRIAL, 70),
    SheildID.REFLECTIVE: Shield(SheildID.REFLECTIVE, 200, 20000, TechLevel.POST_INDUSTRIAL, 30),
    SheildID.LIGHTNING: Shield(SheildID.LIGHTNING, 350, 45000, TechLevel.UNAVAILABLE, 0),
}
GADGETS = {
    GadgetID.CARGOBAYS: Gadget(GadgetID.CARGOBAYS, Skills.NONE, 2500, TechLevel.EARLY_INDUSTRIAL, 35),
    GadgetID.AUTOREPAIR: Gadget(GadgetID.AUTOREPAIR, Skills.ENGINEER, 7500, TechLevel.INDUSTRIAL, 20),
    GadgetID.NAVIGATION: Gadget(GadgetID.NAVIGATION, Skills.PILOT, 15000, TechLevel.POST_INDUSTRIAL, 20),
    GadgetID.TARGETING: Gadget(GadgetID.TARGETING, Skills.FIGHTER, 2500, TechLevel.POST_INDUSTRIAL, 20),
    GadgetID.CLOAKING: Gadget(GadgetID.CLOAKING, Skills.PILOT, 100000, TechLevel.HI_TECH, 5),
    # Gadgets below can't be bought
    GadgetID.FUELCOMPACTOR: Gadget(GadgetID.FUELCOMPACTOR, Skills.NONE, 30000, TechLevel.UNAVAILABLE, 0),
    GadgetID.SMUGGLERHOLD: Gadget(GadgetID.SMUGGLERHOLD, Skills.NONE, 60000, TechLevel.UNAVAILABLE, 0),
}
SHIPS = {
    ShipID.FLEA: (
        ShipID.FLEA,
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
        TechLevel.EarlyIndustrial,
    ),
    ShipID.GNAT: (
        ShipID.GNAT,
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
        TechLevel.Industrial,
    ),
    ShipID.FIREFLY: (
        ShipID.FIREFLY,
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
        TechLevel.Industrial,
    ),
    ShipID.MOSQUITO: (
        ShipID.MOSQUITO,
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
        TechLevel.Industrial,
    ),
    ShipID.BUMBLEBEE: (
        ShipID.BUMBLEBEE,
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
        TechLevel.Industrial,
    ),
    ShipID.BEETLE: (
        ShipID.BEETLE,
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
        TechLevel.Industrial,
    ),
    ShipID.HORNET: (
        ShipID.HORNET,
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
        TechLevel.PostIndustrial,
    ),
    ShipID.GRASSHOPPER: (
        ShipID.GRASSHOPPER,
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
        TechLevel.PostIndustrial,
    ),
    ShipID.TERMITE: (
        ShipID.TERMITE,
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
        TechLevel.HiTech,
    ),
    ShipID.WASP: (
        ShipID.WASP,
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
        TechLevel.HiTech,
    ),
    # The ships below can't be bought (mostly)
    ShipID.SPACEMONSTER: (
        ShipID.SPACEMONSTER,
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
    ShipID.DRAGONFLY: (
        ShipID.DRAGONFLY,
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
    ShipID.MANTIS: (
        ShipID.MANTIS,
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
    ShipID.SCARAB: (
        ShipID.SCARAB,
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
    ShipID.BOTTLE: (
        ShipID.BOTTLE,
        Size.SMALL,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        10,
        1,
        100,
        0,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        TechLevel.UNAVAILABLE,
    ),
    ShipID.CUSTOM: (
        ShipID.CUSTOM,
        Size.HUGE,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        Activity.UNAVAILABLE,
        TechLevel.UNAVAILABLE,
    ),
    ShipID.SCORPION: (
        ShipID.SCORPION,
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
