import cv2 as cv

from filters.hough import Hough_Transform
from filters.lbp import LBP_Kernel
from filters.discrete_cosine import discrete_cosine_transform

if __name__ == '__main__':
    path = r'C:\Users\Vanshaj\Desktop\Thapar data\Sem 5\Edge AI\Project\filters\car.jpg'
    LBP_img =LBP_Kernel(path)
    cv.imshow('LBP_Kernel.jpg', LBP_img)
    cv.waitKey(0)
    
    Hough_transformed_img = Hough_Transform(path)
    cv.imshow('Hough transformed.jpg', Hough_transformed_img)
    cv.waitKey(0)
    
    discrete_cosine_transformed_img = discrete_cosine_transform(path)
    cv.imshow('discrete cosine transformed.jpg', discrete_cosine_transformed_img)
    cv.waitKey(0)
    
    