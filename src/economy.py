"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Economy Module
    This module contains the classes and functions for the game economy such as trade wares and prices.
"""


class TradeItemId:
    WATER = 0
    FURS = 1
    FOOD = 2
    ORE = 3
    GAMES = 4
    FIREARMS = 5
    MEDICINE = 6
    MACHINERY = 7
    NARCOTICS = 8
    ROBOTS = 9
    NONE = 10

    @staticmethod
    def enum() -> list[int]:
        return range(10)

    @staticmethod
    def lst() -> list[str]:
        return [
            "Water",
            "Furs",
            "Food",
            "Ore",
            "Games",
            "Firearms",
            "Medicine",
            "Machinery",
            "Narcotics",
            "Robots",
        ]


class Ware:
    """
    Class containing the trade wares and their respective attributes.

    params: name - Trade item name
    params: tech_level_prod - Tech level needed for production
    params: tech_level_min - Tech level needed to use
    params: tech_level_max - Tech level which produces this item the most
    params: max_price - Medium price at lowest tech level
    params: min_price - Price increase per tech level
    params: pressure_price - Max percentage above or below calculated price
    params: pressure - Price increases considerably when this event occurs
    params: special_resource_drop - When this resource is available, this trade item is cheap
    params: special_resource_hike - When this resource is available, this trade item is expensive
    params: min_prod - Minimum price to buy/sell in orbit
    params: max_prod - Maximum price to buy/sell in orbit
    params: quantity - Roundoff price for trade in orbit
    """

    # TODO min and max price descriptions need to be checked against code
    # TODO min_prod and max_prod descriptions need to be checked against code, seem duplicated
    def __init__(
        self,
        name: str,
        tech_level_prod: int,
        tech_level_min: int,
        tech_level_max: int,
        max_price: int,
        min_price: int,
        pressure_price: int,
        pressure: int,
        special_resource_drop: int,
        special_resource_hike: int,
        min_prod: int,
        max_prod: int,
        quantity: int,
    ):
        self.name = name
        self.tech_level_prod = tech_level_prod
        self.tech_level_min = tech_level_min
        self.tech_level_max = tech_level_max
        self.max_price = max_price
        self.min_price = min_price
        self.pressure_price = pressure_price
        self.pressure = pressure
        self.special_resource_drop = special_resource_drop
        self.special_resource_hike = special_resource_hike
        self.min_prod = min_prod
        self.max_prod = max_prod
        self.quantity = quantity

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
