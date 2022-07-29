"""
Author: Kevin Holt
Version: 0.2.15
Project: TTRPG Helper
File: Root

Disclaimer:
    There are still many things that do not work quite as intended.
    Many features are planned, but have not been fully developed.
    A good example of this is seen below. The SpellsFrame is partialy developed, but not fully opperational yet.
    Thus, it is commented out. If you want to experiment with it, simply remove the comment on the two lines below.
    Just know, you have been warned that it does not work fully as intended and may break something.

    Beyond the SpellsFrame, there are still other features that don't work as intended.
    This mainly includes the updating of information across the entire program.

    I have included "ttrpg_spell.py" and "ttrpg_item.py" because I started implementing them
    and I don't want to go through and find all of the references that will break if I don't include them.

Things that are currently planned:
    > Saving/Loading characters
    > Spells & Items panels
    > Pop-out versions of each panel
        > Maybe pop-out for each module
    > Proficiencies
    > Character Creator

Things I am considering adding in the future:
    > Pre-generated races/classes that automatically give bonuses (according to the PHB)
"""
import tkinter as tk
from tkinter import ttk
from ttrpg_character import Character
from ttrpg_frames import *


"""Initialization of gui & base settings"""
window = tk.Tk()
window.resizable(True, True)
window.title("TTRPG Helper")

notebook = ttk.Notebook(window)
notebook.pack(expand = True)

player = Character()


"""Creating the frames to go into the notebook""" # *From ttrpg_frames.py
characterFrame = CharacterFrame(notebook, player)
statsFrame = StatsFrame(notebook, player)
toolsFrame = ToolsFrame(notebook, player)
#spellsFrame = SpellsFrame(notebook, player)

"""Adding frames to notebook"""
notebook.add(characterFrame.get(), text = "Character")
notebook.add(statsFrame.get(), text = "Stats")
notebook.add(toolsFrame.get(), text = "Tools")
#notebook.add(spellsFrame.get(), text = "Spells")

window.mainloop()
