import requests

data={'name':'qianfg','age':'22'}
r=requests.post('http://httpbin.org/post',data=data)
print(r.text)