from lxml import etree

text='''
<html><body><div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html"><span>second item</span></a></li>
<li class="item-inactive"><a href="link3.html">first item</a></li>
<li class="item-1"><a href="link4.html">forth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</li></ul>
</div>
</body></html>
'''
html=etree.HTML(text)
#获取所有节点
result=html.xpath('//*')
print(result)
#获取子节点
result=html.xpath('//li/a')
print(result)
#获取父节点
result=html.xpath('//a[@href="link3.html"]/../@class')
print(result)
#属性匹配
result=html.xpath('//li[@class="item-0"]')
print(result)
#文本获取
result=html.xpath('//li[@class="item-0"]//text()')
print(result)
result=html.xpath('//li[@class="item-0"]/a/text()')
print(result)
#属性获取
result=html.xpath('//li/a/@href')
print(result)
