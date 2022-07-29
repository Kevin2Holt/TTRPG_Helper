"""
Author: Kevin Holt
Version: 0.2.15
Project: TTRPG Helper
File: Modules

Each class in this file represents a single module.
These are seen as LabelFrames on the program (each individual box).
The only exception (so-far) is the HeaderModule which creates the header at the top of each panel. (It isn't in a LabelFrame. Thus, no box)

Each module is then used to build each frame.
*See ttrpg_frames.py for more info


Each module (generally) consists of these parts:
    __init__()
        > This sets the base for the module, creating the LabelFrame and putting the ttk widgets in it.
    edit()
        > Some modules have need for an edit feature,
        > which allows the user to change values that are rarely changed
        > or change values in large quantities (rather than just 1 that the buttons allow)
        >
        > The main purpose of this function is to create a new window that is layed out specifically to make this process easier.
        > This generally includes Entry widgets rather than buttons
    update()
        > This function updates all of the values that change in that module.
        > This currently only happens when you use the "Edit" and "Save" buttons or the "Update" button for the SkillsModule
    setPos()
        > This allows external code (outside of the module) to set the position of the module in the grid

    self.outerBox
        > The container that holds the module
        > Basically only used in defining self.box
    self.box
        > The container that is the module
        > Usually the LabelFrame
    self.player
        > Most modules/functions rely on 1+ stat(s) in the Character() object
        > This is the module's reference to that object
"""
import tkinter as tk
from tkinter import ttk
import random

class HPModule(object):

    def __init__(self, newOuterBox, newPlayer):
        self.player = newPlayer
        self.outerBox = newOuterBox

        def hpUp():
            #This has no hard cap due to abilities that raise hp above the player's max
            self.player.curHP += 1
            self.update()

        def hpDown():
            #this has no hard cap due to cases and situations where the player's hp falls below 0
            self.player.curHP -= 1
            self.update()

        def edit():
            self.editWindow = tk.Tk()
            self.editWindow.resizable(True, True)
            self.editWindow.title("TTRPG Helper | Edit HP")
            self.curHPLabel = ttk.Label(self.editWindow, text = "Current HP: ")
            self.curHPLabel.grid(column = 0, row = 0, sticky = tk.E)
            self.curHPEntry = ttk.Entry(self.editWindow, width = 8)
            self.curHPEntry.insert(0,str(self.player.curHP))
            self.curHPEntry.grid(column = 1, row = 0)
            self.maxHPLabel = ttk.Label(self.editWindow, text = "Max HP: ")
            self.maxHPLabel.grid(column = 0, row = 1, sticky = tk.E)
            self.maxHPEntry = ttk.Entry(self.editWindow, width = 8)
            self.maxHPEntry.insert(0, self.player.maxHP)
            self.maxHPEntry.grid(column = 1, row = 1)
            def closeWindow():
                try:
                    self.player.curHP = int(self.curHPEntry.get())
                except:
                    print("Current HP value is not an integer")
                try:
                    self.player.maxHP = int(self.maxHPEntry.get())
                except:
                    print("Max HP value is not an integer")
                self.editWindow.destroy()
                self.update()
            self.hpBtn = ttk.Button(self.editWindow, text = "Save", command = closeWindow, width = 0)
            self.hpBtn.grid(column = 0, row = 2, columnspan = 2, sticky = tk.W)

        self.box = ttk.LabelFrame(self.outerBox, text = "HP: " + str(self.player.curHP) + "/" + str(self.player.maxHP))
        self.hpDownBtn = ttk.Button(self.box, text = "-", command = hpDown, width = 0)
        self.hpDownBtn.grid(column = 0, row = 0)
        self.hpProgressBar = ttk.Progressbar(self.box, orient = "horizontal", mode = "determinate", length = 100)
        self.hpProgressBar["value"] = (self.player.curHP / self.player.maxHP) * 100
        self.hpProgressBar.grid(column = 1, row = 0)
        self.hpUpBtn = ttk.Button(self.box, text = "+", command = hpUp, width = 0)
        self.hpUpBtn.grid(column = 2, row = 0,)
        self.hpBtn = ttk.Button(self.box, text = "Edit", command = edit, width = 0)
        self.hpBtn.grid(column = 0, row = 1, columnspan = 2, sticky = tk.W)


    def __str__(self):
        return "HP: " + str(self.player.curHP) + "/" + str(self.player.maxHP)

    def update(self):
        self.box.config(text = "HP: " + str(self.player.curHP) + "/" + str(self.player.maxHP))
        self.hpProgressBar["value"] = (self.player.curHP / self.player.maxHP) * 100

    def setPos(self, newColumn = 0, newRow = 0, newColumnspan = 1, newRowspan = 1, newSticky = ""):
        self.box.grid(column = newColumn, row = newRow, columnspan = newColumnspan, rowspan = newRowspan, sticky = newSticky)

