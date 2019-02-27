from requests import Request,Session

url='http://httpbin.org/post'
data={'name':'qianfg','age':'22'}
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
    AppleWebKit/536.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
s=Session()
req=Request('POST',url,data=data,headers=headers)
prepped=s.prepare_request(req)
r=s.send(prepped)
print(r.text)