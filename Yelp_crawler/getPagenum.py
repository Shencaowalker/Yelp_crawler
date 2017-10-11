#coding:utf-8
import time
import urllib2
import re
import urllib

def getPagenum(url):

	request=urllib2.Request(url)
        response=urllib2.urlopen(request)
	html=response.read().decode('utf-8')
	pattern=re.compile(r'class="page-of-page.*?>.*?of (.*?)\s+<',re.S)
	num=re.search(pattern,html)
	return num.group(1)
	
if __name__=="__mian__":
	
	rawlink=raw_input('please enter the link:')
	Pagenum=getPagenum(rawlink)
	print Pagenum
