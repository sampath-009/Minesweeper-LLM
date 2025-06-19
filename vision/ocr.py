
import pytesseract
import numpy as np
import cv2

def extract_grid_text(image):
    """
    Runs OCR on the preprocessed image and returns text.
    """
    config = "--psm 6 digits"
    text = pytesseract.image_to_string(image, config=config)
    return text
