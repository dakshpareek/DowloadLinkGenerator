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


def make_soup(url):
    try:
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}).content
    except:
        return None
    return BeautifulSoup(html,"lxml")

url = "http://extramovies.cc/"
#url2 = raw_input("Enter Link")
soup = make_soup(url)
movies = soup.findAll("div", {"class": "thumbnail"})
all_data=[]
#all movies links are stored here
for every_movie in movies:
	a_tag=every_movie.findAll("a")
	title=a_tag[0].attrs["title"]
	link=a_tag[0].attrs["href"]
	all_data.append([title,link])

for i,j in enumerate(all_data):
	print "<h2>ID:",i,j[0],"</h2>"

print '''
</body>
</html>
'''
