while True:
    try:
        z = raw_input().split()
        a = int(z[0])
        b = int(z[2])
        relacja = z[1]

        if relacja=='==':
            if a==b:
                print "1"
            else:
                print "0"
        elif relacja=='<=':
            if a<=b:
                print "1"
            else:
                print "0"
        elif relacja=='>=':
            if a>=b:
                print "1"
            else:
                print "0"
        elif relacja=='!=':
            if a!=b:
                print "1"
            else:
                print "0"
        
    except EOFError:
        break
