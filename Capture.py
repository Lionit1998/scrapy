import requests

request_header = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
'cache-control': 'max-age=0',
'cookie': 'q_c1=0de1541ad52b43b98ce15c7ce3f45b02|1550033502000|1550033502000; r_cap_id="NzVjNzQ5MDc4ZDY0NDJhZGIzZDk1YjhiMjEyNzNlY2Q=|1550033502|115027d791bc048ef1e858d5b99bb338ced002dc"; cap_id="MDUwNDIxNDM4ODkyNDE4Yzg2N2FmNWJjMmRmNDI3OGQ=|1550033502|95f05a069289f9d50edca4e9cbf28c8d58935bbb"; l_cap_id="NGQyY2I0YTA3MDljNGFkMGE3MGVlMGQ3YTY1OTRmMWE=|1550033502|f7d37e84f9207030a94f325015cfdf71a96c38a8"; d_c0="ANDgjj1g-Q6PTjYSWG_T1ttLBio2nJgwakY=|1550033504"; _zap=31537872-c307-4a5b-b2f4-ac6b59ca4122; _xsrf=Ce2qy2jim0Kep6HqncCmzkoZnZBuKdf6; capsion_ticket="2|1:0|10:1550059563|14:capsion_ticket|44:ZTFkNDZjMzZlYTEzNDhlMDg4OWM5N2ZmYWVhZjNmMDg=|59c446890676d36399f62a510379f9602c55dc2cdda83e45b1d10b20370e1780"; z_c0="2|1:0|10:1550059571|4:z_c0|92:Mi4xeGpkMUFnQUFBQUFBME9DT1BXRDVEaVlBQUFCZ0FsVk5NMVpSWFFCcF8yN1I3aTdmV0hTaEI2Nk9MOXNrWnpzSUJR|ca75f49a160c8c8c7116e61dfe8e0b241b5ae76b38ea9f222a096c86b902f9bd"; tst=r; __utma=51854390.858078679.1550033516.1550033516.1550109799.2; __utmc=51854390; __utmz=51854390.1550109799.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20160108=1^3=entry_date=20160108=1; tgw_l7_route=73af20938a97f63d9b695ad561c4c10c',
'referer': 'https://www.zhihu.com/search?type=people&q=vczh',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

url = 'https://www.zhihu.com/people/excited-vczh/activities'
z = requests.get(url,headers=request_header)
print (z.content)