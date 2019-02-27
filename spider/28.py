import requests

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
    AppleWebKit/536.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
r=requests.get('https://wwww.baidu.com/explore',headers=headers)
print(r.text)
