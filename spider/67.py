import requests
from urllib.parse import urlencode

headers={
    "Referer":"https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
}
headers2={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
def get_page(offset):
    params={
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'cur_tab':'1',
        'from':'search_tab'
    }

    url='https://www.toutiao.com/search_content/?'+urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_imags(json):
    if json.get('data'):
        for item in json.get('data'):
            title=item.get('title')
            images=item.get('image_list')
            try:
                for image in images:
                    yield{
                        'image':image.get('url'),
                        'title':title
                    }
            except TypeError:
                print('NoneType')

import os
from hashlib import md5

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response=requests.get('http:'+item.get('image'),headers=headers2)
        if response.status_code==200:
            file_path='{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            #print(file_path)
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded',file_path)
    except requests.ConnectionError:
        print('Failed to save image')

from multiprocessing.pool import Pool

def main(offset):
    json=get_page(offset)
    for item in get_imags(json):
        print(item)
        save_image(item)



GROUP_START=1
GROUP_END=3

if __name__=='__main__':
    pool=Pool()
    groups=([x*20 for x in range(GROUP_START,GROUP_END+1)])
    pool.map(main,groups)
    pool.close()
    pool.join()
