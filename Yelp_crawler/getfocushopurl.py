#coding:utf-8
import re
import Tkinter as tk
import urllib
import urllib2
import time
from db_forshop import *
import MySQLdb
baseurl='https://www.yelp.com'

#输入
class par:
	def __init__(self):
		self.city=''
		self.shopname=''#是店铺名或者是标签



#这个是确定输入的是不是只是shopname确定的店铺名或者是标签名
class loc:
	def __init__(self):
		self.name=''
		self.link=''
		self.star=''
		self.address=''
		self.title=''


def getPagenum(url):
	request=urllib2.Request(url)
        response=urllib2.urlopen(request)
	html=response.read().decode('utf-8')
	pattern=re.compile(r'class="page-of-page.*?>.*?of (.*?)\s+<',re.S)
	num=re.search(pattern,html)
	return num.group(1)
	



def getfocushopurl(strupar,num):
	securl=baseurl+'/search?find_desc='+strupar.shopname+'&find_loc='+strupar.city
	shoplists=[]
	
	for i in range(num):
		lists=[]
		endurl=securl+'&start='+str(i*10)
		print endurl
		request=urllib2.Request(endurl)
		response=urllib2.urlopen(request)
        	html=response.read().decode('utf-8')
		pattern=re.compile(r'class="indexed-biz-name">.*?href="(.*?)".*?<span >(.*?)</a>.*?rating-large" title="(.*?) star rating.*?price-category.*?category-str-list">(.*?)</span>.*?<address>(.*?)</address>',re.S)
		#pattern=re.compile(r'class="indexed-biz-name">.*?href="(.*?)".*?<span >(.*?)</a>.*?i-stars i-stars--regular-4 rating-large" title="(.*?) star rating.*?price-category.*?category-str-list">(.*?)</span>',re.S)		
		#pattern=re.compile(r'class="indexed-biz-name">.*?href="(.*?)".*?<span >(.*?)</a>.*?.*?price-category.*?category-str-list">(.*?)</span>',re.S)
        	shoplist=re.findall(pattern,html)
		for i in shoplist:
			pattern=re.compile(r'<a.*?>(.*?)</a>',re.S)
			titlelist=re.findall(pattern,i[3])
			shopname=re.sub(r'</span>','',re.sub(r'<span.*?>','',i[1]))
			addresses=re.sub(r'<br>',' ',i[4])
			'''
			print "3"
			print shopname,i[0]
			print "\n"
			if strupar.shopname in shopname or strupar.shopname in titlelist:
			'''
			a=loc()
			a.link=i[0]
			a.name=shopname
			a.star=i[2]
			a.address=addresses
			a.title=",".join(titlelist)			
			lists.append(a)
		shoplists.append(lists)
	return  shoplists

if __name__=="__main__":
	'''	
	a=par()
	a.shopname=raw_input('please enter the shopname or title:')
	a.city=raw_input('please enter the city:')
	#getfocushopurl(a)
	insertshopdb(getfocushopurl(a))
	#selectshopdb()
	selectshopdb()
	'''
	url=raw_input('please enter the shopname or title:')
	print int(getPagenum(url))+1
	