class XPModule(object):
    def __init__(self, newOuterBox, newPlayer):

        self.outerBox = newOuterBox
        self.player = newPlayer

        def addXp():
            if self.player.exp + int(self.xpEntry.get()) < 0:
                try:
                    self.player.exp = 0
                except:
                    print("XP value is not an integer")
            else:
                try:
                    self.player.exp += int(self.xpEntry.get())
                except:
                    print("XP value is not an integer")
            self.update()

        def edit():
            self.editWindow = tk.Tk()
            self.editWindow.resizable(True, True)
            self.editWindow.title("TTRPG Helper | Edit XP")
            self.curXPLabel = ttk.Label(self.editWindow, text = "Current XP: ")
            self.curXPLabel.grid(column = 0, row = 0, sticky = tk.E)
            self.curXPEntry = ttk.Entry(self.editWindow, width = 8)
            self.curXPEntry.insert(0,str(self.player.exp))
            self.curXPEntry.grid(column = 1, row = 0)
            self.maxXPLabel = ttk.Label(self.editWindow, text = "XP to Next: ")
            self.maxXPLabel.grid(column = 0, row = 1, sticky = tk.E)
            self.maxXPEntry = ttk.Entry(self.editWindow, width = 8)
            self.maxXPEntry.insert(0, self.player.expToNext)
            self.maxXPEntry.grid(column = 1, row = 1)
            def closeWindow():
                try:
                    self.player.exp = int(self.curXPEntry.get())
                except:
                    print("Current XP value is not an integer")
                try:
                    self.player.expToNext = int(self.maxXPEntry.get())
                except:
                    print("XP to Next value is not an integer")
                self.editWindow.destroy()
                self.update()
            self.xpBtn = ttk.Button(self.editWindow, text = "Save", command = closeWindow, width = 0)
            self.xpBtn.grid(column = 0, row = 2, columnspan = 2, sticky = tk.W)

        self.box = ttk.LabelFrame(self.outerBox, text = "XP: " + str(self.player.exp) + "/" + str(self.player.expToNext))
        self.xpProgressBar = ttk.Progressbar(self.box, orient = "horizontal", mode = "determinate", length = 100)
        self.xpProgressBar["value"] = (self.player.exp / self.player.expToNext) * 100
        self.xpProgressBar.grid(column = 0, row = 0, columnspan = 2)
        self.xpEntryBtn = ttk.Button(self.box, text = "Add XP:", width = 0, command = addXp)
        self.xpEntryBtn.grid(column = 0, row = 1)
        self.xpEntry = ttk.Entry(self.box, width = 8)
        self.xpEntry.grid(column = 1, row = 1, sticky = tk.W+tk.E)
        self.xpBtn = ttk.Button(self.box, text = "Edit", command = edit, width = 0)
        self.xpBtn.grid(column = 0, row = 2, columnspan = 2, sticky = tk.W)

    def __str__(self):
        return "XP: " + str(self.player.exp) + "/" + str(self.player.expToNext)
    def update(self):
            self.box.config(text = "XP: " + str(self.player.exp) + "/" + str(self.player.expToNext))
            self.xpProgressBar["value"] = (self.player.exp / self.player.expToNext) * 100

    def setPos(self, newColumn = 0, newRow = 0, newColumnspan = 1, newRowspan = 1, newSticky = ""):
            self.box.grid(column = newColumn, row = newRow, columnspan = newColumnspan, rowspan = newRowspan, sticky = newSticky)

