from tkinter import Tk
from .core import core

def lockInput( window : Tk):
    core.win = window
    core.win.bind('<Escape>', core.unlockInput)
    core.win.bind('<KeyPress>', core.keyInput)
    core.win.bind('<Motion>', core.mouseInput)
    core.win.config(cursor="none")
