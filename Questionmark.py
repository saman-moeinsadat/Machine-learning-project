""" Have the function QuestionsMarks(str) take the str string parameter,
which will contain single digit numbers, letters, and question marks, and
check if there are exactly 3 question marks between every pair of two numbers
that add up to 10. If so, then your program should return the string true, otherwise
it should return the string false. If there aren't any two numbers that add up
to 10 in the string, then your program should return false as well.
For example: if str is "arrb6???4xxbl5???eee5" then your program should
 return true because there are exactly 3 question marks between 6 and 4,
 and 3 question marks between 5 and 5 at the end of the string"""

def Questionmarks(str):

    spstring = list(str)
    patcount = 0
    for i in range(len(spstring)):
        for j in range(i+1,len(spstring)):
            try:
                if int(spstring[i])+int(spstring[j]) == 10:
                    newstr= spstring[i+1:j]
                    if newstr.count('?') ==3:
                        patcount+=1
            except:
                continue
    if patcount ==0:
        print 'False, there is no occuring pattern'
    else:
        print 'True, this pattern is repeating %d time(s)' %patcount

x =Questionmarks('arrb6???4xxbl5???eee5')
