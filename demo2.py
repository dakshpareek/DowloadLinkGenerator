import requests
import ssl
from bs4 import BeautifulSoup
from PIL import Image
import urllib, cStringIO

i="https://static.pexels.com/photos/5390/sunset-hands-love-woman.jpg"
file = cStringIO.StringIO(urllib.urlopen(i).read())
im = Image.open(file)
im.show()
