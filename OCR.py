from PIL import Image
import pytesseract

def tesseractReader(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(image)
    return text
    #print(text.replace(" ",""))

