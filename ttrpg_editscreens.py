import tkinter as tk
from tkinter import ttk
from ttrpg_character import Character

class EditWindow(object):

    def __init__(self, newPlayer, newTitle):
        self.editWindow = tk.Tk()
        self.editWindow.resizable(True, True)
        self.editWindow.title("TTRPG Helper | Edit " + newTitle)
        self.editWindow.mainloop()






    def close(self):
        self.editWindow.destroy()

class EditXP():
    def start(tempChar = Character(), xpBox = ttk.LabelFrame(), xpProgressBar = ttk.Progressbar()):
        editXPWindow = tk.Tk()
        editXPWindow.resizable(True, True)
        editXPWindow.title("TTRPG Helper | Edit XP")

        editCurXPLabel = ttk.Label(editXPWindow, text = "Current XP: ")
        editCurXPLabel.grid(column = 0, row = 0, sticky = tk.E)
        editCurXPEntry = ttk.Entry(editXPWindow)
        editCurXPEntry.insert(0, str(tempChar.exp))
        editCurXPEntry.grid(column = 1, row = 0)
        editXPToNextLabel = ttk.Label(editXPWindow, text = "XP To Next: ")
        editXPToNextLabel.grid(column = 0, row = 1, sticky = tk.E)
        editXPToNextEntry = ttk.Entry(editXPWindow)
        editXPToNextEntry.insert(0, str(tempChar.expToNext))
        editXPToNextEntry.grid(column = 1, row = 1)
        def stop():
            editXPWindow.destroy()
            xpBox.config(text = "XP: " + str(tempChar.exp) + "/" + str(tempChar.expToNext))
            xpProgressBar["value"] = (tempChar.exp / tempChar.expToNext) * 100
        def saveXP():
            tempChar.exp = int(editCurXPEntry.get())
            tempChar.expToNext = int(editXPToNextEntry.get())
            stop()
        editXPSave = ttk.Button(editXPWindow, text = "Save Changes", command = saveXP)
        editXPSave.grid(column = 0, row = 2, columnspan = 2)

class EditAbilityScores():
    def start(tempChar = Character()):
        editAbilityWindow = tk.Tk()
        editAbilityWindow.resizable(True, True)
        editAbilityWindow.title("TTRPG Helper | Edit Ability Scores")
