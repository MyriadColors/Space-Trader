#!/usr/bin/env python3
# coding: utf-8
#
# $Id: constants.py 1546.v0.2-dev.1 $
# SPDX-License-Identifier: BSD-2-Clause

"""
    Game constants, to be imported

    From:
    https://github.com/blind-coder/SpaceTrader/blob/master/SpaceTrader/src/main/java/de/anderdonau/spacetrader/Main.java
    https://github.com/blind-coder/SpaceTrader/tree/master/SpaceTrader/src/main/java/de/anderdonau/spacetrader/DataTypes
"""

from enum import Enum

COLORS = {
    "default": "brown",
    "limit": "red",
    "homeworld": "blue",
    "visited": "green",
    "target": "grey",
    "selected": "brown",
    "background": "lightgrey",
}
OVERVIEW = [
    "Space Trader is a complex game, in which the player's aim",
    "is to amass enough money to be able to buy a moon to retire",
    "to. The player starts out with a small space ship, armed",
    "with one simple laser, and 1000 credits in cash. The safest",
    "and easiest way to earn money is to trade goods between",
    "neighbouring solar systems. If the player chooses the goods",
    "to trade wisely, it isn't too difficult to sell them with",
    "a profit. There are other ways to get rich, though. You",
    "might become a bounty hunter and hunt down pirates. It is",
    "also possible to become a pirate yourself and rob honest",
    "traders of their cargo. Beware, though: pirating is a way",
    "to get rich quickly, but the police force will go after you.",
]

# Galaxy
GALAXYWIDTH = 154
GALAXYHEIGHT = 110
MIN_DISTANCE = 7
MAX_DISTANCE = 20
WORMHOLE_DISTANCE = 25
SECTOR_DIAMETER = 13

# Economy
INTEREST_RATE = 0.1
INSURANCE_RATE = 0.0025
DEBT_WARN = 75000
DEBT_LIMIT = 100000
MAX_NOCLAIM = 90  # TODO define
START_CREDITS = 1000


# Crime
class CriminalRecord(Enum):
    PSYCHOPATH = 0
    VILLAIN = 1
    CRIMINAL = 2
    CROOK = 3
    DUBIOUS = 4
    CLEAN = 5
    LAWFUL = 6
    TRUSTED = 7
    LIKED = 8
    HERO = 9
    ERRNO = 10


# Combat
class CombatReputation(Enum):
    HARMLESS = 0
    MOSTLY_HARMLESS = 1
    POOR = 2
    AVERAGE = 3
    ABOVE_AVERAGE = 4
    COMPETENT = 5
    DANGEROUS = 6
    DEADLY = 7
    ELITE = 8
    BORG = 9


# System
class Activity(Enum):
    ABSENT = 0
    MINIMAL = 1
    FEW = 2
    SOME = 3
    MODERATE = 4
    MANY = 5
    ABUNDANT = 6
    SWARMS = 7
    UNAVAILABLE = 100


class Government(Enum):
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


class TechLevel(Enum):
    PRE_AGRICULTURAL = 0
    AGRICULTURAL = 1
    MEDIEVAL = 2
    RENAISSANCE = 3
    EARLY_INDUSTRIAL = 4
    INDUSTRIAL = 5
    POST_INDUSTRIAL = 6
    HI_TECH = 7
    UNAVAILABLE = 8


class Size(Enum):
    TINY = 0
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    HUGE = 4
    GARGANTUAN = 5


class SpecialResource(Enum):
    NOTHING = 0
    MINERAL_RICH = 1
    MINERAL_POOR = 2
    DESERT = 3
    SWEETOCEANS = 4
    RICHSOIL = 5
    POORSOIL = 6
    RICHFAUNA = 7
    LIFELESS = 8
    WEIRDMUSHROOMS = 9
    SPECIALHERBS = 10
    ARTISTIC = 11
    WARLIKE = 12


class SystemPressure(Enum):
    NONE = 0
    WAR = 1
    PLAGUE = 2
    DROUGHT = 3
    BOREDOM = 4
    COLD = 5
    CROPFAILURE = 6
    EMPLOYMENT = 7


SYSTEMSIZE = {
    SystemSize.TINY: "Tiny",
    SystemSize.SMALL: "Small",
    SystemSize.MEDIUM: "Medium",
    SystemSize.LARGE: "Large",
    SystemSize.HUGE: "Huge",
    SystemSize.GARGANTUAN: "Gargantuan",
}
SPECIALRESOURCES = {
    SpecialResource.NOTHING: "Nothing special",  # Uneventful
    SpecialResource.MINERAL_RICH: "Mineral rich",  # produce Ore
    SpecialResource.MINERAL_POOR: "Mineral poor",  # Ore in demand
    SpecialResource.DESERT: "Desert",  # Water in demand
    SpecialResource.SWEETOCEANS: "Sweetwater oceans",  # produce Water
    SpecialResource.RICHSOIL: "Rich soil",  # produce Food
    SpecialResource.POORSOIL: "Poor soil",  # Food in demand
    SpecialResource.RICHFAUNA: "Rich fauna",  # produce Fur
    SpecialResource.LIFELESS: "Lifeless",  # Water and Food in demand
    SpecialResource.WEIRDMUSHROOMS: "Weird mushrooms",  # produce Narcotics
    SpecialResource.SPECIALHERBS: "Special herbs",  # produce Narcotics
    SpecialResource.ARTISTIC: "Artistic populace",  # Narcotics in demand
    SpecialResource.WARLIKE: "Warlike populace",  # Weapons in demand
}
PRESSURE = {
    SystemPressure.NONE: "under no particular pressure",  # Uneventful
    SystemPressure.WAR: "at war",  # Ore and Weapons in demand
    SystemPressure.PLAGUE: "ravaged by a plague",  # Medicine in demand
    SystemPressure.DROUGHT: "suffering from a drought",  # Water in demand
    SystemPressure.BOREDOM: "suffering from extreme boredom",  # Games and Narcotics in demand
    SystemPressure.COLD: "suffering from a cold spell",  # Furs in demand
    SystemPressure.CROPFAILURE: "suffering from a crop failure",  # Food in demand
    SystemPressure.EMPLOYMENT: "lacking enough workers",
}  # Machinery and Robots in demand


# Equipment
class EquipmentType(Enum):
    WEAPON = 0
    SHIELD = 1
    GADGET = 2


class GadgetID(Enum):
    CARGOBAYS = 0
    AUTOREPAIR = 1
    NAVIGATION = 2
    TARGETING = 3
    CLOAKING = 4
    FUELCOMPACTOR = 5
    SMUGGLERHOLD = 6


class WeaponID(Enum):
    PULSELASER = 0
    BEAMLASER = 1
    MILITARYLASER = 2
    MORGANSLASER = 3
    PHOTONDISRUPTOR = 4
    QUANTUMDISRUPTOR = 5


class SheildID(Enum):
    ENERGY = 0
    REFLECTIVE = 1
    LIGHTNING = 2


# Ships
class ShipID(Enum):
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


