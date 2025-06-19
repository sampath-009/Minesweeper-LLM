import cv2
import numpy as np
from PIL import Image

def preprocess(pil_img):
    """
    Converts a PIL image to grayscale OpenCV format and applies denoising.
    """
    img = np.array(pil_img)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    return blur
