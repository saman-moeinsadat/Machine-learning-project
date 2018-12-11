def ScaleBalancing(strArr):
    balance, weights = eval(strArr)
    weights= sorted(weights)

    dif = abs(balance[1]-balance[0])
    if dif in weights:
        print str(dif)


    else:
        for i in range(len(weights)):
            baln=balance[:]
            newW= weights[:]
            minimum = min(baln)
            idx = baln.index(minimum)
            baln[idx]+= weights[i]
            diff = abs(baln[1] - baln[0])
            newW.pop(i)
            if diff in newW:
                print '%s,%s' % (str(weights[i]),str(diff))
                break






x = ScaleBalancing('[13, 4],[1, 2, 3, 6, 14]')
