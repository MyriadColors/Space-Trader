/*******************************************************************************
 *
 * Space Trader for Windows 2.00
 *
 * Copyright (C) 2005 Jay French, All Rights Reserved
 *
 * Additional coding by David Pierron
 * Original coding by Pieter Spronck, Sam Anderson, Samuel Goldstein, Matt Lee
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the Free
 * Software Foundation; either version 2 of the License, or (at your option) any
 * later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
 *
 * If you'd like a copy of the GNU General Public License, go to
 * http://www.gnu.org/copyleft/gpl.html.
 *
 * You can contact the author at spacetrader@frenchfryz.com
 *
 ******************************************************************************/
using System;
using System.Collections;
using System.Drawing;
using System.IO;

namespace Fryz.Apps.SpaceTrader
{
	public class Consts
	{
		#region Individual Constants

		// Directory structure and File constants.
		public static	string	BaseDirectory									= Environment.CurrentDirectory;
		public static	string	CustomDirectory								= Path.Combine(BaseDirectory, "custom");
		public static	string	DataDirectory									= Path.Combine(BaseDirectory, "data");
		public static	string	SaveDirectory									= Path.Combine(BaseDirectory, "save");

		public static	string	CustomImagesDirectory					= Path.Combine(CustomDirectory, "images");
		public static	string	CustomTemplatesDirectory			= Path.Combine(CustomDirectory, "templates");

		public static	string	HighScoreFile									= Path.Combine(DataDirectory, "HighScores.bin");
		public static	string	DefaultSettingsFile						= Path.Combine(DataDirectory, "DefaultSettings.bin");

	
		public const	int			StartClicks										= 20;
		public const	int			MaxFuelTanks									= 20;
		public const	int			FuelCompactorTanks						= 3;
		public const	int			HullUpgrade										= 50;
		public const	int			MaxShip												= 9;
		public const	int			MaxSlots											= 5;
		public const	int			FleaConversionCost						= 500;
		public const	int			PodTransferCost								= 200;

		public const	int			ImagesPerShip									= 4;
		public const	int			ShipImgOffsetNormal						= 0;
		public const	int			ShipImgOffsetDamage						= 1;
		public const	int			ShipImgOffsetShield						= 2;
		public const	int			ShipImgOffsetSheildDamage			= 3;
		public const	int			ShipImgUseDefault							= -1;
		public const	int			EncounterImgAlien							= 0;
		public const	int			EncounterImgPirate						= 1;
		public const	int			EncounterImgPolice						= 2;
		public const	int			EncounterImgSpecial						= 3;
		public const	int			EncounterImgTrader						= 4;

		public const	int			StoryProbability							= 50/8;
		public const	int			FabricRipInitialProbability		= 25;

		public const	int			DirectionUp										= 0;
		public const	int			DirectionDown									= 1;
		public const	int			DirectionLeft									= 2;
		public const	int			DirectionRight								= 3;

		public const	int			DisruptorSystemsMultiplier		= 3;

		
		#endregion

		#region Constant Arrays

