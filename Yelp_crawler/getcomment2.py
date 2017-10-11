#coding:utf-8
import re
import Tkinter as tk
import urllib
import urllib2
import time
import sys
from getfocushopurl import *
from db_forshop import *
from city import *
import threading



#lock=threading.Lock()



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




getLinklist(cityurl)
while 1:
	enter=par()
	enter.shopname=raw_input('please enter the shopname or title:')
	enter.city=raw_input('please enter the city:')
	commenturl=baseurl+'/search?find_desc='+enter.shopname+'&find_loc='+enter.city
	num=getPagenum(commenturl)
	if num!=None:
		break
num=int(num)
if num >4:
	num=4

ss=getfocushopurl(enter,num)
for i in ss:
	insertshopdb(i)
selectshopdb()



#把得到应该在界面上显示的内容@profile
def getcomment(baseurl,shoplists,offset):
#	cur = conn.cursor()
#	sqli="insert ignore into shopcomment values(NULL,%s,%s,%s,%s,%s)"
	filename=open("huanchun"+str(offset)+".txt",'w')	
	for i in shoplists[offset]:
	
		endurl=baseurl+i.link
		
		request=urllib2.Request(endurl)
        	response=urllib2.urlopen(request)
        	commenthtml=response.read().decode('utf-8')
		pattern=re.compile(r'class="user-name">.*?>(.*?)</a>.*?title="(.*?)star.*?rating-qualifier">(.*?)</span>.*?<p lang="en">(.*?)</p>',re.S)
		items=re.findall(pattern,commenthtml)

		for k in items:			
			'''
			a=unit()
                	a.shopname=i.name
			a.username=k[0]
			a.star=k[1]
			a.commenttime=k[2]
			pattern=re.compile(r'<a.*?>',re.S)
			a.comment=re.sub(r'<br>','\n',re.sub(r'</a>','',re.sub(pattern,'',k[3])))

			
			cur.execute(sqli,(a.shopname.strip().encode("utf-8"),a.username.strip().encode("utf-8"),a.star.encode("utf-8"),a.commenttime.strip().encode("utf-8"),a.comment.strip().encode("utf-8")))
				
	
	cur.close()
	conn.commit()

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
	filename.close()
		
		



threads=[]
for i in range(num):
	thread=threading.Thread(target=getcomment,args=[baseurl,ss,i])
    	threads.append(thread)
    	thread.start()
	for thread in threads:
    		thread.join()	




'''
getcomment(baseurl,ss)
shopname=raw_input("Which shop do you want to see?\n")
selectshopnamecomment(shopname)
#filename.close()
#	selectshopdb()
'''



