t = int(raw_input())

for v in range(0,t):
    try:
        g = raw_input().split()
        
        n = int(g[0])
        x = int(g[1])
        y = int(g[2])

        for i in range(2,n):
            if i%y!=0 and i%x==0:
                print i,
        print

    except EOFError:
        break
