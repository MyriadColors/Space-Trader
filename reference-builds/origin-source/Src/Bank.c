/* 
 * Bank.c
  */

#include "external.h"

// *************************************************************************
// Maximum loan
// *************************************************************************
static long MaxLoan( void )
{
	return (PoliceRecordScore >= CLEANSCORE ? 
		min( 25000L, max( 1000L, ((CurrentWorth() / 10L) / 500L) * 500L ) ) : 500L);
}


// *************************************************************************
// Lending money
// *************************************************************************
static void GetLoan( long Loan )
{
	long Amount;
	
	Amount = min( MaxLoan() - Debt, Loan );
	Credits += Amount;
	Debt += Amount;
}


// *************************************************************************
// Paying back
// *************************************************************************
static void PayBack( long Cash )
{
	long Amount;
	
	Amount = min( Debt, Cash );
	Amount = min( Amount, Credits );
	Credits -= Amount;
	Debt -= Amount;
}

// *************************************************************************
// Show the Bank screen
// *************************************************************************
static void ShowBank( void )
   {
	FormPtr frmP;
	
	frmP = FrmGetActiveForm();

	RectangularShortcuts( frmP, BankBButton );
	
	if (Debt <= 0)
		FrmHideObject( frmP, FrmGetObjectIndex( frmP, BankPayBackButton ) );
	else
		FrmShowObject( frmP, FrmGetObjectIndex( frmP, BankPayBackButton ) );

	if (Insurance)
	{
		FrmHideObject( frmP, FrmGetObjectIndex( frmP, BankBuyInsuranceButton ) );
		FrmShowObject( frmP, FrmGetObjectIndex( frmP, BankStopInsuranceButton ) );
	}
	else
	{
		FrmShowObject( frmP, FrmGetObjectIndex( frmP, BankBuyInsuranceButton ) );
		FrmHideObject( frmP, FrmGetObjectIndex( frmP, BankStopInsuranceButton ) );
	}

	FrmDrawForm( frmP );

	EraseRectangle( 80, 32, 80, 26 );

	StrIToA( SBuf, Debt );
	StrCat( SBuf, " cr." );
	DrawChars( SBuf, 80, 32 );			
	
	StrIToA( SBuf, MaxLoan() );
	StrCat( SBuf, " cr." );
	DrawChars( SBuf, 80, 46 );			

	EraseRectangle( 80, 100, 80, 40 );

	StrIToA( SBuf, CurrentShipPriceWithoutCargo( true ) );
	StrCat( SBuf, " cr. " );
	DrawChars( SBuf, 80, 100 );			

	StrIToA( SBuf, min( NoClaim, 90 ) );
	StrCat( SBuf, "%" );
	if (NoClaim == 90)
		StrCat( SBuf, " (maximum)" );
	DrawChars( SBuf, 80, 114 );			
	
	StrIToA( SBuf, InsuranceMoney() );
	StrCat( SBuf, " cr. daily" );
	DrawChars( SBuf, 80, 128 );			
	
	DisplayTradeCredits();
   }

// *************************************************************************
// Handling of events on the Bank screen
// *************************************************************************
Boolean BankFormHandleEvent(EventPtr eventP)
{
    Boolean handled = false;
    FormPtr frmP;
	int d;
	long Amount;
	Handle AmountH;

	switch (eventP->eType) 
	{
		case frmOpenEvent:
		case frmUpdateEvent:
			ShowBank();
			handled = true;
			break;

		case ctlSelectEvent:
			if (eventP->data.ctlSelect.controlID == BankGetLoanButton)
			{
				if (Debt >= MaxLoan())
				{
					FrmAlert( DebtTooHighAlert );
					handled = true;
					break;
				}
			
				frmP = FrmInitForm( GetLoanForm );
	
				AmountH = (Handle) SetField( frmP, GetLoanGetLoanField, "", 6, true );

				StrCopy( SBuf, "You can borrow up to " );
				StrIToA( SBuf2, (MaxLoan() - Debt) );
				StrCat( SBuf, SBuf2 );
				StrCat( SBuf, " credits." );
				setLabelText( frmP, GetLoanMaxLoanLabel, SBuf );
	
				d = FrmDoDialog( frmP );

				GetField( frmP, GetLoanGetLoanField, SBuf, AmountH );
				if (SBuf[0] == '\0')
					Amount = 0;
				else
					Amount = StrAToI( SBuf );

				FrmDeleteForm( frmP );

				if (d == GetLoanEverythingButton)
					GetLoan( MaxLoan() );
				else if (d != GetLoanNothingButton)
					GetLoan( Amount );
			}
			else if (eventP->data.ctlSelect.controlID == BankPayBackButton)
			{
				if (Debt <= 0)
				{
					FrmAlert( NoDebtAlert );
					handled = true;
					break;
				}
			
				frmP = FrmInitForm( PayBackForm );
	
				AmountH = (Handle) SetField( frmP, PayBackPayBackField, "", 6, true );
	
				StrCopy( SBuf, "You have a debt of " );
				StrIToA( SBuf2, Debt );
				StrCat( SBuf, SBuf2 );
				StrCat( SBuf, " credits." );
				setLabelText( frmP, PayBackMaxDebtLabel, SBuf );
	
				d = FrmDoDialog( frmP );

				GetField( frmP, PayBackPayBackField, SBuf, AmountH );
				if (SBuf[0] == '\0')
					Amount = 0;
				else
					Amount = StrAToI( SBuf );

				FrmDeleteForm( frmP );

				if (d == PayBackEverythingButton)
					PayBack( 99999 );
				else if (d != PayBackNothingButton)
					PayBack( Amount );
			}
			else if (eventP->data.ctlSelect.controlID == BankBuyInsuranceButton)
			{
				if (!EscapePod)
				{
					FrmAlert( NoEscapePodAlert );
					handled = true;
					break;
				}
				
				Insurance = true;
			}			
			else if (eventP->data.ctlSelect.controlID == BankStopInsuranceButton)
			{
				if (FrmAlert( StopInsuranceAlert ) == StopInsuranceNo)
				{
					handled = true;
					break;
				}
				
				Insurance = false;
				NoClaim = 0;
			}			
			ShowBank();
			handled = true;
			break;
				
		default:
			break;
	}
	
	return handled;
}

