import os
import easyocr

reader = easyocr.Reader(['en'])

def ocr(input):
    text = reader.readtext(input)
    return text