import pytesseract as ocr
from PIL import Image
import PIL
import pytesseract

print(pytesseract.image_to_string('/Users/luizandre/Downloads/teste.jpg'))