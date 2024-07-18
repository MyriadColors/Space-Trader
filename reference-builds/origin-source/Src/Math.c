/* 
 * Math.c
  */

// *************************************************************************
// Math.c
// *************************************************************************

#include "external.h"

// *************************************************************************
// Temporary implementation of square root
// *************************************************************************
int sqrt( int a )
{
	int i;
	
	i = 0;
	while (SQR( i ) < a)
		++i;
	if (i > 0)
		if ((SQR( i ) - a) > (a - SQR( i-1 )))
			--i;
	return( i );
}

// *************************************************************************
// Square of the distance between two solar systems
// *************************************************************************
long SqrDistance( SOLARSYSTEM a, SOLARSYSTEM b )
{
	return (SQR( a.X - b.X ) + SQR( a.Y - b.Y ));
}


// *************************************************************************
// Distance between two solar systems
// *************************************************************************
long RealDistance( SOLARSYSTEM a, SOLARSYSTEM b )
{
	return (sqrt( SqrDistance( a, b ) ));
}


// *************************************************************************
// Pieter's new random functions, tweaked a bit by SjG
// *************************************************************************

#define DEFSEEDX 521288629
#define DEFSEEDY 362436069

static UInt16 SeedX = DEFSEEDX;
static UInt16 SeedY = DEFSEEDY;

int GetRandom2(int maxVal)
{
	return (int)(Rand() % maxVal);	
}

UInt16 Rand()
{
   static UInt16 a = 18000;
   static UInt16 b = 30903;

   SeedX = a*(SeedX&MAX_WORD) + (SeedX>>16);
   SeedY = b*(SeedY&MAX_WORD) + (SeedY>>16);

   return ((SeedX<<16) + (SeedY&MAX_WORD));
}

void RandSeed( UInt16 seed1, UInt16 seed2 )
{
   if (seed1)
       SeedX = seed1;   /* use default seeds if parameter is 0 */
   else
       SeedX = DEFSEEDX;

   if (seed2)
       SeedY = seed2;
   else
       SeedY = DEFSEEDY;
} 
