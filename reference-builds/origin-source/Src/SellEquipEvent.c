/* 
 * SellEquipEvent.c
  */

// *************************************************************************
// Handling of the events of the Sell Equipment form.
// *************************************************************************
#include "external.h"

Boolean SellEquipmentFormHandleEvent( EventPtr eventP )
{
    Boolean handled = false;
    Boolean Sale;
	FormPtr frmP;
	int i;

	switch (eventP->eType) 
	{
		case frmOpenEvent:
			DrawSellEquipment();
			handled = true;
			break;

		case frmUpdateEvent:
			DrawSellEquipment();
			handled = true;
			break;

		case ctlSelectEvent:
			if (FrmAlert( SellItemAlert ) != SellItemYes)
			{
				handled = true;
				break;
			}
		
			frmP = FrmGetActiveForm();

			Sale = true;

			if (eventP->data.ctlSelect.controlID >= SellEquipmentSell0Button &&
				eventP->data.ctlSelect.controlID < SellEquipmentSell0Button+MAXWEAPON)
			{
				Credits += WEAPONSELLPRICE( eventP->data.ctlSelect.controlID - SellEquipmentSell0Button );
				for (i=eventP->data.ctlSelect.controlID - SellEquipmentSell0Button + 1; i<MAXWEAPON; ++i)
					Ship.Weapon[i-1] = Ship.Weapon[i];
				Ship.Weapon[MAXWEAPON-1] = -1;
			}

			if (eventP->data.ctlSelect.controlID >= SellEquipmentSell0Button+MAXWEAPON &&
				eventP->data.ctlSelect.controlID < SellEquipmentSell0Button+MAXWEAPON+MAXSHIELD)
			{
				Credits += SHIELDSELLPRICE( eventP->data.ctlSelect.controlID - SellEquipmentSell0Button - MAXWEAPON );
				for (i=eventP->data.ctlSelect.controlID - SellEquipmentSell0Button - MAXWEAPON + 1; i<MAXSHIELD; ++i)
				{
					Ship.Shield[i-1] = Ship.Shield[i];
					Ship.ShieldStrength[i-1] = Ship.ShieldStrength[i];
				}
				Ship.Shield[MAXSHIELD-1] = -1;
				Ship.ShieldStrength[MAXSHIELD-1] = 0;
			}

			if (eventP->data.ctlSelect.controlID >= SellEquipmentSell0Button+MAXWEAPON+MAXSHIELD &&
				eventP->data.ctlSelect.controlID < SellEquipmentSell0Button+MAXWEAPON+MAXSHIELD+MAXGADGET)
			{
				if (Ship.Gadget[eventP->data.ctlSelect.controlID - SellEquipmentSell0Button - MAXWEAPON - MAXSHIELD] == EXTRABAYS)
				{
					if (FilledCargoBays() > TotalCargoBays() - 5)
					{
						FrmAlert( CargoBaysFullAlert );
						Sale = false;						
					}
				}
			
				if (Sale)
				{
					Credits += GADGETSELLPRICE( eventP->data.ctlSelect.controlID - SellEquipmentSell0Button - MAXWEAPON - MAXSHIELD );
					for (i=eventP->data.ctlSelect.controlID - SellEquipmentSell0Button - MAXWEAPON - MAXSHIELD + 1; i<MAXGADGET; ++i)
						Ship.Gadget[i-1] = Ship.Gadget[i];
					Ship.Gadget[MAXGADGET-1] = -1;
				}
			}

			if (Sale)
				DrawSellEquipment();

			handled = true;
			break;

		default:
			break;
	}
	
	return handled;
}
