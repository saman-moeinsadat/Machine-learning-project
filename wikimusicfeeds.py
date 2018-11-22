import urllib2
from bs4 import BeautifulSoup

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

out = open('musicWikiFeeds.txt','w')
for feed in validlist:
    out.write(feed)
    out.write('\n')
