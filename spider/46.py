html='''
<div class='wrap'>
<div id='container'>
<ul class='list'>
<li class='item-0'><a href='link1.html'>first item</a></li>
<li class='item-1'><a href='link2.html'>second item</a></li>
<li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
<li class='item-1 active'><a href='link4.html'>forth item</a></li>
<li class='item-0'><a href='link5.html'>fifth item</a>
</ul>
</div>
'''

from pyquery import PyQuery as pq
#字符串初始化
#doc=pq(html)
#print(doc('li'))
#url初始化
# doc=pq(url='http://cuiqingcai.com')
#print(doc('title'))
import requests

#doc=pq(requests.get('http://cuiqingcai.com').text)
#print(doc('title'))
#文件初始化
#doc=pq(filename='test.html')
#print(doc('li'))

doc=pq(html)
#print(doc('#container .list li'))
#print(type(doc('#container .list li')))
#查找子节点
items=doc('.list')
#print(type(items))
#print(items)
#lis=items.find('li')
#print(type(lis))
#print(lis)
#子节点
#lis=items.children('.item-0')
#print(lis)
#父节点
#container=items.parent()
#print(type(container))
#print(container)
#祖先节点
#parents=items.parents('.wrap')
#print(type(parents))
#print(parents)

#兄弟节点
#li=doc('.item-0.active')
#print(li)
#print(str(li))

#lis=doc('li').items()
#print(type(lis))
#for li in lis:
#    print(li)

#获取信息
#a=doc('.item-0.active a')
#a=doc('a') #只返回第一个节点属性
#print(a,type(a))
#print(a.attr['href'])
#print(a.attr.href)

#a=doc('a')
#for item in a.items():
#    print(item.attr.href)

'''
a=doc('li')
print(a.html())
print(a.text())
print(type(a.text()))

print(type(a))
for li in a.items():
    print(li.html())
'''

#节点操作
li=doc('.item-0.active')
print(li)
li.remove_class('active')
print(li)
li.add_class('pipixia')
print(li)
#改变属性
li.attr('name','qianfg')
print(li)
li.text('change item') #节点内部文本全都替换
print(li)
li.html('<span>hahaha</span>')
print(li)



