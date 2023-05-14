from tkinter import Tk
import core as cr


def lockInput( window : Tk):
    cr.win = window
    cr.win.bind('<Escape>', cr.unlockInput)
    cr.win.bind('<KeyPress>', cr.keyInput)
    cr.win.bind('<Motion>', cr.mouseInput)