		#region PoliticalSystems
		public static PoliticalSystem[]	PoliticalSystems	= new PoliticalSystem[]
		{
			new PoliticalSystem(PoliticalSystemType.Anarchy,      0, Activity.Absent,   Activity.Swarms,   Activity.Minimal,  TechLevel.PreAgricultural, TechLevel.Industrial,      7, true,  true,  TradeItemType.Food),
			new PoliticalSystem(PoliticalSystemType.Capitalist,   2, Activity.Some,     Activity.Few,      Activity.Swarms,   TechLevel.EarlyIndustrial, TechLevel.HiTech,          1, true,  true,  TradeItemType.Ore),
			new PoliticalSystem(PoliticalSystemType.Communist,    6, Activity.Abundant, Activity.Moderate, Activity.Moderate, TechLevel.Agricultural,    TechLevel.Industrial,      5, true,  true,  TradeItemType.NA),
			new PoliticalSystem(PoliticalSystemType.Confederacy,  5, Activity.Moderate, Activity.Some,     Activity.Many,     TechLevel.Agricultural,    TechLevel.PostIndustrial,  3, true,  true,  TradeItemType.Games),
			new PoliticalSystem(PoliticalSystemType.Corporate,    2, Activity.Abundant, Activity.Few,      Activity.Swarms,   TechLevel.EarlyIndustrial, TechLevel.HiTech,          2, true,  true,  TradeItemType.Robots),
			new PoliticalSystem(PoliticalSystemType.Cybernetic,   0, Activity.Swarms,   Activity.Swarms,   Activity.Many,     TechLevel.PostIndustrial,  TechLevel.HiTech,          0, false, false, TradeItemType.Ore),
			new PoliticalSystem(PoliticalSystemType.Democracy,    4, Activity.Some,     Activity.Few,      Activity.Many,     TechLevel.Renaissance,     TechLevel.HiTech,          2, true,  true,  TradeItemType.Games),
			new PoliticalSystem(PoliticalSystemType.Dictatorship, 3, Activity.Moderate, Activity.Many,     Activity.Some,     TechLevel.PreAgricultural, TechLevel.HiTech,          2, true,  true,  TradeItemType.NA),
			new PoliticalSystem(PoliticalSystemType.Fascist,      7, Activity.Swarms,   Activity.Swarms,   Activity.Minimal,  TechLevel.EarlyIndustrial, TechLevel.HiTech,          0, false, true,  TradeItemType.Machines),
			new PoliticalSystem(PoliticalSystemType.Feudal,       1, Activity.Minimal,  Activity.Abundant, Activity.Few,      TechLevel.PreAgricultural, TechLevel.Renaissance,     6, true,  true,  TradeItemType.Firearms),
			new PoliticalSystem(PoliticalSystemType.Military,     7, Activity.Swarms,   Activity.Absent,   Activity.Abundant, TechLevel.Medieval,        TechLevel.HiTech,          0, false, true,  TradeItemType.Robots),
			new PoliticalSystem(PoliticalSystemType.Monarchy,     3, Activity.Moderate, Activity.Some,     Activity.Moderate, TechLevel.PreAgricultural, TechLevel.Industrial,      4, true,  true,  TradeItemType.Medicine),
			new PoliticalSystem(PoliticalSystemType.Pacifist,     7, Activity.Few,      Activity.Minimal,  Activity.Many,     TechLevel.PreAgricultural, TechLevel.Renaissance,     1, true,  false, TradeItemType.NA),
			new PoliticalSystem(PoliticalSystemType.Socialist,    4, Activity.Few,      Activity.Many,     Activity.Some,     TechLevel.PreAgricultural, TechLevel.Industrial,      6, true,  true,  TradeItemType.NA),
			new PoliticalSystem(PoliticalSystemType.Satori,       0, Activity.Minimal,  Activity.Minimal,  Activity.Minimal,  TechLevel.PreAgricultural, TechLevel.Agricultural,    0, false, false, TradeItemType.NA),
			new PoliticalSystem(PoliticalSystemType.Technocracy,  1, Activity.Abundant, Activity.Some,     Activity.Abundant, TechLevel.EarlyIndustrial, TechLevel.HiTech,          2, true,  true,  TradeItemType.Water),
			new PoliticalSystem(PoliticalSystemType.Theocracy,    5, Activity.Abundant, Activity.Minimal,  Activity.Moderate, TechLevel.PreAgricultural, TechLevel.EarlyIndustrial, 0, true,  true,  TradeItemType.Narcotics)
		};
		#endregion

		#region ShipImageOffsets
		public static Rectangle[]	ShipImageOffsets	= new Rectangle[]
		{
			// We only care about X and Width, so set Y and Height to 0.
			new Rectangle(22, 0, 19, 0),	// Flea
			new Rectangle(18, 0, 27, 0),	// Gnat
			new Rectangle(18, 0, 27, 0),	// Firefly
			new Rectangle(18, 0, 27, 0),	// Mosquito
			new Rectangle(12, 0, 40, 0),	// Bumblebee
			new Rectangle(12, 0, 40, 0),	// Beetle
			new Rectangle( 7, 0, 50, 0),	// Hornet
			new Rectangle( 7, 0, 50, 0),	// Grasshopper
			new Rectangle( 2, 0, 60, 0),	// Termite
			new Rectangle( 2, 0, 60, 0),	// Wasp
			new Rectangle( 7, 0, 49, 0),	// Space Monster
			new Rectangle(21, 0, 22, 0),	// Dragonfly
			new Rectangle(15, 0, 34, 0),	// Mantis
			new Rectangle( 7, 0, 49, 0),	// Scarab
			new Rectangle( 9, 0, 46, 0),	// Bottle
			new Rectangle( 2, 0, 60, 0),	// Custom
			new Rectangle( 2, 0, 60, 0)		// Scorpion
		};
		#endregion

