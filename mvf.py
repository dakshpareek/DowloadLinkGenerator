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
from pickle import dump
import json
import time
from make_soup import make__soup

start_time = time.time()

def make__soup(url):
    try:
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}).content
    except:
        return None
    return BeautifulSoup(html,"lxml")

url = "http://extramovies.cc/"
#url2 = raw_input("Enter Link")
soup = make__soup(url)
movies = soup.findAll("div", {"class": "thumbnail"})
all_data=[]
#all movies links are stored here
for every_movie in movies:
	a_tag=every_movie.findAll("a")
	title=a_tag[0].attrs["title"]
	link=a_tag[0].attrs["href"]
	all_data.append([title,link])

'''
k=[]

for i in range(len(all_data)):
	soup2=make__soup(all_data[i][1])
	d_link=soup2.findAll("a",{"class": "buttn blue"})
	f_link='http://extramovies.cc'+str(d_link[0].attrs["href"])
	soup3=make__soup(f_link)
	last_link=soup3.findAll("a")
	final=last_link[len(last_link)-2].attrs["href"]
	k.append(final)
'''	
	
for i,j in enumerate(all_data):
	print "<h3><a href='view.py/{}' >{}</a>".format(i,j[0])

f1=open('mydata.txt','a+')
dump(all_data,f1)
f1.close()	

print "--- %s seconds ---" % (time.time() - start_time)
print '''
</body>
</html>
'''


	#print "Click to download: ",final
