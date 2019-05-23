import numpy as np
import cv2
import random

canvas = np.zeros((500, 500, 3), dtype = "uint8")

for _ in range(10):
    x = random.randint(0, 499)
    y = random.randint(0, 499)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    canvas[x,y] = color
    radius = random.randint(3, 25)
    cv2.circle(canvas, (y, x), radius, color, 3)

cv2.imshow("Canvas", canvas)
cv2.imwrite('random_points.jpg', canvas)
cv2.waitKey(0)
