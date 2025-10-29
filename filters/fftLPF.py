import numpy as np
import cv2
from matplotlib import pyplot as plt

import numpy as np
import cv2

def fft_low_pass_filter(img):
    
    dft = np.fft.fft2(img, axes=(0,1))

    
    dft_shift = np.fft.fftshift(dft)

    
    mag = np.abs(dft_shift)
    spec = np.log(mag) / 20

    
    radius = 32
    mask = np.zeros_like(img)
    cy = mask.shape[0] // 2
    cx = mask.shape[1] // 2
    cv2.circle(mask, (cx,cy), radius, (255,255,255), -1)[0]

    
    dft_shift_masked = np.multiply(dft_shift,mask) / 255



    
    back_ishift_masked = np.fft.ifftshift(dft_shift_masked)


    
    img_filtered = np.fft.ifft2(back_ishift_masked, axes=(0,1))

    
    img_filtered = np.abs(img_filtered).clip(0,255).astype(np.uint8)

    

    return img_filtered




