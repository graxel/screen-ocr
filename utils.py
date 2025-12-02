import cv2
import numpy as np

def draw_roi(frame, roi, color=(0, 255, 0), thickness=2):
    """
    Draws the ROI rectangle on the frame.
    roi: tuple (x, y, w, h)
    """
    x, y, w, h = roi
    if w > 0 and h > 0:
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness)

def draw_cross(frame, point, color=(0, 0, 255), size=10, thickness=2):
    """
    Draws a cross at the specified point.
    point: tuple (x, y)
    """
    x, y = point
    cv2.line(frame, (x - size, y), (x + size, y), color, thickness)
    cv2.line(frame, (x, y - size), (x, y + size), color, thickness)

def crop_frame(frame, roi):
    """
    Crops the frame to the specified ROI.
    Returns None if ROI is invalid.
    """
    x, y, w, h = roi
    if w > 0 and h > 0:
        return frame[y:y+h, x:x+w]
    return None

def preprocess_for_ocr(image):
    """
    Preprocesses the image for OCR:
    - Grayscale
    - Thresholding (Otsu's binarization)
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Otsu's thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh
