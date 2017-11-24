n=int(raw_input())

for x in range(0,n):
    try:
        d = raw_input()
        wynik = int(d[0])
        for z in range(1,len(d),2):
            if d[z]=='+':
                wynik=wynik+int(d[z+1])
            elif d[z]=='-':
                wynik=wynik-int(d[z+1])
            else:
                pass
        print wynik
        
    except EOFError:
        break
