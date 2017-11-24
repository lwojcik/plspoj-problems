t = input()
x = 0

while t:
    d = raw_input().split()
    a = int(d[0])
    b = int(d[1])
    n = int(d[2])
    
    bity = str(bin(b))
    bits = list(bity[2:])
    m = int(len(bits))
    x = x % n
    wynik = 1
    x = a
    i = 0

    for g in range(0,m):
        if bits(g)=='1':
            wynik = wynik * x
            wynik = wynik % n
            
        x = x * x
        x = x % n            
            
    print wynik
    t-=1
