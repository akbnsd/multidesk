from core import screenCapture,compressor
import cv2
import numpy as np 
import pyautogui as pg
from time import sleep

cv2.namedWindow("test", cv2.WINDOW_NORMAL)
cv2.resizeWindow("test", 720, 480)
dev = screenCapture.capture()
dev.setFps(30)
dev.beginCapture()

while True:
    frm = compressor.ImageCompressor.inflate(dev.frmQue.get())
    cv2.imshow("test", frm)
    if cv2.waitKey(20) == ord('q'):
        pass


    
