html='''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class='story'>Once upon a time there were three little sisters;and their name were 
<a href='http://wxample.com/elsie' class='sister' id='link1'><span>Elsie</span></a>Hello
<a href='http://wxample.com/lacie' class='sister' id='link2'>Lacie</a>and
<a href='http://wxample.com/tillie' class='sister' id='link3'>Tillie</a>;
and they lived at the bottom of a well.</p>
<p class='story'>...</p>
'''

from bs4 import BeautifulSoup

'''soup=BeautifulSoup(html,'lxml')
#获取直接子节点
print(soup.p.contents)
#生成器类型
for i,child in enumerate(soup.p.children):
    print(i,child)
print('*'*80)
print(soup.p.descendants)
for i,child in enumerate(soup.p.descendants):
    print(i,child)
print('*'*80)
print(list(enumerate(soup.p.parents)))'''

from bs4 import BeautifulSoup

soup=BeautifulSoup(html,'lxml')
'''
print('Next Sibling',soup.a.next_sibling)
print('Prev Sibling',soup.a.previous_sibling)
print('Next Siblings',list(enumerate(soup.a.next_siblings)))
print('Prev Siblings',list(enumerate(soup.a.previous_siblings)))'''

print('Next Sibling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0]['class'])