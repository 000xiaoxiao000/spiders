import requests

data={'name':'qianfg',
      'age':22}
r=requests.get('http://httpbin.org/get',params=data)
print(type(r.text))
print(r.text)
print(r.json())
print(type(r.json()))