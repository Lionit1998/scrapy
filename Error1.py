from urllib import request,error
if __name__ == "__main__":
    req = request.Request("http://www.douyu.com/Jack_Cui.html")
    try:
        response = request.urlopen(req)
    except error.URLError as e:
        print(e.reason) 
    except error.HTTPError as e :
        print(e.code) #try to add something adddada
        print(e.code) #try to add something  adadadad
