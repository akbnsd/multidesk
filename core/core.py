from tkinter import *
import mouse as ms

class core:
    
    # mouse status
    dx, dy, x, y = 0, 0, 0, 0
    win = int()

    def keyInput(key):
        print("pressed ", key)
        pass

    def mouseInput(cords):
        x, y = ms.get_position()
        dx = x - core.x
        dy = y - core.y
        core.x, core.y = x, y
        ms.move(-dx, -dy, absolute=False)

    def unlockInput(e):
        core.win.unbind('<KeyPress>')
        core.win.unbind('<Motion>')
        core.win.config(cursor='arrow')

