from bs4 import BeautifulSoup
import urllib2
from urlparse import urljoin
import sqlite3
import re


class crawler:
    def __init__(self, dbname):
        self.con = sqlite3.connect(dbname)

    def __del__(self):
        self.con.close()

    def dbcommit(self):
        self.con.commit()

    def getentryid(self, table, field, value, createnew=True):
        return None

    def addtoindex(self, url, soup):
        print 'Indexing %s ' % url

    def gettextonly(self, soup):
        v = soup.string
        if v == None:
            c = v.content
            resulttext = ''
            for t in c:
                subtext=self.gettextonly(t)
                resulttext +=subtext
            return resulttext
        else:
            return v.strip()

    def separatewords(self, text):
        splitter = re.complie('\\W*')
        return [s.lower() for s in splitter.split(text) if s!='']

    def isindexed(self, url):
        return False

    def addlinkref(self, urlFrom, urlTo, linkText):
        pass

    def crawl(self, pages, depth=2):
        for i in range(depth):
            newpages=set()
            for page in pages:
                try:
                    c=urllib2.urlopen(page)
                except:
                    print "could not open %s" %page
                    continue
                soup=BeautifulSoup(c.read())
                self.addtoindex(page,soup)


                links=soup('a')
                for link in links:
                    if ('href' in dict(link.attrs)):
                        url=urljoin(page,link['href'])
                        if url.find("'")!= -1:
                            continue
                        url=url.split('#')[0]
                        if url[0:4]=='href' and not self.isindexed():
                            newpages.add(url)
                        linkText=self.gettextonly(link)
                        self.addlinkref(page,url,linkText)

                self.dbcommit()
            pages=newpages


    def createindextables(self):
        self.con.execute('create table urllist(url)')
        self.con.execute('create table wordlist(word)')
        self.con.execute('create table wordlocation(urlid,wordid,location)')
        self.con.execute('create table link(fromid integer,toid integer)')
        self.con.execute('create table linkwords(wordid,linkid)')
        self.con.execute('create index urlidx on urllist(url)')
        self.con.execute('create index wordidx on wordlist(word)')
        self.con.execute('create index wordurlidx on wordlocation(wordid)')
        self.con.execute('create index fromidx on link(fromid)')
        self.con.execute('create index toidx on link(toid)')
        self.dbcommit()

ignorewords = set(['the','of','to','and','a','in','is','it'])
wikifeeds=[]

for line in open('musicWikiFeeds.txt'):
    wikifeeds.append(line.strip('\n'))

# crawler = crawler('searchindex.db')
# crawler.createindextables()