		#region SpecialCrewMemberIds
		public static ArrayList	SpecialCrewMemberIds = new ArrayList(new CrewMemberId[]
		{
			CrewMemberId.Commander,
			CrewMemberId.Dragonfly,
			CrewMemberId.FamousCaptain,
			CrewMemberId.Jarek,
			CrewMemberId.Opponent,
			CrewMemberId.Princess,
			CrewMemberId.Scarab,
			CrewMemberId.Scorpion,
			CrewMemberId.SpaceMonster,
			CrewMemberId.Wild
	});
		#endregion

		#region SpecialEvents
		public static SpecialEvent[]	SpecialEvents	= new SpecialEvent[]
		{
			new SpecialEvent(SpecialEventType.Artifact,                0, 1, false),
			new SpecialEvent(SpecialEventType.ArtifactDelivery,   -20000, 0, true),
			new SpecialEvent(SpecialEventType.CargoForSale,         1000, 3, false),
			new SpecialEvent(SpecialEventType.Dragonfly,               0, 1, true),
			new SpecialEvent(SpecialEventType.DragonflyBaratas,        0, 0, true),
			new SpecialEvent(SpecialEventType.DragonflyDestroyed,      0, 0, true),
			new SpecialEvent(SpecialEventType.DragonflyMelina,         0, 0, true),
			new SpecialEvent(SpecialEventType.DragonflyRegulas,        0, 0, true),
			new SpecialEvent(SpecialEventType.DragonflyShield,         0, 0, false),
			new SpecialEvent(SpecialEventType.EraseRecord,          5000, 3, false),
			new SpecialEvent(SpecialEventType.Experiment,              0, 0, true),
			new SpecialEvent(SpecialEventType.ExperimentFailed,        0, 0, true),
			new SpecialEvent(SpecialEventType.ExperimentStopped,       0, 0, true),
			new SpecialEvent(SpecialEventType.Gemulon,                 0, 0, true),
			new SpecialEvent(SpecialEventType.GemulonFuel,             0, 0, false),
			new SpecialEvent(SpecialEventType.GemulonInvaded,          0, 0, true),
			new SpecialEvent(SpecialEventType.GemulonRescued,          0, 0, true),
			new SpecialEvent(SpecialEventType.Japori,                  0, 1, false),
			new SpecialEvent(SpecialEventType.JaporiDelivery,          0, 0, true),
			new SpecialEvent(SpecialEventType.Jarek,                   0, 1, false),
			new SpecialEvent(SpecialEventType.JarekGetsOut,            0, 0, true),
			new SpecialEvent(SpecialEventType.Lottery,             -1000, 0, true),
			new SpecialEvent(SpecialEventType.Moon,               500000, 4, false),
			new SpecialEvent(SpecialEventType.MoonRetirement,          0, 0, false),
			new SpecialEvent(SpecialEventType.Reactor,                 0, 0, false),
			new SpecialEvent(SpecialEventType.ReactorDelivered,        0, 0, true),
			new SpecialEvent(SpecialEventType.ReactorLaser,            0, 0, false),
			new SpecialEvent(SpecialEventType.Scarab,                  0, 1, true),
			new SpecialEvent(SpecialEventType.ScarabDestroyed,         0, 0, true),
			new SpecialEvent(SpecialEventType.ScarabUpgradeHull,       0, 0, false),
			new SpecialEvent(SpecialEventType.Skill,                3000, 3, false),
			new SpecialEvent(SpecialEventType.SpaceMonster,            0, 1, true),
			new SpecialEvent(SpecialEventType.SpaceMonsterKilled, -15000, 0, true),
			new SpecialEvent(SpecialEventType.Tribble,              1000, 1, false),
			new SpecialEvent(SpecialEventType.TribbleBuyer,            0, 3, false),
			new SpecialEvent(SpecialEventType.Wild,                    0, 1, false),
			new	SpecialEvent(SpecialEventType.WildGetsOut,             0, 0, true),
			new SpecialEvent(SpecialEventType.Sculpture,           -2000, 0, false),
			new SpecialEvent(SpecialEventType.SculptureDelivered,      0, 0, true),
			new SpecialEvent(SpecialEventType.SculptureHiddenBays,     0, 0, false),
			new SpecialEvent(SpecialEventType.Princess,                0, 0, true),
			new SpecialEvent(SpecialEventType.PrincessCentauri,        0, 0, true),
			new SpecialEvent(SpecialEventType.PrincessInthara,         0, 0, true),
			new SpecialEvent(SpecialEventType.PrincessQonos,           0, 0, false),
			new SpecialEvent(SpecialEventType.PrincessQuantum,         0, 0, false),
			new SpecialEvent(SpecialEventType.PrincessReturned,        0, 0, true)
		};
		#endregion

