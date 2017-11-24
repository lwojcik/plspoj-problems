t = int(raw_input())

for x in range(0,t):
    try:
        n = raw_input().split()
        nl = int(n[0])
        liczby = n[1:]

        for f in range(1,len(liczby),2):
            print liczby[f],
        for g in range(0,len(liczby),2):
            print liczby[g],
        print

    except EOFError:
        break
