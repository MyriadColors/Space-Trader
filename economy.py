from constants import SpecialResource, SystemPressure, TechLevel


class Ware:

    def __init__(
        self,
        name,
        tech_level_prod,
        tech_level_min,
        tech_level_max,
        max_price,
        min_price,
        pressure_price,
        pressure,
        special_resource,
        special_resource_no,
        min_prod,
        max_prod,
        quantity,
    ):

        self.name = name
        self.tech_level_prod = tech_level_prod
        self.tech_level_min = tech_level_min
        self.tech_level_max = tech_level_max
        self.max_price = max_price
        self.min_price = min_price
        self.pressure_price = pressure_price
        self.pressure = pressure
        self.special_resource = special_resource
        self.special_resource_no = special_resource_no
        self.min_prod = min_prod
        self.max_prod = max_prod
        self.quantity = quantity


class TradeItem(Ware):

    def __init__(self):
        self.Water = Ware(
            "Water",
            TechLevel.PRE_AGRICULTURAL,
            TechLevel.PRE_AGRICULTURAL,
            TechLevel.MEDIEVAL,
            30,
            3,
            4,
            SystemPressure.DROUGHT,
            SpecialResource.SWEETOCEANS,
            SpecialResource.DESERT,
            30,
            50,
            1,
        )
        self.Furs = Ware(
            "Furs",
            TechLevel.PRE_AGRICULTURAL,
            TechLevel.PRE_AGRICULTURAL,
            TechLevel.PRE_AGRICULTURAL,
            250,
            10,
            10,
            SystemPressure.COLD,
            SpecialResource.RICHFAUNA,
            SpecialResource.LIFELESS,
            230,
            280,
            5,
        )
        self.Food = Ware(
            "Food",
            TechLevel.AGRICULTURAL,
            TechLevel.PRE_AGRICULTURAL,
            TechLevel.AGRICULTURAL,
            100,
            5,
            5,
            SystemPressure.CROPFAILURE,
            SpecialResource.RICHSOIL,
            SpecialResource.POORSOIL,
            90,
            160,
            5,
        )
        self.Ore = Ware(
            "Ore",
            TechLevel.MEDIEVAL,
            TechLevel.MEDIEVAL,
            TechLevel.RENAISSANCE,
            350,
            20,
            10,
            SystemPressure.WAR,
            SpecialResource.MINERAL_RICH,
            SpecialResource.MINERAL_POOR,
            350,
            420,
            10,
        )
        self.Games = Ware(
            "Games",
            TechLevel.RENAISSANCE,
            TechLevel.AGRICULTURAL,
            TechLevel.POST_INDUSTRIAL,
            250,
            -10,
            5,
            SystemPressure.BOREDOM,
            SpecialResource.ARTISTIC,
            SpecialResource.NOTHING,
            160,
            270,
            5,
        )
        self.Firearms = Ware(
            "Firearms",
            TechLevel.RENAISSANCE,
            TechLevel.AGRICULTURAL,
            TechLevel.INDUSTRIAL,
            1250,
            -75,
            100,
            SystemPressure.WAR,
            SpecialResource.WARLIKE,
            SpecialResource.NOTHING,
            600,
            1100,
            25,
        )
        self.Medicine = Ware(
            "Medicine",
            TechLevel.EARLY_INDUSTRIAL,
            TechLevel.AGRICULTURAL,
            TechLevel.POST_INDUSTRIAL,
            650,
            -20,
            10,
            SystemPressure.PLAGUE,
            SpecialResource.SPECIALHERBS,
            SpecialResource.NOTHING,
            400,
            700,
            25,
        )
        self.Machines = Ware(
            "Machines",
            TechLevel.EARLY_INDUSTRIAL,
            TechLevel.RENAISSANCE,
            TechLevel.INDUSTRIAL,
            900,
            -30,
            5,
            SystemPressure.EMPLOYMENT,
            SpecialResource.NOTHING,
            SpecialResource.NOTHING,
            600,
            800,
            25,
        )
        self.Narcotics = Ware(
            "Narcotics",
            TechLevel.INDUSTRIAL,
            TechLevel.PRE_AGRICULTURAL,
            TechLevel.INDUSTRIAL,
            3500,
            -125,
            150,
            SystemPressure.BOREDOM,
            SpecialResource.WEIRDMUSHROOMS,
            SpecialResource.NOTHING,
            2000,
            3000,
            50,
        )
        self.Robots = Ware(
            "Robots",
            TechLevel.POST_INDUSTRIAL,
            TechLevel.EARLY_INDUSTRIAL,
            TechLevel.HI_TECH,
            5000,
            -150,
            100,
            SystemPressure.EMPLOYMENT,
            SpecialResource.NOTHING,
            SpecialResource.NOTHING,
            3500,
            5000,
            100,
        )


