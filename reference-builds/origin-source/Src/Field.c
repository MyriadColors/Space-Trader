/*
 * Field.c
 */

// Field.c - Functions Include:
// Handle SetField( FormPtr frm, int Nr, char* Value, int Size, Boolean Focus )
// void GetField( FormPtr frm, int Nr, char* Value, Handle AmountH )
// void SetCheckBox( FormPtr frm, int Nr, Boolean Value )
// Boolean GetCheckBox( FormPtr frm, int Nr )


#include "external.h"

// *************************************************************************
// Set Field
// *************************************************************************
Handle SetField( FormPtr frm, int Nr, char* Value, int Size, Boolean Focus )
{
	Word objIndex;
	CharPtr AmountP;
	Handle AmountH;
	
	objIndex = FrmGetObjectIndex( frm, Nr );
	AmountH = MemHandleNew( Size );
	AmountP = MemHandleLock( AmountH );
	StrCopy( AmountP, Value );
	MemPtrUnlock( AmountP );
	FldSetTextHandle( FrmGetObjectPtr( frm, objIndex ), AmountH );
	if (Focus)
		FrmSetFocus( frm, objIndex );
	
	return AmountH;
}


// *************************************************************************
// Get Field
// *************************************************************************
void GetField( FormPtr frm, int Nr, char* Value, Handle AmountH )
{
	Word objIndex;
	CharPtr AmountP;

	objIndex = FrmGetObjectIndex( frm, Nr );
	FldSetTextHandle( FrmGetObjectPtr( frm, objIndex ), 0 );
	AmountP = MemHandleLock( AmountH );
	StrCopy( Value, AmountP );
	MemPtrUnlock( AmountP );
	MemHandleFree( AmountH );
}

// *************************************************************************
// Set Trigger List value
// *************************************************************************
void SetTriggerList( FormPtr frm, int Nr, int Index )
{
	Word objIndex;
	ControlPtr cp;
	
	objIndex = FrmGetObjectIndex( frm, Nr );
	cp = (ControlPtr)FrmGetObjectPtr( frm, objIndex );
	LstSetSelection( cp, Index );
}

// *************************************************************************
// Set Control Label
// *************************************************************************
void SetControlLabel( FormPtr frm, int Nr, Char * Label )
{
	Word objIndex;
	ControlPtr cp;
	
	objIndex = FrmGetObjectIndex( frm, Nr );
	cp = (ControlPtr)FrmGetObjectPtr( frm, objIndex );
	CtlSetLabel( cp, Label );
}

// *************************************************************************
// Get Trigger List value
// *************************************************************************
int GetTriggerList( FormPtr frm, int Nr)
{
	Word objIndex;
	ControlPtr cp;
	
	objIndex = FrmGetObjectIndex( frm, Nr );
	cp = (ControlPtr)FrmGetObjectPtr( frm, objIndex );
	return LstGetSelection( cp );
}


// *************************************************************************
// Set Checkbox value
// *************************************************************************
void SetCheckBox( FormPtr frm, int Nr, Boolean Value )
{
	Word objIndex;
	ControlPtr cp;
	
	objIndex = FrmGetObjectIndex( frm, Nr );
	cp = (ControlPtr)FrmGetObjectPtr( frm, objIndex );
	CtlSetValue( cp, (Value ? 1 : 0) );
}


// *************************************************************************
// Get Checkbox value
// *************************************************************************
Boolean GetCheckBox( FormPtr frm, int Nr )
{
	Word objIndex;
	ControlPtr cp;

	objIndex = FrmGetObjectIndex( frm, Nr );
	cp = (ControlPtr)FrmGetObjectPtr( frm, objIndex );
	if (CtlGetValue( cp ) == 0)
		return false;
	else
		return true;
}
