import numpy as np
import cv2 as cv2
from core import net, screenCapture, compressor
import pyautogui as pg
from random import randint
from threading import Thread
import time
import queue
import pickle

port = 23000

sk = net.sock(port)
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 720, 480)

addrs = list()

def discover():
    global remotes, addrs
    while True:
        try:
            data, addr = sk.recvFrom()
            if data != b"hello" or addr in addrs:
                continue
            
            addrs.append(addr)
        except ConnectionRefusedError:
            continue

img = None
def render():
    while True:
        cv2.waitKey(20)
        if img is None:
            continue
        try:
            cv2.imshow("Live", img)
        except:
            pass


def decodeStrm(index):
    global img
    while True:
        time.sleep(0.5)
        if len(addrs) == 0:
            continue
        
        rem = sk.connect(addrs[index])
        
        while True:
            try:
                pkt = rem.recvJ(300000)
                if pkt is None:
                    continue
                img = compressor.ImageCompressor.inflate(pkt)
                # cv2.imshow("Live", img)
            except:
                pass

if __name__ == "__main__":
    
    discoverThrd = Thread(target=discover)
    discoverThrd.start()

    decodeThrd = Thread(target=lambda:decodeStrm(0))
    decodeThrd.start()
    
    render()
    del sk



