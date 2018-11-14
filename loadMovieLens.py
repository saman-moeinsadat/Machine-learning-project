def loadMovieLens():
    movies = {}
    for line in open('u.item.txt'):
        try:
            (id, title) = line.split('|')[0:2]
        except ValueError:
            continue
        movies[id] = title
    movies['1'] = 'Toy Story (1995)'
    prefs = {}
    for line in open('u.data.txt'):
        try:
            (user, movieid, rating, ts) = line.split('\t')
        except ValueError:
            continue
        prefs.setdefault(user,{})
        prefs[user][movies[movieid]] = rating

    return prefs

print(loadMovieLens()['87'])