class AbilityModule(object):
    def __init__(self, newOuterBox, newPlayer):
        self.outerBox = newOuterBox
        self.player = newPlayer

        def edit():
            self.editWindow = tk.Tk()
            self.editWindow.resizable(True, True)
            self.editWindow.title("TTRPG Helper | Edit Ability Scores")

            self.strLabel = ttk.Label(self.editWindow, text = "STR: ")
            self.strLabel.grid(column = 0, row = 0, sticky = tk.E)
            self.strEntry = ttk.Entry(self.editWindow, width = 8)
            self.strEntry.insert(0,str(self.player.str))
            self.strEntry.grid(column = 1, row = 0)

            self.dexLabel = ttk.Label(self.editWindow, text = "DEX: ")
            self.dexLabel.grid(column = 0, row = 1, sticky = tk.E)
            self.dexEntry = ttk.Entry(self.editWindow, width = 8)
            self.dexEntry.insert(0,str(self.player.dex))
            self.dexEntry.grid(column = 1, row = 1)

            self.conLabel = ttk.Label(self.editWindow, text = "CON: ")
            self.conLabel.grid(column = 0, row = 2, sticky = tk.E)
            self.conEntry = ttk.Entry(self.editWindow, width = 8)
            self.conEntry.insert(0,str(self.player.con))
            self.conEntry.grid(column = 1, row = 2)

            self.intLabel = ttk.Label(self.editWindow, text = "INT: ")
            self.intLabel.grid(column = 0, row = 3, sticky = tk.E)
            self.intEntry = ttk.Entry(self.editWindow, width = 8)
            self.intEntry.insert(0,str(self.player.int))
            self.intEntry.grid(column = 1, row = 3)

            self.wisLabel = ttk.Label(self.editWindow, text = "WIS: ")
            self.wisLabel.grid(column = 0, row = 4, sticky = tk.E)
            self.wisEntry = ttk.Entry(self.editWindow, width = 8)
            self.wisEntry.insert(0,str(self.player.wis))
            self.wisEntry.grid(column = 1, row = 4)

            self.chaLabel = ttk.Label(self.editWindow, text = "CHA: ")
            self.chaLabel.grid(column = 0, row = 5, sticky = tk.E)
            self.chaEntry = ttk.Entry(self.editWindow, width = 8)
            self.chaEntry.insert(0,str(self.player.cha))
            self.chaEntry.grid(column = 1, row = 5)

            def closeWindow():
                try:
                    self.player.str = int(self.strEntry.get())
                except:
                    print("STR value is not an integer")
                try:
                    self.player.dex = int(self.dexEntry.get())
                except:
                    print("DEX value is not an integer")
                try:
                    self.player.con = int(self.conEntry.get())
                except:
                    print("CON value is not an integer")
                try:
                    self.player.int = int(self.intEntry.get())
                except:
                    print("INT value is not an integer")
                try:
                    self.player.wis = int(self.wisEntry.get())
                except:
                    print("WIS value is not an integer")
                try:
                    self.player.cha = int(self.chaEntry.get())
                except:
                    print("CHA value is not an integer")
                self.editWindow.destroy()
                self.update()
            self.xpBtn = ttk.Button(self.editWindow, text = "Save", command = closeWindow, width = 0)
            self.xpBtn.grid(column = 0, row = 6, columnspan = 2, sticky = tk.W)

        self.box = ttk.LabelFrame(self.outerBox, text = "Ability Scores")
        self.abilitySeparator = ttk.Separator(self.box, orient = "vertical")
        self.abilitySeparator.grid(column = 2, row = 0, rowspan = 6, sticky = tk.N+tk.S, padx = 10)

        self.strLabel = ttk.Label(self.box, text = "STR: ")
        self.strLabel.grid(column = 0, row = 0)
        self.strValue = ttk.Label(self.box, text = str(self.player.str))
        self.strValue.grid(column = 1, row = 0)
        self.strModValue = ttk.Label(self.box, text = "+" + str(self.player.strMod) if self.player.strMod >= 0 else str(self.player.strMod))
        self.strModValue.grid(column = 3, row = 0)

        self.dexLabel = ttk.Label(self.box, text = "DEX: ")
        self.dexLabel.grid(column = 0, row = 1)
        self.dexValue = ttk.Label(self.box, text = str(self.player.dex))
        self.dexValue.grid(column = 1, row = 1)
        self.dexModValue = ttk.Label(self.box, text = "+" + str(self.player.dexMod) if self.player.dexMod >= 0 else str(self.player.dexMod))
        self.dexModValue.grid(column = 3, row = 1)

        self.conLabel = ttk.Label(self.box, text = "CON: ")
        self.conLabel.grid(column = 0, row = 2)
        self.conValue = ttk.Label(self.box, text = str(self.player.con))
        self.conValue.grid(column = 1, row = 2)
        self.conModValue = ttk.Label(self.box, text = "+" + str(self.player.conMod) if self.player.conMod >= 0 else str(self.player.conMod))
        self.conModValue.grid(column = 3, row = 2)

        self.intLabel = ttk.Label(self.box, text = "INT: ")
        self.intLabel.grid(column = 0, row = 3)
        self.intValue = ttk.Label(self.box, text = str(self.player.int))
        self.intValue.grid(column = 1, row = 3)
        self.intModValue = ttk.Label(self.box, text = "+" + str(self.player.intMod) if self.player.intMod >= 0 else str(self.player.intMod))
        self.intModValue.grid(column = 3, row = 3)

        self.wisLabel = ttk.Label(self.box, text = "WIS: ")
        self.wisLabel.grid(column = 0, row = 4)
        self.wisValue = ttk.Label(self.box, text = str(self.player.wis))
        self.wisValue.grid(column = 1, row = 4)
        self.wisModValue = ttk.Label(self.box, text = "+" + str(self.player.wisMod) if self.player.wisMod >= 0 else str(self.player.wisMod))
        self.wisModValue.grid(column = 3, row = 4)

        self.chaLabel = ttk.Label(self.box, text = "CHA: ")
        self.chaLabel.grid(column = 0, row = 5)
        self.chaValue = ttk.Label(self.box, text = str(self.player.cha))
        self.chaValue.grid(column = 1, row = 5)
        self.chaModValue = ttk.Label(self.box, text = "+" + str(self.player.chaMod) if self.player.strMod >= 0 else str(self.player.chaMod))
        self.chaModValue.grid(column = 3, row = 5)

        self.abilityBtn = ttk.Button(self.box, text = "Edit", width = 0, command = edit)
        self.abilityBtn.grid(column = 0, row = 6, columnspan = 4, sticky = tk.W)

    def __str__(self):
        return False

    def update(self):
        self.player.updateStats()
        self.strValue.config(text = str(self.player.str))
        self.strModValue.config(text = "+" + str(self.player.strMod) if self.player.strMod >= 0 else str(self.player.strMod))
        self.dexValue.config(text = str(self.player.dex))
        self.dexModValue.config(text = "+" + str(self.player.dexMod) if self.player.dexMod >= 0 else str(self.player.dexMod))
        self.conValue.config(text = str(self.player.con))
        self.conModValue.config(text = "+" + str(self.player.conMod) if self.player.conMod >= 0 else str(self.player.conMod))
        self.intValue.config(text = str(self.player.int))
        self.intModValue.config(text = "+" + str(self.player.intMod) if self.player.intMod >= 0 else str(self.player.intMod))
        self.wisValue.config(text = str(self.player.wis))
        self.wisModValue.config(text = "+" + str(self.player.wisMod) if self.player.wisMod >= 0 else str(self.player.wisMod))
        self.chaValue.config(text = str(self.player.cha))
        self.chaModValue.config(text = "+" + str(self.player.chaMod) if self.player.chaMod >= 0 else str(self.player.chaMod))

    def setPos(self, newColumn = 0, newRow = 0, newColumnspan = 1, newRowspan = 1, newSticky = ""):
            self.box.grid(column = newColumn, row = newRow, columnspan = newColumnspan, rowspan = newRowspan, sticky = newSticky)

