import cv2 as cv
import pickle as p
import numpy as np

class ImageCompressor:

    def compress(data):
        comp = cv.imencode(".png", np.array(data))[1]
        return comp


    def inflate(bin):
        img = cv.imdecode(bin, cv.IMREAD_COLOR)
        return img

