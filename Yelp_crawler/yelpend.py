#coding:utf-8
import re
import Tkinter as tk
import urllib
import urllib2
import time

baseurl='https://www.yelp.com/'
#最后在页面上显示的
class unit:
	def __init__(self):
		self.shopname=''
		self.title=''
		self.username=''
		self.comment=''
		self.star=''
		self.commenttime=''
#把得到应该在界面上显示的内容@profile
def getcomment(baseurl,shoplists):
        comments=[]
	for i in shoplists:
                comment=[]
		
		endurl=baseurl+i.link
		
		request=urllib2.Request(endurl)
        	response=urllib2.urlopen(request)
        	commenthtml=response.read().decode('utf-8')
		pattern=re.compile(r'class="user-name">.*?>(.*?)</a>.*?title="(.*?)star.*?rating-qualifier">(.*?)</span>.*?<p lang="en">(.*?)</p>',re.S)
		items=re.findall(pattern,commenthtml)
		
		for k in items:
			a=unit()
                	a.shopname=i.name
			for j in i.title:
				a.title=a.title+j+' '
			a.username=k[0]
			a.star=k[1]
			a.commenttime=k[2]
			pattern=re.compile(r'<a.*?>',re.S)
			a.comment=re.sub(r'<br>','\n',re.sub(r'</a>','',re.sub(pattern,'',k[3])))
			comment.append(a)
		comments.append(comment)
	return comments

			
		
		



#得到国家城市和城市链接的结构体
class link:
	def __init__(self):
		self.country=''
		self.city=''
		self.link=''

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
		self.title=[]


shoplists


#
#得到的是国家 城市 城市URL的列表
def getLinklist(url):
	endurl=url+'locations'
	request=urllib2.Request(endurl)
	response=urllib2.urlopen(request)
	
        cityAllhtml=response.read().decode('utf-8')
	natpattern=re.compile(r'class="state">.*?div>(.*?)</div>(.*?)</ul>',re.S)
	natitems=re.findall(natpattern,cityAllhtml)


	linklist=[]
	for i in natitems:
		citpattern=re.compile(r'<li>.*?"(.*?)">(.*?)</a>',re.S)
                cititems=re.findall(citpattern,i[1])
		for j in cititems:
			a=link()
			a.country=i[0]
			a.city=j[1]
			a.link=j[0]
			linklist.append(a)
	return linklist

	


#得到页面的总页数

def getPagenum(url):
	request=urllib2.Request(url)
        response=urllib2.urlopen(request)
	html=response.read().decode('utf-8')
	pattern=re.compile(r'class="page-of-page.*?>.*?of (.*?)\s+<',re.S)
	num=re.search(pattern,html)
	return num.group(1)


#得到最后全部URL的页面查找@profile
def getfocushopurl(strupar):
	securl=baseurl+'/search?find_desc='+strupar.shopname+'&find_loc='+strupar.city
	num=int(getPagenum(securl))
	print num	
	shoplists=[]
	for i in range(num):
		endurl=securl+'&start='+str(i*10)
		request=urllib2.Request(endurl)
		print '1'
		response=urllib2.urlopen(request)
		print '2'
        	html=response.read().decode('utf-8')
		print '3'
		pattern=re.compile(r'class="indexed-biz-name">.*?href="(.*?)".*?<span >(.*?)</a>.*?price-category.*?category-str-list">(.*?)</span>',re.S)		
		#pattern=re.compile(r'class="indexed-biz-name">.*?href="(.*?)".*?<span >(.*?)</a>.*?price-category.*?category-str-list">(.*?)</span>',re.S)
        	shoplist=re.findall(pattern,html)
		print '4'
		print shoplist
		print '\n'
		for i in shoplist:
			pattern=re.compile(r'<a.*?>(.*?)</a>',re.S)
			titlelist=re.findall(pattern,i[2])
			print titlelist
			print '\n'
			shopname=re.sub(r'</span>','',re.sub(r'<span.*?>','',i[1]))
			print shpname
			print '\n'
			if strupar.shopname in shopname or strupar.shopname in titlelist:
				a=loc()
				a.link=i[0]
				a.name=shopname
				for j in titlelist:
					a.title.append(j)
				shoplists.append(a)
	print  shoplists
	
			
		

def getfous(url,par):
	request=urllib2.Request(url)
	response=urllib2.urlopen(request)
	html=response.read().decode('utf-8')
	pattern=re.compile(par,re.S)
	items=re.findall(pattern,html)
	print items

	

	

a=par()
a.shopname=raw_input('please enter the shopname or title:')
a.city=raw_input('please enter the city:')
start = time.clock()
start1 = time.time()


getfocushopurl(a)

#comm=getcomment(baseurl,s)
#print comm
end = time.clock()
end1 = time.time()

print end1-start1
print end-start
'''
for i in comm:
	for j in i:
		print j.shopname,j.title,j.username,j.comment,j.star,j.commenttime
		raw_input('if you want continue? y or n:')
'''


