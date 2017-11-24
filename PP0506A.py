t = int(raw_input())

for u in range(0,t):
    try:
        p = int(raw_input())
        punkty = ()
        wspolrzedne = ()
        for v in range(0,p):
            try:
                z = raw_input().split()
                punkty = punkty.append(z[0])
                wspolrzedne = wspolrzedne.append(z[1]).append(z[2])
                print punkty
                print wspolrzedne
            except EOFError:
                break

                    

    except EOFError:
        break
