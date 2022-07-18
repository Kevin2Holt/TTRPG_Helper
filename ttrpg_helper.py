from tkinter import *
import random
from ttrpg_character import Character

window = Tk()
window.geometry("300x50")

def roll(d = 20):
    return random.randint(1, d+1)
