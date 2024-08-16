screens = {
    "I": {
        "name": "system_info",
        "title": "System Info",
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

    def __init__(self, game):
        self.game = game
        self.screens = screens
        self.current_screen = None

    def set_screen(self, screen):
        self.current_screen = screen

    def get_screen(self, screen):
        return self.screens[screen]

    def go_to_screen(self, screen):
        self.game.current_state = self.get_screen(screen)["name"]
