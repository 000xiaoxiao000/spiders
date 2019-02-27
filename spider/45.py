html='''
<div class='panel'>
<div class='panel-heading'>
<h4>Hello</h4>
</div>
<div class='panel-body'>
<ul class='list' id='list-1'>
<li class='element'>Foo</li>
<li class='element'>Bar</li>
<li class='element'>Jay</li>
</ul>
<ul class='list list-small' id='list-2'>
<li class='element'>Foo</li>
<li class='element'>Bar</li>
</ul>
</div>
</div>
'''
from bs4 import BeautifulSoup

soup=BeautifulSoup(html,'lxml')
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))
#嵌套
for ul in soup.select('ul'):
    print(ul.select('li'))
    print(ul['id'])
    print(ul.attrs['id'])
print('*'*80)
#获取文本三种方式
for li in soup.select('li'):
    print(li.get_text())
    print(li.string)
    print(li.text)