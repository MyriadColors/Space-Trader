// External Definitions 
// This file is included into all sources
// Defines Global Variables for external reference 
//
// Global Variables defined in Global.c
// Any new Global Variable should be referenced here and can then
// be used in any source file
#define PILOT_PRECOMPILED_HEADERS_OFF 1

#include <PalmCompatibility.h>
#include <PalmOS.h>
#include <SysEvtMgr.h>
#include <Graffiti.h>
#include <font.h>
#include <datetime.h>
#include <StringMgr.h>
#include "MerchantRsc.h"
#include "MerchantGraphics.h"
#include "spacetrader.h"   // Includes data definitions and Prototypes

// Global Variables
extern long Credits;
extern long Debt; 
extern long PoliceRecordScore;
extern long ReputationScore;
extern long PoliceKills; 
extern long TraderKills; 
extern long PirateKills; 
extern long SellPrice[];
extern long BuyPrice[];
extern long BuyingPrice[];
extern long ShipPrice[];
extern long MonsterHull;
extern unsigned long GalacticChartUpdateTicks;

extern int CheatCounter;
extern int Days; 
extern int CurForm;
extern int EncounterType;
extern int WarpSystem;
extern int NoClaim;
extern int SelectedShipType;
extern int LeaveEmpty; 
extern int GalacticChartSystem;
extern int NewsSpecialEventCount;
extern int TrackedSystem;
extern int ChanceOfVeryRareEncounter;
extern int ChanceOfTradeInOrbit;
extern int Shortcut1;
extern int Shortcut2;
extern int Shortcut3;
extern int Shortcut4;
extern int ShortcutTarget[];
 
extern char MonsterStatus;
extern char DragonflyStatus;
extern char JaporiDiseaseStatus;
extern char JarekStatus;
extern char WildStatus;
extern char InvasionStatus;
extern char ExperimentStatus;
extern char FabricRipProbability;
extern char VeryRareEncounter;
extern char Difficulty;
extern char ReactorStatus;
extern char ScarabStatus;
extern char SBuf[];
extern char SBuf2[];
extern char NameCommander[];
extern char Wormhole[];
extern char* Shortcuts[];
extern char* SolarSystemName[];
extern char* SystemSize[];
extern char* TechLevel[];
extern char* Activity[];
extern char* DifficultyLevel[];
extern char* SpecialResources[];
extern char* Status[];
extern char* MercenaryName[];

extern Boolean MoonBought;
extern Boolean Clicks;
extern Boolean Raided;
extern Boolean Inspected;
extern Boolean AlwaysIgnoreTraders;
extern Boolean AlwaysIgnorePolice; 
extern Boolean AlwaysIgnorePirates; 
extern Boolean AlwaysIgnoreTradeInOrbit; 
extern Boolean TribbleMessage;
extern Boolean AutoFuel; 
extern Boolean AutoRepair; 
extern Boolean Insurance; 
extern Boolean EscapePod;
extern Boolean PriceDifferences;
extern Boolean ArtifactOnBoard;
extern Boolean APLscreen;
extern Boolean ReserveMoney; 
extern Boolean AlwaysInfo;
extern Boolean TextualEncounters;
extern Boolean AutoAttack;
extern Boolean AutoFlee;
extern Boolean Continuous;
extern Boolean AttackIconStatus;
extern Boolean AttackFleeing;
extern Boolean PossibleToGoThroughRip;
extern Boolean UseHWButtons;
extern Boolean NewsAutoPay;
extern Boolean ShowTrackedRange;
extern Boolean JustLootedMarie;
extern Boolean ArrivedViaWormhole;
extern Boolean AlreadyPaidForNewspaper;
extern Boolean TrackAutoOff;
extern Boolean RemindLoans;
extern Boolean CanSuperWarp;
extern Boolean GameLoaded;
extern Boolean LitterWarning;
extern Boolean SharePreferences;
extern Boolean IdentifyStartup;
extern Boolean RectangularButtonsOn;

extern SHIP Ship;
extern SHIP Opponent;
extern SHIP Dragonfly;
extern SHIP SpaceMonster;
extern SHIP Scarab;

extern SOLARSYSTEM SolarSystem[];
extern SHIPTYPE Shiptype[];
extern SHIELD Shieldtype[];
extern WEAPON Weapontype[];
extern GADGET Gadgettype[];
extern CREWMEMBER Mercenary[];
extern POLITICS Politics[];
extern POLICERECORD PoliceRecord[];
extern TRADEITEM Tradeitem[];
extern SPECIALEVENT SpecialEvent[];
extern HIGHSCORE Hscores[];
extern REPUTATION Reputation[];

extern Handle SystemBmp;
extern Handle CurrentSystemBmp;
extern Handle ShortRangeSystemBmp;
extern Handle WormholeBmp;
extern Handle SmallWormholeBmp;
extern Handle VisitedSystemBmp;
extern Handle CurrentVisitedSystemBmp;
extern Handle VisitedShortRangeSystemBmp;
extern Handle ShipBmp[];
extern Handle DamagedShipBmp[];
extern Handle ShieldedShipBmp[];
extern Handle DamagedShieldedShipBmp[];
extern Handle IconBmp[];
  
extern BitmapPtr ShipBmpPtr[];
extern BitmapPtr SystemBmpPtr;
extern BitmapPtr CurrentSystemBmpPtr;
extern BitmapPtr ShortRangeSystemBmpPtr;
extern BitmapPtr WormholeBmpPtr;
extern BitmapPtr SmallWormholeBmpPtr;
extern BitmapPtr VisitedSystemBmpPtr;
extern BitmapPtr CurrentVisitedSystemBmpPtr;
extern BitmapPtr VisitedShortRangeSystemBmpPtr;
extern BitmapPtr DamagedShipBmpPtr[];
extern BitmapPtr ShieldedShipBmpPtr[];
extern BitmapPtr DamagedShieldedShipBmpPtr[];
extern BitmapPtr IconBmpPtr[];
 
extern Handle NameH;
//extern DmOpenRef pmDB;

extern DWord romVersion;
