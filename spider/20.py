from urllib import request,error

try:
    response=request.urlopen('http://www.qianfg123.cn/1')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
except error.URLError as e:
    print(e.reason,e.code,e.headers,sep='\n')
else:
    print('Request Successfully')