"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Economy Module
    This module contains the classes and functions for the game economy such as trade wares and prices.
"""

from constants import SocietalPressure, SpecialResource, TechLevel, TradeItemType


# TODO min and max price descriptions need to be checked against code
# TODO min_prod and max_prod descriptions need to be checked against code, seem duplicated
class Ware:
    """
    Class containing the trade wares and their respective attributes.

    params: id - enum TradeItemType
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

    def __init__(
        self,
        id,
        tech_level_prod,
        tech_level_min,
        tech_level_max,
        max_price,
        min_price,
        pressure_price,
        pressure,
        special_resource_drop,
        special_resource_hike,
        min_prod,
        max_prod,
        quantity,
    ):

        self.id = id
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


TradeItems = {
    TradeItemType.WATER: Ware(
        "Water",
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.MEDIEVAL,
        30,
        3,
        4,
        SocietalPressure.DROUGHT,
        SpecialResource.SWEETOCEANS,
        SpecialResource.DESERT,
        30,
        50,
        1,
    ),
    TradeItemType.FURS: Ware(
        "Furs",
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.PRE_AGRICULTURAL,
        250,
        10,
        10,
        SocietalPressure.COLD,
        SpecialResource.RICHFAUNA,
        SpecialResource.LIFELESS,
        230,
        280,
        5,
    ),
    TradeItemType.FOOD: Ware(
        "Food",
        TechLevel.AGRICULTURAL,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.AGRICULTURAL,
        100,
        5,
        5,
        SocietalPressure.CROPFAILURE,
        SpecialResource.RICHSOIL,
        SpecialResource.POORSOIL,
        90,
        160,
        5,
    ),
    TradeItemType.ORE: Ware(
        "Ore",
        TechLevel.MEDIEVAL,
        TechLevel.MEDIEVAL,
        TechLevel.RENAISSANCE,
        350,
        20,
        10,
        SocietalPressure.WAR,
        SpecialResource.MINERAL_RICH,
        SpecialResource.MINERAL_POOR,
        350,
        420,
        10,
    ),
    TradeItemType.GAMES: Ware(
        "Games",
        TechLevel.RENAISSANCE,
        TechLevel.AGRICULTURAL,
        TechLevel.POST_INDUSTRIAL,
        250,
        -10,
        5,
        SocietalPressure.BOREDOM,
        SpecialResource.ARTISTIC,
        SpecialResource.NOTHING,
        160,
        270,
        5,
    ),
    TradeItemType.FIREARMS: Ware(
        "Firearms",
        TechLevel.RENAISSANCE,
        TechLevel.AGRICULTURAL,
        TechLevel.INDUSTRIAL,
        1250,
        -75,
        100,
        SocietalPressure.WAR,
        SpecialResource.WARLIKE,
        SpecialResource.NOTHING,
        600,
        1100,
        25,
    ),
    TradeItemType.MEDICINE: Ware(
        "Medicine",
        TechLevel.EARLY_INDUSTRIAL,
        TechLevel.AGRICULTURAL,
        TechLevel.POST_INDUSTRIAL,
        650,
        -20,
        10,
        SocietalPressure.PLAGUE,
        SpecialResource.SPECIALHERBS,
        SpecialResource.NOTHING,
        400,
        700,
        25,
    ),
    TradeItemType.MACHINERY: Ware(
        "Machinery",
        TechLevel.EARLY_INDUSTRIAL,
        TechLevel.RENAISSANCE,
        TechLevel.INDUSTRIAL,
        900,
        -30,
        5,
        SocietalPressure.EMPLOYMENT,
        SpecialResource.NOTHING,
        SpecialResource.NOTHING,
        600,
        800,
        25,
    ),
    TradeItemType.NARCOTICS: Ware(
        "Narrcotics",
        TechLevel.INDUSTRIAL,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.INDUSTRIAL,
        3500,
        -125,
        150,
        SocietalPressure.BOREDOM,
        SpecialResource.WEIRDMUSHROOMS,
        SpecialResource.NOTHING,
        2000,
        3000,
        50,
    ),
    TradeItemType.ROBOTS: Ware(
        "Robots",
        TechLevel.POST_INDUSTRIAL,
        TechLevel.EARLY_INDUSTRIAL,
        TechLevel.HI_TECH,
        5000,
        -150,
        100,
        SocietalPressure.EMPLOYMENT,
        SpecialResource.NOTHING,
        SpecialResource.NOTHING,
        3500,
        5000,
        100,
    ),
}
