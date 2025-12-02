import cv2
import numpy as np
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ocr_engine import OCREngine

def test_ocr_simple():
    # Create a white image
    img = np.ones((100, 300, 3), dtype=np.uint8) * 255
    
    # Put text on it
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'HELLO WORLD', (10, 60), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Run OCR
    ocr = OCREngine()
    text = ocr.extract_text(img)
    
    print(f"Expected: 'HELLO WORLD'")
    print(f"Got: '{text}'")
    
    if "HELLO" in text and "WORLD" in text:
        print("PASS")
    else:
        print("FAIL")

if __name__ == "__main__":
    test_ocr_simple()
