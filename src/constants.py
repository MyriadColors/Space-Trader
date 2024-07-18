"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Constants Module
    Game constants and enums, to be imported by other modules.
"""

from enum import Enum
from random import randint

# Galaxy
GALAXYWIDTH = 154
GALAXYHEIGHT = 110
MIN_DISTANCE = 7
MAX_DISTANCE = 20
WORMHOLE_DISTANCE = 25
SECTOR_DIAMETER = 13
MAX_WORMHOLES = 10


# Economy
START_CREDITS = 1000
INTEREST_RATE = 0.1
DEBT_WARN = 75000
DEBT_LIMIT = 100000
""" Insurance Info
Insurance rate is the percentage of the ship's value that is paid as insurance daily.
This rate begins at 100% and drops by 1% for each day without a claim
MAX_NOCLAIM is the lowest rate that can be achieved
"""
INSURANCE_RATE = 0.0025
MAX_NOCLAIM = 90


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
class PlanetId:
    ACAMAR = 0
    ADAHN = 1
    ALDEA = 2
    ANDEVIAN = 3
    ANTEDI = 4
    BALOSNEE = 5
    BARATAS = 6
    BOB = 7
    BRAX = 8
    BRETEL = 9
    CALONDIA = 10
    CAMPOR = 11
    CAPELLE = 12
    CARZON = 13
    CASTOR = 14
    CESTUS = 15
    CHERON = 16
    COURTENEY = 17
    DALED = 18
    DAMAST = 19
    DAVLOS = 20
    DENEB = 21
    DENEVA = 22
    DEVIDIA = 23
    DRAYLON = 24
    DREMA = 25
    ENDOR = 26
    ESMEE = 27
    EXO = 28
    FERRIS = 29
    FESTEN = 30
    FOURMI = 31
    FROLIX = 32
    GEMULON = 33
    GUINIFER = 34
    HADES = 35
    HAMLET = 36
    HELENA = 37
    HULST = 38
    IODINE = 39
    IRALIUS = 40
    JANUS = 41
    JAPORI = 42
    JARADA = 43
    JASON = 44
    KAYLON = 45
    KHEFKA = 46
    KIRA = 47
    KLAATU = 48
    KLAESTRON = 49
    KORMA = 50
    KRAVAT = 51
    KRIOS = 52
    LAERTES = 53
    LARGO = 54
    LAVE = 55
    LIGON = 56
    LOWRY = 57
    MAGRAT = 58
    MALCORIA = 59
    MELINA = 60
    MENTAR = 61
    MERIK = 62
    MINTAKA = 63
    MONTOR = 64
    MORDAN = 65
    MYRTHE = 66
    NELVANA = 67
    NIX = 68
    NYLE = 69
    ODET = 70
    OG = 71
    OMEGA = 72
    OMPHALOS = 73
    ORIAS = 74
    OTHELLO = 75
    PARADE = 76
    PENTHARA = 77
    PICARD = 78
    POLLUX = 79
    QUATOR = 80
    RAKHAR = 81
    RAN = 82
    REGULAS = 83
    RELVA = 84
    RHYMUS = 85
    ROCHANI = 86
    RUBICUM = 87
    RUTIA = 88
    SARPEIDON = 89
    SEFALLA = 90
    SELTRICE = 91
    SIGMA = 92
    SOL = 93
    SOMARI = 94
    STAKORON = 95
    STYRIS = 96
    TALANI = 97
    TAMUS = 98
    TANTALOS = 99
    TANUGA = 100
    TARCHANNEN = 101
    TEROSA = 102
    THERA = 103
    TITAN = 104
    TORIN = 105
    TRIACUS = 106
    TURKANA = 107
    TYRUS = 108
    UMBERLEE = 109
    UTOPIA = 110
    VADERA = 111
    VAGRA = 112
    VANDOR = 113
    VENTAX = 114
    XENON = 115
    XERXES = 116
    YEW = 117
    YOJIMBO = 118
    ZALKON = 119
    ZUUL = 120


class Activity:
    ABSENT = 0
    MINIMAL = 1
    FEW = 2
    SOME = 3
    MODERATE = 4
    MANY = 5
    ABUNDANT = 6
    SWARMS = 7
    UNAVAILABLE = 100


class TechLevel:
    PRE_AGRICULTURAL = 0
    AGRICULTURAL = 1
    MEDIEVAL = 2
    RENAISSANCE = 3
    EARLY_INDUSTRIAL = 4
    INDUSTRIAL = 5
    POST_INDUSTRIAL = 6
    HI_TECH = 7
    UNAVAILABLE = 8


class Size:
    TINY = 0
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    HUGE = 4
    GARGANTUAN = 5


class SpecialResource:
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

    def random() -> int:
        return randint(1, 12)


class SocietalPressure:
    NONE = 0
    WAR = 1
    PLAGUE = 2
    DROUGHT = 3
    BOREDOM = 4
    COLD = 5
    CROPFAILURE = 6
    EMPLOYMENT = 7


PLANET_NAMES = {
    PlanetId.ACAMAR: "Acamar",
    PlanetId.ADAHN: "Adahn",
    PlanetId.ALDEA: "Aldea",
    PlanetId.ANDEVIAN: "Andevian",
    PlanetId.ANTEDI: "Antedi",
    PlanetId.BALOSNEE: "Balosnee",
    PlanetId.BARATAS: "Baratas",
    PlanetId.BOB: "Bob",
    PlanetId.BRAX: "Brax",
    PlanetId.BRETEL: "Bretel",
    PlanetId.CALONDIA: "Calondia",
    PlanetId.CAMPOR: "Campor",
    PlanetId.CAPELLE: "Capelle",
    PlanetId.CARZON: "Carzon",
    PlanetId.CASTOR: "Castor",
    PlanetId.CESTUS: "Cestus",
    PlanetId.CHERON: "Cheron",
    PlanetId.COURTENEY: "Courteney",
    PlanetId.DALED: "Daled",
    PlanetId.DAMAST: "Damast",
    PlanetId.DAVLOS: "Davlos",
    PlanetId.DENEB: "Deneb",
    PlanetId.DENEVA: "Deneva",
    PlanetId.DEVIDIA: "Devidia",
    PlanetId.DRAYLON: "Draylon",
    PlanetId.DREMA: "Drema",
    PlanetId.ENDOR: "Endor",
    PlanetId.ESMEE: "Esmee",
    PlanetId.EXO: "Exo",
    PlanetId.FERRIS: "Ferris",
    PlanetId.FESTEN: "Festen",
    PlanetId.FOURMI: "Fourmi",
    PlanetId.FROLIX: "Frolix",
    PlanetId.GEMULON: "Gemulon",
    PlanetId.GUINIFER: "Guinifer",
    PlanetId.HADES: "Hades",
    PlanetId.HAMLET: "Hamlet",
    PlanetId.HELENA: "Helena",
    PlanetId.HULST: "Hulst",
    PlanetId.IODINE: "Iodine",
    PlanetId.IRALIUS: "Iralius",
    PlanetId.JANUS: "Janus",
    PlanetId.JAPORI: "Japori",
    PlanetId.JARADA: "Jarada",
    PlanetId.JASON: "Jason",
    PlanetId.KAYLON: "Kaylon",
    PlanetId.KHEFKA: "Khefka",
    PlanetId.KIRA: "Kira",
    PlanetId.KLAATU: "Klaatu",
    PlanetId.KLAESTRON: "Klaestron",
    PlanetId.KORMA: "Korma",
    PlanetId.KRAVAT: "Kravat",
    PlanetId.KRIOS: "Krios",
    PlanetId.LAERTES: "Laertes",
    PlanetId.LARGO: "Largo",
    PlanetId.LAVE: "Lave",
    PlanetId.LIGON: "Ligon",
    PlanetId.LOWRY: "Lowry",
    PlanetId.MAGRAT: "Magrat",
    PlanetId.MALCORIA: "Malcoria",
    PlanetId.MELINA: "Melina",
    PlanetId.MENTAR: "Mentar",
    PlanetId.MERIK: "Merik",
    PlanetId.MINTAKA: "Mintaka",
    PlanetId.MONTOR: "Montor",
    PlanetId.MORDAN: "Mordan",
    PlanetId.MYRTHE: "Myrthe",
    PlanetId.NELVANA: "Nelvana",
    PlanetId.NIX: "Nix",
    PlanetId.NYLE: "Nyle",
    PlanetId.ODET: "Odet",
    PlanetId.OG: "Og",
    PlanetId.OMEGA: "Omega",
    PlanetId.OMPHALOS: "Omphalos",
    PlanetId.ORIAS: "Orias",
    PlanetId.OTHELLO: "Othello",
    PlanetId.PARADE: "Parade",
    PlanetId.PENTHARA: "Penthara",
    PlanetId.PICARD: "Picard",
    PlanetId.POLLUX: "Pollux",
    PlanetId.QUATOR: "Quator",
    PlanetId.RAKHAR: "Rakhar",
    PlanetId.RAN: "Ran",
    PlanetId.REGULAS: "Regulas",
    PlanetId.RELVA: "Relva",
    PlanetId.RHYMUS: "Rhymus",
    PlanetId.ROCHANI: "Rochani",
    PlanetId.RUBICUM: "Rubicum",
    PlanetId.RUTIA: "Rutia",
    PlanetId.SARPEIDON: "Sarpeidon",
    PlanetId.SEFALLA: "Sefalla",
    PlanetId.SELTRICE: "Seltrice",
    PlanetId.SIGMA: "Sigma",
    PlanetId.SOL: "Sol",
    PlanetId.SOMARI: "Somari",
    PlanetId.STAKORON: "Stakoron",
    PlanetId.STYRIS: "Styris",
    PlanetId.TALANI: "Talani",
    PlanetId.TAMUS: "Tamus",
    PlanetId.TANTALOS: "Tantalos",
    PlanetId.TANUGA: "Tanuga",
    PlanetId.TARCHANNEN: "Tarchannen",
    PlanetId.TEROSA: "Terosa",
    PlanetId.THERA: "Thera",
    PlanetId.TITAN: "Titan",
    PlanetId.TORIN: "Torin",
    PlanetId.TRIACUS: "Triacus",
    PlanetId.TURKANA: "Turkana",
    PlanetId.TYRUS: "Tyrus",
    PlanetId.UMBERLEE: "Umberlee",
    PlanetId.UTOPIA: "Utopia",
    PlanetId.VADERA: "Vadera",
    PlanetId.VAGRA: "Vagra",
    PlanetId.VANDOR: "Vandor",
    PlanetId.VENTAX: "Ventax",
    PlanetId.XENON: "Xenon",
    PlanetId.XERXES: "Xerxes",
    PlanetId.YEW: "Yew",
    PlanetId.YOJIMBO: "Yojimbo",
    PlanetId.ZALKON: "Zalkon",
    PlanetId.ZUUL: "Zuul",
}
SYSTEMSIZE = {
    Size.TINY: "Tiny",
    Size.SMALL: "Small",
    Size.MEDIUM: "Medium",
    Size.LARGE: "Large",
    Size.HUGE: "Huge",
    Size.GARGANTUAN: "Gargantuan",
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
    SocietalPressure.NONE: "under no particular pressure",  # Uneventful
    SocietalPressure.WAR: "at war",  # Ore and Weapons in demand
    SocietalPressure.PLAGUE: "ravaged by a plague",  # Medicine in demand
    SocietalPressure.DROUGHT: "suffering from a drought",  # Water in demand
    SocietalPressure.BOREDOM: "suffering from extreme boredom",  # Games and Narcotics in demand
    SocietalPressure.COLD: "suffering from a cold spell",  # Furs in demand
    SocietalPressure.CROPFAILURE: "suffering from a crop failure",  # Food in demand
    SocietalPressure.EMPLOYMENT: "lacking enough workers",
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
class Merc(Enum):
    ALYSSA = 1
    ARMATUR = 2
    BENTOS = 3
    C2U2 = 4
    CHITI = 5
    CRYSTAL = 6
    DANE = 7
    DEIRDRE = 8
    DOC = 9
    DRACO = 10
    IRANDA = 11
    JEREMIAH = 12
    JUJUBAL = 13
    KRYDON = 14
    LUIS = 15
    MERCEDZ = 16
    MILETE = 17
    MURIL = 18
    MYSTYC = 19
    NANDI = 20
    ORESTES = 21
    PANCHO = 22
    PS37 = 23
    QUARCK = 24
    SOSUMI = 25
    UMA = 26
    WESLEY = 27
    WONTON = 28
    YORVICK = 29
    ZEETHIBAL = 30


MERCENARYNAMES = {
    Merc.ALYSSA: "Alyssa",
    Merc.ARMATUR: "Armatur",
    Merc.BENTOS: "Bentos",
    Merc.C2U2: "C2U2",
    Merc.CHITI: "Chi'Ti",
    Merc.CRYSTAL: "Crystal",
    Merc.DANE: "Dane",
    Merc.DEIRDRE: "Deirdre",
    Merc.DOC: "Doc",
    Merc.DRACO: "Draco",
    Merc.IRANDA: "Iranda",
    Merc.JEREMIAH: "Jeremiah",
    Merc.JUJUBAL: "Jujubal",
    Merc.KRYDON: "Krydon",
    Merc.LUIS: "Luis",
    Merc.MERCEDZ: "Mercedez",
    Merc.MILETE: "Milete",
    Merc.MURIL: "Muri-L",
    Merc.MYSTYC: "Mystyc",
    Merc.NANDI: "Nandi",
    Merc.ORESTES: "Orestes",
    Merc.PANCHO: "Pancho",
    Merc.PS37: "PS37",
    Merc.QUARCK: "Quarck",
    Merc.SOSUMI: "Sosumi",
    Merc.UMA: "Uma",
    Merc.WESLEY: "Wesley",
    Merc.WONTON: "Wonton",
    Merc.YORVICK: "Yorvick",
    Merc.ZEETHIBAL: "Zeethibal",  # anagram of Elizabeth
}


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


# Gamestate codes
class GameStateID:
    SPLASH = 0
    CHAR_CREATE = 1


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

STARTCLICKS = 20
MAXFUELTANKS = 20
FUELCOMPACTORTANKS = 3
HULLUPGRADE = 50
MAXSHIP = 9
MAXSLOTS = 5
FLEACONVERSIONCOST = 500
PODTRANSFERCOST = 200

IMAGESPERSHIP = 4
SHIPIMGOFFSETNORMAL = 0
SHIPIMGOFFSETDAMAGE = 1
SHIPIMGOFFSETSHIELD = 2
SHIPIMGOFFSETSHEILDDAMAGE = 3
SHIPIMGUSEDEFAULT = -1
ENCOUNTERIMGALIEN = 0
ENCOUNTERIMGPIRATE = 1
ENCOUNTERIMGPOLICE = 2
ENCOUNTERIMGSPECIAL = 3
ENCOUNTERIMGTRADER = 4

STORYPROBABILITY = 50 / 8
FABRICRIPINITIALPROBABILITY = 25

DIRECTIONUP = 0
DIRECTIONDOWN = 1
DIRECTIONLEFT = 2
DIRECTIONRIGHT = 3

DISRUPTORSYSTEMSMULTIPLIER = 3
