import urllib.parse
import urllib.request

data=bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf8')
response=urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read())