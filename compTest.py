from core import compressor as c
import pyautogui as pg
import cv2
import numpy as np


img = pg.screenshot()

cv2.namedWindow("test")

cv2.imencode(".png", np.array(img))
frm = c.ImageCompressor.compress(img)
imgD = c.ImageCompressor.inflate(frm)

cv2.imshow("test", np.array(imgD))

while True:
    if cv2.waitKey(10) == ord('q'):
        break
