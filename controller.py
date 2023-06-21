import cv2 as cv2
from core import net, screenCapture, compressor
import pyautogui as pg
from random import randint
from threading import Thread
import time
import controllerGui as gui

port = 23000
sk = net.sock(port)
rem = None


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
        except (AttributeError, ConnectionRefusedError):
            continue

img = None
renderRun = True


fx, fy = 0, 0
lDown, rDown = False, False

def onMouse(event, x, y, flags, param):

    global fx,fy, lDown, rDown
    w, h = cv2.getWindowImageRect("Live")[2:]
    fx, fy = x, y

    lDown = (event == cv2.EVENT_LBUTTONDOWN)
    rDown = (event == cv2.EVENT_RBUTTONDOWN)


def render():
    global renderRun
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live", 720, 480)    
    cv2.setMouseCallback('Live',onMouse)


    while True:
        cv2.waitKey(1)
        if img is None:
            continue
        try:
            if cv2.imshow("Live", img) == ord('q'):
                break
        except:
            pass
    cv2.destroyWindow("Live")

# Create a black image, a window and bind the function to window

def decodeStrm(index):
    global img, rem
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


def sendInputs():
    global rem, fx, fy
    while(renderRun):
        rem.sendJ("{} {}".format(fx, fy))
        if lDown:
            rem.sendJ("left down")
        else:
            rem.sendJ("left up")
        
        if rDown:
            rem.sendJ("right down")
        else:
            rem.sendJ("right up")

        time.sleep(0.05)


def startStreaming():
    global renderRun
    renderRun = False
    
    time.sleep(0.5)
    sel = gui.host_listbox.curselection()[0]
    decodeThrd = Thread(target=lambda : decodeStrm(sel))
    renderRun = True
    decodeThrd.start()
    
    time.sleep(0.5)
    inputThrd = Thread(target=sendInputs)
    inputThrd.start()

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



