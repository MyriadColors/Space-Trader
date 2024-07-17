# Changelog for Divergent Updates from PalmOS 1.2x

My code is based as closely as possible to the original PalmOS 1.2x codebase. There have been a few maintainers and contributors that have created expanded versions which I do not intend to carry forward (at least to begin). This changelog documents those 'reverted' changes for archival purposes.

## Space Trader for Java 8

### Authored By Stavila Leonid aka Leonis

[The history of commits](https://github.com/LeonisX/space-trader/commits/master)

16.02.2019 v.3.51.225

All Very Rare Encounters in Quest System:

* Captain Ahab (with possibility to disable)
* Captain Conrad
* Captain Huie
* Dated Tonic
* Good Tonic
* Marie Celeste

Changelog:

* GigaGaia cheat
* Rareware cheat
* Get rid of several static methods in Game class
* Reorganize docs
* Refactor ENCOUNTER_SHOW_ACTION_BUTTONS

Bug fixes:

* Fix bug with mercenaries list
* Fix "free" ships in Shipyard
* Fix Events cheat
* Repair encounter
* Repair cheats

20.01.2019 v.3.43.178

New quests in Quest System:

* Space Monster
* Scarab Stolen
* Skill Increase
* Moon For Sale
* Japori Disease
* Alien Invasion
* Dangerous Experiment
* Erase Record
* Dragonfly
* Alien Artifact (with improvement)
* Cargo For Sale

Changelog:

* Remove unneeded SpecialEventType enum
* Allow to create few independent quests with same type
* Delete unneeded files

Bug fixes:

* Fix warp to Ray system
* Fix error when try to see high scores w/o started game

31.12.2018 v.3.32.138

The main innovation of the third version is the Quest Engine. 
Now the logic of each quest is collected in a separate class. 
This greatly simplifies the process of creating new quests, as well as testing.
At the moment, the following quests have been processed:

* Lottery Winner
* Ambassador Jarek
* Kidnapped Princess
* Jonathan Wild
* Stolen Sculpture
* Morgan's Reactor
* Troubles with Tribbles

Changelog:

* Debug controls in FormViewCommander
* FormMonster: show quest/shipyard features; order by feature
* Cheats subMenu (FormMonster)
* Shipyard form in Cheats menu
* Dialogs and Alerts tests in Cheats menu
* Docs (Russian and English): spaceships and travelling through Space, skills, mercenaries, encounters in Space, trade goods, equipment
* Logging (via Java Util Logging)
* Encounters in separate class (not in Game)

Bug Fixes:

* Fix all/max buttons on Cargo Panel
* Fix shield initial charge bug
* Fix special ships graphic bugs
* Fix stealable cargo
* Show all quests in MonsterCom
* Avoid negative values for ship slots
* After deal in Shipyard - alert in center of Shipyard form
* Fix bug in hasCrew method

13.11.2018. v.2.17.21

* Full translation for File Dialogs
* FormMonsters and FormViewQuests now fully workable.
* Docs: game overview and specifications

* Remove unused classes: AnchorStyles, ComboBoxStyle, FlatStyle, Link*.

12.11.2018. v.2.13.15

* Save/load game and options using serialization
* Set locale with language (need for correct number formatting)
* Move all IO functions to IOUtils

11.11.2018. v.2.11.13

* Keep main window position and language in registry
* Distance + "parsec" in TargetSystemPanel
* Update Russian script

Bug fixes:

* Fix game loading from scratch
* Correct determination of the number of lines in Label
* Fix version comparisons

Refactor:

* Simplify classes: MyComboBoxModel, MyListModel, ResourceManager, OpenFileDialog, SaveFileDialog
* Remove unneeded methods: beginInit(), endInit(), suspendLayout() 
* Remove unneeded methods: setSize(Dimension size) 
* Remove unneeded methods: setLocation(Point location)
* Remove unneeded classes: ContentAlignment, Size class, SolidBrush
* Remove unneeded interface IContainer 
* Remove unneeded value WinformJPanel.autoScaleBaseSize

10.11.2018. v.2.8.9

* Case and Plural Support
* Support single line comments in properties files
* Migrate all comments to the names and titles in the language files
* First unit tests for few functions

Bug fixes:

* Corrections in Russian translation
* Small corrections in the English text
* Refinement Bar Status
* Fixed splash screen size

06.11.2018. v2.3.1-RC1

* Upgrade Gradle to 4.10.2 version
* Show game version from Gradle in FormAbout
* Automatic prepare BAT file and copy JAR file to root
* Solve compilation warnings

05.11.2018. v2.00-RC1

New features:

* Multilingual support for UI dialogs and in-game strings
* Russian translation
* Gradle as main build tool
* Full refactor, code clean-up
* Custom strings reader
* Autosize labels, buttons, panels
* Measure multiline labels

Bug fixes:

* High Score is working now
* Many other minor bug fixes

Started at 13.10.2018

## Space Trader for Java

### Authored By Aviv Eyal (09.10.2008-03.12.2010)

13.03.2010 1.12

A few tiny changes, including one or two bug fixes.
This version is mostly about syncing the binary version with the code - many changes that did not on their own were important enough for a binary release, combined with the long time passed, it's time for a new one.

Most notable bug fix is that exiting the game should now always work. Also, ship designers will now limit the points you can use for your ship.

* Many code changes, that don't (shouldn't) affect game.
* Fixed another "Can't exit" bug (Whenever a window was closed by hitting the X button)
* Fixed the bug where there was no upper limit on the amounts of Design Points you could
  put in your ship.

