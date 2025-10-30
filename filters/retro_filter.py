from skimage.io import imread
from skimage.util import img_as_float
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import numpy as np


def retro_filter(img, fade=0.3, warmth=0.2, vignette_strength=0.6, grain_strength=0.03):
    """
    Apply a retro / vintage photo effect to an image.

    Parameters:
        img : ndarray
            Input RGB image.
        fade : float
            Amount of desaturation and brightness fade (0–1).
        warmth : float
            Adds a yellow/orange tint (0–1).
        vignette_strength : float
            Darkness toward the edges (0–1).
        grain_strength : float
            Adds random film grain (0–0.1 typical).
    """
    img = img_as_float(img)
    h, w, _ = img.shape

    # Step 1: Fade colors (simulate old film)
    gray = rgb2gray(img)[..., np.newaxis]
    faded = img * (1 - fade) + gray * fade * 0.8

    # Step 2: Add warmth (yellow/orange tint)
    warm_matrix = np.array([1 + warmth * 0.6, 1, 1 - warmth * 0.4])  # (R,G,B) scaling
    warm = np.clip(faded * warm_matrix, 0, 1)

    # Step 3: Add vignette effect
    Y, X = np.ogrid[:h, :w]
    center_y, center_x = h / 2, w / 2
    distance = np.sqrt((X - center_x) ** 2 + (Y - center_y) ** 2)
    max_dist = np.sqrt(center_x**2 + center_y**2)
    vignette = 1 - vignette_strength * (distance / max_dist)
    vignette = np.clip(vignette, 0.4, 1)
    vignetted = warm * vignette[..., np.newaxis]

    # Step 4: Add film grain
    noise = np.random.normal(0, grain_strength, (h, w, 3))
    retro = np.clip(vignetted + noise, 0, 1)

    return retro
