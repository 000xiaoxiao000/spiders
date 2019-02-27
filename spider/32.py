import requests

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
    AppleWebKit/536.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Cookie':'d_c0="ADDlm2fexQ2PTjl33mZxmlNU8AqDw5gDRq4=|1529397047"; _zap=d69479ec-1aee-4b7f-a9b8-ee5be36bb8a1; _xsrf=DoekFn59T48aoAZWu0eV0mbXIiMIBnuU; capsion_ticket="2|1:0|10:1531901756|14:capsion_ticket|44:YzM0ZWNiMGM0ZTVmNGNiOWE0OThkZDI0MTE3ZDliYjk=|0c159d62c6478ad2d553931d2d3fc7c784b2ec4c9af0b3511f283cbc0b0d1f27"; z_c0="2|1:0|10:1531901817|4:z_c0|92:Mi4xWklQMUJnQUFBQUFBTU9XYlo5N0ZEU1lBQUFCZ0FsVk5lVVU4WEFEWk5KeVM3VGxJTUVTR1FkcHk5VmRraXhiS0h3|74faaa1b749193a81886b6d73156cb09edb921e2bc520b2582e81621e42672b7"; __utma=51854390.498695361.1531994911.1531994911.1531994911.1; __utmz=51854390.1531994911.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20171220=1^3=entry_date=20171220=1; q_c1=1fe4e8782e9f4262aef00ddb37a9f6ad|1532052958000|1529397047000; tgw_l7_route=c919f0a0115842464094a26115457122',
    'Host':'www.zhihu.com'
}
s=requests.Session()
response=s.get('http://www.zhihu.com',headers=headers)
print(response.text)
r=s.get('http://www.zhihu.com')
print(r.text)