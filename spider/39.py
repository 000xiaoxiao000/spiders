from lxml import etree

text='''
<html><body><div><li class="li li-first" name="item" age="20"><a href="link.html">first item</a></li>
<li class="item-0"><a href="link1.html">second item</a></li>
<li class="item-1"><a href="link2.html"><span>third item</span></a></li>
<li class="item-inactive"><a href="link3.html">forth item</a></li>
<li class="item-1"><a href="link4.html">fifth item</a></li>
<li class="item-0"><a href="link5.html">sixth item</a>
</li></div>
</body></html>
'''

html=etree.HTML(text)
result=etree.tostring(html)
print(result.decode('utf8'))
#属性多值、多属性匹配
result=html.xpath('//li[contains(@class,"li") and @name="item"]//text()')
print(result)
#按序选择
result=html.xpath('//li[2]//text()')
print(result)
result=html.xpath('//li[position()<4]//text()')
print(result)
result=html.xpath('//li[last()]//text()')
print(result)
result=html.xpath('//li[last()-4]//text()')
print(result)
result=html.xpath('//li[@age>18]//text()')
print(result)
#节点轴选择
print('*'*80)
result=html.xpath('//li[3]/ancestor::*')
print(result)
result=html.xpath('//li[3]/ancestor::div')
print(result)
result=html.xpath('//li[1]/attribute::*')
print(result)
result=html.xpath('//li[3]/child::a[@href="link2.html"]')
print(result)
result=html.xpath('//li[3]/following::*')
print(result)
