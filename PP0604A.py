t = int(raw_input())

while t:
    try:
        suma = 0
        c = raw_input().split()
        n = int(c[0])

        for x in c[1:]:
            suma = suma + int(x)

        srednia = float(suma)/n

        

        t-=1

    except EOFError:
        break
