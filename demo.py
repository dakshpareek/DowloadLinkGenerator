import requests
import os,webbrowser
from bs4 import BeautifulSoup

def make_soup(url):
    try:
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}).content
    except:
        return None
    return BeautifulSoup(html,"lxml")

check=input("enter page number:")
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

req=input("Enter ID to get Download Link: ")
soup2=make_soup(all_data[req][1])
img=soup2.findAll("img",{"class": "alignnone"})
for j in range(1,len(img)):
	i=img[j].attrs["src"]
	print i
	webbrowser.open(i)
