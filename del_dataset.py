def initializeUserDict(tag,count):
    user_dict = {}
    for p1 in get_popular(tag=tag)[0:5]:
        for p2 in get_urlpost(p1['href']):
            user = p2['user']
            user_dict[user] = {}
    return user_dict

def fillItem(user_dict):
    all_items = {}
    for user in user_dict:
        for i in range(3):
            try:
                posts = get_userposts(user)
                break
            except:
                print('failed user: '+user+'retrying')
                time.sleep(4)
        for post in posts:
            url = post['href']
            user_dict[user][url] = 1.0
            all_items[url] = 1.0
    for ratings in user_dict.values():
        for item in all_items:
            if item not in ratings:
                ratings[item] = 0


    return user_dict
