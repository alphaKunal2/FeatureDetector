from scipy.fftpack import dct, idct
from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pylab as plt

# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')


def discrete_cosine_transform(img):
    
    # read lena RGB image and convert to grayscale
    im = rgb2gray(img) 
    imF = dct2(im)
    return imF