import numpy as np
import cv2
from matplotlib import pyplot as plt

import numpy as np
import cv2

def fft_low_pass_filter(img):
    # do dft saving as complex output
    dft = np.fft.fft2(img, axes=(0,1))

    # apply shift of origin to center of image
    dft_shift = np.fft.fftshift(dft)

    # generate spectrum from magnitude image (for viewing only)
    mag = np.abs(dft_shift)
    spec = np.log(mag) / 20

    # create circle mask
    radius = 32
    mask = np.zeros_like(img)
    cy = mask.shape[0] // 2
    cx = mask.shape[1] // 2
    cv2.circle(mask, (cx,cy), radius, (255,255,255), -1)[0]

    # apply mask to dft_shift
    dft_shift_masked = np.multiply(dft_shift,mask) / 255



    # shift origin from center to upper left corner
    back_ishift_masked = np.fft.ifftshift(dft_shift_masked)


    # do idft saving as complex output
    img_filtered = np.fft.ifft2(back_ishift_masked, axes=(0,1))

    # combine complex real and imaginary components to form (the magnitude for) the original image again
    img_filtered = np.abs(img_filtered).clip(0,255).astype(np.uint8)

    # cv2.normalize(img_back, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    return img_filtered

