|#finding 2*2 matrix of vowls in a matrix of alphabets and return the most top-left index




def VowelSquare(strArr):
    strlist = strArr.split(',')
    if len(strlist)< 2 or len(strlist[0]) < 2:
        print 'the matrix must be atleast 2*2 in Dimension'
        return
    vowls = ['i','e','o','u','a']
    square = []
    for i in range(len(strlist)-1):
        for j in range(len(strlist[0])-1):
            if strlist[i][j] in vowls and strlist[i][j+1] in vowls and strlist[i+1][j] in vowls and strlist[i+1][j+1] in vowls:
                square.append((i,j))

    if len(square) ==0:
        print 'No match found'
        return
    else:
        return sorted(square)[0]

print VowelSquare('aqrst,ukaei,ffooo')
