import requests

r=requests.get('http://www.baidu.com')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text.encode('utf-8'))
print(r.cookies)