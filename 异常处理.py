# # 处理异常
# # URLError
# from urllib import request,error
# try:
#     response=request.urlopen('http://www.qianfg123.cn/3.html')
#     print(response.read().decode('utf-8'))
# except error.URLError as e:
#     print(e.reason)

# # HTTPError
# from urllib import request,error
# try:
#     response=request.urlopen('http://www.qianfg123.cn/3.html')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers,sep='\n')

# from urllib import request,error
# try:
#     response=request.urlopen('http://www.qianfg123.cn/3.html')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers,sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')