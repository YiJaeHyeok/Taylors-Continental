from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open('C:/Users/Jae/Desktop/Mongo/test/captured.png'))

print(text)
#print(text.replace(" ",""))