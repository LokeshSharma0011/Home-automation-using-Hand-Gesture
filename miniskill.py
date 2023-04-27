from cvzone.SerialModule import SerialObject
from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
cap.set(10,150)
detector = HandDetector(detectionCon=0.8, maxHands=1)
arduino = SerialObject()

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        arduino.sendData(fingers[1:])
        print(fingers[1:])

    cv2.imshow("Image", img)
    cv2.waitKey(1)
   
