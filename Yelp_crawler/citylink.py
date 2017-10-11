#coding:utf-8
import re
import Tkinter as tk
import urllib
import urllib2
import time

baseurl='https://www.yelp.com/'


class link:
	def __init__(self):
		self.country=''
		self.city=''
		self.link=''


file=open("city.pc",'w')

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
			'''


			a=link()
			a.country=i[0]
			a.city=j[1]
			a.link=j[0]
			linklist.append(a)
	return linklist
			'''
			file.write(i[0].encode('utf-8'))
			file.write("\t")
			file.write(j[1].encode('utf-8'))
			file.write("\t")
			file.write(j[0].encode('utf-8'))
			file.write("\n")
getLinklist(baseurl)

file.close()
				

#citylink=getLinklist(baseurl)


