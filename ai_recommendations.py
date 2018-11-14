from ai_critics import critics
from ai_pearson import sim_pearson

def getRecommendations(prefs,person,sim = sim_pearson):
    totals={}
    sum_sim={}
    for other in prefs:
        if other==person: continue
        similarity = sim(prefs,person,other)
        if similarity <= 0: continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item]==0:
                totals.setdefault(item,0)
                totals[item]+= prefs[other][item]*similarity
                sum_sim.setdefault(item,0)
                sum_sim[item] += similarity
    rankings = [(total / sum_sim[item], item) for item,total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings
