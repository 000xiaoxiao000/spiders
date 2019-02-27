from lxml import etree

text='''
<div>
<ul>
<li class='item-0'><a href='link1.html'>first item</a></li>
<li class='item-1'><a href='link2.html'>second item</a></li>
<li class='item-inactive'><a href='link3.html'>first item</a></li>
<li class='item-1'><a href='link4.html'>forth item</a></li>
<li class='item-0'><a href='link5.html'>fifth item</a>
</ul>
</div>
'''
html=etree.HTML(text)
result=etree.tostring(html)
print(result.decode('utf8'))
with open('./test.html','w') as f:
    f.write('''<div>
<ul>
<li class='item-0'><a href='link1.html'>first item</a></li>
<li class='item-1'><a href='link2.html'>second item</a></li>
<li class='item-inactive'><a href='link3.html'>first item</a></li>
<li class='item-1'><a href='link4.html'>forth item</a></li>
<li class='item-0'><a href='link5.html'>fifth item</a>
</ul>
</div>''')