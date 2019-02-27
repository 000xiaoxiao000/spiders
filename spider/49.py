import requests
from pyquery import PyQuery as pq

url='https://www.zhihu.com/explore'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
html=requests.get(url=url,headers=headers).text
doc=pq(html)
items=doc('.explore-tab .feed-item').items()
for item in items:
    question=item.find('h2').text()
    print(question)
    author=item.find('.author-link').text()
    print(author)
    answer=pq(item.find('.content').html()).text()
    print(answer)
    with open('explore.txt','a',encoding='utf-8') as f:
        f.write('\n'.join([question,author,answer]))
        f.write('\n'+'='*80+'\n')