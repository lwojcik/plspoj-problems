def geo(n,a1=1,q=2):
    return a1*q**n-1



print "Program oblicza n-ty element ci�gu geometrycznego."
n = input("Podaj numer elementu ci�gu (n):")
a1 = input("Podaj warto�� pierwszego elementu ci�gu (a1, domy�lnie 1):")
q = input("Podaj warto�� iloczynu ci�gu (q, domy�lnie 2):")
print "a"+n+"=",geo(n,a1,q)
