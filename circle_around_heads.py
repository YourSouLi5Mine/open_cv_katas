import numpy as np
import cv2

rhydon = cv2.imread('rhydon.jpg')
dragonite = cv2.imread('dragonite.jpg')
cv2.circle(rhydon, (62, 52), 50, (70, 87, 198), 5)
cv2.circle(dragonite, (60, 42), 38, (67, 106, 104), 5)
cv2.imshow("rhydon", rhydon)
cv2.imshow("dragonite", dragonite)
cv2.waitKey(0)
