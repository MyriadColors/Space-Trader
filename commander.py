import constants as const


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
            debt_interest = max(1, self.debt * const.INTEREST_RATE)
            if self.credits > debt_interest:
                self.credits -= debt_interest
            else:
                self.debt += debt_interest - self.credits
                self.credits = 0
        self.debt = self.debt * 1.1
