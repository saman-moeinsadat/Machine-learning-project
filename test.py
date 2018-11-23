from bs4 import BeautifulSoup
import urllib2
import re


def gettext(soup):
    v=soup.string
    if v == None:
        c=soup.contents
        resulttext=''
        for t in c:
            subtext=gettext(t)
            resulttext+=subtext+'\n'

        return resulttext


    else:
        return v.strip()


c = urllib2.urlopen('https://en.wikipedia.org/wiki/IndieFeed')
soup = BeautifulSoup(c.read(),'lxml')
v1 = gettext(soup)
#encoding the string for preventing the ascii error risen
string_out1 = v1.encode('utf8')

v2 = soup.get_text()
string_out2 = v2.encode('utf8')

s = re.compile('\\W*')
#comparing the method written in the book and get_text() method in bs4
li1 = s.split(v1)
li2 = s.split(v2)
extras = []
for item in li1:
    if item not in li2:
        extras.append(item)

print extras
# turned out the get_text() function works better
