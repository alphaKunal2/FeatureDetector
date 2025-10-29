from skimage.io import imread
from skimage.color import rgb2gray
from scipy.ndimage import gaussian_filter
import matplotlib.pylab as plt
import numpy as np

def pencil_art_filter(img, sigma_blur=5, blend_strength=0.8):
    """
    Convert an image into a pencil sketch effect.

    Parameters:
        img : ndarray
            Input RGB or grayscale image.
        sigma_blur : float
            Controls background smoothing (higher = smoother tone).
        blend_strength : float
            Controls how strong the pencil lines appear (0–1).
    """
    # Convert to grayscale
    im_gray = rgb2gray(img)

    # Invert the grayscale image
    inverted = 1 - im_gray

    # Apply Gaussian blur to the inverted image
    blurred = gaussian_filter(inverted, sigma=sigma_blur)

    # Dodge blend: simulate pencil strokes
    sketch = im_gray / (1 - blend_strength * blurred + 1e-5)
    sketch = np.clip(sketch, 0, 1)

    return im_gray, sketch
