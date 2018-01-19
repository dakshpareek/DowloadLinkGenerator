import requests
import ssl
from bs4 import BeautifulSoup
from PIL import Image
import urllib, cStringIO

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image

i="https://static.pexels.com/photos/5390/sunset-hands-love-woman.jpg"
#file = cStringIO.StringIO(urllib.urlopen(i).read())
#im = Image.open(file)
#im.show()





class MyApp(App):

  def build(self):
  	return Image(source=i)

MyApp().run()
