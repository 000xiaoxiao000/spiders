html='''
<div id='pipixia' class='wrap'>
    hello,world
<p>This is a paragraph</p>
</div>
'''
from pyquery import PyQuery as pq

doc=pq(html)
wrap=doc('.wrap')
print(wrap)
print(type(wrap))
wrap.find('p').remove()
print(wrap.text())