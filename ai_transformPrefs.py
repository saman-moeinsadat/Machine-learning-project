from ai_critics import critics
from ai_topMatches import topMatches
from ai_recommendations import getRecommendations

def transformPrefs(prefs):
    result = {}
    for other in prefs:
        for item in prefs[other]:
            result.setdefault(item,{})
            result[item][other] = prefs[other][item]

    return result
