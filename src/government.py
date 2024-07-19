"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Government Module
    These classes and functions define the political systems and their
    respective traits as a result of the government.
"""

from .constants import Activity, TechLevel
from .economy import TradeItemId


class GovernmentId:
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


class PoliticalSystem:

    def __init__(
        self,
        name,
        stability,
        law,
        crime,
        economy,
        minTech,
        maxTech,
        bribe_difficulty,
        drug_tolerance,
        firearm_tolerance,
        tradeItemId,
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


GOVERNMENTS = {
    GovernmentId.ANARCHY: PoliticalSystem(
        "Anarchy",
        0,
        Activity.ABSENT,
        Activity.SWARMS,
        Activity.MINIMAL,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.INDUSTRIAL,
        7,
        True,
        True,
        TradeItemId.FOOD,
    ),
    GovernmentId.CAPITALIST: PoliticalSystem(
        "Capitalist",
        2,
        Activity.SOME,
        Activity.FEW,
        Activity.SWARMS,
        TechLevel.EARLY_INDUSTRIAL,
        TechLevel.HI_TECH,
        1,
        True,
        True,
        TradeItemId.ORE,
    ),
    GovernmentId.COMMUNIST: PoliticalSystem(
        "Communist",
        6,
        Activity.ABUNDANT,
        Activity.MODERATE,
        Activity.MODERATE,
        TechLevel.AGRICULTURAL,
        TechLevel.INDUSTRIAL,
        5,
        True,
        True,
        TradeItemId.NONE,
    ),
    GovernmentId.CONFEDERACY: PoliticalSystem(
        "Confederacy",
        5,
        Activity.MODERATE,
        Activity.SOME,
        Activity.MANY,
        TechLevel.AGRICULTURAL,
        TechLevel.POST_INDUSTRIAL,
        3,
        True,
        True,
        TradeItemId.GAMES,
    ),
    GovernmentId.CORPORATE: PoliticalSystem(
        "Corporate",
        2,
        Activity.ABUNDANT,
        Activity.FEW,
        Activity.SWARMS,
        TechLevel.EARLY_INDUSTRIAL,
        TechLevel.HI_TECH,
        2,
        True,
        True,
        TradeItemId.ROBOTS,
    ),
    GovernmentId.CYBERNETIC: PoliticalSystem(
        "Cybernetic",
        0,
        Activity.SWARMS,
        Activity.SWARMS,
        Activity.MANY,
        TechLevel.POST_INDUSTRIAL,
        TechLevel.HI_TECH,
        0,
        False,
        False,
        TradeItemId.ORE,
    ),
    GovernmentId.DEMOCRACY: PoliticalSystem(
        "Democracy",
        4,
        Activity.SOME,
        Activity.FEW,
        Activity.MANY,
        TechLevel.RENAISSANCE,
        TechLevel.HI_TECH,
        2,
        True,
        True,
        TradeItemId.GAMES,
    ),
    GovernmentId.DICTATORSHIP: PoliticalSystem(
        "Dictatorship",
        3,
        Activity.MODERATE,
        Activity.MANY,
        Activity.SOME,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.HI_TECH,
        2,
        True,
        True,
        TradeItemId.NONE,
    ),
    GovernmentId.FASCIST: PoliticalSystem(
        "Fascist",
        7,
        Activity.SWARMS,
        Activity.SWARMS,
        Activity.MINIMAL,
        TechLevel.EARLY_INDUSTRIAL,
        TechLevel.HI_TECH,
        0,
        False,
        True,
        TradeItemId.MACHINERY,
    ),
    GovernmentId.FEUDAL: PoliticalSystem(
        "Feudal",
        1,
        Activity.MINIMAL,
        Activity.ABUNDANT,
        Activity.FEW,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.RENAISSANCE,
        6,
        True,
        True,
        TradeItemId.FIREARMS,
    ),
    GovernmentId.MILITARY: PoliticalSystem(
        "Military",
        7,
        Activity.SWARMS,
        Activity.ABSENT,
        Activity.ABUNDANT,
        TechLevel.MEDIEVAL,
        TechLevel.HI_TECH,
        0,
        False,
        True,
        TradeItemId.ROBOTS,
    ),
    GovernmentId.MONARCHY: PoliticalSystem(
        "Monarchy",
        3,
        Activity.MODERATE,
        Activity.SOME,
        Activity.MODERATE,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.INDUSTRIAL,
        4,
        True,
        True,
        TradeItemId.MEDICINE,
    ),
    GovernmentId.PACIFIST: PoliticalSystem(
        "Pacifist",
        7,
        Activity.FEW,
        Activity.MINIMAL,
        Activity.MANY,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.RENAISSANCE,
        1,
        True,
        False,
        TradeItemId.NONE,
    ),
    GovernmentId.SOCIALIST: PoliticalSystem(
        "Socialist",
        4,
        Activity.FEW,
        Activity.MANY,
        Activity.SOME,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.INDUSTRIAL,
        6,
        True,
        True,
        TradeItemId.NONE,
    ),
    GovernmentId.SATORI: PoliticalSystem(
        "Satori",
        0,
        Activity.MINIMAL,
        Activity.MINIMAL,
        Activity.MINIMAL,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.AGRICULTURAL,
        0,
        False,
        False,
        TradeItemId.NONE,
    ),
    GovernmentId.TECHNOCRACY: PoliticalSystem(
        "Technocracy",
        1,
        Activity.ABUNDANT,
        Activity.SOME,
        Activity.ABUNDANT,
        TechLevel.EARLY_INDUSTRIAL,
        TechLevel.HI_TECH,
        2,
        True,
        True,
        TradeItemId.WATER,
    ),
    GovernmentId.THEOCRACY: PoliticalSystem(
        "Theocracy",
        5,
        Activity.ABUNDANT,
        Activity.MINIMAL,
        Activity.MODERATE,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.EARLY_INDUSTRIAL,
        0,
        True,
        True,
        TradeItemId.NARCOTICS,
    ),
}

GOVT_NAMES = {
    GovernmentId.ANARCHY: "Anarchy",
    GovernmentId.CAPITALIST: "Capitalist",
    GovernmentId.COMMUNIST: "Communist",
    GovernmentId.CONFEDERACY: "Confederacy",
    GovernmentId.CORPORATE: "Corporate",
    GovernmentId.CYBERNETIC: "Cybernetic",
    GovernmentId.DEMOCRACY: "Democracy",
    GovernmentId.DICTATORSHIP: "Dictatorship",
    GovernmentId.FASCIST: "Facist",
    GovernmentId.FEUDAL: "Feudal",
    GovernmentId.MILITARY: "Military",
    GovernmentId.MONARCHY: "Monarchy",
    GovernmentId.PACIFIST: "Pacifist",
    GovernmentId.SOCIALIST: "Socialist",
    GovernmentId.SATORI: "Satori",
    GovernmentId.TECHNOCRACY: "Technocracy",
    GovernmentId.THEOCRACY: "Theocracy",
}
