html='''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class='title' name='dormouse'><b>The Dormouse's story</b></p>
<p class='story'>Once upon a time there were three little sisters;and their name were 
<a href='http://wxample.com/elsie' class='sister' id='link1'><!--Elsie--></a>,
<a href='http://wxample.com/lacie' class='sister' id='link2'>Lacie</a>and
<a href='http://wxample.com/tillie' class='sister' id='link3'>Tillie</a>;
and they lived at the bottom of a well.</p>
<p class='story'>...</p>
'''
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
#print(soup.prettify())
#print(soup.title.text)
'''print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.title.name)
print(soup.head)
print(soup.p)'''
#获取节点名称
print(soup.title.name)
#获取节点属性
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.p['class'])
#获取内容
print(soup.p.string)
#嵌套选择
print(soup.head.title)
print(type(soup.head))
print(type(soup.head.title))
print(soup.head.title.string)
