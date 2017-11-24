t = int(raw_input())
znakimale = []
znakiduze = []
ilosci = {}

for x in range(0,t):
    try:
        slowa = raw_input()
        for d in slowa:
            if d == d.lower():
                if d not in znakimale:
                    znakimale.append(d)
            elif d == d.upper():
                if d not in znakiduze:
                    znakiduze.append(d)
            else:
                pass
        znakimale.sort()
        znakiduze.sort()
        for j in znakimale:
            q = int(ilosci[j])+znakiduze.count(j)
            ilosci[j]=q
        for o in znakiduze:
            z = int(ilosci[o])+znakiduze.count(o)
            ilosci[o]=z

    except EOFError:
        break

for g in znakimale:
    print g, ilosci[g]
for h in znakiduze:
    print h, ilosci[h]
