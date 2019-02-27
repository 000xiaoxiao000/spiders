# urllib基本用法
# urlopen
# import urllib.request
#
# r=urllib.request.urlopen('http://www.python.org')
# print(r.read().decode('utf-8'))
# print(type(r))
# print(r.status)
# print(r.getheaders())
# print(r.getheader('Server'))

# data参数
# import urllib.parse
# import urllib.request
#
# data=bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf-8')
# r=urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(r.read())

#timeout参数
# import urllib.request
# import urllib.error
# import socket
# try:
#     r=urllib.request.urlopen('http://httpbin.org/get',timeout=1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')

# import urllib.request
# request=urllib.request.Request('http://www.python.org')
# response=urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# #Request
# from urllib import request,parse
# url='http://httpbin.org/post'
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
# dict={'name':'pipixia'}
# data=bytes(parse.urlencode(dict),encoding='utf-8')
# req=request.Request(url=url,data=data,headers=headers,method='POST')
# response=request.urlopen(req)
# print(response.read().decode('utf-8'))


