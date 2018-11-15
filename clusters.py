from ai_topMatches import topMatches

def readFile(filename):
    lines = [line for line in open(filename)]
    colnames = lines[0].strip().split('\t')[1:]

    rownames = []
    data = []
    for line in lines[1:]:
        p = line.strip().split('\t')
        rownames.append(p[0])
        data.append([float(x) for x in p[1:]])

    return rownames, colnames, data


[r,c,d] = readFile('blogdata.txt')
print(r)
#print(c)
#print(d)
wordFrequency = {}
for blog in r:
    wordFrequency.setdefault(blog,{})
    for word in c:
        wordFrequency[blog][word] = d[r.index(blog)][c.index(word)]
print(wordFrequency)
print(topMatches(wordFrequency,'PaulStamatiou.com - Technology, Design and Photography'))
