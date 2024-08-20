from .commander_status import CommanderInfo, Personnel, Quests, ShipInfo, SpecialCargo
from .markets import Bank, BuyCargo, BuyEquipment, SellCargo, SellEquipment
from .screens import Screen
from .shipyard import BuyShip, Shipyard
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
        print(f"Screens: {self.screens}")
        self.current_screen = "I"
        self.go_to_screen(self.current_screen)

    def get_screen(self, screen):
        return self.screens[screen]

    def go_to_screen(self, key):
        try:
            self.screens[key].tkraise()
        except KeyError:
            raise KeyError(f"Key {key} not found in screens")
        except AttributeError:
            # self.screens[key].place(x=0, y=0, relwidth=1, relheight=1)
            raise AttributeError(f"{self.screens} at {key} does not have a tkraise method")
        except Exception as e:
            raise Exception(f"Unexpected error in go_to_screen: {e}")
        else:
            print(f"Switched to screen {key} ({self.screens[key]})")

    def build_screens(self) -> dict[str, Screen]:
        screen_dict = {
            "I": SystemInfo(self.window, "System Info", self),
            "B": BuyCargo(self.window, "Buy Cargo", self),
            "S": SellCargo(self.window, "Sell Cargo", self),
            "Y": Shipyard(self.window, "Shipyard", self),
            "W": ShortRange(self.window, "Short Range Chart", self),
            "E": BuyEquipment(self.window, "Buy Equipment", self),
            "Q": SellEquipment(self.window, "Sell Equipment", self),
            "P": Personnel(self.window, "Personnel", self),
            "K": Bank(self.window, "Bank", self),
            "C": CommanderInfo(self.window, "Character Info", self),
            "G": LongRange(self.window, "Long Range Chart", self),
            "O": Quests(self.window, "Quests", self),
            "A": ShipInfo(self.window, "Ship Info", self),
            "U": SpecialCargo(self.window, "Special Cargo", self),
            "T": TargetSystem(self.window, "Target System", self),
            "V": AvgPrices(self.window, "Average Prices", self),
            "Z": BuyShip(self.window, "Buy Ship", self),
        }
        return screen_dict
