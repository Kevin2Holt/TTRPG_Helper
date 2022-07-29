"""
Author: Kevin Holt
Version: 0.2.15
Project: TTRPG Helper
File: Spell

This file is not fully implemented and currently does nothing.
"""

class Spell(object):
    def __init__(self, newLevel = 0, newName = "Spell", newComponents = "", newShortDesc = "Short Description", newLongDesc = "Long Description"):
        self.level = newLevel
        self.name = newName
        self.components = newComponents
        self.shortDesc = newShortDesc
        self.longDesc = newLongDesc

    def __str__(self):
        return "Lvl." + str(self.level) + self.name + " | " + self.components + " | " + self.shortDesc

    def editName(self, newName = "Spell"):
        self.name = newName
    def editComponents(self, newComponents = ""):
        self.components = newComponents
    def editShortDesc(self, newShortDesc = "Short Description"):
        self.shortDesc = newShortDesc
    def editLongDesc(self, newLongDesc = "Long Description"):
        self.longDesc = newLongDesc
    def editLevel(self, newLevel = 0):
        self.level = newLevel

    def get(self):
        return (str(self.level), self.name, self.components, self.shortDesc, self.longDesc)
