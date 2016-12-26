# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
from StringIO import StringIO
import gzip
 
page = 1
url1 = 'http://www.qiushibaike.com/hot/page/' + str(page)
url2 = 'http://www.runoob.com'
url3 = 'http://www.oschina.net/'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

rule1 = '<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+ 'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>'
rule2 = "<span class=.detail.>.*? target=.*?>(.*?)<\/a>"
rule3 = '<div class="content">.*?<span>(.*?)<\/span>.*?<\/div>'
rule4 = "<li class='today'.*?>.*?target=.*?>(.*?)<\/a>"

string1 = '<li class="today">'

try:
    request = urllib2.Request(url3,headers = headers)
    request.add_header('accept-encoding', 'gzip')
    response = urllib2.urlopen(request)
    strBuf = StringIO(response.read())
    print type(response)
    gzf = gzip.GzipFile(fileobj=strBuf)
    content = gzf.read().decode('utf-8')
    pattern = re.compile(rule2,re.S)
    #print(re.search(string1, content))
    items = re.findall(pattern,content)

    for item in items:
        print item
        #haveImg = re.search("img",item[3])
        #if not haveImg:
        #    print item[0],item[1],item[2],item[4]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
