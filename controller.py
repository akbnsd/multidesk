import numpy as np
import cv2 as cv2
from core import net, screenCapture, compressor
import pyautogui as pg
from random import randint
from threading import Thread
import time
import queue
import pickle
import controllerGui as gui

port = 23000

sk = net.sock(port)


addrs = list()

def discover():
    global remotes, addrs
    while True:
        try:
            data, addr = sk.recvFrom()
            if data != b"hello" or addr in addrs:
                continue
            
            addrs.append(addr)
            gui.host_listbox.insert(gui.tk.END, addr[0])
        except ConnectionRefusedError:
            continue

img = None
renderRun = True

def render():
    global renderRun
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live", 720, 480)
    while True:
        cv2.waitKey(20)
        if img is None:
            continue
        try:
            if cv2.imshow("Live", img) == ord('q'):
                break
        except:
            pass
    cv2.destroyWindow("Live")


def decodeStrm(index):
    global img
    time.sleep(0.5)
    if len(addrs) == 0:
        return        
    rem = sk.connect(addrs[index])
    rem.buffer = b""
    
    while renderRun:
        try:
            pkt = rem.recvJ(300000)
            if pkt is None:
                continue
            img = compressor.ImageCompressor.inflate(pkt)
            # cv2.imshow("Live", img)
        except:
            pass
    del rem

def startStreaming():
    global renderRun
    renderRun = False
    
    time.sleep(2)
    sel = gui.host_listbox.curselection()[0]
    decodeThrd = Thread(target=lambda : decodeStrm(sel))
    renderRun = True
    decodeThrd.start()

gui.openStreamingWindow = startStreaming



if __name__ == "__main__":
    
    GuiThrd = Thread(target=gui.renderGui)
    GuiThrd.start()
    
    discoverThrd = Thread(target=discover)
    discoverThrd.start()

    render()
    while True:
        time.sleep(2)
    # del sk



