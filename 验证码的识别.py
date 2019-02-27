#获取cnki验证码图片
# import requests
# url='http://my.cnki.net/elibregister/CheckCode.aspx'
# response=requests.get(url)
# with open('code.jpg','wb') as f:
#     f.write(response.content)

#图形验证码的识别
#识别测试
# import pytesseract
# from PIL import Image
# image=Image.open('验证码.jpg')
# result=pytesseract.image_to_string(image)
# print(result)

#校准
# import pytesseract
# from PIL import Image
# image=Image.open('验证码.jpg')
# image=image.convert('L')    #转为灰度图片
# image.show()
# image=image.convert('1')    #二值化处理
# image.show()

#先转为灰度，在指定二值化阈值
import pytesseract
from PIL import Image
image=Image.open('code.jpg')
# image.show()
image=image.convert('L')
# image.show()
threshold=127
table=[]
for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)
# print(table)
image=image.point(table,'1')
# image.show()
result=pytesseract.image_to_string(image)
print(result)

# import pytesseract
# from PIL import Image
# image=Image.open('code.jpg')
# image=image.convert('L')
# threshold=60
# table=[]
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# image=image.point(table,'1')
# result=pytesseract.image_to_string(image)
# print(result)


#极验滑动验证码的识别
# http://jxgl.hainu.edu.cn/