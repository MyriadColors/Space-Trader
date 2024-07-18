/* 
 * ShipEvent.c
  */

#include "external.h"

static void DrawCurrentShipForm()
{
    FormPtr frmP = FrmGetActiveForm();
	int i, j, k, Line, FirstEmptySlot;
	

	RectangularShortcuts( frmP, CurrentShipBButton );

	FrmDrawForm( frmP );

	FntSetFont( boldFont );
	DrawChars( "Type:", 0, 18 );			

	DrawChars( "Equipment:", 0, 32 );			

	FntSetFont( stdFont );
	if (ScarabStatus == 3)
	{
		StrCopy( SBuf, Shiptype[Ship.Type].Name);
		StrCat ( SBuf, "/hardened hull");
		DrawChars( SBuf, 60, 18 );			
	}
	else
		DrawChars( Shiptype[Ship.Type].Name, 60, 18 );			

	Line = 32;

	for (i=0; i<MAXWEAPONTYPE+EXTRAWEAPONS; ++i)
	{
		j = 0;
		for (k=0; k<MAXWEAPON; ++k)
		{
			if (Ship.Weapon[k] == i)
				++j;
		}
		if (j > 0)
		{
			SBuf[0] = '\0';
			SBufMultiples( j, Weapontype[i].Name );
			StrToLower( SBuf2, SBuf );
			DrawChars( SBuf2, 60, Line );
			Line += 14;
		}
	}

	for (i=0; i<MAXSHIELDTYPE+EXTRASHIELDS; ++i)
	{
		j = 0;
		for (k=0; k<MAXSHIELD; ++k)
		{
			if (Ship.Shield[k] == i)
				++j;
		}
		if (j > 0)
		{
			SBuf[0] = '\0';
			SBufMultiples( j, Shieldtype[i].Name );
			StrToLower( SBuf2, SBuf );
			DrawChars( SBuf2, 60, Line );		
			Line += 14;
		}
	}
	for (i=0; i<MAXGADGETTYPE+EXTRAGADGETS; ++i)
	{
		j = 0;
		for (k=0; k<MAXGADGET; ++k)
		{
			if (Ship.Gadget[k] == i)
				++j;
		}
		if (j > 0)
		{
			if (i == EXTRABAYS)
			{
				j = j*5;
				StrIToA( SBuf, j );
				StrCat( SBuf, " extra cargo bays" );
			}
			else
			{
				StrCopy(SBuf, Gadgettype[i].Name );
			}
			StrToLower( SBuf2, SBuf );
			DrawChars( SBuf2, 60, Line );
			Line += 14;			
		}
	}

	if (EscapePod)
	{
		DrawChars( "an escape pod", 60, Line );			
		Line += 14;
	}

	if (AnyEmptySlots(&Ship))
	{			
		FntSetFont( boldFont );
		DrawChars( "Unfilled:        ", 0, Line );			

		FntSetFont( stdFont );

		FirstEmptySlot = GetFirstEmptySlot( Shiptype[Ship.Type].WeaponSlots, Ship.Weapon );
		if (FirstEmptySlot >= 0)
		{
			SBuf[0] = '\0';
			SBufMultiples( Shiptype[Ship.Type].WeaponSlots - FirstEmptySlot, "weapon slot" );
			DrawChars( SBuf, 60, Line );			
			Line += 14;
		}
		
		FirstEmptySlot = GetFirstEmptySlot( Shiptype[Ship.Type].ShieldSlots, Ship.Shield );
		if (FirstEmptySlot >= 0)
		{
			SBuf[0] = '\0';
			SBufMultiples( Shiptype[Ship.Type].ShieldSlots - FirstEmptySlot, "shield slot" );
			DrawChars( SBuf, 60, Line );			
			Line += 14;
		}
		
		FirstEmptySlot = GetFirstEmptySlot( Shiptype[Ship.Type].GadgetSlots, Ship.Gadget );
		if (FirstEmptySlot >= 0)
		{
			SBuf[0] = '\0';
			SBufMultiples( Shiptype[Ship.Type].GadgetSlots - FirstEmptySlot, "gadget slot" );
			DrawChars( SBuf, 60, Line );			
			Line += 14;
		}
	}

}


// *************************************************************************
// Event handler for the Current Ship screen
// ********************************************************************
Boolean CurrentShipFormHandleEvent( EventPtr eventP )
{
    Boolean handled = false;

	switch (eventP->eType) 
	{

		case frmOpenEvent:
		case frmUpdateEvent:
			DrawCurrentShipForm();
			handled = true;
			break;

		case ctlSelectEvent:
			if (eventP->data.ctlSelect.controlID == CurrentShipStatusButton)
			{
				CurForm = CommanderStatusForm;
			}
			else if (eventP->data.ctlSelect.controlID == CurrentShipQuestsButton)
			{
				CurForm = QuestsForm;
			}
			else if (eventP->data.ctlSelect.controlID == CurrentShipSpecialButton)
			{
				CurForm = SpecialCargoForm;
			}
			
			FrmGotoForm( CurForm );
			handled = true;
			break;
			
		default:
			break;
	}
	
	return handled;
}