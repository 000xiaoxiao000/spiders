import urllib.parse
import urllib.request
import socket

data=bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf-8')
try:
    response=urllib.request.urlopen('http://httpbin.org/post',data=data,timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('Time Out')