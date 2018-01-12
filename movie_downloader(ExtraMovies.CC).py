import requests
from bs4 import BeautifulSoup

def make_soup(url):
    try:
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}).content
    except:
        return None
    return BeautifulSoup(html, "lxml")

url = "http://extramovies.cc/"
url2 = "http://extramovies.cc/a-monster-calls-2016-full-movie-english-dd5-1-720p-bluray-esubs-download/"
soup = make_soup(url)
movies = soup.findAll("div", {"class": "thumbnail"})
all_data=[]

#all movies links are stored here
for every_movie in movies:
	a_tag=every_movie.findAll("a")
	title=a_tag[0].attrs["title"]
	link=a_tag[0].attrs["href"]

	soup2=make_soup(link)
	d_link=soup2.findAll("a",{"class": "buttn blue"})
	f_link='http://extramovies.cc'+str(d_link[0].attrs["href"])
	soup3=make_soup(f_link)
	last_link=soup3.findAll("a")
	final=last_link[len(last_link)-2].attrs["href"]

	all_data.append([title,final])

print all_data
'''
#print all_data[0][1]
all_download_links=[]
for every_link in all_data:
	soup2=make_soup(every_link[1])
	d_link=soup2.findAll("a",{"class": "buttn blue"})
	f_link='http://extramovies.cc'+str(d_link[0].attrs["href"])
	soup3=make_soup(f_link)
	last_link=soup3.findAll("a")
	all_download_links.append(last_link[len(last_link)-2].attrs["href"])

#print all_download_links
for name,link in zip(all_data,all_download_links):
	print name[0],link
'''