import numpy as np
import cv2 as cv2
from core import net, screenCapture
import pyautogui as pg
from random import randint
from threading import Thread
import time
import queue
import pickle

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
dev.setFps(30)


if __name__ == "__main__":
    
    sk.listen()

    while True:
        broadcast = True
        broadcastThread = Thread(target=sendBroadcasts)
        broadcastThread.start()
        listenCont()
        
        dev.run = True
        dev.beginCapture()
        
        while True:
            try:
                controller.sendJ(dev.frmQue.get())
                pass
            except (BrokenPipeError, ConnectionResetError):
                dev.run=False
                break
    