class MoneyModule(object):
    def __init__(self, newOuterBox, newPlayer):
        self.outerBox = newOuterBox
        self.player = newPlayer

        def edit():
            self.editWindow = tk.Tk()
            self.editWindow.resizable(True, True)
            self.editWindow.title("TTRPG Helper | Edit Coins")

            self.platinumLabel = ttk.Label(self.editWindow, text = "Platinum: ")
            self.platinumLabel.grid(column = 0, row = 0, sticky = tk.E)
            self.platinumEntry = ttk.Entry(self.editWindow, width = 8)
            self.platinumEntry.insert(0,str(self.player.coinPlatinum))
            self.platinumEntry.grid(column = 1, row = 0)

            self.goldLabel = ttk.Label(self.editWindow, text = "Gold: ")
            self.goldLabel.grid(column = 0, row = 1, sticky = tk.E)
            self.goldEntry = ttk.Entry(self.editWindow, width = 8)
            self.goldEntry.insert(0,str(self.player.coinGold))
            self.goldEntry.grid(column = 1, row = 1)

            self.silverLabel = ttk.Label(self.editWindow, text = "Silver: ")
            self.silverLabel.grid(column = 0, row = 2, sticky = tk.E)
            self.silverEntry = ttk.Entry(self.editWindow, width = 8)
            self.silverEntry.insert(0,str(self.player.coinSilver))
            self.silverEntry.grid(column = 1, row = 2)

            self.copperLabel = ttk.Label(self.editWindow, text = "Copper: ")
            self.copperLabel.grid(column = 0, row = 3, sticky = tk.E)
            self.copperEntry = ttk.Entry(self.editWindow, width = 8)
            self.copperEntry.insert(0,str(self.player.coinCopper))
            self.copperEntry.grid(column = 1, row = 3)

            def closeWindow():
                try:
                    self.player.coinCopper = int(self.copperEntry.get())
                except:
                    print("Copper value is not an integer")
                try:
                    self.player.coinSilver = int(self.silverEntry.get())
                except:
                    print("Silver value is not an integer")
                try:
                    self.player.coinGold = int(self.goldEntry.get())
                except:
                    print("Gold value is not an integer")
                try:
                    self.player.coinPlatinum = int(self.platinumEntry.get())
                except:
                    print("Platinum value is not an integer")
                self.editWindow.destroy()
                self.update()
            self.moneyBtn = ttk.Button(self.editWindow, text = "Save", command = closeWindow, width = 0)
            self.moneyBtn.grid(column = 0, row = 4, columnspan = 2, sticky = tk.W)

        self.box = ttk.LabelFrame(self.outerBox, text = "Currency")

        def moneyUpPlat():
            self.player.coinPlatinum += 1
            self.update()
        def moneyUpGold():
            self.player.coinGold += 1
            self.update()
        def moneyUpSilver():
            self.player.coinSilver += 1
            self.update()
        def moneyUpCopper():
            self.player.coinCopper += 1
            self.update()

        def moneyDownPlat():
            self.player.coinPlatinum -= 1
            self.update()
        def moneyDownGold():
            self.player.coinGold -= 1
            self.update()
        def moneyDownSilver():
            self.player.coinSilver -= 1
            self.update()
        def moneyDownCopper():
            self.player.coinCopper -= 1
            self.update()


        self.moneyLabelPlat = ttk.Label(self.box, text = "Platinum: ")
        self.moneyLabelPlat.grid(column = 0, row = 0)
        self.moneyBtnDownPlat = ttk.Button(self.box, text = "-", command = moneyDownPlat, width = 0)
        self.moneyBtnDownPlat.grid(column = 1, row = 0)
        self.moneyValuePlat = ttk.Label(self.box, text = str(self.player.coinPlatinum))
        self.moneyValuePlat.grid(column = 2, row = 0)
        self.moneyBtnUpPlat = ttk.Button(self.box, text = "+", command = moneyUpPlat, width = 0)
        self.moneyBtnUpPlat.grid(column = 3, row = 0)

        self.moneyLabelGold = ttk.Label(self.box, text = "Gold: ")
        self.moneyLabelGold.grid(column = 0, row = 1)
        self.moneyBtnDownGold = ttk.Button(self.box, text = "-", command = moneyDownGold, width = 0)
        self.moneyBtnDownGold.grid(column = 1, row = 1)
        self.moneyValueGold = ttk.Label(self.box, text = str(self.player.coinGold))
        self.moneyValueGold.grid(column = 2, row = 1)
        self.moneyBtnUpGold = ttk.Button(self.box, text = "+", command = moneyUpGold, width = 0)
        self.moneyBtnUpGold.grid(column = 3, row = 1)

        self.moneyLabelSilver = ttk.Label(self.box, text = "Silver: ")
        self.moneyLabelSilver.grid(column = 0, row = 2)
        self.moneyBtnDownSilver = ttk.Button(self.box, text = "-", command = moneyDownSilver, width = 0)
        self.moneyBtnDownSilver.grid(column = 1, row = 2)
        self.moneyValueSilver = ttk.Label(self.box, text = str(self.player.coinSilver))
        self.moneyValueSilver.grid(column = 2, row = 2)
        self.moneyBtnUpSilver = ttk.Button(self.box, text = "+", command = moneyUpSilver, width = 0)
        self.moneyBtnUpSilver.grid(column = 3, row = 2)

        self.moneyLabelCopper = ttk.Label(self.box, text = "Copper: ")
        self.moneyLabelCopper.grid(column = 0, row = 3)
        self.moneyBtnDownCopper = ttk.Button(self.box, text = "-", command = moneyDownCopper, width = 0)
        self.moneyBtnDownCopper.grid(column = 1, row = 3)
        self.moneyValueCopper = ttk.Label(self.box, text = str(self.player.coinCopper))
        self.moneyValueCopper.grid(column = 2, row = 3)
        self.moneyBtnUpCopper = ttk.Button(self.box, text = "+", command = moneyUpCopper, width = 0)
        self.moneyBtnUpCopper.grid(column = 3, row = 3)

        self.moneyBtn = ttk.Button(self.box, text = "Edit", width = 0, command = edit)
        self.moneyBtn.grid(column = 0, row = 4, columnspan = 2, sticky = tk.W)

    def __str__(self):
        return False

    def update(self):
        self.moneyValuePlat.config(text = str(self.player.coinPlatinum))
        self.moneyValueGold.config(text = str(self.player.coinGold))
        self.moneyValueSilver.config(text = str(self.player.coinSilver))
        self.moneyValueCopper.config(text = str(self.player.coinCopper))

    def setPos(self, newColumn = 0, newRow = 0, newColumnspan = 1, newRowspan = 1, newSticky = ""):
        self.box.grid(column = newColumn, row = newRow, columnspan = newColumnspan, rowspan = newRowspan, sticky = newSticky)

