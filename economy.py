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
        self.Water = (
            Ware(
                "Water",
                TechLevel.PreAgricultural,
                TechLevel.PreAgricultural,
                TechLevel.Medieval,
                30,
                3,
                4,
                SystemPressure.Drought,
                SpecialResource.SweetOceans,
                SpecialResource.Desert,
                30,
                50,
                1,
            ),
        )
        self.Furs = (
            Ware(
                "Furs",
                TechLevel.PreAgricultural,
                TechLevel.PreAgricultural,
                TechLevel.PreAgricultural,
                250,
                10,
                10,
                SystemPressure.Cold,
                SpecialResource.RichFauna,
                SpecialResource.Lifeless,
                230,
                280,
                5,
            ),
        )
        self.Food = (
            Ware(
                "Food",
                TechLevel.Agricultural,
                TechLevel.PreAgricultural,
                TechLevel.Agricultural,
                100,
                5,
                5,
                SystemPressure.CropFailure,
                SpecialResource.RichSoil,
                SpecialResource.PoorSoil,
                90,
                160,
                5,
            ),
        )
        self.Ore = (
            Ware(
                "Ore",
                TechLevel.Medieval,
                TechLevel.Medieval,
                TechLevel.Renaissance,
                350,
                20,
                10,
                SystemPressure.War,
                SpecialResource.MineralRich,
                SpecialResource.MineralPoor,
                350,
                420,
                10,
            ),
        )
        self.Games = (
            Ware(
                "Games",
                TechLevel.Renaissance,
                TechLevel.Agricultural,
                TechLevel.PostIndustrial,
                250,
                -10,
                5,
                SystemPressure.Boredom,
                SpecialResource.Artistic,
                SpecialResource.NA,
                160,
                270,
                5,
            ),
        )
        self.Firearms = (
            Ware(
                "Firearms",
                TechLevel.Renaissance,
                TechLevel.Agricultural,
                TechLevel.Industrial,
                1250,
                -75,
                100,
                SystemPressure.War,
                SpecialResource.Warlike,
                SpecialResource.NA,
                600,
                1100,
                25,
            ),
        )
        self.Medicine = (
            Ware(
                "Medicine",
                TechLevel.EarlyIndustrial,
                TechLevel.Agricultural,
                TechLevel.PostIndustrial,
                650,
                -20,
                10,
                SystemPressure.Plague,
                SpecialResource.SpecialHerbs,
                SpecialResource.NA,
                400,
                700,
                25,
            ),
        )
        self.Machines = (
            Ware(
                "Machines",
                TechLevel.EarlyIndustrial,
                TechLevel.Renaissance,
                TechLevel.Industrial,
                900,
                -30,
                5,
                SystemPressure.Employment,
                SpecialResource.NA,
                SpecialResource.NA,
                600,
                800,
                25,
            ),
        )
        self.Narcotics = (
            Ware(
                "Narcotics",
                TechLevel.Industrial,
                TechLevel.PreAgricultural,
                TechLevel.Industrial,
                3500,
                -125,
                150,
                SystemPressure.Boredom,
                SpecialResource.WeirdMushrooms,
                SpecialResource.NA,
                2000,
                3000,
                50,
            ),
        )
        self.Robots = Ware(
            "Robots",
            TechLevel.PostIndustrial,
            TechLevel.EarlyIndustrial,
            TechLevel.HiTech,
            5000,
            -150,
            100,
            SystemPressure.Employment,
            SpecialResource.NA,
            SpecialResource.NA,
            3500,
            5000,
            100,
        )