SHIPTYPES = {
    "escapepod": {
        "model": "escapepod",
        "cargo": 0,
        "weapon": 0,
        "shield": 0,
        "shieldstrengh": 0,
        "gadget": 0,
        "crew": 0,
        "efficiency": 1,
        "hull": 500,
        "tribbles": False,
    },
    "flea": {
        "model": "flea",
        "cargo": 10,
        "weapon": 1,
        "shield": 0,
        "shieldstrengh": 0,
        "gadget": 1,
        "crew": 0,
        "efficiency": 1,
        "hull": 2000,
        "tribbles": False,
    },
    "gnat": {
        "model": "gnat",
        "cargo": 15,
        "weapon": 1,
        "shield": 1,
        "shieldstrengh": 1,
        "gadget": 1,
        "crew": 1,
        "efficiency": 0.93,
        "hull": 10000,
        "tribbles": False,
    },
    "firefly": {
        "model": "firefly",
        "cargo": 20,
        "weapon": 1,
        "shield": 1,
        "shieldstrengh": 1,
        "gadget": 1,
        "crew": 2,
        "efficiency": 1.15,
        "hull": 25000,
        "tribbles": False,
    },
    "mosquito": {
        "model": "mosquito",
        "cargo": 15,
        "weapon": 2,
        "shield": 1,
        "shieldstrengh": 1,
        "gadget": 1,
        "crew": 5,
        "efficiency": 0.86,
        "hull": 30000,
        "tribbles": False,
    },
    "bumblebee": {
        "model": "bumblebee",
        "cargo": 25,
        "weapon": 1,
        "shield": 2,
        "shieldstrengh": 2,
        "gadget": 2,
        "crew": 5,
        "efficiency": 1,
        "hull": 60000,
        "tribbles": False,
    },
    "beetle": {
        "model": "beetle",
        "cargo": 50,
        "weapon": 0,
        "shield": 1,
        "shieldstrengh": 1,
        "gadget": 3,
        "crew": 5,
        "efficiency": 0.93,
        "hull": 80000,
        "tribbles": False,
    },
    "hornet": {
        "model": "hornet",
        "cargo": 20,
        "weapon": 3,
        "shield": 2,
        "shieldstrengh": 1,
        "gadget": 2,
        "crew": 5,
        "efficiency": 1.06,
        "hull": 100000,
        "tribbles": False,
    },
    "grasshopper": {
        "model": "grasshopper",
        "cargo": 30,
        "weapon": 2,
        "shield": 2,
        "shieldstrengh": 3,
        "gadget": 3,
        "crew": 6,
        "efficiency": 1,
        "hull": 150000,
        "tribbles": False,
    },
    "termite": {
        "model": "termite",
        "cargo": 60,
        "weapon": 1,
        "shield": 3,
        "shieldstrengh": 2,
        "gadget": 3,
        "crew": 7,
        "efficiency": 0.86,
        "hull": 225000,
        "tribbles": False,
    },
    "wasp": {
        "model": "wasp",
        "cargo": 35,
        "weapon": 3,
        "shield": 2,
        "shieldstrengh": 2,
        "gadget": 3,
        "crew": 7,
        "efficiency": 0.93,
        "hull": 300000,
        "tribbles": False,
    },
    "spacemonster": {
        "model": "spacemonster",
        "cargo": 0,
        "weapon": 3,
        "shield": 0,
        "shieldstrengh": 0,
        "gadget": 1,
        "crew": 0,
        "efficiency": 0.5,
        "hull": 500000,
        "tribbles": False,
    },
    # these have special purpose and cannot be bought
    "dragonfly": {
        "model": "dragonfly",
        "cargo": 0,
        "weapon": 2,
        "shield": 3,
        "shieldstrengh": 2,
        "gadget": 1,
        "crew": 1,
        "efficiency": 0.53,
        "hull": 500000,
        "tribbles": False,
    },
    "mantis": {
        "model": "mantis",
        "cargo": 0,
        "weapon": 3,
        "shield": 1,
        "shieldstrengh": 3,
        "gadget": 1,
        "crew": 1,
        "efficiency": 0.53,
        "hull": 500000,
        "tribbles": False,
    },
    "scarab": {
        "model": "scarab",
        "cargo": 20,
        "weapon": 2,
        "shield": 0,
        "shieldstrengh": 0,
        "gadget": 2,
        "crew": 1,
        "efficiency": 0.53,
        "hull": 500000,
        "tribbles": False,
    },
    "bottle": {
        "model": "bottle",
        "cargo": 0,
        "weapon": 0,
        "shield": 0,
        "shieldstrengh": 0,
        "gadget": 1,
        "crew": 1,
        "efficiency": 0.53,
        "hull": 100,
        "tribbles": False,
    },
}


