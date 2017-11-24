t = int(raw_input())

while t:
    tab = raw_input().split()
    tablica = tab[1:]
    tablica.reverse()
    for x in tablica:
        print x,
    print
    t-=1
