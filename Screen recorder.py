import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

dim = (width, height)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("test.mp4", fourcc, 30.0, dim)
now = time.time()
dur = 10
end = now + dur

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    if time.time() > end:
        break

out.release()
print("Recording Completed")