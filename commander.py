from constants import INSURANCE_RATE, INTEREST_RATE, Skills


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
