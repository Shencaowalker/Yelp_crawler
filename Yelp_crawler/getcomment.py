#coding:utf-8
import re
import Tkinter as tk
import urllib
import urllib2
import time
import sys
from getfocushopurl import *
from db_forshop import *




reload(sys)
sys.setdefaultencoding('utf-8')

baseurl='https://www.yelp.com'
#最后在页面上显示的
class unit:
	def __init__(self):
		self.shopname=''
		self.username=''
		self.comment=''
		self.star=''
		self.commenttime=''





a=par()
a.shopname=raw_input('please enter the shopname or title:')
a.city=raw_input('please enter the city:')
ss=getfocushopurl(a)

insertshopdb(ss)




filename=open("comment.lw",'w')
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
			a.username=k[0]
			a.star=k[1]
			a.commenttime=k[2]
			pattern=re.compile(r'<a.*?>',re.S)
			a.comment=re.sub(r'<br>','\n',re.sub(r'</a>','',re.sub(pattern,'',k[3])))

			
			print a.shopname,a.username,a.star,a.commenttime,a.comment
			comment.append(a)
		comments.append(comment)
	return comments
'''
			filename.write(i.name)
			filename.write("\t")
			filename.write(k[0])
			filename.write("\t")
			filename.write(k[1])
			filename.write("\t")
			filename.write(k[2])
			filename.write("\t")
			filename.write(k[3])
			filename.write("\n")
		
'''		

insertshopuserdb(getcomment(baseurl,ss))
#filename.close()
#	selectshopdb()



