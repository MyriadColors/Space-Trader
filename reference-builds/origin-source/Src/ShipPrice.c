/* 
 * Shipprice.c
  */

// *************************************************************************
// ShipPrice.c - Functions include:
// long CurrentShipPriceWithoutCargo( Boolean ForInsurance )
// long CurrentShipPrice( Boolean ForInsurance )
//
// Modifications:
// mm/dd/yy - description - author
// *************************************************************************

#include "external.h"

// *************************************************************************
// Determine value of ship
// *************************************************************************
long EnemyShipPrice( SHIP* Sh )
{
	int i;
	long CurPrice;
	
	CurPrice = Shiptype[Sh->Type].Price;
	for (i=0; i<MAXWEAPON; ++i)
		if (Sh->Weapon[i] >= 0)
			CurPrice += Weapontype[Sh->Weapon[i]].Price;
	for (i=0; i<MAXSHIELD; ++i)
		if (Sh->Shield[i] >= 0)
			CurPrice += Shieldtype[Sh->Shield[i]].Price;
	// Gadgets aren't counted in the price, because they are already taken into account in
	// the skill adjustment of the price.
			
	CurPrice = CurPrice * (2 * PilotSkill( Sh ) + EngineerSkill( Sh ) + 3 * FighterSkill( Sh ))	/ 60;
			
	return CurPrice;
}	

// *************************************************************************
// Determine value of current ship, including equipment.
// *************************************************************************
long CurrentShipPriceWithoutCargo( Boolean ForInsurance )
{
	int i;
	long CurPrice;
	
	CurPrice = 
		// Trade-in value is three-fourths the original price
		((Shiptype[Ship.Type].Price * (Ship.Tribbles > 0 && !ForInsurance? 1 : 3)) / 4)
		// subtract repair costs
		- (GetHullStrength() - Ship.Hull) * Shiptype[Ship.Type].RepairCosts 
		// subtract costs to fill tank with fuel
		- (Shiptype[Ship.Type].FuelTanks - GetFuel()) * Shiptype[Ship.Type].CostOfFuel;
	// Add 2/3 of the price of each item of equipment
	for (i=0; i<MAXWEAPON; ++i)
		if (Ship.Weapon[i] >= 0)
			CurPrice += WEAPONSELLPRICE( i );
	for (i=0; i<MAXSHIELD; ++i)
		if (Ship.Shield[i] >= 0)
			CurPrice += SHIELDSELLPRICE( i );
	for (i=0; i<MAXGADGET; ++i)
		if (Ship.Gadget[i] >= 0)
			CurPrice += GADGETSELLPRICE( i );
			
	return CurPrice;
}	


// *************************************************************************
// Determine value of current ship, including goods and equipment.
// *************************************************************************
long CurrentShipPrice( Boolean ForInsurance )
{
	int i;
	long CurPrice;
	
	CurPrice = CurrentShipPriceWithoutCargo( ForInsurance );
	for (i=0; i<MAXTRADEITEM; ++i)
		CurPrice += BuyingPrice[i];
			
	return CurPrice;
}	
