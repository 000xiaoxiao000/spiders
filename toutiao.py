import os
import requests
import pymongo
from hashlib import md5
from urllib.parse import urlencode

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
headers = {'User-Agent': user_agent}

def get_url(offset):
    base_url = 'https://www.toutiao.com/search_content/?'
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '美女',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    url = base_url + urlencode(params)
    return url

def get_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code is 200:
            return response.json()
    except requests.ConnectionError:
        return None

def parse_page(json):
    if json:
        items = json.get('data')
        for item in items:
            title = item.get('title')
            if title:
                yield {
                    'title': title,
                    'image_url': item.get('large_image_url')
                }

def save_to_mongo(result):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client['picture']
    collection = db['mm']
    if collection.insert(result):
        print('Success to save to mongodb')

def download_image(result):
    title = result.get('title')
    image_url = result.get('image_url')
    if not os.path.exists(title):
        os.makedirs(title)
    try:
        response = requests.get(image_url, headers=headers)
        if response.status_code is 200:
            file_path = '{0}/{1}.{2}'.format(title, md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Download')
    except requests.ConnectionError:
        print('Failed to save image')

if __name__ == '__main__':
    for offset in range(0, 50, 20):
        url = get_url(offset)
        page = get_page(url)
        results = parse_page(page)
        for result in results:
            save_to_mongo(result)
            download_image(result)