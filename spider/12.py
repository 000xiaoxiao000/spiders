from urllib import request,parse

url='http://httpbin.org/post'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
dict={'name':'wahaha'}
data=bytes(parse.urlencode(dict),encoding='utf-8')
req=request.Request(url=url,headers=headers,data=data)
response=request.urlopen(req)
print(response.read().decode('utf-8'))
