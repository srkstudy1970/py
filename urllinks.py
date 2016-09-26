# BeautifulSoup is the package which has been downloaded in placed in the same foloder as in urllinks.py
import urllib
from BeautifulSoup import *
url = raw_input("Enter URL :- ")
html= urllib.urlopen(url).read()
soup=BeautifulSoup(html)
tags =soup('script')
for tag in tags:
    #this statement is only to get tags which are anchor tags and have herf
    print tag.get('src', None)
