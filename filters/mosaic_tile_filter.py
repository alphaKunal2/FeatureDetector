from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import img_as_float
import matplotlib.pylab as plt
import numpy as np


def mosaic_tile_filter(img, tile_size=10, edge_thickness=1, edge_color=(0, 0, 0)):
    """
    Apply a mosaic tile (pixelation) effect to an image.

    Parameters:
        img : ndarray
            Input RGB image.
        tile_size : int
            Size of each mosaic tile in pixels.
        edge_thickness : int
            Thickness of tile borders (0 for none).
        edge_color : tuple
            RGB color of tile borders (0–1).
    """
    img = img_as_float(img)
    h, w, c = img.shape
    mosaic = np.zeros_like(img)

    # Step 1: Average colors in non-overlapping blocks
    for i in range(0, h, tile_size):
        for j in range(0, w, tile_size):
            block = img[i : i + tile_size, j : j + tile_size]
            color = block.mean(axis=(0, 1))
            mosaic[i : i + tile_size, j : j + tile_size] = color

    # Step 2: Add tile edges (optional)
    if edge_thickness > 0:
        mosaic_with_edges = mosaic.copy()
        for i in range(0, h, tile_size):
            mosaic_with_edges[i : i + edge_thickness, :] = edge_color
        for j in range(0, w, tile_size):
            mosaic_with_edges[:, j : j + edge_thickness] = edge_color
        mosaic = mosaic_with_edges

    return mosaic
