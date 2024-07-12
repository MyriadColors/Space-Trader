"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Planet Module
    This module houses the classes and functions for a planet object.
    This subsequently includes the planets' government, economy, and tech level.
"""

from math import floor, pow, sqrt
from random import choice, randint

from constants import GOVT_NAMES, SPECIALRESOURCES


class Planet:
    """
    Object representing a single planet in the game world.

    params: name - planet name
    params: x - x coordinate of the planet
    params: y - y coordinate of the planet
    params: size - planet size
    params: tech_level - tech level of the planet
    params: govt_type - political system type of the planet
    params: soci_pressure - current pressure on the planet
    params: special_resource - current special resource of the planet
    params: quest_system - whether the planet is a quest host
    params: trade_items - items available for trade on the planet
    #? params: count_down - countdown
    params: visited - whether the planet has been visited
    #? params: shipyard_id - id of the shipyard in the system
    """

    def __init__(self, name, x, y, size, govt_type, tech_level, soci_pressure, special_resource):
        self.name = name
        self.x = x
        self.y = y
        self.size = size
        self.govt_type = govt_type
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
    def get_location(self):
        return (self.x, self.y)

    def get_size(self):
        """
        Planet sizes:

        0 = Tiny
        1 = Small
        2 = Medium
        3 = Large
        4 = Huge
        5 = Gargantuan
        """
        return self.size

    def set_visited(self):
        self.visited = True

    def get_tech_level(self):
        """
        Tech levels:

        0 = Pre-Agricultural
        1 = Agricultural
        2 = Medieval
        3 = Renaissance
        4 = Early Industrial
        5 = Industrial
        6 = Post-Industrial
        7 = Hi-Tech
        """
        return self.tech_level

    def set_tech_level(self, value):
        self.tech_level = value

    # TODO implement
    def dest_is_ok(self):
        comm = Game.current_game.commander
        return self != comm.current_system and (
            self.get_distance() <= comm.ship.fuel or Functions.wormhole_exists(comm.current_system, self)
        )

    def get_distance(self, target_planet=None):
        return int(floor(sqrt(pow(self.x - target_planet.x, 2) + pow(self.y - target_planet.y, 2))))

    # Political Interfaces
    # TODO maybe change to alter_ and handle political shift logic here
    def set_govt_type(self, value):
        self.govt_type = value

    def get_govt_type(self):
        return self.govt_type

    def get_government_name(self):
        return GOVT_NAMES[self.govt_type]

    # Economic Interfaces
    def get_pressure(self):
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

    def set_pressure(self, value):
        self.soci_pressure = value

    def get_special_resource(self):
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
            self.special_resource = choice(SPECIALRESOURCES)
            return self.special_resource

    def initialize_trade_items(self):
        for i in range(len(Consts.TradeItems)):
            if not self.is_item_traded(Consts.TradeItems[i]):
                self.trade_items[i] = 0
            else:
                self.trade_items[i] = (self.size.cast_to_int() + 1) * (
                    randint(9, 14)
                    - abs(Consts.TradeItems[i].tech_top_production.cast_to_int() - self.tech_level.cast_to_int())
                )

                if i >= TradeItemType.NARCOTICS.cast_to_int():
                    self.trade_items[i] = (
                        (self.trade_items[i] * (5 - Game.current_game.difficulty_id))
                        / (6 - Game.current_game.difficulty_id)
                    ) + 1

                if self.special_resource == Consts.TradeItems[i].resource_low_price:
                    self.trade_items[i] = self.trade_items[i] * 4 / 3

                if self.special_resource == Consts.TradeItems[i].resource_high_price:
                    self.trade_items[i] = self.trade_items[i] * 3 / 4

                if self.system_pressure == Consts.TradeItems[i].pressure_price_hike:
                    self.trade_items[i] = self.trade_items[i] / 5

                self.trade_items[i] = self.trade_items[i] - randint(10) + randint(10)

                if self.trade_items[i] < 0:
                    self.trade_items[i] = 0

    def is_item_traded(self, item):
        return (
            (item.item_type != TradeItemType.NARCOTICS or self.get_political_system().is_drugs_ok())
            and (item.item_type != TradeItemType.FIREARMS or self.get_political_system().is_firearms_ok())
            and self.tech_level.cast_to_int() >= item.tech_production.cast_to_int()
        )

    def item_used(self, item):
        return (
            (item.item_type != TradeItemType.NARCOTICS or self.get_political_system().is_drugs_ok())
            and (item.item_type != TradeItemType.FIREARMS or self.get_political_system().is_firearms_ok())
            and self.tech_level.cast_to_int() >= item.tech_usage.cast_to_int()
        )

    def get_inventory(self):
        return self.trade_items

    # Misc Interfaces
    # TODO implement
    def get_mercenaries_for_hire(self):
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
        cmdr = Game.current_game.commander
        return [
            merc
            for merc in Game.current_game.mercenaries.values()
            if merc.is_mercenary() and merc.current_system == cmdr.current_system and not cmdr.ship.has_crew(merc.id)
        ]

    def is_quest_system(self):
        return self.quest_system

    def set_quest_system(self, value):
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
        pass
