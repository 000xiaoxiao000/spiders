import pytesseract
from PIL import Image


image=Image.open('code.jpg')
image=image.convert('L')
image.show()
result=pytesseract.image_to_string(image)
print(result)

