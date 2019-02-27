#request基本用法
# 实例引入
# import requests
# r=requests.get('http://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# #get请求
# import requests
# r=requests.get('http://httpbin.org/get')
# print(r.text)

# #返回str类型，json格式,通过json()方法获得字典类型
# import requests
# data={
#     'name':'qianfg',
#     'age':22
# }
# r=requests.get('http://httpbin.org/get',params=data)
# print(type(r.text))
# print(r.text)
# print(type(r.json()))
# print(r.json())

# #抓取网页
# import requests
# import re
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
# r=requests.get('http://www.zhihu.com/explore',headers=headers)
# pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)   #re.S表示“.”（不包含外侧双引号，下同）的作用扩展到整个字符串，包括“\n”
# titles=re.findall(pattern,r.text)
# print(titles)

# #抓取二进制数据,音频、视频也可采用这种方法获取
# import requests
# r=requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)
# with open('facicon.ico','wb') as f:
#     f.write(r.content)

# #POST请求
# import requests
# data={
#     'name':'qianfg',
#     'age':'22'
# }
# r=requests.post('http://httpbin.org/post',data=data)
# print(r.text)

#响应
import requests
headers={
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
 }
r=requests.get('http://www.jianshu.com',headers=headers)
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)
print(type(r.history),r.history)