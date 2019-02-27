import requests

proxies={
    'http':'http://122.152.235.129:3128',
    'https':'http://122.152.235.129:3128'
}

r=requests.get('https://www.taobao.com',proxies=proxies)
print(r.status_code)