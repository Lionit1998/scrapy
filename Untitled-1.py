#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'scrapy'))
	print(os.getcwd())
except:
	pass
import urllib.request
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode('utf-8'))
#%%
import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
print(data)
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

#%%
import urllib.request
response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
print(response) 

#%%
import socket
import urllib.request
import urllib.error

try:
	response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
	if isinstance(e.reason,socket.timeout):
		print('timeout')

#%%
import urllib.request

response = urllib.request.urlopen('http://www.python.org')
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('server'))


#%%
import urllib.request
request = urllib.request.Request('http://www.python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

#%%
from urllib import request,parse

url = 'http://httpbin.org/post'
header = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
'Host': 'httpbin.org'}
dict = {'name':'zhaofan'}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req = request.Request(url=url,data=data,headers=header)
response = request.urlopen(req)
print(response.read().decode('utf-8')) 

#%%
from urllib import request,parse
url = 'http://httpbin.org/post'

dict = {'name':'Gremy'}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req = request.Request(url=url,data=data,method='POST')
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

#%%
import urllib.request

proxy_handler = urllib.request.ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://httpbin.org/get')
print(response.read())


#%%
import http.cookiejar,urllib.request
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
	print(item.name+"="+item.value)

#%%
import http.cookiejar, urllib.request
filename = "cookie.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

#%%
import http.cookiejar, urllib.request
cookie = http.cookiejar.MozillaCookieJar()
cookie.load("cookie.txt",ignore_discard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))


#%%
from urllib import request,error
try:
	response = request.urlopen("http://pythonsite.com/1111.html")
except error.URLError as e:
	print(e.reason)

#%%
from urllib import request,error
try:
	response = request.urlopen("http://pythonsite.com/1111.html")
except error.HTTPError as e:
	print(e.code)
	print(e.reason)
	print(e.headers)
except error.URLError as e:
	print(e.reason)
else:
	print('requset successfully')	


#%%
import socket
from urllib import request,error
try:
	response = request.urlopen("http://www.pythonsite.com/",timeout=0.001)
except error.URLError as e:
	if isinstance(e.reason,socket.timeout):
		print(e.reason)

#%%
from urllib.parse import urlparse

result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
print(result)


#%%
result = urlparse("www.baidu.com/index.html;user?id=5#comment",scheme='https')

#%%
print(result)

#%%
from urllib.parse import urlunparse
result = urlunparse(['http','www.baidu.com','index.html','user','a=123','commit']) 
print(result)

#%%
from urllib.parse import urljoin

print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://pythonsite.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://pythonsite.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))

#%%
from urllib.parse import urlencode
params = {"name":"zhaofan",
"age":"23"}
base_url = "http://www.baidu.com?"
print(base_url+urlencode(params))

#%%
import requests


#%%
response = requests.get("http://www.baidu.com")
print(type(response))
print(response.status_code)
print(response.text)
print(type(response.text))
print(response.cookies)
print(response.content)
print(response.content.decode('utf-8'))
#%%
response = requests.get("http://www.baidu.com")
response.encoding='utf-8'
print(response.text) 

#%%
import requests
response = requests.get("http://httpbin.org/get?name=zhaofan&age=23")
print(response.text)
#%%
import requests
data = {"name":"zhaofan",
		"age":"23"}
response = requests.get("http://httpbin.org/get",params=data)
print(response.url)
print(response.text)


#%%
import requests
import json

response = requests.get("http://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))



#%%
print(response.content.decode("utf-8"))


#%%
response = requests.get("http://www.zhihu.com")
print(response.text)
#%%
import requests
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
response = requests.get("http://www.zhihu.com",headers=header)
print(response.text)
print(response.content.decode('utf-8'))

#%%
data={"name":"zhaofan",
		"age":23}
response = requests.post("http://httpbin.org/post",data=data)
print(response.text)


#%%
import requests
response = requests.get("http://www.baidu.com")
if response.status_code == requests.codes.ok:
	print('访问成功')

#%%
files={"files":open("git.jpeg","rb")}
response = requests.post("http://httpbin.org/post",files=files)
print(response.text)

#%%
import requests
files= {"files":open("git.jpeg","rb")}
response = requests.post("http://httpbin.org/post",files=files)
print(response.text)

#%%
response = requests.get("http://www.baidu.com")
print(response.cookies)
for key,value in response.cookies.items():
	print(key+"="+value)

#%%
s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456")
response = s.get("http://httpbin.org/cookies")
print(response.text)

#%%
import requests

proxy = '127.0.0.1:1080'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
try:
    response = requests.get('http://www.youtube.com/', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)

#%%
import requests

from requests.exceptions import ReadTimeout,ConnectionError,RequestException


try:
    response = requests.get("http://httpbin.org/get",timeout=0.1)
    print(response.status_code)
except ReadTimeout:
    print("timeout")
except ConnectionError:
    print("connection Error")
except RequestException:
    print("error")



#%%
