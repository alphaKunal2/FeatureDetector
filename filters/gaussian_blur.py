from skimage.io import imread
from skimage.color import rgb2gray
from scipy.ndimage import gaussian_filter
import matplotlib.pylab as plt


def gaussian_blur(img, sigma=2):
    """
    Apply Gaussian blur in the spatial domain.

    Parameters:
        img : ndarray
            Input RGB or grayscale image.
        sigma : float
            Standard deviation of the Gaussian kernel (controls blur amount).
    """
    im_gray = rgb2gray(img)
    blurred = gaussian_filter(im_gray, sigma=sigma)
    return blurred
