from math import sqrt
from ai_critics import critics

def sim_euclidean(prefs,person1,person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0:
        return 0

    sum_of_sq = sum([pow(prefs[person1][item] - prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
    return 1 / (1 + sqrt(sum_of_sq))
