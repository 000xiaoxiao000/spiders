import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq

base_url="https://www.zhihu.com/api/v4/search_v3?"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
def get_page(offset):
    params={
        't':'general',
        'q':'问题疫苗',
        'correction':'1',
        'offset':offset,
        'limit':'10',
        'search_hash_id':'b1b1474e3733596cd61d7d386577c746'
    }
    url=base_url+urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_data(json):
    if json.get('data'):
        for item in json.get('data'):
            try:
                title=item.get('highlight').get('title')
                Title=pq(title).text()
                html=item.get('object').get('content')
                content=pq(html).text()
                print(Title)
                print('*'*50)
                print(content)
                print('*'*100)
                with open('yimiao.txt','a',encoding='utf-8') as f:
                    f.write('\n\n\n'.join([Title,content]))
                    f.write('\n'+'='*80+'\n')
            except TypeError:
                return None

if __name__=="__main__":
    for offset in range(5,100,10):
        json=get_page(offset)
        get_data(json)







#browser=webdriver.Chrome()
#browser.get(url)