class ReferenceModule(object):
    def __init__(self, newOuterBox, newPlayer):
        self.outerBox = newOuterBox
        self.player = newPlayer

        def edit():
            self.editWindow = tk.Tk()
            self.editWindow.resizable(True, True)
            self.editWindow.title("TTRPG Helper | Edit Coins")

            self.editACLabel = ttk.Label(self.editWindow, text = "Armor Class: ")
            self.editACLabel.grid(column = 0, row = 0, sticky = tk.E)
            self.editACEntry = ttk.Entry(self.editWindow, width = 8)
            self.editACEntry.insert(0,str(self.player.armorClass))
            selfeditACcEntry.grid(column = 1, row = 0)

            self.editSpeedLabel = ttk.Label(self.editWindow, text = "Speed: ")
            self.editSpeedLabel.grid(column = 0, row = 0, sticky = tk.E)
            self.editSpeedEntry = ttk.Entry(self.editWindow, width = 8)
            self.editSpeedEntry.insert(0,str(self.player.speed))
            self.editSpeedEntry.grid(column = 1, row = 0)

            self.editPassPercLabel = ttk.Label(self.box, text = "Passive Perception: ")
            self.editPassPercLabel.grid(column = 0, row = 2, sticky = tk.E)
            self.editPassPercValue = ttk.Label(self.box, text = str(self.player.skillMod[11] + 10))
            self.editPassPercValue.grid(column = 1, row = 2)


            def closeWindow():
                try:
                    self.player.armorClass = int(self.editACEntry.get())
                except:
                    print("Armor Class value is not an integer")
                try:
                    self.player.speed = int(self.editSpeedEntry.get())
                except:
                    print("Speed value is not an integer")
                self.editWindow.destroy()
                self.update()
            self.moneyBtn = ttk.Button(self.editWindow, text = "Save", command = closeWindow, width = 0)
            self.moneyBtn.grid(column = 0, row = 4, columnspan = 2, sticky = tk.W)

        self.box = ttk.LabelFrame(self.outerBox, text = "Reference")

        self.acLabel = ttk.Label(self.box, text = "AC: ")
        self.acLabel.grid(column = 0, row = 0, sticky = tk.E)
        self.acValue = ttk.Label(self.box, text = str(self.player.armorClass))
        self.acValue.grid(column = 1, row = 0)

        self.speedLabel = ttk.Label(self.box, text = "Speed: ")
        self.speedLabel.grid(column = 0, row = 1, sticky = tk.E)
        self.speedValue = ttk.Label(self.box, text = str(self.player.speed))
        self.speedValue.grid(column = 1, row = 1)

        self.passPercLabel = ttk.Label(self.box, text = "Passive Perception: ")
        self.passPercLabel.grid(column = 0, row = 2, sticky = tk.E)
        self.passPercValue = ttk.Label(self.box, text = str(self.player.skillMod[11] + 10))
        self.passPercValue.grid(column = 1, row = 2)

        self.referenceBtn = ttk.Button(self.box, text = "Edit", width = 0, command = edit)
        self.referenceBtn.grid(column = 0, row = 4, columnspan = 2, sticky = tk.W)

    def __str__(self):
        return False

    def update(self):
        self.acValue.config(text = str(self.player.armorClass))
        self.speedValue.config(text = str(self.player.speed))
        self.passPercValue.config(text = str(self.player.skillMod[11] + 10))

    def setPos(self, newColumn = 0, newRow = 0, newColumnspan = 1, newRowspan = 1, newSticky = ""):
        self.box.grid(column = newColumn, row = newRow, columnspan = newColumnspan, rowspan = newRowspan, sticky = newSticky)

class HeaderModule(object):
    def __init__(self, newOuterBox, newPlayer):
        self.outerBox = newOuterBox
        self.player = newPlayer

        def edit():
            self.editWindow = tk.Tk()
            self.editWindow.resizable(True, True)
            self.editWindow.title("TTRPG Helper | Edit HP")

            self.editNameLabel = ttk.Label(self.editWindow, text = "Name: ")
            self.editNameLabel.grid(column = 0, row = 0, sticky = tk.E)
            self.editNameEntry = ttk.Entry(self.editWindow, width = 8)
            self.editNameEntry.insert(0,str(self.player.name))
            self.editNameEntry.grid(column = 1, row = 0)

            self.editAlignmentLabel = ttk.Label(self.editWindow, text = "Alignment: ")
            self.editAlignmentLabel.grid(column = 0, row = 1, sticky = tk.E)
            self.editAlignmentEntry = ttk.Entry(self.editWindow, width = 8)
            self.editAlignmentEntry.insert(0, self.player.alignment)
            self.editAlignmentEntry.grid(column = 1, row = 1)

            self.editRaceLabel = ttk.Label(self.editWindow, text = "Race: ")
            self.editRaceLabel.grid(column = 0, row = 2, sticky = tk.E)
            self.editRaceEntry = ttk.Entry(self.editWindow, width = 8)
            self.editRaceEntry.insert(0, self.player.race)
            self.editRaceEntry.grid(column = 1, row = 2)

            self.editLvlLabel = ttk.Label(self.editWindow, text = "Level: ")
            self.editLvlLabel.grid(column = 0, row = 3, sticky = tk.E)
            self.editLvlEntry = ttk.Entry(self.editWindow, width = 8)
            self.editLvlEntry.insert(0, self.player.level)
            self.editLvlEntry.grid(column = 1, row = 3)

            self.editClassLabel = ttk.Label(self.editWindow, text = "Class: ")
            self.editClassLabel.grid(column = 0, row = 4, sticky = tk.E)
            self.editClassEntry = ttk.Entry(self.editWindow, width = 8)
            self.editClassEntry.insert(0, self.player.playerClass)
            self.editClassEntry.grid(column = 1, row = 4)

            def closeWindow():
                self.player.name = self.editNameEntry.get()
                self.player.alignment = self.editAlignmentEntry.get()
                self.player.race = self.editRaceEntry.get()
                try:
                    self.player.level = int(self.editLvlEntry.get())
                except:
                    print("Level value is not an integer")
                self.player.playerClass = self.editClassEntry.get()
                self.editWindow.destroy()
                self.update()
            self.referenceBtn = ttk.Button(self.editWindow, text = "Save", command = closeWindow, width = 0)
            self.referenceBtn.grid(column = 0, row = 5, columnspan = 2, sticky = tk.W)

        self.box = ttk.Frame(self.outerBox)
        self.nameLabel = ttk.Label(self.box, text = self.player.name + " | ")
        self.nameLabel.grid(column = 0, row = 0, sticky = tk.W)

        self.alignmentLabel = ttk.Label(self.box, text = self.player.alignment + " | ")
        self.alignmentLabel.grid(column = 1, row = 0)

        self.raceLabel = ttk.Label(self.box, text = self.player.race + " | ")
        self.raceLabel.grid(column = 2, row = 0)

        self.lvlLabel = ttk.Label(self.box, text = "Level " + str(self.player.level) + " | ")
        self.lvlLabel.grid(column = 3, row = 0)

        self.classLabel = ttk.Label(self.box, text = self.player.playerClass)
        self.classLabel.grid(column = 4, row = 0)

        self.headerSeparator = ttk.Separator(self.box, orient = "horizontal")
        self.headerSeparator.grid(column = 0, row = 1, columnspan = 6, sticky = tk.W+tk.E)

        self.headerBtn = ttk.Button(self.box, text = "Edit", width = 0, command = edit)
        self.headerBtn.grid(column = 5, row = 0)

    def __str__(self):
        return False

    def update(self):
        self.nameLabel.config(text = self.player.name + " | ")
        self.alignmentLabel.config(text = self.player.alignment + " | ")
        self.raceLabel.config(text = self.player.race + " | ")
        self.lvlLabel.config(text = "Level " + str(self.player.level) + " | ")
        self.classLabel.config(text = self.player.playerClass)

    def setPos(self, newColumn = 0, newRow = 0, newColumnspan = 1, newRowspan = 1, newSticky = ""):
        self.box.grid(column = newColumn, row = newRow, columnspan = newColumnspan, rowspan = newRowspan, sticky = newSticky)

