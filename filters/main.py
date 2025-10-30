from .discrete_cosine import discrete_cosine_transform
from .emboss_filter import emboss_filter
from .fftHPF import fft_high_pass_filter
from .fftLPF import fft_low_pass_filter
from .gabor import Gabor
from .gaussian_blur import gaussian_blur
from .hough import Hough_Transform
from .lbp import LBP_Kernel as local_binary_pattern
from .mosaic_tile_filter import mosaic_tile_filter
from .pencil_art import pencil_art_filter
from .retro_filter import retro_filter
from .watercolor_filter import watercolor_filter
import cv2


filter_mapping = {
    "discrete_cosine": discrete_cosine_transform,
    "emboss": emboss_filter,
    "fft_high_pass": fft_high_pass_filter,
    "fft_low_pass": fft_low_pass_filter,
    "gabor": Gabor,
    "gaussian_blur": gaussian_blur,
    "hough_transform": Hough_Transform,
    "local_binary_pattern": local_binary_pattern,
    "mosaic_tile": mosaic_tile_filter,
    "pencil_art": pencil_art_filter,
    "retro": retro_filter,
    "watercolor": watercolor_filter,
}


def apply_filter(filter_name, img_path):
    """
    Apply the given filter to the image at img_path.

    Args:
        filter_name (str): The name of the filter to apply.
        img_path (str): Path to the input image.

    Returns:
        numpy.ndarray: The filtered image.
    """
    if filter_name not in filter_mapping:
        raise ValueError(
            f"Filter '{filter_name}' not found. Available filters: {list(filter_mapping.keys())}"
        )

    filter_func = filter_mapping[filter_name]
    img = cv2.imread(img_path)

    if img is None:
        raise FileNotFoundError(f"Image not found at path: {img_path}")

    result = filter_func(img)
    return result
