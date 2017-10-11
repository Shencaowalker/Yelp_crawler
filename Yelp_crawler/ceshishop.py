#coding:utf-8
import re
import Tkinter as tk
import urllib
import urllib2
import time

endurl="https://www.yelp.com/search?find_desc=pizza&find_loc=San+Francisco%2C+CA&ns=1"
request=urllib2.Request(endurl)
response=urllib2.urlopen(request)
html=response.read().decode('utf-8')
pattern=re.compile(r'class="indexed-biz-name">.*?href="(.*?)".*?<span >(.*?)</a>.*?rating-large" title="(.*?) star rating.*?price-category.*?category-str-list">(.*?)</span>.*?<address>(.*?)</address>',re.S)
shoplist=re.findall(pattern,html)

print shoplist

