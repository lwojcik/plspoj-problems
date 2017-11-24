while True:
    try:
        n = raw_input().split(';')
        n1 = str(n[0]).split(': ')
        n2 = str(n[1]).split(': ')
        n3 = str(n[2]).split(': ')
        n4 = str(n3[1]).split('-')

        imie = n1[1]
        nazwisko = n2[1]
        rok = n4[0]
        miesiac = n4[1]
        dzien = n4[2]

        if imie != imie.title() or imie.isalpha() == False:
            print "0"
            
        elif nazwisko != nazwisko.title() or nazwisko.isalpha() == False:
            print "1"

        elif rok.isdigit()==False or miesiac.isdigit()==False or dzien.isdigit()==False or int(rok)<1900 or int(rok)>2000 or int(miesiac)<1 or int(miesiac)>12 or int(dzien)<1 or int(dzien)>31:
            print "2"
            
        else:
            print t3"

    except EOFError:
        break
