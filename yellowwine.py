import requests
from urllib.parse import urlencode
import os
base_url='https://www.toutiao.com/search_content/?'
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
def get_page(page):
    params={
        "offset":page,
        "format": "json",
        "keyword": "黄酒",
        "autoload": "true",
        "count": "20",
        "cur_tab": "1",
        "from": "search_tab"
    }
    url=base_url+urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error:',e.args)


def parse_data(json):
    items=json.get('data')
    for item in items:
        item=item.get('image_url')
        if item:
            url='http:'+item
            yield url
def main():
    k=0
    for i in range(0,100,20):
        json=get_page(i)
        for url in parse_data(json):
            k+=1
            response=requests.get(url,headers=headers)
            if response.status_code==200:
                with open(str(k)+'.jpg','wb') as f:
                    f.write(response.content)
if __name__=='__main__':
    main()
