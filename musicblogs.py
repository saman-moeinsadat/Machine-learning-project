import urllib2
from bs4 import BeautifulSoup
import re


def getWords(soup):
    content = soup.find('div',class_='mw-parser-output').find_all('p')
    con = iter(content)
    char = re.compile(r'\[.*?\]')
    content_strip = char.sub('',str(next(con).get_text()))
    while len(content_strip.split(' ')) < 30:
        content_strip += char.sub('',str(next(con)))

    list = content_strip.split(' ')
    return [item.lower() for item in list]

def getWordCount(feed):
    wc = {}
    url = urllib2.urlopen(feed)
    soup1 = BeautifulSoup(url,'lxml')
    title = soup1.title.get_text()
    words = getWords(soup1)
    for word in words:
        wc.setdefault(word,0)
        wc[word]+=1

    return title,wc

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

apcount={}
wordcount = {}
for item in validlist:
    try:
        titl,words = getWordCount(item)
    except Exception:
        continue
    wordcount[titl] = words
    for w,c in words.items():
        apcount.setdefault(w,0)
        if c > 1:
            apcount[w]+=1

wordlist = []

for w,bc in apcount.items():
    frac = (float(bc)/len(validlist))*1000
    if frac > 5 and frac <30:
        wordlist.append(w)

out = open('musicblogdata.txt','w')
out.write('Musoc_Websites.txt')
for word in wordlist:
    out.write('\t%s' % word)
out.write('\n')
for blog,wc in wordcount.items():
    try:
        out.write(str(blog))
        for word in wordlist:
            if word in wc:
                out.write('\t%d' % wc[word])
            else:
                out.write('\t0')
    except ValueError:
        continue
    out.write('\n')

print len(wordcount)
print len(wordlist)
