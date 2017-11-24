def spacje(tekst):
    tresc = tekst.split()
    wynik = ""
    for x in tresc:
        a = str(x)
        b = a.title()
        wynik = wynik + b
    ''.join(wynik)
    print wynik
    
while True:
    try:
        t = raw_input()
        spacje(t)
    except EOFError:
        break
