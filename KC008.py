suma = 0
while True:
    try:
        n = raw_input().split()
        wynik = 0
        for x in n:
            if x!=0:
                wynik=wynik+int(x)
        print wynik
        suma = suma+wynik

    except EOFError:
        print suma
        break
