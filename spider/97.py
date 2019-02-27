#存储模块
MAX_SCORE=100
MIN_SCORE=0
INITIAL_SCORE=10
REDIS_HOST='localhost'
REDIS_PORT='6379'
REDIS_PASSWORD=None
REDIS_KEY='proxies'

import redis
from random import choice

class RedisClient(object):
    def __init__(self,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD):
        self.db=redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)

    def add(self,proxy,score=INITIAL_SCORE):
        if not self.db.zscore(REDIS_KEY,proxy):
            return self.db.zadd(REDIS_KEY,score,proxy)

    def random(self):
        result=self.db.zrangebyscore(REDIS_KEY,MAX_SCORE,MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result=self.db.zrevrange(REDIS_KEY,0,100)
            if len(result):
                return choice(result)
            else:
                raisr PoolEmptyError

    def decrease(self,proxy):
        score=self.db.zscore(REDIS_KEY,procy)
        if score and score > MIN_SCORE:
            print('代理',proxy,'当前分数',score,'减1')
            return self.db.zincrby(REDIS_KEY,proxy,-1)
        else:
            print('代理',proxy,'当前分数',score,'移除')
            return self.db.zrem(REDIS_KEY,proxy)

    def exists(self,proxy):
        return self.db.zscore(REDIS_KEY,proxy)==None

    def max(self,proxy):
        print('代理',proxy,'可用，设置为',MAX_SCORE)
        return self.db.zadd(REDIS_KEY,MAX_SCORE,proxy)

    def count(self):
        return self.db.zcard(REDIS_KEY)

    def all(self):
        return self.db.zrangebyscore(REDIS_KEY,MIN_SCORE,MAX_SCORE)

# 获取模块
import json
from .utils import get_page
from pyquery import PyQuery as pq

class ProxyMetaclass(type):
    def __new__(cls,name,basws,attrs):
        count=0
        attrs['__CrawFunc__']=[]
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count+=1
        attrs['__crawFunc__']=count
        return type.__new__(cls,name,bases,attrs)

class Crawler(object,metaclass=ProxyMetaclass):
    def get_proxies(self,callback):
        proxies=[]
        for proxy in eval('self.{}()'.format(callback)):
            print('成功获取到代理',proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self,page_count=4):
        start_url='http://www.66ip.cn/{}.html'
        urls=[start_url.format(page) for page in range(1,page_count+1)]
        for url in urls:
            print('Crawling',url)
            html=get_page(url)
            if html:
                doc=pq(html)
                trs=doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip=tr.find('td:nth-child(1)').text()
                    port=tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip,port])

    def crawl_proxy360(self):
        start_url='http://www.proxy360.cn/Region/China'
        print('Crawling',start_url)
        html=get_page(start_url)
        if html:
            doc=pq(html)
            lines=doc('div[name="list_proxy_ip"]').items()
            for line in lines:
                ip=line.find('.tbBottomLine:nth-child(1)').text()
                port=line.find('.tbBottomLine:nth-child(2)').text()
                yield ':'.join([ip,port])

    def crawl_goubanjia(self):
        start_url='http://www.goubanjia.com/free/gngn/index.shtml'
        html=get_page(start_url)
        if html:
            doc=pq(html)
            tds=doc('td.ip').items()
            for td in tds:
                td.find('p').remove()
                yield td.text().replace(' ','')
                
