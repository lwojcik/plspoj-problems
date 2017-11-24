from math import sqrt

n = input()
for x in range (0,n):
    try:
        n = input()
        p=1
        if n==2:
            print "TAK"
        elif n%2==0:
            print "NIE"
        else:
            for i in range(3,int(sqrt(n))):
                if (n%i)==0:
                    p+=1
                    if p>2:
                        print "NIE"
                    

    except EOFError:
        break
