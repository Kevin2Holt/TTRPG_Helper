"""
Author: Kevin Holt
Version: 0.2.15
Project: TTRPG Helper
File: Item

This file is not fully implemented and currently does nothing.
"""

class Item(object):
    def __init__(self, newName = "Item", newDesc = "Description"):

        self.name = newName
        self.desc = newDesc

    def __str__(self):
        return self.name + " | " + self.desc

    def editName(self, newName = "Item"):
        self.name = newName
    def editDesc(self, newDesc = "Description"):
        self.desc = newDesc

    def get(self):
        return (self.name, self.desc)

class Weapon(Item, object):
    def __init__(self, newName = "Item", newDmgMod = 0, newDmgDie = 4, newNumDie = 1, newHitMod = 0, newDesc = "Description"):
        super.__init__(newName, newDesc)
        self.dmgMod = newDmgMod
        self.dmgDie = newDmgDie
        self.numDie = newNumDie
        self.hitMod = newHitMod

    def editDmgMod(self, newDmgMod = 0):
        self.dmgMod = newDmgMod
    def editDmgDie(self, newDmgDie = 4):
        self.dmgDie = newDmgDie
    def editHitMod(self, newHitMod = 0):
        self.hitMod = newHitMod

    def get(self):
        return (self.name, "+" + str(self.dmgMod) if self.dmgMod >= 0 else str(self.dmgMod), str(self.numDie) + "d" + str(self.dmgDie), "+" + str(self.hitMod) if self.hitMod >= 0 else str(self.hitMod), self.desc)

class Armor(Item, object):
    def __init__(self, newName = "Item", newAC = 0, newDesc = "Description"):
        super.__init__(newName, newDesc)
        self.armorClass = newAC

    def editArmor(self, newAC = 0):
        self.armorClass = newAC

    def get(self):
        return (self.name, self.armor, self.desc)
