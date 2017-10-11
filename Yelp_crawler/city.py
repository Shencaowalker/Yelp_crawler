#coding:utf-8
import re
import Tkinter as tk
import urllib
import urllib2
import time

cityurl='https://www.yelp.com/locations'



def getLinklist(url):
	request=urllib2.Request(url)
	response=urllib2.urlopen(request)
        cityAllhtml=response.read().decode('utf-8')
	natpattern=re.compile(r'class="cities">(.*?)</ul>',re.S)
	natitems=re.findall(natpattern,cityAllhtml)
	for i in natitems:
		citpattern=re.compile(r'">(.*?)</a>',re.S)
		ititems=re.findall(citpattern,i)
		for j in ititems:
			print j+";",
		print "\n"
	

if __name__=="__main__":
	getLinklist(cityurl)
