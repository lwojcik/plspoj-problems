while True:
    try:
        t = raw_input().split()
        xld = int(t[0])
        yld = int(t[1])
        xpg = int(t[2])
        ypg = int(t[3])

        xm = xpg-xld
        ym = ypg-yld

        if xm==0:
            print 0

        elif yld==0 and xm==1 and xld%2==0:
            print 0
            
        else:
            if xm==ym:
                if xpg%2!=0:
                    xpg-=1
                if ypg%2!=0:
                    ypg-=1
                cz = (ypg-yld)*((xpg-xld)*0.5)+((xpg-xld)*0.5)
                print "%.0f" % cz
            
            elif xm>ym:
                if ypg%2==0:
                    cz = (((ypg-yld)*0.5)*(xpg-xld))+((ypg-yld)*0.5)
                    print "%.0f" % cz
                elif ypg%2!=0:
                    cz = (ypg-yld)*(0.5*(xpg-xld))
                    print "%.0f" % cz
                
            elif xm<ym:
                if ypg%2==0:
                    cz = (xpg-xld)*(0.5*(ypg-yld))
                    print "%.0f" % cz
                elif ypg%2!=0:
                    ypg-=1
                    cz = ((ypg-yld)*0.5)*(xpg-xld)
                    print "%.0f" % cz

            else:
                print "Dupa :P"

    except EOFError:
        break