"""
class TradeItem/Goods:
Tradeitem("Water", 0, 0, 2, 30, +3, 4, GameState.DROUGHT, GameState.LOTSOFWATER, GameState.DESERT, 30, 50, 1)
    key: name;
    tp: techProduction          // Tech level needed for production
    tu: techUsage               // Tech level needed to use
    ttp: techTopProduction      // Tech level which produces this item the most
    plt: priceLowTech           // Medium price at lowest tech level
    pi: priceInc                // Price increase per tech level
    var: variance               // Max percentage above or below calculated price
    dps: doublePriceStatus      // Price increases considerably when this event occurs
    cr: cheapResource           // When this resource is available, this trade item is cheap
    er: expensiveResource       // When this resource is available, this trade item is expensive
    mintp: minTradePrice        // Minimum price to buy/sell in orbit
    maxtp: maxTradePrice        // Maximum price to buy/sell in orbit
    ro: roundOff                // Roundoff price for trade in orbit
"""
GOODS = {
    "water": {
        "tp": 0,
        "tu": 0,
        "ttp": 2,
        "plt": 30,
        "pi": +3,
        "var": 4,
        "dps": "DROUGHT",
        "cr": "lotsofwater",
        "er": "desert",
        "mintp": 30,
        "maxtp": 50,
        "ro": 1,
    },
    "furs": {
        "tp": 0,
        "tu": 0,
        "ttp": 0,
        "plt": 250,
        "pi": +10,
        "var": 10,
        "dps": "cold",
        "cr": "faunarich",
        "er": "lifepoor",
        "mintp": 230,
        "maxtp": 280,
        "ro": 5,
    },
    "food": {
        "tp": 1,
        "tu": 0,
        "ttp": 1,
        "plt": 100,
        "pi": +5,
        "var": 5,
        "dps": "cropfailure",
        "cr": "soilrich",
        "er": "soilpoor",
        "mintp": 90,
        "maxtp": 160,
        "ro": 5,
    },
    "ore": {
        "tp": 2,
        "tu": 2,
        "ttp": 3,
        "plt": 350,
        "pi": +20,
        "var": 10,
        "dps": "war",
        "cr": "mineralrich",
        "er": "mineralpoor",
        "mintp": 350,
        "maxtp": 420,
        "ro": 10,
    },
    "games": {
        "tp": 3,
        "tu": 1,
        "ttp": 6,
        "plt": 250,
        "pi": -10,
        "var": 5,
        "dps": "boredom",
        "cr": "artistic",
        "er": None,
        "mintp": 160,
        "maxtp": 270,
        "ro": 5,
    },
    "firearms": {
        "tp": 3,
        "tu": 1,
        "ttp": 5,
        "plt": 1250,
        "pi": -75,
        "var": 100,
        "dps": "war",
        "cr": "warlike",
        "er": None,
        "mintp": 600,
        "maxtp": 1100,
        "ro": 25,
    },
    "medicines": {
        "tp": 4,
        "tu": 1,
        "ttp": 6,
        "plt": 650,
        "pi": -20,
        "var": 10,
        "dps": "plague",
        "cr": "lotsofherbs",
        "er": None,
        "mintp": 400,
        "maxtp": 700,
        "ro": 25,
    },
    "machines": {
        "tp": 4,
        "tu": 3,
        "ttp": 5,
        "plt": 900,
        "pi": -30,
        "var": 5,
        "dps": "lackofworkers",
        "cr": None,
        "er": None,
        "mintp": 600,
        "maxtp": 800,
        "ro": 25,
    },
    "narcotics": {
        "tp": 5,
        "tu": 0,
        "ttp": 5,
        "plt": 3500,
        "pi": -125,
        "var": 150,
        "dps": "boredom",
        "cr": "weirdmushrooms",
        "er": None,
        "mintp": 2000,
        "maxtp": 3000,
        "ro": 50,
    },
    "robots": {
        "tp": 6,
        "tu": 4,
        "ttp": 7,
        "plt": 5000,
        "pi": -150,
        "var": 100,
        "dps": "lackofworkers",
        "cr": None,
        "er": None,
        "mintp": 3500,
        "maxtp": 5000,
        "ro": 100,
    },
    "fuel": {
        "tp": 4,
        "tu": 0,
        "ttp": 7,
        "plt": 17,
        "pi": -1,
        "var": 15,
        "dps": "war",
        "cr": "warlike",
        "er": None,
        "mintp": 17,
        "maxtp": 5000,
        "ro": 1,
    },
}
