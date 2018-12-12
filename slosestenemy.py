from math import sqrt



def ClosestEnemyII(str):
    strlist = str.split(',')
    n = len(strlist)
    matrix = [[int(strlist[i][j]) for j in range(n)] for i in range(n)]
    ones= []
    twos= []
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==1:
                ones.append((j,i))

            elif matrix[i][j] ==2:
                twos.append((j,i))

    moves=[]
    for (x1,y1) in ones:
        for (x2,y2) in twos:
            d1 = abs(x2-x1)+abs(y2-y1)
            if x1<= (n/2):
                drow = abs(x2-x1-n)+abs(y2-y1)
            if x1> (n/2):
                drow = abs(x2-x1+n)+abs(y2-y1)
            if y1<= (n/2):
                dcol = abs(x2-x1)+abs(y2-y1-n)
            if y1> (n/2):
                dcol = abs(x2-x1)+abs(y2-y1+n)

            moves.append(min([d1,drow,dcol]))

    return min(moves)



print ClosestEnemyII('0000,2010,0000,2002')
