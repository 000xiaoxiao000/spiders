import requests
from requests.packages import urllib3

urllib3.disable_warnings()
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
    AppleWebKit/536.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
response=requests.get('https://www.12306.cn',verify=False)
print(response.status_code)