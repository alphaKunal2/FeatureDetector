import cv2 as cv
import numpy as np
from copy import deepcopy


def Hough_Transform(img):

    # img = cv.imread(path)
    copy_img = deepcopy(img)
    gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges=cv.Canny(gray, 50, 150, apertureSize=3)
    lines=cv.HoughLines(edges, 1, np.pi/180, 120)

    for r_theta in lines:
        arr=np.array(r_theta[0], dtype=np.float64)
        r, theta=arr
        a=np.cos(theta)
        b=np.sin(theta)
        x0=a*r
        y0=b*r
        x1=int(x0 + 1000*(-b))
        y1=int(y0 + 1000*(a))
        x2=int(x0 - 1000*(-b))
        y2=int(y0 - 1000*(a))
        cv.line(copy_img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        
    return copy_img