08.10.2009 1.11

I've spent the last couple of weeks making the game actually playable in non-windows stations - thanks to Chris (For pointing out it doesn't work, and for repeatedly testing versions on his Linux station) and to Sonia (For testing on the Mac).

It should now work on any computer with a 5.0 JRE installed.

Also: I know of are two bugs in the game; If you happen to run across any more, please let me know, so I can fix them :)

* Game now runs under Linux, Mac, and hopefully everything else. Thanks Chris and Sonia!
* Everything is compiled as Java version 1.5 (Macs have problems with version 1.6)
* Fixed a bug that you could't exit the game without saving or retiring.

04.07.2009 1.1

* Separate main window to several classes.
* Enable play in non-cheat mode (Just enter a name in the New Game dialog)
* Fixed bugs in high-score: sort during save, read from file

21.11.2008 0.9

The first release is out - Version 0.9. Play today!

## Space Trader for Windows

### Authored By Jay French aka JAF (08.12.2003-14.08.2008)

14.08.2008
2.01 Changes:
* Fixed 6 bugs logged at sf.net.
* 1844296	100 Bays truncate to 10 during plunder 
* 1844287	Hull Hardening 
* 1844164	V 2.00 police choice negated 
* 1684012	v2.00 money error 
* 1184044	shipyard design error 
* 1173304	cargo transfer by pirate crashes the game 

* Removed installer and game converter projects
* Added folders to zip file for custom ship data, saved games, and settings data
* Added 4 new sets of custom ship images - thanks to William W. Connors!

23.03.2005
2.0 Enhancements:
* Bounty offered for capture/killing of player based on their Police Record
* Custom ship designs in Shipyards, and newspaper will have notice when nearby system has a shipyard
* Redesigned Equipment screen
* Redesigned Personnel screen
* Added color to Special button
* Added some tooltips
* Added 15 new mercenaries and 8 new systems; allow up to three mercenaries per system at when new game is started
* Added option to show newspaper automatically on arrival
* Redesigned the saved game file format, so that new versions of Space Trader will always be able to open saved games from previous versions (back to 2.0)
* Created file converter (saved games, high scores, options) to convert 1.3 files to 2.0
* Added folders to the base folder for the saved games, images, etc. to reside in
* Added 2 new quests
* Added 1 new gadget
* Numerous bug fixes
* Added lots more images for equipment, etc.
* Require confirmation when loading a game, starting a new game, or quitting game (but only when at least one day has passed since the last save)
* Fixed code that generates opponents - the opponents were usually weaker than they should have been
* Added 2 new weapons that can disable an opponent without distroying them

2004-02-09 - Space Trader 1.2 has been released. It includes 2 bug fixes. See the History page for the list of fixes. Visit the Download page to download the latest install.

* You can't manually enter larger values on the new game screen to give total skills greater than 20.
* Fixed a bug that prevented the Alien Artifact quest from ever being finished.
* Didn't break saved-game compatability!
    
2003-12-23 - Space Trader 1.1 has been released. It includes several bug fixes. See the History page for the list of fixes.

* Buying a new ship when you had already upgraded from the Gnat no longer causes an error.
* Jarek and Wild will now leave the ship when you arrive at the destination you agreed to transport them to (you must click the Special button at the destination for them to leave your ship, though).
* There was a bug where if you had special cargo (cargo that wasn't a trade item but takes up cargo bays) an error message would pop up when you defeated an opponent.
* Firing a mercenary caused an error if your ship had 2 crew quarters (if you had 3 there was no error, which is what made this one elusive for me).

2003-12-08 - Space Trader for Windows 1.0 is released! Thanks to all my beta testers, including (but not limited to):

* David Besselievre
* David Dousay
* Ames Grawert
* Andrew Kuehler
* Jack Lindsay
* Tim Schaab
* Jean-Paul Turcotte
* Eric Zippe

And of course a huge "Thanks!" to Pieter Spronk for creating such a great game in the first place. 