# Names
SYSTEM_NAMES = [
    "Acamar",
    "Adahn",
    "Aldea",
    "Andevian",
    "Antedi",
    "Balosnee",
    "Baratas",
    "Bob",
    "Brax",
    "Bretel",
    "Calondia",
    "Campor",
    "Capelle",
    "Carzon",
    "Castor",
    "Cestus",
    "Cheron",
    "Courteney",
    "Daled",
    "Damast",
    "Davlos",
    "Deneb",
    "Deneva",
    "Devidia",
    "Draylon",
    "Drema",
    "Endor",
    "Esmee",
    "Exo",
    "Ferris",
    "Festen",
    "Fourmi",
    "Frolix",
    "Gemulon",
    "Guinifer",
    "Hades",
    "Hamlet",
    "Helena",
    "Hulst",
    "Iodine",
    "Iralius",
    "Janus",
    "Japori",
    "Jarada",
    "Jason",
    "Kaylon",
    "Khefka",
    "Kira",
    "Klaatu",
    "Klaestron",
    "Korma",
    "Kravat",
    "Krios",
    "Laertes",
    "Largo",
    "Lave",
    "Ligon",
    "Lowry",
    "Magrat",
    "Malcoria",
    "Melina",
    "Mentar",
    "Merik",
    "Mintaka",
    "Montor",
    "Mordan",
    "Myrthe",
    "Nelvana",
    "Nix",
    "Nyle",
    "Odet",
    "Og",
    "Omega",
    "Omphalos",
    "Orias",
    "Othello",
    "Parade",
    "Penthara",
    "Picard",
    "Pollux",
    "Quator",
    "Rakhar",
    "Ran",
    "Regulas",
    "Relva",
    "Rhymus",
    "Rochani",
    "Rubicum",
    "Rutia",
    "Sarpeidon",
    "Sefalla",
    "Seltrice",
    "Sigma",
    "Sol",
    "Somari",
    "Stakoron",
    "Styris",
    "Talani",
    "Tamus",
    "Tantalos",
    "Tanuga",
    "Tarchannen",
    "Terosa",
    "Thera",
    "Titan",
    "Torin",
    "Triacus",
    "Turkana",
    "Tyrus",
    "Umberlee",
    "Utopia",
    "Vadera",
    "Vagra",
    "Vandor",
    "Ventax",
    "Xenon",
    "Xerxes",
    "Yew",
    "Yojimbo",
    "Zalkon",
    "Zuul",
]
MERCENARYNAMES = [
    "Alyssa",
    "Armatur",
    "Bentos",
    "C2U2",
    "Chi'Ti",
    "Crystal",
    "Dane",
    "Deirdre",
    "Doc",
    "Draco",
    "Iranda",
    "Jeremiah",
    "Jujubal",
    "Krydon",
    "Luis",
    "Mercedez",
    "Milete",
    "Muri-L",
    "Mystyc",
    "Nandi",
    "Orestes",
    "Pancho",
    "PS37",
    "Quarck",
    "Sosumi",
    "Uma",
    "Wesley",
    "Wonton",
    "Yorvick",
    "Zeethibal",  # anagram of Elizabeth
]


# Character
class Skills(Enum):
    NONE = 0
    PILOT = 1
    FIGHTER = 2
    TRADER = 3
    ENGINEER = 4


class Difficulty(Enum):
    BEGINNER = 0
    EASY = 1
    NORMAL = 2
    HARD = 3
    IMPOSSIBLE = 4


MAXTRIBBLES = 100000
MAXSKILL = 10
SKILLBONUS = 3
CLOAKBONUS = 2
BOUNTYMOD = 1000  # Price paid by govt for each neg police point
POLICE_RECORDS = {
    CriminalRecord.PSYCHOPATH: -100,
    CriminalRecord.VILLAIN: -70,
    CriminalRecord.CRIMINAL: -30,
    CriminalRecord.CROOK: -10,
    CriminalRecord.DUBIOUS: -5,
    CriminalRecord.CLEAN: 0,
    CriminalRecord.LAWFUL: 5,
    CriminalRecord.TRUSTED: 10,
    CriminalRecord.LIKED: 25,
    CriminalRecord.HERO: 75,
    CriminalRecord.ERRNO: 100,
}
REPUTATION = {
    CombatReputation.HARMLESS: 0,
    CombatReputation.MOSTLY_HARMLESS: 10,
    CombatReputation.POOR: 20,
    CombatReputation.AVERAGE: 40,
    CombatReputation.ABOVE_AVERAGE: 80,
    CombatReputation.COMPETENT: 150,
    CombatReputation.DANGEROUS: 300,
    CombatReputation.DEADLY: 600,
    CombatReputation.ELITE: 1500,
    CombatReputation.BORG: 3000,
}


# TODO Unknown values/usage
SCOREATTACKPIRATE = 0
SCOREATTACKPOLICE = -3
SCOREATTACKTRADER = -2
SCORECAUGHTWITHWILD = -4
SCOREFLEEPOLICE = -2
SCOREKILLCAPTAIN = 100
SCOREKILLPIRATE = 1
SCOREKILLPOLICE = -6
SCOREKILLTRADER = -4
SCOREPLUNDERPIRATE = -1
SCOREPLUNDERTRADER = -2
SCORETRAFFICKING = -1

SHIPTEMPLATESEPARATOR = "----------------------------"
