import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui
from pynput.mouse import Controller as MouseController

wCam, hCam = 640, 480
frameR = 20  
smoothening = 7

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

detector = htm.handDetector(maxHands=1)
mouse = MouseController()
wScr, hScr = pyautogui.size()
# print(wScr, hScr)

while True:
    # 1 - Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 2 - Tip of index and middle finger
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        
        # print(f"Webcam coordinates: x1={x1}, y1={y1}")

        # 3 - Check which fingers are up
        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        # 4 - Only index in moving
        if fingers[1] == 1 and fingers[2] == 0:
            # 5 - convert coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
            
            
            # print(f"Mapped coordinates: x3={x3}, y3={y3}")
            
            # 6 - smoothen the values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # 7 - move mouse
            mouse.position = (wScr - clocX, clocY)  # Move mouse
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # 8 - both index and middle up: clicking mode
        if fingers[1] == 1 and fingers[2] == 1:
            # 9 - find dist between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)

            # print(length)
            # 10 - click mouse if distance is short
            if length < 43:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 255), cv2.FILLED)
                pyautogui.click()

    # 11 - frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

    # 12 - display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
