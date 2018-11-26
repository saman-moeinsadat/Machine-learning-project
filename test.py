from bs4 import BeautifulSoup
import urllib2
import re
from urlparse import urljoin
pages = open('musicWikiFeeds.txt')
for i in range(2):
    newpages = set()
    for page in pages:
        try:
            c=urllib2.urlopen(page)
            print 'indexing %s' % page
        except:
            print "could not open %s" %page
            continue
        soup=BeautifulSoup(c.read())


        links=soup('a')
        for link in links:
            if ('href' in dict(link.attrs)):
                url=urljoin(page,link['href'])
                if url.find("'")!= -1:
                    continue
                url=url.split('#')[0]
                if url[0:4]=='http':
                    newpages.add(url)

    pages=newpages