class SkillsModule(object):
    def __init__(self, newOuterBox, newPlayer):
        self.outerBox = newOuterBox
        self.player = newPlayer

        self.box = ttk.LabelFrame(self.outerBox, text = "Skills")

        def update():
            i = 0
            self.acrobaticsValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 1
            self.animalValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 2
            self.arcanaValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 3
            self.athleticsValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 4
            self.deceptionValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 5
            self.historyValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 6
            self.insightValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 7
            self.intimidationValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 8
            self.investigationValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 9
            self.medicineValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 10
            self.natureValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 11
            self.perceptionValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 12
            self.performanceValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 13
            self.persuasionValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 14
            self.religionValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 15
            self.sleightValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 16
            self.stealthValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
            i = 17
            self.survivalValue.config(text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))

        i = 0
        self.acrobaticsLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.acrobaticsLabel.grid(column = 0, row = i, sticky = tk.E)
        self.acrobaticsValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.acrobaticsValue.grid(column = 1, row = i, padx = 5)
        i = 1
        self.Label = ttk.Label(self.box, text = self.player.skillNames[i])
        self.Label.grid(column = 0, row = i, sticky = tk.E)
        self.Value = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.Value.grid(column = 1, row = i, padx = 5)
        i = 1
        self.animalLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.animalLabel.grid(column = 0, row = i, sticky = tk.E)
        self.animalValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.animalValue.grid(column = 1, row = i, padx = 5)
        i = 2
        self.arcanaLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.arcanaLabel.grid(column = 0, row = i, sticky = tk.E)
        self.arcanaValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.arcanaValue.grid(column = 1, row = i, padx = 5)
        i = 3
        self.athleticsLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.athleticsLabel.grid(column = 0, row = i, sticky = tk.E)
        self.athleticsValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.athleticsValue.grid(column = 1, row = i, padx = 5)
        i = 4
        self.deceptionLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.deceptionLabel.grid(column = 0, row = i, sticky = tk.E)
        self.deceptionValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.deceptionValue.grid(column = 1, row = i, padx = 5)
        i = 5
        self.historyLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.historyLabel.grid(column = 0, row = i, sticky = tk.E)
        self.historyValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.historyValue.grid(column = 1, row = i, padx = 5)
        i = 6
        self.insightLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.insightLabel.grid(column = 0, row = i, sticky = tk.E)
        self.insightValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.insightValue.grid(column = 1, row = i, padx = 5)
        i = 7
        self.intimidationLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.intimidationLabel.grid(column = 0, row = i, sticky = tk.E)
        self.intimidationValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.intimidationValue.grid(column = 1, row = i, padx = 5)
        i = 8
        self.investigationLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.investigationLabel.grid(column = 0, row = i, sticky = tk.E)
        self.investigationValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.investigationValue.grid(column = 1, row = i, padx = 5)
        i = 9
        self.medicineLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.medicineLabel.grid(column = 0, row = i, sticky = tk.E)
        self.medicineValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.medicineValue.grid(column = 1, row = i, padx = 5)
        i = 10
        self.natureLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.natureLabel.grid(column = 0, row = i, sticky = tk.E)
        self.natureValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.natureValue.grid(column = 1, row = i, padx = 5)
        i = 11
        self.perceptionLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.perceptionLabel.grid(column = 0, row = i, sticky = tk.E)
        self.perceptionValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.perceptionValue.grid(column = 1, row = i, padx = 5)
        i = 12
        self.performanceLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.performanceLabel.grid(column = 0, row = i, sticky = tk.E)
        self.performanceValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.performanceValue.grid(column = 1, row = i, padx = 5)
        i = 13
        self.persuasionLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.persuasionLabel.grid(column = 0, row = i, sticky = tk.E)
        self.persuasionValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.persuasionValue.grid(column = 1, row = i, padx = 5)
        i = 14
        self.religionLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.religionLabel.grid(column = 0, row = i, sticky = tk.E)
        self.religionValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.religionValue.grid(column = 1, row = i, padx = 5)
        i = 15
        self.sleightLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.sleightLabel.grid(column = 0, row = i, sticky = tk.E)
        self.sleightValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.sleightValue.grid(column = 1, row = i, padx = 5)
        i = 16
        self.stealthLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.stealthLabel.grid(column = 0, row = i, sticky = tk.E)
        self.stealthValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.stealthValue.grid(column = 1, row = i, padx = 5)
        i = 17
        self.survivalLabel = ttk.Label(self.box, text = self.player.skillNames[i])
        self.survivalLabel.grid(column = 0, row = i, sticky = tk.E)
        self.survivalValue = ttk.Label(self.box, text = "+" + str(self.player.skillMod[i]) if self.player.skillMod[i] >= 0 else str(self.player.skillMod[i]))
        self.survivalValue.grid(column = 1, row = i, padx = 5)

        self.skillsBtn = ttk.Button(self.box, text = "Update", command = update, width = 0)
        self.skillsBtn.grid(column = 0, row = len(self.player.skillMod), sticky = tk.W)

    def __str__(self):
        return False



    def setPos(self, newColumn = 0, newRow = 0, newColumnspan = 1, newRowspan = 1, newSticky = ""):
        self.box.grid(column = newColumn, row = newRow, columnspan = newColumnspan, rowspan = newRowspan, sticky = newSticky)

