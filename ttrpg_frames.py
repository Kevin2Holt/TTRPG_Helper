"""
Author: Kevin Holt
Version: 0.2.15
Project: TTRPG Helper
File: Frames

Each frame is a pre-set (pre-built) layout of certain modules.
This generally comes from a theme such as for the StatsFrame.

Each class creates one layout, which involves creating and setting the position of each module
Essentially, each Frame is a larger module.
    Or a module of modules

Each Frame (generally) consists of these parts:
    __init__()
        > This sets the base, creating the Frame and putting the modules in it.
    get()
        > Returns the frame reference so external code can reference it.

    self.outerBox
        > The container that holds the frame
        > Basically only used in defining self.frame
    self.frame
        > The container that holds all of the modules
    self.player
        > Most modules rely on 1+ stat(s) in the Character() object
        > This is the Frame's reference to that object
"""
import tkinter as tk
from tkinter import ttk
from ttrpg_modules import *

class CharacterFrame(object):
    def __init__(self, newOuterBox, newPlayer):
        self.outerBox = newOuterBox
        self.player = newPlayer
        self.maxGridCol = 4
        self.maxGridRow = 2

        self.frame = ttk.Frame(self.outerBox)
        self.frame.pack(fill = "both", expand = True)

        self.headerModule = HeaderModule(self.frame, self.player)
        self.headerModule.setPos(0, 0, self.maxGridCol + 1, 1, "NWE")

        self.hpModule = HPModule(self.frame, self.player)
        self.hpModule.setPos(0, 1, 1, 1, "NSWE")
        self.referenceModule = ReferenceModule(self.frame, self.player)
        self.referenceModule.setPos(1, 1, 2, 2, "N")
        self.xpModule = XPModule(self.frame, self.player)
        self.xpModule.setPos(self.maxGridCol - 1, 1, 2, 1, "NE")

        self.abilityModule = AbilityModule(self.frame, self.player)
        self.abilityModule.setPos(0, 2, 1, 2, "WN")
        self.moneyModule = MoneyModule(self.frame, self.player)
        self.moneyModule.setPos(self.maxGridCol - 1, 2, 2, 2, "EN")

    def get(self):
        return self.frame

class StatsFrame(object):
    def __init__(self, newOuterBox, newPlayer):
        self.outerBox = newOuterBox
        self.player = newPlayer
        self.maxGridCol = 1
        self.maxGridRow = 2

        self.frame = ttk.Frame(self.outerBox)
        self.frame.pack(fill = "both", expand = True)

        self.headerModule = HeaderModule(self.frame, self.player)
        self.headerModule.setPos(0, 0, self.maxGridCol + 1, 1, "NWE")

        self.skillsModule = SkillsModule(self.frame, self.player)
        self.skillsModule.setPos(0, 1, 1, 3, "NW")

        self.abilityModule = AbilityModule(self.frame, self.player)
        self.abilityModule.setPos(1, 1, 1, 1, "NW")

        self.moneyModule = MoneyModule(self.frame, self.player)
        self.moneyModule.setPos(1, 2, 1, 1, "NW")

    def get(self):
        return self.frame

"""This class 'SpellsFrame' is currently not fully developed and is currently not being used"""
class SpellsFrame(object):
    def __init__(self, newOuterBox, newPlayer):
        self.outerBox = newOuterBox
        self.player = newPlayer
        self.maxGridCol = 0
        self.maxGridRow = 1

        self.frame = ttk.Frame(self.outerBox)
        self.frame.pack(fill = "both", expand = True)

        self.headerModule = HeaderModule(self.frame, self.player)
        self.headerModule.setPos(0,0,self.maxGridCol+1,1,"NWE")

        self.spellListModule = SpellListModule(self.frame, self.player)
        self.spellListModule.setPos(0,1,1,1,"NW")

    def get(self):
        return self.frame

class ToolsFrame(object):
    def __init__(self, newOuterBox, newPlayer):
        self.outerBox = newOuterBox
        self.player = newPlayer

        self.frame = ttk.Frame(self.outerBox)
        self.frame.pack(fill = "both", expand = True)

        self.diceModule = DiceModule(self.frame)
        self.diceModule.setPos(0,0,1,1,"")

    def get(self):
        return self.frame
