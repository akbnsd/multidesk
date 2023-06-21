import numpy as np
import cv2 as cv2
from core import net, screenCapture
import pyautogui as pg
from random import randint
from threading import Thread
import time
import queue
import pickle
import re

broadcastAddress = ("255.255.255.255", 23000)
remAddr = ()


class message:
    def __init__(self):
        self.cmd = int()
        


broadcastMsg = "hello"

sk = net.sock(randint(10000, 65000))

# broadcast section
broadcast = True
brIntr = 5
def sendBroadcasts():
    while(broadcast):
        sk.send(broadcastMsg, broadcastAddress)
        time.sleep(brIntr)


controller = int()
def listenCont():
    global controller
    global broadcast
    
    controller = sk.accept()
    broadcast = False


dev = screenCapture.capture()
dev.setFps(40)


def recvInput():
    global broadcast
    while not broadcast:
        data = controller.recvJ()
        if data is None:
            continue
        if data == "left down":
            pg.mouseDown(button="left")
        elif data == "left up":
            pg.mouseUp(button='left')
        elif data == "right down":
            pg.mouseDown(button='right')
        elif data == "right up":
            pg.mouseDown(button='right')
        else:
            try:
                pos = re.findall('[\d.]*', data)
                pg.moveTo(int(pos[0]),int(pos[2]))
            except ValueError:
                continue

if __name__ == "__main__":
    
    sk.listen()

    while True:
        broadcast = True
        broadcastThread = Thread(target=sendBroadcasts)
        broadcastThread.start()
        listenCont()
        
        dev.run = True
        dev.beginCapture()
        recvInputThrd = Thread(target=recvInput)
        recvInputThrd.start()
        
        while True:
            try:
                controller.sendJ(dev.frmQue.get())
                pass
            except (BrokenPipeError, ConnectionResetError):
                dev.run=False
                break
    



