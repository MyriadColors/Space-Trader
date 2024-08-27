"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Commander Module
    Handles the players stats, skills and progress through the game as well as crew info.
"""

import random

from .constants import INSURANCE_RATE, INTEREST_RATE, MAXSKILL, MERCENARYNAMES, CombatReputation, CriminalRecord, Skills
from .economy import SHIPS, Ship


class Commander:

    def __init__(self, name, pilot_skill, fighter_skill, trader_skill, engineer_skill):
        self.name = name
        self.pilotSkill = pilot_skill
        self.fighterSkill = fighter_skill
        self.traderSkill = trader_skill
        self.engineerSkill = engineer_skill
        self.credits = 1000
        self.debt = 0
        self.ship = SHIPS[Ship.GNAT]
        self.kills = 0
        self.reputation = 0
        self.policeRecord = 0
        self.timePlayed = 0
        self.currentSystem = random.randint(0, 120)

    def __str__(self) -> str:
        return self.name

    def pprint(self) -> str:
        cmdr_string = f"Name: {self.name}\n \
            Skills: {self.pilotSkill}/{self.fighterSkill}/{self.traderSkill}/{self.engineerSkill}\n \
            Credits: {self.credits}\n \
            Debt: {self.debt}\n \
            Ship: {self.ship.name}\n \
            Kills: {self.kills}\n \
            Reputation: {self.reputation}\n \
            Police Record: {self.policeRecord}\n \
            Time Played: {self.timePlayed}"
        return cmdr_string

    def get_net_worth(self):
        # TODO include moon value eventually
        return self.credits + self.ship.get_value() - self.debt

    def get_reputation(self) -> str:
        return CombatReputation.get_reputation_string(self.reputation)

    def get_police_record(self):
        return CriminalRecord.get_record_string(self.policeRecord)

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

    def pay_insurance(self):
        #! AI generated placeholder
        insurance = self.ship.get_value() * INSURANCE_RATE
        if self.credits > insurance:
            self.credits -= insurance
        else:
            self.debt += insurance - self.credits
            self.credits = 0

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
