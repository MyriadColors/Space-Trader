from .markets import Bank, BuyCargo, BuyEquipment, SellCargo, SellEquipment

# from .commander_status import CommanderInfo, Personnel, Quests, ShipInfo, SpecialCargo
from .screens import Screen

# from .shipyard import BuyShip, Shipyard
from .system_info import AvgPrices, LongRange, ShortRange, SystemInfo, TargetSystem

SCREENS = {
    "I": {
        "name": "system_info",
        "title": "System Info",
        "class": SystemInfo,
    },
    "B": {
        "name": "buy_cargo",
        "title": "Buy Cargo",
    },
    "S": {
        "name": "sell_cargo",
        "title": "Sell Cargo",
    },
    "Y": {
        "name": "shipyard",
        "title": "Shipyard",
    },
    "W": {
        "name": "short_range_chart",
        "title": "Short Range Chart",
    },
    "E": {
        "name": "buy_equipment",
        "title": "Buy Equipment",
    },
    "Q": {
        "name": "sell_equipment",
        "title": "Sell Equipment",
    },
    "P": {
        "name": "personnel",
        "title": "Personnel",
    },
    "K": {
        "name": "bank",
        "title": "Bank",
    },
    "C": {
        "name": "commander_status",
        "title": "Commander Status",
    },
    "G": {
        "name": "galactic_chart",
        "title": "Galactic Chart",
    },
    "O": {
        "name": "options",
        "title": "Options",
    },
}


class ScreenManager:

    def __init__(self, window):
        self.window = window

        self.screens = self.build_screens()
        self.current_screen = None
        # self.go_to_screen(self.current_screen)

    def set_screen(self, screen):
        self.current_screen = screen

    def get_screen(self, screen):
        return self.screens[screen]

    def go_to_screen(self, key):
        screen = self.get_screen(key)
        screen.tkraise()

    def build_screens(self) -> dict[str, Screen]:
        screen_dict = {
            "I": SystemInfo(self.window, "System Info", self),
            "B": BuyCargo(self.window, "Buy Cargo", self),
            "S": SellCargo(self.window, "Sell Cargo", self),
            # "Y": Shipyard,
            "W": ShortRange(self.window, "Short Range Chart", self),
            "E": BuyEquipment(self.window, "Buy Equipment", self),
            "Q": SellEquipment(self.window, "Sell Equipment", self),
            # "P": Personnel,
            "K": Bank(self.window, "Bank", self),
            # "C": CharInfo,
            "G": LongRange(self.window, "Long Range Chart", self),
            # "O": Quests,
            # "A": ShipInfo,
            # "U": SpecialCargo,
            "T": TargetSystem(self.window, "Target System", self),
            "V": AvgPrices(self.window, "Average Prices", self),
        }
        return screen_dict
