"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Government Module
    These classes and functions define the political systems and their
    respective traits as a result of the government.
"""


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
