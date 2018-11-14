from ai_critics import critics
from ai_pearson import sim_pearson

def topMatches(prefs,person,n=5,sim=sim_pearson):
    scores = [(sim(prefs,person, other), other) for other in prefs if other!=person]
    scores.sort()
    scores.reverse()
    return scores[0:n]
