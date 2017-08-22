# -*- coding: utf-8 -*-

import urllib2, json, urllib
import os
 
data = {}
data["appkey"] = os.getenv('HAPPY_APPKEY')
data["keyword"] = "扬州慢"
data["pagesize"] = 1
data["pagenum"] = 1
 
url_values = urllib.urlencode(data)
url = "http://api.jisuapi.com/songci/search" + "?" + url_values
request = urllib2.Request(url)
result = urllib2.urlopen(request)
jsonarr = json.loads(result.read())
 
if jsonarr["status"] != u"0":
    print jsonarr["msg"]
    exit()
result = jsonarr["result"]
 
print result["total"],result["pagesize"],result["pagenum"]
for val in result["list"]:
    print val["title"],val["type"],val["content"],val["explanation"],val["appreciation"],val["author"]
