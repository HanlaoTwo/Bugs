# -*- coding:utf-8 -*-
import requests
import re

header = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Language': 'en-US,en;q=0.5',
          'Accept-Encoding': 'gzip, deflate, br'
          }
html = requests.get('http://blog.csdn.net/boomhankers?viewmode=list',headers = header)
print('结果：',html.status_code)
print('原因：',html.reason)

rule1 = 'title="阅读次数">阅读<\/a>\((.*?)\)<\/span>'
rule2 = '<span class="link_title"><a href=".*?">(.*?)</a></span>'
patten1 = re.compile(rule1,re.S)
patten2 = re.compile(rule2,re.S)

tileArray = re.findall(patten2,html.text)
timeArray = re.findall(patten1,html.text)

i = 0
for tile in tileArray:
    print(tile+": "+timeArray[i])
    i = i+1