		#region TradeItems
		public static TradeItem[]	TradeItems	= new TradeItem[]
		{
			new TradeItem(TradeItemType.Water,     TechLevel.PreAgricultural, TechLevel.PreAgricultural, TechLevel.Medieval,          30,    3,   4, SystemPressure.Drought,     SpecialResource.SweetOceans,    SpecialResource.Desert,        30,   50,   1),
			new TradeItem(TradeItemType.Furs, 	   TechLevel.PreAgricultural, TechLevel.PreAgricultural, TechLevel.PreAgricultural,  250,   10,  10, SystemPressure.Cold,        SpecialResource.RichFauna,      SpecialResource.Lifeless,     230,  280,   5),
			new TradeItem(TradeItemType.Food, 	   TechLevel.Agricultural,    TechLevel.PreAgricultural, TechLevel.Agricultural,     100,    5,   5, SystemPressure.CropFailure, SpecialResource.RichSoil,       SpecialResource.PoorSoil,      90,  160,   5),
			new TradeItem(TradeItemType.Ore,       TechLevel.Medieval,        TechLevel.Medieval,        TechLevel.Renaissance,      350,   20,  10, SystemPressure.War,         SpecialResource.MineralRich,    SpecialResource.MineralPoor,  350,  420,  10),
			new TradeItem(TradeItemType.Games,     TechLevel.Renaissance,     TechLevel.Agricultural,    TechLevel.PostIndustrial,   250,  -10,   5, SystemPressure.Boredom,     SpecialResource.Artistic,       SpecialResource.NA,           160,  270,   5),
			new TradeItem(TradeItemType.Firearms,  TechLevel.Renaissance,     TechLevel.Agricultural,    TechLevel.Industrial,      1250,  -75, 100, SystemPressure.War,         SpecialResource.Warlike,        SpecialResource.NA,           600, 1100,  25),
			new TradeItem(TradeItemType.Medicine,  TechLevel.EarlyIndustrial, TechLevel.Agricultural,    TechLevel.PostIndustrial,   650,  -20,  10, SystemPressure.Plague,      SpecialResource.SpecialHerbs,   SpecialResource.NA,           400,  700,  25),
			new TradeItem(TradeItemType.Machines,  TechLevel.EarlyIndustrial, TechLevel.Renaissance,     TechLevel.Industrial,       900,  -30,   5, SystemPressure.Employment,  SpecialResource.NA,             SpecialResource.NA,           600,  800,  25),
			new TradeItem(TradeItemType.Narcotics, TechLevel.Industrial,      TechLevel.PreAgricultural, TechLevel.Industrial,      3500, -125, 150, SystemPressure.Boredom,     SpecialResource.WeirdMushrooms, SpecialResource.NA,          2000, 3000,  50),
			new TradeItem(TradeItemType.Robots,    TechLevel.PostIndustrial,  TechLevel.EarlyIndustrial, TechLevel.HiTech,          5000, -150, 100, SystemPressure.Employment,  SpecialResource.NA,             SpecialResource.NA,          3500, 5000, 100)
		};
		#endregion

		#region EquipmentForSale (This comes at the end because it depends on other Constant Arrays)
		public static Equipment[]	EquipmentForSale	= new Equipment[]
		{
			Weapons[(int)WeaponType.PulseLaser],
			Weapons[(int)WeaponType.BeamLaser],
			Weapons[(int)WeaponType.MilitaryLaser],
			Weapons[(int)WeaponType.PhotonDisruptor],
			Shields[(int)ShieldType.Energy],
			Shields[(int)ShieldType.Reflective],
			Gadgets[(int)GadgetType.ExtraCargoBays],
			Gadgets[(int)GadgetType.AutoRepairSystem],
			Gadgets[(int)GadgetType.NavigatingSystem],
			Gadgets[(int)GadgetType.TargetingSystem],
			Gadgets[(int)GadgetType.CloakingDevice]
		};
		#endregion

		#endregion
	}
}
