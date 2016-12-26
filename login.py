import requests
r = requests.get('http://www.csdn.net/')
s = r.text
fo = open("foo.txt", "wb")
fo.write(r.content);
# 关闭打开的文件
fo.close()
