d = int(raw_input())

for x in range(0,d):
    try:
        a = raw_input().split()
        ucz = int(a[0])-1
        cuk = int(a[1])
    
        if cuk==ucz:
            print "NIE"
        elif ucz==0:
            print "TAK"
        elif cuk<ucz:
            print "TAK"
        elif cuk%ucz == 0:
            print "NIE"
        elif cuk%ucz !=0:
            print "TAK"
        
    except EOFError:
        break
