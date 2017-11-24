while True:
    try:
        t = raw_input().split()
        l = raw_input().split()
        n = int(t[0])
        k = int(t[1])
        tablica = [0]
        n=0
        for x in l[:k]:
            tablica.append(x)
        for y in l[k:]:
            tablica.append(y)

        print ' '.join(tablica[1:])
        
    except EOFError:
        break
