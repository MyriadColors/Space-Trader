/* 
 * ShiptypeInfoEvent.c
  */

// *************************************************************************
// Handling of the events of the Shiptype Information form.
// *************************************************************************

#include "external.h"

static void DrawShiptypeInfoForm()
{
    FormPtr frmP;
	frmP = FrmGetActiveForm();
	setLabelText( frmP, ShiptypeInfoShipNameLabel, 
		Shiptype[SelectedShipType].Name );
	setLabelText( frmP, ShiptypeInfoSizeLabel, 
		SystemSize[Shiptype[SelectedShipType].Size] );
	setLabelText( frmP, ShiptypeInfoCargoBaysLabel, 
		StrIToA( SBuf, Shiptype[SelectedShipType].CargoBays ) );
	setLabelText( frmP, ShiptypeInfoWeaponSlotsLabel, 
		StrIToA( SBuf, Shiptype[SelectedShipType].WeaponSlots ) );
	setLabelText( frmP, ShiptypeInfoShieldSlotsLabel, 
		StrIToA( SBuf, Shiptype[SelectedShipType].ShieldSlots ) );
	setLabelText( frmP, ShiptypeInfoGadgetSlotsLabel, 
		StrIToA( SBuf, Shiptype[SelectedShipType].GadgetSlots ) );
	setLabelText( frmP, ShiptypeInfoCrewQuartersLabel, 
		StrIToA( SBuf, Shiptype[SelectedShipType].CrewQuarters ) );
	StrIToA( SBuf, Shiptype[SelectedShipType].FuelTanks );
	StrCat( SBuf, " parsecs" );
	setLabelText( frmP, ShiptypeInfoMaximumRangeLabel, SBuf ); 
	setLabelText( frmP, ShiptypeInfoHullStrengthLabel, 
		StrIToA( SBuf, Shiptype[SelectedShipType].HullStrength ) );
	FrmDrawForm( frmP );
	
	WinDrawBitmap( ShipBmpPtr[SelectedShipType], 
		94+((60-GetBitmapWidth( ShipBmpPtr[SelectedShipType] ))>>1),
		83+((48-GetBitmapHeight( ShipBmpPtr[SelectedShipType] ))>>1) );
}

Boolean ShiptypeInfoFormHandleEvent( EventPtr eventP )
{
    Boolean handled = false;

	switch (eventP->eType) 
	{
		case frmOpenEvent:
		case frmUpdateEvent:
			DrawShiptypeInfoForm();
			handled = true;
			break;
			
		case ctlSelectEvent:
			CurForm = BuyShipForm;
			FrmGotoForm( CurForm );
			handled = true;
			break;
			
		default:
			break;
	}
	
	return handled;
}
