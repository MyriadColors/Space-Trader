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

	
		

		
		#endregion

		#region Constant Arrays

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
