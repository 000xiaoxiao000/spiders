#正则表达式
# #1.match
# import re
# content='Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result=re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
# print(result)
# print(result.group())
# print(result.span())

# #匹配目标
# import re
# content='Hello 1234567 World_This is a Regex Demo'
# result=re.match('^Hello\s(\d+)\sWorld',content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())

# #通用匹配
# import re
# content='Hello 1234567 World_This is a Regex Demo'
# result=re.match('^Hello.*Demo$',content)
# print(result)
# print(result.group())
# print(result.span())

# #贪婪与非贪婪
# import re
# content='Hello 1234567 World_This is a Regex Demo'
# result=re.match('^He.*(\d+).*Demo$',content)   #贪婪
# print(result.group(1))
# result=re.match('^He.*?(\d+).*Demo$',content)   #非贪婪
# print(result.group(1))

# #修饰符
# import re
# content='''Hello 1234567 World_This
# is a Regex Demo
# '''
# result=re.match('^He.*?(\d+).*Demo$',content,re.S)   #使.匹配包括换行在内的所有字符
# print(result.group(1))

'''
re.I        使匹配对大小写不敏感
re.L        做本地化识别匹配
re.M        多行匹配，影响^和$
re.S        使.匹配包括换行符在内的所有字符
re.U        根据Unicode字符集解析字符
re.X        该标志给予你更灵活的格式以便你将正则表达式写得更易于理解
'''

# #转义匹配
# import re
# content='(百度)www.baidu.com'
# result=re.match('\(百度\)www\.baidu\.com',content)
# print(result)

# #2.search  返回第一个匹配目标
# import re
# content='Extra stings Hello 1234567 World_This is a Regex Demo stings'
# result=re.search('Hello.*?(\d+).*?Demo',content)    #使用match无法匹配成功
# print(result)
# print(result.group())
# print(result.group(1))

html='''
<div id='songs-list'>
<h2 class='title'>经典老歌</h2>
<p class='introduction'>
经典老歌列表
</p>
<ul id='list' class='list-group'>
<li data-view='2'>一路有你</li>
<li data-view='7'>
<a href='/2.mp3' singer='任贤齐'>沧海一声笑</a>
</li>
<li data-view='4' class='active'>
<a href='/3.mp3' singer='齐秦'>往事随风</a>
</li>
<li data-view='6'><a href='/4.mp3' singer='beyond'>光辉岁月</a></li>
<li data-view='5'><a href='/5.mp3' singer='陈慧琳'>记事本</a></li>
<li data-view='5'>
<a href='/6.mp3' singer='邓丽君'>但愿人长久</a>
</li>
</ul>
</div>
'''
#import re
# result=re.search("li.*?active.*?singer='(.*?)'>(.*?)</a>",html,re.S)
# if result:
#     print(result.group(1),result.group(2))
# result=re.search("li.*?singer='(.*?)'>(.*?)</a>",html,re.S)   #不加active,返回第一个匹配目标
# if result:
#     print(result.group(1),result.group(2))

# #3.findall   返回所有匹配目标
# import re
# results=re.findall("li.*?href='(.*?)'\ssinger='(.*?)'>(.*?)</a>",html,re.S)
# print(results)
# print(type(results))
# for result in results:
#     print(result)

#4.sub   修改文本
# import re
# content='54aK54yr5oiR54ix5L2g'
# content=re.sub('\d+','',content)
# print(content)
# #获取歌名
# import re
# results=re.findall("<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>",html,re.S)
# print(results)
# for result in results:
#     print(result[1])
#
# import re
# html=re.sub('<a.*?>|</a>','',html)
# print(html)
# results=re.findall('<li.*?>(.*?)</li>',html,re.S)
# print(results)
# for result in results:
#     print(result.strip())

# #5.compile   将正则字符串编译成正则表达式对象
# import re
# content1='2016-12-15 12:00'
# content2='2017-6-15 13:00'
# content3='2018-8-16 11:00'
# pattern=re.compile('\d{2}:\d{2}')
# result1=re.sub(pattern,'',content1)
# result2=re.sub(pattern,'',content2)
# result3=re.sub(pattern,'',content3)
# print(result1,result2,result3)