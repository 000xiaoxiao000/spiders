import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import pymongo


def get_page(page):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.3'
    headers = {'User-Agent': user_agent}
    base_url = 'https://m.weibo.cn/api/container/getIndex?'
    params = {
        'containerid': '102803',
        'openApp': '0',
        'page': page
    }
    url = base_url + urlencode(params)
    response = requests.get(url=url, headers=headers)
    if response.status_code is 200:
        return response.json()
    return None


def parse_page(json):
    items = json.get('data').get('cards')
    for item in items:
        item = item.get('mblog')
        weibo = {}
        try:
            weibo['who'] = item.get('user').get('screen_name')
            weibo['text'] = pq(item.get('text')).text()
            weibo['imageurl'] = item.get('page_info').get('page_pic').get('url')
            weibo['pagetitle'] = item.get('page_info').get('page_title')
            weibo['reposts'] = item.get('reposts_count')
            weibo['comments'] = item.get('comments_count')
            weibo['attitudes'] = item.get('attitudes_count')
            save_to_mongodb(weibo)
        except:
            print('ignore')


def save_to_mongodb(weibo):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client['weibo']
    collection = db['video']
    if collection.insert(weibo):
        print('Saved successfully')


if __name__ == '__main__':
    MAX_PAGE = 100
    for page in range(1, MAX_PAGE + 1):
        json = get_page(page)
        parse_page(json)
