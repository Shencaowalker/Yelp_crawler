"""
type:AUTO
i:pizza
doctype:json
xmlVersion:1.8
keyfrom:fanyi.web
ue:UTF-8
action:FY_BY_CLICKBUTTON
typoResult:true
"""
#coding:utf-8

import urllib
import urllib2
import re
import json


headers={
	"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36"
	}
def get_data(words):  
    data = {}  
    data["type"] = "AUTO"  
    data["i"] = words  
    data["doctype"] = "json"  
    data["xmlVersion"] = "1.8"  
    data["keyfrom:fanyi"] = "web"  
    data["ue"] = "UTF-8"  
    data["action"] = "FY_BY_CLICKBUTTON"  
    data["typoResult"] = "true"  
    data = urllib.urlencode(data).encode('utf-8')  
    return data 

 
def url_open(url,data):
	req=urllib2.Request(url,headers=headers,data=data)
	response=urllib2.urlopen(req)
	commenthtml=response.read().decode('utf-8')
	print commenthtml



def get_data_html(html):
	'''	
	pattern=re.compile(r'class="translated_result">(.*?)<div>',re.S)
	items=re.search(pattern,html)
	print items
	'''
	result = json.loads(html)
	return result 

if __name__=="__main__":
	data=get_data(raw_input("enter:"))
	html=url_open("http://fanyi.youdao.com/",data)
	
	

