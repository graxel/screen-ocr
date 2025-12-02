import pytesseract
from utils import preprocess_for_ocr

class OCREngine:
    def __init__(self):
        pass

    def extract_text(self, image):
        """
        Extracts text from the given image using Tesseract.
        """
        if image is None or image.size == 0:
            return ""
        
        # Preprocess
        processed_img = preprocess_for_ocr(image)
        
        # Run Tesseract
        # config='--psm 6' assumes a single uniform block of text, good for ROIs
        text = pytesseract.image_to_string(processed_img, config='--psm 6')
        return text.strip()
