"""
Author: Kevin Holt
Version: 0.2.15
Project: TTRPG Helper
File: Character

This file holds the Character class which is the base of most of this tool.

One of the biggest purposes of the Character class is to store values and stats for the modules to display and/or run calculations on.
Several calcualtions are also done within the class.
"""
from ttrpg_item import Item
from ttrpg_item import Weapon
from ttrpg_item import Armor
from ttrpg_spell import Spell
import pickle


"""
This global constant defines which base ability score (STR, DEX, CON, INT, WIS, CHA) corresponds with which skill modifier.
This needs to be in the same order as 'self.skillNames', 'self.skillMod', and 'self.skillProf'.
"""
SKILL_MOD_NAME = (
    "dex",
    "wis",
    "int",
    "str",
    "cha",
    "int",
    "wis",
    "cha",
    "int",
    "wis",
    "int",
    "wis",
    "cha",
    "cha",
    "int",
    "dex",
    "dex",
    "wis"
    )

class Character(object):

    def __init__(self):
        """Variable Initialization"""
        self.name = "John Doe"
        self.level = 1
        self.exp = 0
        self.expToNext = 100
        self.playerClass = "Fighter"
        self.race = "Human"
        self.alignment = "NG"
        self.maxHP = 1
        self.curHP = 1
        self.profMod = 2
        self.armorClass = 10
        self.speed = 30

        self.str = 0
        self.dex = 0
        self.con = 0
        self.int = 0
        self.wis = 0
        self.cha = 0
        self.skillNames = [
            "Acrobatics",
            "Animal Handling",
            "Arcana",
            "Athletics",
            "Deception",
            "History",
            "Insight",
            "Intimidation",
            "Investigation",
            "Medicine",
            "Nature",
            "Perception",
            "Performance",
            "Persuasion",
            "Religion",
            "Sleight of Hand",
            "Stealth",
            "Survival"
        ]
        self.skillMod = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.skillProf = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False] # True = Proficiency in skill

        self.strMod = int((self.str - 10) / 2)
        self.dexMod = int((self.dex - 10) / 2)
        self.conMod = int((self.con - 10) / 2)
        self.intMod = int((self.int - 10) / 2)
        self.wisMod = int((self.wis - 10) / 2)
        self.chaMod = int((self.cha - 10) / 2)

        self.coinPlatinum = 0
        self.coinGold = 0
        self.coinSilver = 0
        self.coinCopper = 0

        self.items = []
        self.weapons = []
        self.armor = []
        self.spells = []

        """ This is for the character save/load update and currently does nothing.
        try:
            self.load()
        except:
            self.name = self.name
        """

    """Runs the calculations for the assorted modifier stats and stores them in the corresponding variable"""
    def updateStats(self):
        self.strMod = int((self.str - 10) / 2)
        self.dexMod = int((self.dex - 10) / 2)
        self.conMod = int((self.con - 10) / 2)
        self.intMod = int((self.int - 10) / 2)
        self.wisMod = int((self.wis - 10) / 2)
        self.chaMod = int((self.cha - 10) / 2)

        for i in range(len(self.skillMod)):
            match SKILL_MOD_NAME[i]:
                case "str":
                    self.skillMod[i] = self.strMod + self.profMod if self.skillProf[i] else self.strMod
                case "dex":
                    self.skillMod[i] = self.dexMod + self.profMod if self.skillProf[i] else self.dexMod
                case "con":
                    self.skillMod[i] = self.conMod + self.profMod if self.skillProf[i] else self.conMod
                case "int":
                    self.skillMod[i] = self.intMod + self.profMod if self.skillProf[i] else self.intMod
                case "wis":
                    self.skillMod[i] = self.wisMod + self.profMod if self.skillProf[i] else self.wisMod
                case "cha":
                    self.skillMod[i] = self.chaMod + self.profMod if self.skillProf[i] else self.chaMod
                case _:
                    self.skillMod[i] = 0

    """Everything below this line is planned to be fully implemented in a future update"""
    def newItem(self, newName = "Item", newDesc = "Description"):
        self.items.append(Item(newName, newDesc))
    def newWeapon(self, newName = "Item", newDesc = "Description"):
        self.weapons.append(Weapon(newName, newDm, newDmgDie, newHitMod, newDesc))
    def newArmor(self, newName = "Item", newAC = 0, newDesc = "Description"):
        self.armor.append(Armor(newName, newAC, newDesc))
    def newSpell(self, newName = "Spell", newComponents = "", newShortDesc = "Short Description", newLongDesc = "Long Description"):
        self.spells.append(Spell(newName, newComponents, newShortDesc, newLongDesc))

    def save(self):
        #Saves as <self.name>.txt
        file = open(self.name + ".txt", "w")
        pickle.dump(self, file)
        file.close()
    def load(self):
        file = open(self.name + ".txt","r")
        self = pickle.load(file)
        file.close()
