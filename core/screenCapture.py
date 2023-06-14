import pyautogui as pg
import cv2
import numpy as np
from queue import Queue
from time import time,sleep
from . import compressor
from threading import Thread

class capture:
    def __init__(self):
        self.frmQue = Queue(20)
        self.timing = 500
        self.fpsTiming = 1 / 24
        self.run = True
        self.thrd = Thread()
        
    def setFps(self, fps : int):
        self.fpsTiming  = 1 / fps
    
    def staticCapture(self):
        prev = time()
        while self.run:
            delay = time() - prev
            if self.frmQue.qsize() < 20 and  delay > self.fpsTiming:
                prev = time()
                frame =   np.array(pg.screenshot())
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                data = compressor.ImageCompressor.compress(frame)
                self.frmQue.put(data)
                continue
            sleep(0.01)
            
    def beginCapture(self):
        self.thrd = Thread(target=self.staticCapture)
        self.thrd.start()
