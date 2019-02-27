import requests

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
    AppleWebKit/536.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
r=requests.get('http://www.jianshu.com',headers=headers)
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)
print(type(r.history),r.history)