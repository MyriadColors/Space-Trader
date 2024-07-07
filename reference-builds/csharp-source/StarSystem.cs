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
	public class StarSystem : STSerializableObject
	{


		public void InitializeTradeItems()
		{
			for (int i = 0; i < Consts.TradeItems.Length; i++)
			{
				if (!ItemTraded(Consts.TradeItems[i]))
				{
					_tradeItems[i]	= 0;
				}
				else
				{
					_tradeItems[i]	= ((int)this.Size + 1) * (Functions.GetRandom(9, 14) -
						Math.Abs(Consts.TradeItems[i].TechTopProduction - this.TechLevel));

					// Because of the enormous profits possible, there shouldn't be too many robots or narcotics available.
					if (i >= (int)TradeItemType.Narcotics)
						_tradeItems[i]	= ((_tradeItems[i] * (5 - (int)Game.CurrentGame.Difficulty)) / (6 - (int)Game.CurrentGame.Difficulty)) + 1;

					if (this.SpecialResource == Consts.TradeItems[i].ResourceLowPrice)
						_tradeItems[i]	= _tradeItems[i] * 4 / 3;

					if (this.SpecialResource == Consts.TradeItems[i].ResourceHighPrice)
						_tradeItems[i]	= _tradeItems[i] * 3 / 4;

					if (this.SystemPressure == Consts.TradeItems[i].PressurePriceHike)
						_tradeItems[i]	= _tradeItems[i] / 5;

					_tradeItems[i]	= _tradeItems[i] - Functions.GetRandom(10) + Functions.GetRandom(10);

					if (_tradeItems[i] < 0)
						_tradeItems[i] = 0;
				}
			}
		}

	
		public Shipyard Shipyard
		{
			get
			{
				return (_shipyardId == ShipyardId.NA ? null : Consts.Shipyards[(int)_shipyardId]);
			}
		}

		public ShipyardId ShipyardId
		{
			get
			{
				return _shipyardId;
			}
			set
			{
				_shipyardId	= value;
			}
		}


		#endregion
	}
}
