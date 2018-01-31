#!C:\Python27\python.exe 
print "Content-type:text/html\r\n\r\n"
print '''<html>
<head></head>
<body>
'''

import requests
import ssl
from bs4 import BeautifulSoup
from PIL import Image
import urllib, cStringIO
import cgi
import urlparse,os
from make_soup import make__soup
from pickle import load

f=open("mydata.txt","r")
data=load(f)


#finding id of movie
sid=os.environ['PATH_TRANSLATED']
id=sid.split('\\')
id=int(id[-1])
#print data[id][1]

#All images of movies 
#make_soup fxn required,soup2 using link required
soup2=make__soup(data[id][1])
img=soup2.findAll("img",{"class": "alignnone"})

d_link=soup2.findAll("a",{"class": "buttn blue"})
f_link='http://extramovies.cc'+str(d_link[0].attrs["href"])
soup3=make__soup(f_link)
last_link=soup3.findAll("a")
final=last_link[len(last_link)-2].attrs["href"]
	
for j in range(1,len(img)):
	i=img[j].attrs["src"]
	print "<img src='{}'>".format(i)

print "<a href='{}'>Download</a>".format(final)
print '''
</body>
</html>
'''