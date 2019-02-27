# 抓取首页
import requests
import re
import json
import time


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/536.36',
    }
    response = requests.get(url, headers=headers)
    if response.status_code is 200:
        return response.text
    return None


# 正则提取
def parse_one_page(html):
    pattern = re.compile('''<dd>.*?board-index.*?>(.*?)</i>.*?\
title="(.*?)".*?\
"star".*?>(.*?)</p>.*?\
"releasetime">(.*?)</p>.*?\
"integer">(.*?)</i>.*?\
"fraction">(.*?)</i>.*?</dd>
''', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'rank': item[0],
            'movie': item[1],
            'actor': item[2].strip()[3:],
            'time': item[3][5:],
            'score': item[4].strip() + item[5].strip()
        }


# 写入文件
def write_to_file(content):
    with open('movie.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(i * 10)
        time.sleep(1)
