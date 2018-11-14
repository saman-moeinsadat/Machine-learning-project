from ai_topMatches import topMatches
from ai_critics import critics
from ai_transformPrefs import transformPrefs
from ai_euclidean import sim_euclidean

def calSimItem(prefs,n=10):
    result = {}
    itemPrefs = transformPrefs(prefs)
    c = 0
    for item in itemPrefs:
        c+=1
        if c%100==0 : print('%d / %d' % (c,len(itemPrefs)))
        scores = topMatches(itemPrefs,item,n=n,sim = sim_euclidean)
        result[item] = scores
    return result

itemSim = calSimItem(critics)
print(itemSim)

def getRecommendationsItem(prefs,itemMatch,user):
    userRatings = prefs[user]
    scores = {}
    sum_sim = {}

    for (item,rating) in userRatings.items():
        for (similarity,item2) in itemMatch[item]:
            if item2 in userRatings : continue
            scores.setdefault(item2,0)
            scores[item2]+= similarity*rating
            sum_sim.setdefault(item2,0)
            sum_sim[item2]+=similarity

    rankings = [(score/sum_sim[item],item) for item,score in scores.items()]
    rankings.sort()
    rankings.reverse()
    return rankings

print(getRecommendationsItem(critics,itemSim,'Toby'))
