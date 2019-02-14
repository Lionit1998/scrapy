from urllib import request
import chardet
import sys
import io
if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 
    response = request.urlopen("http://fanyi.baidu.com/")
    html = response.read()
    html = html.decode("utf-8")
    print(html)
