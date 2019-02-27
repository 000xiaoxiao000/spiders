import pytesseract
from PIL import Image

#灰度处理
image=Image.open('code.jpg')

image=image.convert('L')
threshold=130
table=[]
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image=image.point(table,'1')
result=pytesseract.image_to_string(image)
print(result)