class SpellListModule(object):
    def __init__(self, newOuterBox, newPlayer, newBtnTxt = "Edit"):
        self.outerBox = newOuterBox
        self.player = newPlayer
        self.btnTxt = newBtnTxt

        def editSpellList():
            return None

        def closeSpellListWindow():
            return None

        self.box = ttk.Frame(self.outerBox)
        self.tree = ttk.Treeview(self.box, columns = ("name", "components", "shortDesc", "longDesc"), show = "headings")
        self.tree.heading("name", text = "Name")
        self.tree.heading("components", text = "Components")
        self.tree.heading("shortDesc", text = "Quick Description")
        self.tree.heading("longDesc", text = "Full Description")

        self.yScrollbar = ttk.Scrollbar(self.box, orient = tk.VERTICAL, command = self.tree.yview)
        self.tree.configure(yscroll = self.yScrollbar.set)
        self.yScrollbar.grid(column = 1, row = 0, sticky = tk.N+tk.S)

        self.xScrollbar = ttk.Scrollbar(self.box, orient = "horizontal", command = self.tree.xview)
        self.tree.configure(xscroll = self.xScrollbar.set)
        self.xScrollbar.grid(column = 0, row = 1, sticky = tk.W+tk.E)

    def __str__(self):
        return False

    def update(self):
        self.tree.delete(*self.tree.get_children())
        for item in self.player.spells:
            self.tree.insert("", tk.END, values = item.get())

    def setPos(self, newColumn = 0, newRow = 0, newColumnspan = 1, newRowspan = 1, newSticky = ""):
        self.box.grid(column = newColumn, row = newRow, columnspan = newColumnspan, rowspan = newRowspan, sticky = newSticky)

