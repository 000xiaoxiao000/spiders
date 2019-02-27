from urllib.parse import urlparse

result=urlparse('https://www.baidu.com/s?ie=utf-8&f=8&\
rsv_bp=1&rsv_idx=1&tn=99669880_hao_pg&wd=API&oq=api&rsv_\
pq=a34f4ec00000315b&rsv_t=5b6ci1jPHfo6oyqibFlpGRBTpGKEzti\
7dP9MUP36FBeaXI%2FB6c8bAOQWIP41wy4%2BCsBtg142&rqlang=cn&\
rsv_enter=\1&inputT=1764&rsv_sug3=60&rsv_sug1=55&rsv_sug7\
=100&rsv_sug2=0&rsv_sug4=1764#shabi',scheme='http',allow_fragments=False)
print(result)
print(result.path,result[2])