"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Commander Module
    Handles the players stats, skills and progress through the game as well as crew info.
"""

import random

from .constants import INSURANCE_RATE, INTEREST_RATE, MAXSKILL, MERCENARYNAMES, Skills


class CriminalRecord:
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


class CombatReputation:
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


class Commander:

    def __init__(self, name):
        self.name = name
        self.pilotSkill = None
        self.fighterSkill = None
        self.traderSkill = None
        self.engineerSkill = None
        self.credits = 1000
        self.debt = 0
        self.ship = None
        self.kills = 0
        self.reputation = 0
        self.policeRecord = 0
        self.timePlayed = 0

    def get_net_worth(self):
        # TODO include moon value eventually
        return self.credits + self.ship.get_value() - self.debt

    def pay_interest(self):

        debt_interest = 0
        if self.debt > 0:
            debt_interest = max(1, self.debt * INTEREST_RATE)
            if self.credits > debt_interest:
                self.credits -= debt_interest
            else:
                self.debt += debt_interest - self.credits
                self.credits = 0
        self.debt = self.debt * 1.1

    def get_debt(self):
        return self.debt

    def improve_skill(self, skill: int, improvement: int):
        # TODO add skill cap
        if skill == Skills.PILOT:
            self.pilotSkill += improvement
        elif skill == Skills.FIGHTER:
            self.fighterSkill += improvement
        elif skill == Skills.TRADER:
            self.traderSkill += improvement
        elif skill == Skills.ENGINEER:
            self.engineerSkill += improvement
        else:
            raise ValueError(f"Invalid skill type, expected [0-3] but got {skill}!")

    def deteriorate_skill(self, skill: int, deterioration: int):
        # TODO prevent from going below 1
        if skill == Skills.PILOT:
            self.pilotSkill -= deterioration
        elif skill == Skills.FIGHTER:
            self.fighterSkill -= deterioration
        elif skill == Skills.TRADER:
            self.traderSkill -= deterioration
        elif skill == Skills.ENGINEER:
            self.engineerSkill -= deterioration
        else:
            raise ValueError(f"Invalid skill type, expected [0-3] but got {skill}!")


class Crew:

    def __init__(self, id):
        self.id = id
        self.pilotSkill = None
        self.fighterSkill = None
        self.traderSkill = None
        self.engineerSkill = None
        self.currentSystem = None

    def __str__(self) -> str:
        return MERCENARYNAMES[self.id]

    def __repr__(self) -> str:
        return self.id

    def get_salary(self):
        """
        I think special crewmembers are free? Or something like that

        return Consts.SpecialCrewMemberIds.Contains(Id) || Id == CrewMemberId.Zeethibal ? 0 :
        """
        return sum([self.pilotSkill, self.fighterSkill, self.traderSkill, self.engineerSkill]) * 3

    def get_skills(self):
        return [self.pilotSkill, self.fighterSkill, self.traderSkill, self.engineerSkill]

    def mod_random_skill(self, amount: int):
        """
        Modifies a random skill by the given amount. The value can be negative,
        but the skill will not go below 1 or above {MAXSKILL}.

        #TODO In source, looks like there is some recalculation done as well
            int	curTrader	= Game.CurrentGame.Commander.Ship.Trader;
                                Skills[skill]	+= amount;
                                if (Game.CurrentGame.Commander.Ship.Trader != curTrader)
                                        Game.CurrentGame.RecalculateBuyPrices(Game.CurrentGame.Commander.CurrentSystem);

        param amount: The amount to modify the skill by.
        """

        # Create a sublist of skills that will be within the bounds
        skills = [skill for skill in self.get_skills() if 1 <= skill + amount <= MAXSKILL]

        # If there are no skills that can be modified, return
        if not skills:
            return
        else:
            # Choose a random skill from the sublist
            skill = random.choice(skills)

            # Modify the skill by the given amount
            skill += amount
