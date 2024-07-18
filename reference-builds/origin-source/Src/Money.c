/* 
 * Money.c
  */

#include "external.h"
// *************************************************************************
// Functions Include:
//
// long CurrentWorth( void )
// void PayInterest( void )
//

// *************************************************************************
// Current worth of commander
// *************************************************************************
long CurrentWorth( void )
{
	return (CurrentShipPrice( false ) + Credits - Debt + (MoonBought ? COSTMOON : 0));
}


// *************************************************************************
// Pay interest on debt
// *************************************************************************
void PayInterest( void )
{
	long IncDebt;

	if (Debt > 0)
	{
		IncDebt = max( 1, Debt / 10 );
		if (Credits > IncDebt)
			Credits -= IncDebt;
		else 
		{
			Debt += (IncDebt - Credits);
			Credits = 0;
		}
	}
}

