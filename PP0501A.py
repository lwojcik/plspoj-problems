t = input()


while t:
    nwd = 0
    d=0
    c = raw_input().split()
    a, b = int(c[0]), int(c[1])
    r=a%b
    if a==b:
        nwd=b
            
    while a%b!=0:
        a=b
        b=r
        r = a % b
        nwd = b
            
    print nwd
    t-=1
