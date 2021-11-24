import cv2
import numpy as np

cap = cv2.VideoCaputre("summer.mp4")

while True:
    _, frame = cap.read()
    cv2.imshow = cap.read()

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyyAllWindows()