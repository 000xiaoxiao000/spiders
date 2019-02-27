#解析链接
#1.urlparse()
# from urllib.parse import urlparse
# result=urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(result)
# print(result.scheme)
# print(result[0])
# print(result.netloc)
# print(result[1])

# from urllib.parse import urlparse
# result=urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https')
# print(result)

# from urllib.parse import urlparse
# result=urlparse('www.baidu.com/index.html#comment',scheme='https',allow_fragments=False)
# print(result)

# #2.urlunparse
# from urllib.parse import urlunparse
# data=('https','www.baidu.com','index','user','id=5','comment')   #可用列表、元组或其他数据结构,长度必须为6
# print(urlunparse(data))

#3.urlsplit
# from urllib.parse import urlsplit
# result=urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
# print(result)
# print(result.scheme)
# print(result[0])

# #4.urllibunsplit
# from urllib.parse import urlunsplit
# data=['http','www.baidu.com','index.html','id=5','comment']   #可用列表、元组或其他数据结构,长度必须为5
# result=urlunsplit(data)
# print(result)

# #5.urljoin 只要基础链接的scheme,netloc,path,若新链存在，则使用新链
# from urllib.parse import urljoin
# print(urljoin('http://www.baidu.com','index.html'))
# print(urljoin('http://www.baidu.com','http://www.qianfg123.cn/2.html'))
# print(urljoin('http://www.baidu.com/about.html','http://www.qianfg123.cn/2.html'))
# print(urljoin('http://www.baidu.com/about.html','http://www.qianfg123.cn/2.html?id=5'))
# print(urljoin('http://www.baidu.com?wd=5','http://www.qianfg123.cn/2.html'))
# print(urljoin('www.baidu.com','?id=5#comment'))
# print(urljoin('www.baidu.com#comment','?id=5'))

# #6.urlencode
# from urllib.parse import urlencode
# params={
#     'name':'qianfg',
#     'age':22
# }
# base_url='http://www.baidu.com?'
# url=base_url+urlencode(params)
# print(url)

# #7.parse_qs  反序列化，转为字典
# from urllib.parse import parse_qs
# url='name=qianfg&age=22'
# print(parse_qs(url))

# #8.parse_qsl 反序列化，转为元组组成的列表
# from urllib.parse import parse_qsl
# url='name=qianfg&age=22'
# print(parse_qsl(url))

# #9.quote 把内容转化为URL编码格式
# from urllib.parse import quote
# keyword='壁纸'
# url='http://www.baidu.com?wd='+quote(keyword)
# print(url)
#
# #10.unquote
# from urllib.parse import unquote
# url='http://www.baidu.com?wd=%E5%A3%81%E7%BA%B8'
# print(unquote(url))

