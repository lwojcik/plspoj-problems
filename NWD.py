t = input()

while t:
    z = raw_input().split()
    a,b = int(z[0]), int(z[1])
    
    if a>b:
        w = a
        m = b
    else:
        w = b
        m = a

    r = w % m

    while r:
        w = m
        m = r
        r = w % m

    print m
    t-=1
