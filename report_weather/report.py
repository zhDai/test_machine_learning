# _*_ coding:utf-8 _*_
import sys, urllib, urllib2, json
import time
reload(sys)
sys.setdefaultencoding( "utf-8" )

url = 'http://apis.baidu.com/turing/turing/turing?key=879a6cb3afb84dbf4fc84a1df2ab7319&info=%E6%9F%A5%E5%A4%A9%E6%B0%94%E2%80%9C%E5%8C%97%E4%BA%AC%E4%BB%8A%E5%A4%A9%E5%A4%A9%E6%B0%94%E2%80%9D&userid=eb2edb736'


req = urllib2.Request(url)

req.add_header("apikey", "f844cbb01eda8efcd5ba4551a61be36d")

print req

resp = urllib2.urlopen(req)

content = resp.read()

data = json.loads(content)
if(data):
    for key,value in data.iteritems():
	if key == "text":
	    with open("report.txt","a") as f:
	        f.write(time.strftime('%Y-%m-%d %H:%M:%S')+": "+value+"\n")

