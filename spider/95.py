import requests

proxy='127.0.0.1'
proxies={
    'http':'https://'+proxy,
    'https':'https://'+proxy
}
try:
    response=requests.get('http://httpbin.org/get',proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)