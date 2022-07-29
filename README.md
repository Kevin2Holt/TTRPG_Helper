Author: Kevin Holt
Version: 0.2.15
Project: TTRPG Helper
File: README

Overview:
    This project stemmed from my love of table-top role-playing games (TTRPGs).
    Everything in this program is based on Dungeons & Dragons 5e (D&D 5e).
        *I do not get any royalties from any D&D products, and are in no way affiliated with Wizards of the Coast.

    I have long since made many spreadsheets for a large variety of things ranging from DM tools to character sheets.
    While spreadsheets are fun and, for the most part, fill the needs I have, I have considered coding an actual tool for a long time.
    A project for a college class finally prompted me to start this project, though I only was able to submit a very rudimentary version.

    Things that are currently planned:
        > Saving/Loading characters
        > Spells & Items panels
        > Pop-out versions of each panel
            > Maybe pop-out for each module
        > Proficiencies
        > Character Creator

    Things I am considering adding in the future:
        > Pre-generated races/classes that automatically give bonuses (according to the PHB)


User Manual:
    Most things are pretty self-contained.
    While there is an overarching character that is shared across the entire program, each module generally functions separately from the others.

    For this user manual, I am going to assume that you either:
        > Know how to play D&D
        > Have a basic understanding of D&D,
        > Have access to the appropriate resources to explain the mechanics of D&D.
    I will not be explaining the purpose of each statistic, number, or value.
    The purpose of this user manual is to explain how to use this tool.


    *** IMPORTANT ***
    * This tool currently does not save your character and their stats.
    * Be sure to record your stats somewhere before closing the tool.
    *
    * Saving is planned to be implemented in a future update.

    Each module can be separated by the labeled boxes.


    'Edit' Button:
        Most modules have an 'Edit' button.
        This allows you to quickly edit values that aren't changed very often or change values in large quantities (rather than just 1 that the buttons allow)

        Clicking on the 'Edit' button will bring up a new window where you can change the values.
        Clicking on the 'Save' button with then save the data you've input so it can be used by other modules.
            This will update the values in that module.
            Currently, this is the only way to update values in a module. Modules that are used multiple times need to be updated separately.

        If you input a value that doesn't match what is expected (e.g. inputting "Cow" when a number is expected), then it will be discarded.
        Currently, all numbers are integers, meaning that there are no decimal values. All decimal values are discarded.

    Header Module:
    At the top of each screen, you can find basic information about your character including:
        > Name
        > Alignment
        > Race
        > Level
        > Class
    These can be changed by clicking the 'Edit' button and changing the corresponding values.


    Character Tab:
        The 'Character' tab shows an overview of your character and their stats.
        Some other modules are included for convenience.

        HP Module:
            The HP module shows the character's health points.
            A numerical representation can be seen in the module's title.
            A graphical representation can be seen as a green bar between the plus ('+') and minus ('-') buttons.

            To change the maximum HP, you need to click the 'Edit' button and change the value labeled 'Max HP'.
            Current HP can also be changed using the 'Edit' screen, though you can quickly make adjustments by using the plus ('+') and minus ('-') buttons

        Ability Scores Module:
            The Ability Scores module displays the six core ability scores.
            Each score is labeled on the left of the module.
            In the middle (the left number), you will find the ability score.
            On the right, the corresponding ability modifier is shown.

            Ability scores can be changed by clicking the 'Edit' button and changing the appropriate values.

        Reference Module:
            This module shows many values, scores, and modifiers that are good to have on hand, but aren't changed very often.
            Each number (on the right) is labeled (on the left).
            Clicking the 'Edit' button allows you to change any values that aren't strictly calculated.
                Currently Armor Class (AC) is not calculated.

        XP Module:
            A numerical representation of your xp is shown in the module's title.
            A graphical representation is shown immediately below the title (at the top of the module).

            XP can quickly be added by inputting a number into the text box and clicking the 'Add XP' button.
                XP can be taken away by inputting a negative number.
            The 'Edit' button allows you to edit both the current XP and XP needed for the next level.

        Currency Module:
            Each currency has a plus ('+') and a minus ('-') button that will add or subtract one from your total.
            The 'Edit' button allows you to quickly make larger changes.

    Stats Tab:
        The 'Stats' tab shows a more in-depth view of your character's stats.
        You can find the Header module at the top of this tab.

        Skills Module:
            Each skill and the corresponding modifier can be seen in this module.

            This module does not automatically update with each change to your ability scores.
            You need to click the 'Update' button to update the skill modifier values.

        Currency Module:
            Each currency has a plus ('+') and a minus ('-') button that will add or subtract one from your total.
            The 'Edit' button allows you to quickly make larger changes.

        Ability Scores Module:
            The Ability Scores module displays the six core ability scores.
            Each score is labeled on the left of the module.
            In the middle (the left number), you will find the ability score.
            On the right, the corresponding ability modifier is shown.

            Ability scores can be changed by clicking the 'Edit' button and changing the appropriate values.

    Tools Tab:
        The 'Tools' tab holds useful tools for your sessions.

        Die Roller Module:
            Clicking on the corresponding button generates a random number (a roll) of that die.
            Clicking on the 'Pop Out' button lets you have this tool as a separate window for convenience.
