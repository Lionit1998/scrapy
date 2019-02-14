from urllib import request,error
if __name__ == "__main__":
    req = request.Request("http://www.douyu.com/Gui_Cai.html")
    try:
        response = request.urlopen(req)
    except error.URLError as e:
        if hasattr (e,"code"):
            print('HTTPError,%s'%(e.code))
        elif hasattr (e,'reason'):
            print('URLError,%s'%(e.reason))
    
