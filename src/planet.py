"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Planet Module
    This module houses the classes and functions for a planet object.
    This subsequently includes the planets' government, economy, and tech level.
"""

from math import floor, pow, sqrt
from random import randint

from .constants import Size, SpecialResource
from .economy import TradeItemId
from .game_data import TRADEITEMS
from .government import PoliticalSystem

TMPGAMEDIFFICULTY = 1


class Planet:
    """
    Object representing a single planet in the game world.

    params: name - planet name
    params: x - x coordinate of the planet
    params: y - y coordinate of the planet
    params: size - planet size
    params: tech_level - tech level of the planet
    params: government - political system type of the planet
    params: soci_pressure - current pressure on the planet
    params: special_resource - current special resource of the planet
    params: quest_system - whether the planet is a quest host
    params: trade_items - items available for trade on the planet
    #? params: count_down - countdown
    params: visited - whether the planet has been visited
    #? params: shipyard_id - id of the shipyard in the system
    """

    def __init__(
        self,
        name,
        x: int,
        y: int,
        size: int,
        government: PoliticalSystem,
        tech_level: int,
        soci_pressure: int,
        special_resource: int,
    ):
        self.name = name
        self.x = x
        self.y = y
        self.size = size
        self.government = government
        self.tech_level = tech_level
        self.soci_pressure = soci_pressure
        self.special_resource = special_resource
        self.quest_system = False
        self.trade_items = [0] * 10
        self.count_down = 0
        self.visited = False
        self.shipyard_id = None

        self.initialize_trade_items()

    # Basic Info Interfaces
    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        repr_str = f"{self.name} ({self.x}, {self.y}), \
            {Size.name(self.size)}, {self.get_government_name()}, \
            {self.get_tech_level()}, {SpecialResource.name(self.special_resource)}, \
            {self.soci_pressure}, {self.government.law}, {self.government.crime}"
        return repr_str

    def pprint(self) -> str:
        info = f"""---------------
        Planet: {self.name} at ({self.x}, {self.y})\n \
        Size: {Size.name(self.size)}\n \
        Tech Level: {self.tech_level}\n \
        Government: {self.get_government_name()}\n \
        Resources: {SpecialResource.name(self.special_resource)}\n \
        Police: {self.government.law}\n \
        Pirates: {self.government.crime}\n \
        Pressure: {self.soci_pressure}\n \
        ---------------
        """
        return info

    def get_location(self) -> tuple[int, int]:
        return (self.x, self.y)

    def get_size(self) -> int:
        return self.size

    def get_tech_level(self) -> int:
        return self.tech_level

    def set_visited(self) -> None:
        self.visited = True

    def set_tech_level(self, value) -> None:
        self.tech_level = value

    # TODO implement
    def dest_is_ok(self) -> bool:
        """
        Check if the destination is reachable with the current fuel level
        Also account for wormholes

        return: bool - whether the destination is reachable
        """
        raise NotImplementedError("Planet.dest_is_ok not implemented")
        # comm = Game.current_game.commander
        # return self != comm.current_system and (
        #     self.get_distance() <= comm.ship.fuel or Functions.wormhole_exists(comm.current_system, self)
        # )

    def get_distance(self, target_planet=None):
        return int(floor(sqrt(pow(self.x - target_planet.x, 2) + pow(self.y - target_planet.y, 2))))

    # Political Interfaces
    # TODO maybe change to alter_ and handle political shift logic here
    def set_govt_type(self, value) -> None:
        self.government = value

    def get_govt_type(self) -> PoliticalSystem:
        return self.government

    def get_government_name(self) -> str:
        return str(self.government)

    # Economic Interfaces
    def get_pressure(self) -> int:
        """
        Societal pressures:

        0 = under no particular pressure; Uneventful
        1 = at war; Ore and Weapons in demand
        2 = ravaged by a plague; Medicine in demand
        3 = suffering from a drought; Water in demand
        4 = suffering from extreme boredom; Games and Narcotics in demand
        5 = suffering from a cold spell; Furs in demand
        6 = suffering from a crop failure; Food in demand
        7 = lacking enough workers; Machinery and Robots in demand
        """
        return self.soci_pressure

    def set_pressure(self, value: int) -> None:
        self.soci_pressure = value

    def get_special_resource(self) -> int:
        """
        Special resources:

        0 = Nothing Special
        1 = Mineral Rich
        2 = Mineral Poor
        3 = Desert
        4 = Sweetwater Oceans
        5 = Rich Soil
        6 = Poor Soil
        7 = Rich Fauna
        8 = Lifeless
        9 = Weird Mushrooms
        10 = Special Herbs
        11 = Artistic Populace
        12 = Warlike Populace
        """
        if self.visited:
            return self.special_resource
        # TODO maybe not random here?
        else:
            self.special_resource = SpecialResource.random()
            return self.special_resource

    def initialize_trade_items(self):
        """
        Set the starting quantity of each trade good for the planet
        """

        for item_id in TradeItemId.enum():

            # Make sure the item is allowed to be traded
            if not self.is_item_traded(item_id):
                self.trade_items[item_id] = 0
            else:
                # Quantity is dictated by the planet tech level, size, and a bit of randomness
                self.trade_items[item_id] = (self.size + 1) * (
                    randint(9, 14) - abs(TRADEITEMS[item_id].tech_level_max - self.tech_level)
                )

            # Because of the enormous profitssss possible,
            # there shouldn't be too many robots or narcotics available
            if item_id >= TradeItemId.NARCOTICS:
                self.trade_items[item_id] = (
                    (self.trade_items[item_id] * (5 - TMPGAMEDIFFICULTY)) / (6 - TMPGAMEDIFFICULTY)
                ) + 1

            # Adjust for special resources and societal pressures
            if self.special_resource == TRADEITEMS[item_id].special_resource_drop:
                self.trade_items[item_id] = self.trade_items[item_id] * 4 / 3
            if self.special_resource == TRADEITEMS[item_id].special_resource_hike:
                self.trade_items[item_id] = self.trade_items[item_id] * 3 / 4
            if self.soci_pressure == TRADEITEMS[item_id].pressure:
                self.trade_items[item_id] = self.trade_items[item_id] / 5

            # Another small random factor
            self.trade_items[item_id] = self.trade_items[item_id] - randint(1, 10) + randint(1, 10)

            # Finally just make sure it's not negative
            if self.trade_items[item_id] < 0:
                self.trade_items[item_id] = 0

    def is_item_traded(self, item) -> bool:
        """
        Given an item ID, check with the planets political system to see if it can be traded

        params: item - item ID to check

        return: bool - whether the item can be traded
        """

        if item not in [TradeItemId.FIREARMS, TradeItemId.NARCOTICS]:
            return True

        if item == TradeItemId.FIREARMS:
            return self.government.firearms_ok()

        elif item == TradeItemId.NARCOTICS:
            return self.government.drugs_ok()

        else:
            raise ValueError(f"Item ID {item} not valid!")

    def item_used(self, item):
        raise NotImplementedError("Planet.item_used not implemented")
        # return (
        #     (item.item_type != d.NARCOTICS or self.get_political_system().is_drugs_ok())
        #     and (item.item_type != d.FIREARMS or self.get_political_system().is_firearms_ok())
        #     and self.tech_level.cast_to_int() >= item.tech_usage.cast_to_int()
        # )

    def get_inventory(self):
        return self.trade_items

    # Misc Interfaces
    # TODO implement
    def get_mercenaries_for_hire(self) -> list:
        """
        Commander			cmdr		= Game.CurrentGame.Commander;
        CrewMember[]	mercs		= Game.CurrentGame.Mercenaries;
        ArrayList			forHire	= new ArrayList(3);

        for (int i = 1; i < mercs.Length; i++)
        {
                if (mercs[i].CurrentSystem == cmdr.CurrentSystem && !cmdr.Ship.HasCrew(mercs[i].Id))
                        forHire.Add(mercs[i]);
        }

        return (CrewMember[])forHire.ToArray(typeof(CrewMember));
        """
        raise NotImplementedError("Planet.get_mercenaries_for_hire not implemented")
        # cmdr = Game.current_game.commander
        # return [
        #     merc
        #     for merc in Game.current_game.mercenaries.values()
        #     if merc.is_mercenary() and merc.current_system == cmdr.current_system and not cmdr.ship.has_crew(merc.id)
        # ]

    def is_quest_system(self) -> bool:
        return self.quest_system

    def set_quest_system(self, value) -> None:
        self.quest_system = value

    # TODO implement
    def show_quest_button(self):
        """
        public bool ShowSpecialButton()
        {
        Game	game	= Game.CurrentGame;
        bool	show	= false;

        switch (SpecialEventType)
        {
                case SpecialEventType.Artifact:
                case SpecialEventType.Dragonfly:
                case SpecialEventType.Experiment:
                case SpecialEventType.Jarek:
                        show	= game.Commander.PoliceRecordScore >= Consts.PoliceRecordScoreDubious;
                        break;
                case SpecialEventType.ArtifactDelivery:
                        show	= game.Commander.Ship.ArtifactOnBoard;
                        break;
                case SpecialEventType.CargoForSale:
                        show	= game.Commander.Ship.FreeCargoBays >= 3;
                        break;
                case SpecialEventType.DragonflyBaratas:
                        show	= game.QuestStatusDragonfly > SpecialEvent.StatusDragonflyNotStarted &&
                        game.QuestStatusDragonfly < SpecialEvent.StatusDragonflyDestroyed;
                        break;
                case SpecialEventType.DragonflyDestroyed:
                        show	= game.QuestStatusDragonfly == SpecialEvent.StatusDragonflyDestroyed;
                        break;
                case SpecialEventType.DragonflyMelina:
                        show	= game.QuestStatusDragonfly > SpecialEvent.StatusDragonflyFlyBaratas &&
                        game.QuestStatusDragonfly < SpecialEvent.StatusDragonflyDestroyed;
                        break;
                case SpecialEventType.DragonflyRegulas:
                        show	= game.QuestStatusDragonfly > SpecialEvent.StatusDragonflyFlyMelina &&
                        game.QuestStatusDragonfly < SpecialEvent.StatusDragonflyDestroyed;
                        break;
                case SpecialEventType.DragonflyShield:
                case SpecialEventType.ExperimentFailed:
                case SpecialEventType.Gemulon:
                case SpecialEventType.GemulonFuel:
                case SpecialEventType.GemulonInvaded:
                case SpecialEventType.Lottery:
                case SpecialEventType.ReactorLaser:
                case SpecialEventType.PrincessQuantum:
                case SpecialEventType.SculptureHiddenBays:
                case SpecialEventType.Skill:
                case SpecialEventType.SpaceMonster:
                case SpecialEventType.Tribble:
                        show	= true;
                        break;
                case SpecialEventType.EraseRecord:
                case SpecialEventType.Wild:
                        show	= game.Commander.PoliceRecordScore < Consts.PoliceRecordScoreDubious;
                        break;
                case SpecialEventType.ExperimentStopped:
                        show	= game.QuestStatusExperiment > SpecialEvent.StatusExperimentNotStarted &&
                    game.QuestStatusExperiment < SpecialEvent.StatusExperimentPerformed;
                        break;
                case SpecialEventType.GemulonRescued:
                        show	= game.QuestStatusGemulon > SpecialEvent.StatusGemulonNotStarted &&
                        game.QuestStatusGemulon < SpecialEvent.StatusGemulonTooLate;
                        break;
                case SpecialEventType.Japori:
                        show	= game.QuestStatusJapori						== SpecialEvent.StatusJaporiNotStarted &&
                        game.Commander.PoliceRecordScore	>= Consts.PoliceRecordScoreDubious;
                        break;
                case SpecialEventType.JaporiDelivery:
                        show	= game.QuestStatusJapori == SpecialEvent.StatusJaporiInTransit;
                        break;
                case SpecialEventType.JarekGetsOut:
                        show	= game.Commander.Ship.JarekOnBoard;
                        break;
                case SpecialEventType.Moon:
                        show	= game.QuestStatusMoon == SpecialEvent.StatusMoonNotStarted &&
                        game.Commander.Worth >  SpecialEvent.MoonCost * .8;
                        break;
                case SpecialEventType.MoonRetirement:
                        show	= game.QuestStatusMoon == SpecialEvent.StatusMoonBought;
                        break;
                case SpecialEventType.Princess:
                        show	= game.Commander.PoliceRecordScore	>= Consts.PoliceRecordScoreLawful &&
                        game.Commander.ReputationScore		>= Consts.ReputationScoreAverage;
                        break;
                case SpecialEventType.PrincessCentauri:
                        show	= game.QuestStatusPrincess >= SpecialEvent.StatusPrincessFlyCentauri &&
                        game.QuestStatusPrincess <= SpecialEvent.StatusPrincessFlyQonos;
                        break;
                case SpecialEventType.PrincessInthara:
                        show	= game.QuestStatusPrincess >= SpecialEvent.StatusPrincessFlyInthara &&
                        game.QuestStatusPrincess <= SpecialEvent.StatusPrincessFlyQonos;
                        break;
                case SpecialEventType.PrincessQonos:
                        show	= game.QuestStatusPrincess == SpecialEvent.StatusPrincessRescued &&
                                !game.Commander.Ship.PrincessOnBoard;
                        break;
                case SpecialEventType.PrincessReturned:
                        show	= game.Commander.Ship.PrincessOnBoard;
                        break;
                case SpecialEventType.Reactor:
                        show	= game.QuestStatusReactor						== SpecialEvent.StatusReactorNotStarted &&
                        game.Commander.PoliceRecordScore	<  Consts.PoliceRecordScoreDubious &&
                        game.Commander.ReputationScore		>= Consts.ReputationScoreAverage;
                        break;
                case SpecialEventType.ReactorDelivered:
                        show	= game.Commander.Ship.ReactorOnBoard;
                        break;
                case SpecialEventType.Scarab:
                        show	= game.QuestStatusScarab					== SpecialEvent.StatusScarabNotStarted &&
                                                        game.Commander.ReputationScore	>= Consts.ReputationScoreAverage;
                        break;
                case SpecialEventType.ScarabDestroyed:
                case SpecialEventType.ScarabUpgradeHull:
                        show	= game.QuestStatusScarab == SpecialEvent.StatusScarabDestroyed;
                        break;
                case SpecialEventType.Sculpture:
                        show	= game.QuestStatusSculpture					== SpecialEvent.StatusSculptureNotStarted &&
                        game.Commander.PoliceRecordScore	<  Consts.PoliceRecordScoreDubious &&
                        game.Commander.ReputationScore		>= Consts.ReputationScoreAverage;
                        break;
                case SpecialEventType.SculptureDelivered:
                        show	= game.QuestStatusSculpture	== SpecialEvent.StatusSculptureInTransit;
                        break;
                case SpecialEventType.SpaceMonsterKilled:
                        show	= game.QuestStatusSpaceMonster == SpecialEvent.StatusSpaceMonsterDestroyed;
                        break;
                case SpecialEventType.TribbleBuyer:
                        show	= game.Commander.Ship.Tribbles > 0;
                        break;
                case SpecialEventType.WildGetsOut:
                        show	= game.Commander.Ship.WildOnBoard;
                        break;
                default:
                        break;
        }

        return show;
        }
        """
        raise NotImplementedError("Planet.show_quest_button not implemented")
