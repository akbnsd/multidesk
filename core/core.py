from tkinter import *

class core:
    
    # mouse status
    dx, dy, x, y = 0, 0, 0, 0
    win = int()

    def keyInput(key):
        print("pressed ", key)
        pass

    def mouseInput(cords):
        dx = cords.x - core.x
        dy = cords.y - core.y
        core.x, core.y = cords.x, cords.y

    def unlockInput(e):
        core.win.unbind('<KeyPress>')
        core.win.unbind('<Motion>')
