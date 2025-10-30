from skimage.io import imread
from skimage.color import rgb2gray
from skimage import img_as_float
from scipy.ndimage import gaussian_filter
import matplotlib.pylab as plt
import numpy as np
from skimage.util import img_as_ubyte
from sklearn.cluster import KMeans


def watercolor_filter(img, sigma_smooth=1.5, n_colors=16, edge_strength=0.8):
    """
    Create a watercolor effect from an image.

    Parameters:
        img : ndarray
            Input RGB image.
        sigma_smooth : float
            Gaussian blur amount for smoothing (higher = softer).
        n_colors : int
            Number of color clusters for quantization (controls posterization).
        edge_strength : float
            How visible the dark edges are (0–1).
    """
    # Convert image to float in [0, 1]
    img = img_as_float(img)

    # Step 1: Smooth the image to create a soft blending
    smoothed = gaussian_filter(img, sigma=(sigma_smooth, sigma_smooth, 0))

    # Step 2: Quantize colors (reduce palette for paint-like areas)
    pixels = smoothed.reshape(-1, 3)
    kmeans = KMeans(n_clusters=n_colors, random_state=42, n_init=5)
    labels = kmeans.fit_predict(pixels)
    new_colors = kmeans.cluster_centers_[labels]
    quantized = new_colors.reshape(smoothed.shape)

    # Step 3: Detect edges using grayscale difference
    gray = rgb2gray(img)
    edge = np.abs(gray - gaussian_filter(gray, sigma=1))
    edge = 1 - np.clip(edge * 5, 0, 1)  # invert for dark outlines

    # Step 4: Blend edges back into color image
    watercolor = quantized * edge[..., np.newaxis] ** edge_strength

    return watercolor
