#节点测试
import time
import requests
from pyquery import PyQuery as pq
r=requests.get('http://search.cnki.net/down/default.aspx?filename=YYSB201702032&dbcode=CJFD&year=2017&dflag=pdfdown')
html=r.content
doc=pq(html)

'''items=doc('.main .wrap .login .btn').items()
for item in items:
    print(item)
    print(item.text())'''

item1=doc('#Button1')
item2=doc('#Button2')
print(item1)
time.sleep(2)
print('2')
print(item2)