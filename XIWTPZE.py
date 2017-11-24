t = int(raw_input())

for d in range(0,t):
    try:
        z = raw_input().split()
        n = int(z[0])
        k = int(z[1])

        if n==k or n==(k+1) or n<k:
            print "TAK"
                    
        else:
            print "NIE"
                
    except EOFError:
        break
