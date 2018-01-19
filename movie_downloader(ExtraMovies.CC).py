#pip install bs4
#pip install requests

import requests
import ssl
from bs4 import BeautifulSoup
from PIL import Image
import urllib, cStringIO

def make_soup(url):
    try:
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}).content
    except:
        return None
    return BeautifulSoup(html,"lxml")

check=input("enter page number to get movies eg: 1,2,.. :")
if check!=1:
	url="http://extramovies.cc/page/"+str(check)
else:
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
	print "ID:",i,j[0]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req=input(" Enter ID of movies to get Download Link: ")
soup2=make_soup(all_data[req][1])
img=soup2.findAll("img",{"class": "alignnone"})
for j in range(1,len(img)):
	i=img[j].attrs["src"]
	#print i
	file = cStringIO.StringIO(urllib.urlopen(i,context=ctx).read())
	im = Image.open(file)
	im.show()


d_link=soup2.findAll("a",{"class": "buttn blue"})
f_link='http://extramovies.cc'+str(d_link[0].attrs["href"])
soup3=make_soup(f_link)
last_link=soup3.findAll("a")
final=last_link[len(last_link)-2].attrs["href"]

print "Click to download: ",final
