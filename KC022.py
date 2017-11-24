while True:
    try:
        test = raw_input().split()
        liczby = test[1:]
        wynik = []
        i = int(test[0])
        
        for x in liczby:
            if x not in wynik:
                wynik.append(x)
            else:
                pass
            
        wynik.sort()
        if len(wynik)>=i:
            print wynik[-i]
        else:
            print "-"
            
        
    except EOFError:
        break
