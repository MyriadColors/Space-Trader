from constants import ACTIVITY, GOVERNMENT, TECHLEVEL


class PoliticalSystem:

    def __init__(
        self, type, stability, law, crime, economy, minTech, maxTech, trade, tradeable, smuggle, tradeItemType
    ):
        self.type = type
        self.stability = stability
        self.law = law
        self.crime = crime
        self.economy = economy
        self.minTech = minTech
        self.maxTech = maxTech
        self.trade = trade
        self.tradeable = tradeable
        self.smuggle = smuggle
        self.tradeItemType = tradeItemType


class PoliticalSystemType(PoliticalSystem):

    def __init__(self):
        self.Anarchy = PoliticalSystem(0, 0, 0, 7, 1, 0, 5, 7, True, True, TradeItemType.Food)
        self.Capitalist = PoliticalSystem(1, 2, 3, 2, 7, 4, 7, 1, True, True, TradeItemType.Ore)
        self.Communist = PoliticalSystem(2, 6, 5, 4, 4, 1, 5, 5, True, True, TradeItemType.NA)
        self.Confederacy = PoliticalSystem(3, 5, 4, 3, 6, 1, 6, 3, True, True, TradeItemType.Games)
        self.Corporate = PoliticalSystem(4, 2, 5, 2, 7, 4, 7, 2, True, True, TradeItemType.Robots)
        self.Cybernetic = PoliticalSystem(5, 0, 7, 7, 6, 6, 7, 0, False, False, TradeItemType.Ore)
        self.Democracy = PoliticalSystem(6, 4, 3, 2, 6, 3, 7, 2, True, True, TradeItemType.Games)
        self.Dictatorship = PoliticalSystem(7, 3, 4, 6, 3, 0, 7, 2, True, True, TradeItemType.NA)
        self.Fascist = PoliticalSystem(8, 7, 7, 7, 1, 4, 7, 0, False, True, TradeItemType.Machines)
        self.Feudal = PoliticalSystem(9, 1, 1, 5, 2, 0, 3, 6, True, True, TradeItemType.Firearms)
        self.Military = PoliticalSystem(10, 7, 7, 0, 5, 2, 7, 0, False, True, TradeItemType.Robots)
        self.Monarchy = PoliticalSystem(11, 3, 4, 3, 4, 0, 5, 4, True, True, TradeItemType.Medicine)
        self.Pacifist = PoliticalSystem(12, 7, 2, 1, 6, 0, 3, 1, True, False, TradeItemType.NA)
        self.Socialist = PoliticalSystem(13, 4, 2, 6, 3, 0, 5, 6, True, True, TradeItemType.NA)
        self.Satori = PoliticalSystem(14, 0, 1, 1, 1, 0, 1, 0, False, False, TradeItemType.NA)
        self.Technocracy = PoliticalSystem(15, 1, 5, 3, 5, 4, 7, 2, True, True, TradeItemType.Water)
        self.Theocracy = PoliticalSystem(16, 5, 5, 1, 4, 0, 4, 0, True, True, TradeItemType.Narcotics)
