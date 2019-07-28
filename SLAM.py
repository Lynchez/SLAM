import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


class Feature(object):

    def gft(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        corners = cv.goodFeaturesToTrack(gray, maxCorners=3000,qualityLevel=0.01,minDistance=10)
        corners = np.int0(corners)

        for i in corners:
            x, y = i.ravel()
            cv.circle(img, (x, y), 3, 255, 1)
        return img


cap = cv.VideoCapture('test.mp4')
fe = Feature()

while cap.isOpened():
    ret, frame = cap.read()

    result = fe.gft(frame)

    cv.imshow("last", result)

    key = cv.waitKey(10)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()
