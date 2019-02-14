from urllib import parse,request
import json
if __name__ == "__main__":
    req = request.Request("http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule")
    Form_Data = {}
    Form_Data['i'] = 'Jack'
    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = '15501402425799'
    Form_Data['sign'] = 'c2da10c6ef59319dd9a97bea37f1be88'
    Form_Data['ts'] = '1550140242579'
    Form_Data['bv'] = '363eb5a1de8cfbadd0cd78bd6bd43bee'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_REALTIME'
    Form_Data['typoResult'] = 'false'
    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(req,data)
    html = response.read().decode('utf-8')
    translate_result = json.loads(html)
    translate_result = translate_result["translateResult"][0][0]['tgt']
    print("翻译结果是 ：%s"%translate_result)   