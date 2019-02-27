from urllib import request
response=request.urlopen('http://www.python.org')
print(response.status)
print(response.getheaders())
print(response.getheader('Content-Type'))