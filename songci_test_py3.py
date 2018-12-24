# -*- coding: utf-8 -*-

import urllib,json,os
import requests


data = {}
data["appkey"] = os.getenv('HAPPY_APPKEY')
data["keyword"] = "扬州慢"
data["pagesize"] = 1
data["pagenum"] = 1

url_values = urllib.urlencode(data)

url = "http://api.jisuapi.com/songci/search" + "?" + url_values
req = requests.get(url)
html = unicode(req.text).encode('utf-8')
print(html)

jsonarr = json.loads(html)
if jsonarr["status"] != u'0':
    print(jsonarr["status"])

result = jsonarr["result"]
print(result["total"],result["pagesize"],result["pagenum"])