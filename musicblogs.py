import urllib2
from bs4 import BeautifulSoup
import re


def getWords(feed):
    url = urllib2.urlopen(feed)
    soup1 = BeautifulSoup(url,'lxml')
    content = soup1.find('div',class_='mw-parser-output').find('p').get_text()
    char = re.compile(r'\[.*?\]')
    content_strip = char.sub('',str(content))
    title = soup1.title.get_text()

    return title,content_strip

website_url = urllib2.urlopen('https://en.wikipedia.org/wiki/Category:Music_websites')
soup = BeautifulSoup(website_url, 'lxml')
content = soup.find('div',id='mw-pages')
subc= content.find_all('div',class_='mw-category-group')
links=[]
for item in subc:
    link = item.find_all('a')
    for n in link:
        links.append(n)

music_websites = []
for item in links:
    link = 'https://en.wikipedia.org'+ item.get('href')
    music_websites.append(link)

validlist = []
for item in music_websites:
    try:
        if urllib2.urlopen(item):
            validlist.append(item)
    except urllib2.HTTPError, e:
        print(item,e.code)
    except urllib2.URLError, e:
        print(item,e.args)
length={}
for item in validlist:
    try:
        titl,words = getWords(item)
        wordlist = words.split(' ')
        length.setdefault(titl,0)
        length[titl] = len(wordlist)
    except Exception:
        continue

print length
print len(length)
print len(validlist)

for item in length.values():
    print item
