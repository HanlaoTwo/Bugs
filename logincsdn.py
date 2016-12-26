# -*- coding: utf-8 -*-
import requests
import time
import os
from bs4 import BeautifulSoup as bs
from http.cookiejar import LWPCookieJar
from io import StringIO
from io import BytesIO
import gzip


def toJson(str):
    '''
    提取lt流水号，将数据化为一个字典
    '''
    soup = bs(str,"html.parser")
    tt = {}
    for inp in soup.form.find_all('input'):
        if inp.get('name') != None:
            tt[inp.get('name')] =inp.get('value')
    return tt

# cookie setting
s = requests.Session()
s.cookies = LWPCookieJar('cookiejar')
header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}
if not os.path.exists('cookiejar'):
    print ("there is no cookie,setting")
    r = s.get("http://passport.csdn.net/account/login")
    soup = toJson(r.text)
    payload ={'username':'hankeboom@163.com','password':'hq1993','lt':soup["lt"],'execution':'e1s1','_eventId':'submit'}

    print (payload)
    r = s.post("http://passport.csdn.net/account/login",data=payload,headers=header)
    fo = open("loginlater.html", "wb")
    fo.write(r.content)
    fo.close()
    s.cookies.save(ignore_discard=True)
else:
    print ("cookie exists,restore")
    s.cookies.load(ignore_discard=True)

r = s.get("http://www.csdn.net/",headers=header)
fo = open("foo.html", "wb")
fo.write(r.content);
fo.close()