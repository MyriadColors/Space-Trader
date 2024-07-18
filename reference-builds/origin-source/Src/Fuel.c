/* 
 * Fuel.c
  */

// *************************************************************************
// Fuel.c - Functions include:
// char GetFuelTanks( void )
// char GetFuel( void )
// void BuyFuel( int Amount )
//
// Modifications:
// mm/dd/yy - description - author
// *************************************************************************

#include "external.h"

// *************************************************************************
// Determine size of fueltanks
// *************************************************************************
char GetFuelTanks( void )
{
	return (HasGadget( &Ship, FUELCOMPACTOR ) ? 18 : Shiptype[Ship.Type].FuelTanks);
}


// *************************************************************************
// Determine fuel in tank
// *************************************************************************
char GetFuel( void )
{
	return min( Ship.Fuel, GetFuelTanks() );
}


// *************************************************************************
// Buy Fuel for Amount credits
// *************************************************************************
void BuyFuel( int Amount )
{
	int MaxFuel;
	int Parsecs;
	
	MaxFuel = (GetFuelTanks() - GetFuel()) * Shiptype[Ship.Type].CostOfFuel;
	if (Amount > MaxFuel)
		Amount = MaxFuel;
	if (Amount > Credits)
		Amount = Credits;
		
	Parsecs = Amount / Shiptype[Ship.Type].CostOfFuel;
	
	Ship.Fuel += Parsecs;
	Credits -= Parsecs * Shiptype[Ship.Type].CostOfFuel;
}
