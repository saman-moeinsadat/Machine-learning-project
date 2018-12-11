import random

def CorrectPath(str):
    while True:
        route=[]
        tracepos = []
        flag = 1
        x=1
        y=5
        for item in str:
            if item == '?':
                item = random.choice('lrud')
            elif item =='u':
                y+= 1
            elif item =='d':
                y-=1
            elif item =='r':
                x+=1
            elif item == 'l':
                x-=1

            if (x,y) in tracepos:
                flag = 0
                break
            else:
                tracepos.append((x,y))
            if x==0 or x==6 or y==0 or y==6:
                flag = 0
                break
            route.append(item)

        if x ==5 and y ==1 and flag==1:
            return ''.join(route)


print CorrectPath('r?d?drdd')
