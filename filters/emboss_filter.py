from skimage.io import imread
from skimage.color import rgb2gray
from scipy.ndimage import convolve
import matplotlib.pylab as plt
import numpy as np


def emboss_filter(img):
    """
    Apply an emboss filter to a grayscale version of the input image.
    """
    im_gray = rgb2gray(img)

    # Emboss kernel (you can rotate it to change light direction)
    kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])

    # Apply convolution
    embossed = convolve(im_gray, kernel)

    # Normalize to displayable range [0, 1]
    embossed = (embossed - embossed.min()) / (embossed.max() - embossed.min())

    return embossed
