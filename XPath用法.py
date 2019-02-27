#XPath
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
# html=etree.HTML(text)   #初始化
# result=etree.tostring(html)
# print(result.decode('utf-8'))   #bytes转为str

# #读取文本形式
# from lxml import etree
# html=etree.parse('test.html',etree.HTMLParser())
# result=etree.tostring(html)
# print(result.decode('utf-8'))

# #所有节点
# from lxml import etree
# html=etree.parse('test.html',etree.HTMLParser())
# result=html.xpath('//*')
# print(result)
#
# #子节点 所有li下的直接a子节点
# from lxml import etree
# html=etree.parse('test.html',etree.HTMLParser())
# result=html.xpath('//li/a')
# print(result)

# #父节点
# from lxml import etree
# html=etree.parse('test.html',etree.HTMLParser())
# result=html.xpath("//li/a[@href='link4.html']/../@class")
# print(result)

# # 文本获取
# from lxml import etree
# html=etree.parse('test.html',etree.HTMLParser())
# result=html.xpath("//li[@class='item-0']/a/text()")
# print(result)

# #属性获取
# from lxml import etree
# html=etree.parse('test.html',etree.HTMLParser())
# result=html.xpath("//li/a/@href")
# print(result)

# #属性多值匹配
# from lxml import etree
# text='''
# <li class='li li-first'><a href='link.html'>first item</a></li>
# '''
# html=etree.HTML(text)
# result=html.xpath("//li[contains(@class,'li')]//text()")  #属性多值，用contains
# print(result)

# #多属性匹配
# from lxml import etree
# text='''
# <li class='li li-first' name='item'><a href='link.html'>first item</a></li>
# '''
# html=etree.HTML(text)
# result=html.xpath("//li[contains(@class,'li') and @name='item']//text()")  #多属性，用and连接
# print(result)

# #按序选择
# from lxml import etree
# html=etree.parse('test.html',etree.HTMLParser())
# result=html.xpath("//li[1]/a/text()")
# print(result)
# result=html.xpath("//li[last()]/a/text()")
# print(result)
# result=html.xpath("//li[position()<3]//text()")
# print(result)
# result=html.xpath("//li[last()-1]//text()")
# print(result)

#节点轴选择
from lxml import etree
text='''
<div>
<ul>
<li class='item-0'><a href='link1.html'><span>first item</span></a></li>
<li class='item-1'><a href='link2.html'>second item</a></li>
<li class='item-inactive'><a href='link3.html'>first item</a></li>
<li class='item-1'><a href='link4.html'>forth item</a></li>
<li class='item-0'><a href='link5.html'>fifth item</a>
</ul>
</div>
'''
html=etree.HTML(text)
print(etree.tostring(html).decode('utf-8'))
result=html.xpath("//li[1]/ancestor::*")     #获取所有祖先节点
print(result)
result=html.xpath("//li[1]/ancestor::div")       #获取祖先节点的div节点
print(result)
result=html.xpath("//li[1]/attribute::*")     #获取所有属性
print(result)
result=html.xpath("//li/child::a[@href='link1.html']")       #获取href属性为'link1.html'的a节点
print(result)
result=html.xpath("//li[1]/descendant::span")        #获取所有子孙节点的span节点
print(result)
result=html.xpath("//li[1]/following::*")        #获取当前节点后的所有节点
print(result)
result=html.xpath("//li[1]/following-sibling::*")       #获取当前节点后的所有同级节点
print(result)

#更多资料请查询：http://www.w3school.com.cn/xpath/index.asp