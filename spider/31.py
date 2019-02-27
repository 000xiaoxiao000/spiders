import requests

data={'name':'qianfg','age':'22'}
files={'file':open('favicon.ico','rb')}
r=requests.post('http://httpbin.org/post',data=data,files=files)
print(r.text)