class DiceModule(object):
    def __init__(self, newOuterBox):
        self.outerBox = newOuterBox
        self.rollList = []
        self.rollDieList = []

        def popOut():
            self.popOutWindow = tk.Tk()
            self.popOutWindow.resizable(True, True)
            self.popOutWindow.title("Die Roller")

            self.d20Label = ttk.Label(self.popOutWindow, text = "-", width = 3)
            self.d20Label.grid(column = 1, row = 0, sticky = tk.W)
            self.d12Label = ttk.Label(self.popOutWindow, text = "-", width = 3)
            self.d12Label.grid(column = 1, row = 1, sticky = tk.W)
            self.d100Label = ttk.Label(self.popOutWindow, text = "-", width = 3)
            self.d100Label.grid(column = 3, row = 0, sticky = tk.W)
            self.d10Label = ttk.Label(self.popOutWindow, text = "-", width = 3)
            self.d10Label.grid(column = 3, row = 1, sticky = tk.W)
            self.d8Label = ttk.Label(self.popOutWindow, text = "-", width = 3)
            self.d8Label.grid(column = 5, row = 0, sticky = tk.W)
            self.d6Label = ttk.Label(self.popOutWindow, text = "-", width = 3)
            self.d6Label.grid(column = 5, row = 1, sticky = tk.W)
            self.d4Label = ttk.Label(self.popOutWindow, text = "-", width = 3)
            self.d4Label.grid(column = 7, row = 0, sticky = tk.W)

            def roll20():
                self.rollList.append(random.randint(1, 20))
                self.rollDieList.append(20)
                self.d20Label.config(text = str(self.rollList[-1]))
            def roll12():
                self.rollList.append(random.randint(1, 12))
                self.rollDieList.append(12)
                self.d12Label.config(text = str(self.rollList[-1]))
            def roll100():
                self.rollList.append(random.randint(1, 100))
                self.rollDieList.append(100)
                self.d100Label.config(text = str(self.rollList[-1]))
            def roll10():
                self.rollList.append(random.randint(1, 10))
                self.rollDieList.append(10)
                self.d10Label.config(text = str(self.rollList[-1]))
            def roll8():
                self.rollList.append(random.randint(1, 8))
                self.rollDieList.append(8)
                self.d8Label.config(text = str(self.rollList[-1]))
            def roll6():
                self.rollList.append(random.randint(1, 6))
                self.rollDieList.append(6)
                self.d6Label.config(text = str(self.rollList[-1]))
            def roll4():
                self.rollList.append(random.randint(1, 4))
                self.rollDieList.append(4)
                self.d4Label.config(text = str(self.rollList[-1]))

            self.d20Btn = ttk.Button(self.popOutWindow, command = roll20, text = "d20", width = 4)
            self.d20Btn.grid(column = 0, row = 0)
            self.d12Btn = ttk.Button(self.popOutWindow, command = roll12, text = "d12", width = 4)
            self.d12Btn.grid(column = 0, row = 1)
            self.d100Btn = ttk.Button(self.popOutWindow, command = roll100, text = "d%", width = 4)
            self.d100Btn.grid(column = 2, row = 0)
            self.d10Btn = ttk.Button(self.popOutWindow, command = roll10, text = "d10", width = 4)
            self.d10Btn.grid(column = 2, row = 1)
            self.d8Btn = ttk.Button(self.popOutWindow, command = roll8, text = "d8", width = 4)
            self.d8Btn.grid(column = 4, row = 0)
            self.d6Btn = ttk.Button(self.popOutWindow, command = roll6, text = "d6", width = 4)
            self.d6Btn.grid(column = 4, row = 1)
            self.d4Btn = ttk.Button(self.popOutWindow, command = roll4, text = "d4", width = 4)
            self.d4Btn.grid(column = 6, row = 0)

        self.box = ttk.LabelFrame(self.outerBox, text = "Die Roller")
        self.d20Label = ttk.Label(self.box, text = "-", width = 3)
        self.d20Label.grid(column = 1, row = 0, sticky = tk.W)
        self.d12Label = ttk.Label(self.box, text = "-", width = 3)
        self.d12Label.grid(column = 1, row = 1, sticky = tk.W)
        self.d100Label = ttk.Label(self.box, text = "-", width = 3)
        self.d100Label.grid(column = 3, row = 0, sticky = tk.W)
        self.d10Label = ttk.Label(self.box, text = "-", width = 3)
        self.d10Label.grid(column = 3, row = 1, sticky = tk.W)
        self.d8Label = ttk.Label(self.box, text = "-", width = 3)
        self.d8Label.grid(column = 5, row = 0, sticky = tk.W)
        self.d6Label = ttk.Label(self.box, text = "-", width = 3)
        self.d6Label.grid(column = 5, row = 1, sticky = tk.W)
        self.d4Label = ttk.Label(self.box, text = "-", width = 3)
        self.d4Label.grid(column = 7, row = 0, sticky = tk.W)

        def roll20():
            self.rollList.append(random.randint(1, 20))
            self.rollDieList.append(20)
            self.d20Label.config(text = str(self.rollList[-1]))
        def roll12():
            self.rollList.append(random.randint(1, 12))
            self.rollDieList.append(12)
            self.d12Label.config(text = str(self.rollList[-1]))
        def roll100():
            self.rollList.append(random.randint(1, 100))
            self.rollDieList.append(100)
            self.d100Label.config(text = str(self.rollList[-1]))
        def roll10():
            self.rollList.append(random.randint(1, 10))
            self.rollDieList.append(10)
            self.d10Label.config(text = str(self.rollList[-1]))
        def roll8():
            self.rollList.append(random.randint(1, 8))
            self.rollDieList.append(8)
            self.d8Label.config(text = str(self.rollList[-1]))
        def roll6():
            self.rollList.append(random.randint(1, 6))
            self.rollDieList.append(6)
            self.d6Label.config(text = str(self.rollList[-1]))
        def roll4():
            self.rollList.append(random.randint(1, 4))
            self.rollDieList.append(4)
            self.d4Label.config(text = str(self.rollList[-1]))

        self.d20Btn = ttk.Button(self.box, command = roll20, text = "d20", width = 4)
        self.d20Btn.grid(column = 0, row = 0)
        self.d12Btn = ttk.Button(self.box, command = roll12, text = "d12", width = 4)
        self.d12Btn.grid(column = 0, row = 1)
        self.d100Btn = ttk.Button(self.box, command = roll100, text = "d%", width = 4)
        self.d100Btn.grid(column = 2, row = 0)
        self.d10Btn = ttk.Button(self.box, command = roll10, text = "d10", width = 4)
        self.d10Btn.grid(column = 2, row = 1)
        self.d8Btn = ttk.Button(self.box, command = roll8, text = "d8", width = 4)
        self.d8Btn.grid(column = 4, row = 0)
        self.d6Btn = ttk.Button(self.box, command = roll6, text = "d6", width = 4)
        self.d6Btn.grid(column = 4, row = 1)
        self.d4Btn = ttk.Button(self.box, command = roll4, text = "d4", width = 4)
        self.d4Btn.grid(column = 6, row = 0)

        self.popBtn = ttk.Button(self.box, command = popOut, text = "Pop Out", width = 0)
        self.popBtn.grid(column = 6, row = 1, columnspan = 2)


    def __str__(self):
        return False

    def setPos(self, newColumn = 0, newRow = 0, newColumnspan = 1, newRowspan = 1, newSticky = ""):
        self.box.grid(column = newColumn, row = newRow, columnspan = newColumnspan, rowspan = newRowspan, sticky = newSticky)

"""This is a template class and does nothing. It exists solely to be a copy/past template so making a new module can go faster"""
class TEMPLATE(object):
    def __init__(self, newOuterBox, newPlayer):
        self.outerBox = newOuterBox
        self.player = newPlayer

        def edit_():
            return False

        self.box = ttk.Frame(self.outerBox)


    def __str__(self):
        return False

    def update(self):
        return False

    def setPos(self, newColumn = 0, newRow = 0, newColumnspan = 1, newRowspan = 1, newSticky = ""):
        self.box.grid(column = newColumn, row = newRow, columnspan = newColumnspan, rowspan = newRowspan, sticky = newSticky)
