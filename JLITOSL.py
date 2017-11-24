def geo(n,a1=1,q=2):
    return a1*q**n-1



print "Program oblicza n-ty element ci퉓u geometrycznego."
n = input("Podaj numer elementu ci퉓u (n):")
a1 = input("Podaj warto쒏 pierwszego elementu ci퉓u (a1, domy쐋nie 1):")
q = input("Podaj warto쒏 iloczynu ci퉓u (q, domy쐋nie 2):")
print "a"+n+"=",geo(n,a1,q)
