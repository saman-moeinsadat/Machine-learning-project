import feedparser
import re
import urllib2

def getWordCounts(url):
    d = feedparser.parse(url)
    wc = {}

    for e in d.entries:
        if 'summary' in e: summary = e.summary
        else: summary = e.description

        words = getwords(e.title+' '+summary)
        for word in words:
            wc.setdefault(word,0)
            wc[word]+=1

    return d.feed.title, wc


def getwords(html):
    txt = re.compile(r'<[^>]+>').sub(' ', html)
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    return [word.lower() for word in words if word != '']

wordcount = {}
apcount = {}
validatedlist = []
for item in open('feedlist.txt'):
    try:
        if urllib2.urlopen(item):
            validatedlist.append(item)
    except urllib2.HTTPError, e:
        print(item,e.code)
    except urllib2.URLError, e:
        print(item,e.args)

for feed in validatedlist:
    try:
        title, wc = getWordCounts(feed)
    except Exception:
        continue
    wordcount[title] = wc
    for word, count in wc.items():
        apcount.setdefault(word,0)
        if count > 1:
            apcount[word]+=1
wordlist = []
for w,bc in apcount.items():
    frac = float(bc)/len(validatedlist)
    if frac > 0.1 and frac < 0.5:
        wordlist.append(w)

out = open('blogdata.txt','w')
out.write('Blog')
for word in wordlist:
    out.write('\t%s' % word)
out.write('\n')
for blog,wc in wordcount.items():
    try:
        out.write(blog)
        for word in wordlist:
            if word in wc:
                out.write('\t%d' % wc[word])
            else:
                out.write('\t0')
    except ValueError:
        continue
    out.write('\n')
