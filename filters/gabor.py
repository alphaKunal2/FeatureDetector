import numpy as np
import cv2
import os

# cv2.getGaborKernel(ksize, sigma, theta, lambda, gamma, psi, ktype)
# ksize - size of gabor filter (n, n)
# sigma - standard deviation of the gaussian function
# theta - orientation of the normal to the parallel stripes
# lambda - wavelength of the sunusoidal factor
# gamma - spatial aspect ratio
# psi - phase offset
# ktype - type and range of values that each pixel in the gabor kernel can hold

def Gabor(img):
    g_kernel = cv2.getGaborKernel((33, 33), 8.0, np.pi/4, 10.0, 0.5, 0, ktype=cv2.CV_32F) 
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filtered_img = cv2.filter2D(img, cv2.CV_8UC3, g_kernel)
    # h, w = g_kernel.shape[:2]
    # g_kernel = cv2.resize(g_kernel, (3*w, 3*h), interpolation=cv2.INTER_CUBIC)
    

    return filtered_img






