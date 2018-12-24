# -*- coding: utf-8 -*-

import urllib,json,os
import requests


data = {}
data["appkey"] = "75caeccc2dbc4f34"
data["keyword"] = "扬州慢"
data["pagesize"] = 1
data["pagenum"] = 1

url_values = urllib.parse.urlencode(data)

url = "http://api.jisuapi.com/songci/search" + "?" + url_values
req = requests.get(url)
html = req.text
print(html)

jsonarr = json.loads(html)
if jsonarr["status"] != '0':
    print(jsonarr["status"])

result = jsonarr["result"]
print(result["total"],result["pagesize"],result["pagenum"])

temp_text = result["list"][0]["title"] + "\n" + result["list"][0]["author"] + "\n" + result["list"][0]["content"]

block_chars = '⓪①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳❶❷❸❹❺❻❼❽❾❿⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇'
temp = ''
for c in temp_text:
    if not c in block_chars:
        temp += c

send_text = temp.replace('&nbsp;', ' ').replace('<br />', '\n')
print('\n')
print(send_text)