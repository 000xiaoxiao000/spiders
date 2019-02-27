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

doc=pq(html)
#第一个节点
'''li=doc('li:first-child')
print(li)
#最后一个节点
li=doc('li:last-child')
print(li)
#第二个节点
li=doc('li:nth-child(2)')
print(li)'''
#
li=doc('li:gt(3)')
#print(li)
'''#偶数位置节点
li=doc('li:nth-child(2n)')
print(li)
#包含second文本的节点
li=doc('li:contains(second)')
print(li)'''

item=doc('#container .item-0')
print(item)