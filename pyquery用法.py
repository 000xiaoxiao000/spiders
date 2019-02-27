#pyquery
html='''
<div class='wrap'>
<div id='container'>
<ul class='list'>
<li class='item-0'><a href='link1.html'><span>first item</span></a></li>
<li class='item-1'><a href='link2.html'>second item</a></li>
<li class='item-inactive'><a href='link3.html'>first item</a></li>
<li class='item-1 active'><a href='link4.html'>forth item</a></li>
<li class='item-0'><a href='link5.html'>fifth item</a></li>
</ul>
</div>
</div>
'''
# #字符串初始化
# from pyquery import PyQuery as pq
# doc=pq(html)
# print(doc('li'))

# #url初始化
# from pyquery import PyQuery as pq
# doc=pq(url='http://www.qianfg123.cn')
# print(doc('title'))
#
# #文件初始化
# from pyquery import PyQuery as pq
# doc=pq(filename='test.html')
# print(doc('li'))

# #基本CSS选择器
# from pyquery import PyQuery as pq
# doc=pq(html)
# print(doc('#container .list li'))

#查找节点
# #查找子节点
# from pyquery import PyQuery as pq
# doc=pq(html)
# items=doc('.list')
# print(type(items))
# print(items)
# lis=items.find('li')    #find将所有符合条件的节点选择出来，查找所有的子孙节点
# print(type(lis))
# print(lis)
# lis=items.children('.item-inactive')
# print(lis)

# #父节点
# from pyquery import PyQuery as pq
# doc=pq(html)
# items=doc('.list')
# container=items.parent()
# print(type(container))
# print(container)

# #祖先节点
# from pyquery import PyQuery as pq
# doc=pq(html)
# items=doc('.list')
# parents=items.parents('.wrap')  #查找某个祖先节点
# print(type(parents))
# print(parents)

# #兄弟节点
# from pyquery import PyQuery as pq
# doc=pq(html)
# li=doc('.list .item-inactive')
# print(li.siblings())
# print(li.siblings('.item-1'))

# #遍历
# from pyquery import PyQuery as pq
# doc=pq(html)
# lis=doc('li').items()       #调用items(),变成生成器
# for li in lis:
#     print(li)

# #获取信息
# from pyquery import PyQuery as pq
# doc=pq(html)
# a=doc('.item-1.active a')
# print(a,type(a))
# print(a.attr('href'))
# print(a.attr.href)

# #attr只返回第一个节点属性
# from pyquery import PyQuery as pq
# doc=pq(html)
# a=doc('a')
# print(a)
# print(type(a))
# print(a.attr('href'))
# print(a.attr.href)
# for item in a.items():      #多个节点属性用遍历
#     print(item.attr('href'))

# #获取文本 text()纯文本  html()内部的HTML文本
# from pyquery import PyQuery as pq
# doc=pq(html)
# a=doc('.item-1.active')
# print(a)
# print(a.text())
# print(a.html())
# a=doc('li')
# print(a)
# print(a.text())     #返回所有节点纯文本
# print(a.html())     #返回第一个节点的HTML文本
# for i in a.items():
#     print(i.html())

#节点操作
# #addClass和removeClass
# from pyquery import PyQuery as pq
# doc=pq(html)
# li=doc('.item-1.active')
# print(li)
# li.removeClass('active')
# print(li)
# li.addClass('inactive')
# print(li)

# #attr,text,html
# text='''
# <ul class='list'>
# <li class='item-0 active'><a href='link3.html'><span class='bold'>third item</span></a></li>
# </ul>
# '''
# from pyquery import PyQuery as pq
# doc=pq(text)
# li=doc('.item-0.active')
# print(li)
# li.attr('name','pipixia')
# print(li)
# li.text('change item')
# print(li)
# li.html('<span>changed item</span>')
# print(li)

# #remove
# text='''
# <div class='wrap'>
#     Hello,World
# <p>This is a paragraph</p>
# </div>
# '''
# from pyquery import PyQuery as pq
# doc=pq(text)
# wrap=doc('.wrap')
# print(wrap.text())
# wrap.find('p').remove()
# print(wrap.text())
#
# #更多方法请咨询：http://pyquery.readthedocs.io/en/latest/api.html

# #CSS伪类选择器
# from pyquery import PyQuery as pq
# doc=pq(html)
# li=doc('li:first-child') #第一个li节点
# print(li)
# li=doc('li:last-child')     #最后一个节点
# print(li)
# li=doc('li:nth-child(2)')       #第2个节点
# print(li)
# li=doc('li:gt(2)')      #第3个节点后的所有li节点
# print(li)
# li=doc('li:nth-child(2n)')      #偶数位置节点，奇数位置2n-1
# print(li)

#CSS选择器参考：http://www.w3school.com.cn/css/index.asp

