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

namespace Fryz.Apps.SpaceTrader
{
	public class CrewMember : STSerializableObject
	{

		#region Methods


		// *************************************************************************
		// NthLowest Skill. Returns skill with the nth lowest score
		// (i.e., 2 is the second worst skill). If there is a tie, it will return
		// in the order of Pilot, Fighter, Trader, Engineer.
		// JAF - rewrote this to be more efficient.
		// *************************************************************************
		public int NthLowestSkill(int n)
		{
			int[]	skillIds	= new int[] { 0, 1, 2, 3 };

			for (int j = 0; j < 3; j++)
			{
				for (int i = 0; i < 3 - j; i++)
				{
					if (Skills[skillIds[i]] > Skills[skillIds[i + 1]])
					{
						int	temp				= skillIds[i];
						skillIds[i]			= skillIds[i + 1];
						skillIds[i + 1]	= temp;
					}
				}
			}

			return skillIds[n - 1];
		}

		// *************************************************************************
		// Randomly tweak the skills.
		// *************************************************************************
		public void TonicTweakRandomSkill()
		{
			int[]	oldSkills	= (int[])Skills.Clone();

			if (Game.CurrentGame.Difficulty < Difficulty.Hard)
			{
				// add one to a random skill, subtract one from a random skill
				while (Skills[0] == oldSkills[0] && Skills[1] == oldSkills[1] &&
					Skills[2] == oldSkills[2] && Skills[3] == oldSkills[3])
				{
					ChangeRandomSkill(1);
					ChangeRandomSkill(-1);
				}
			}
			else
			{
				// add one to two random skills, subtract three from one random skill
				ChangeRandomSkill(1);
				ChangeRandomSkill(1);
				ChangeRandomSkill(-3);
			}
		}



		#endregion

	}
}
