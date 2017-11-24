#-*- coding: utf-8 -*-

def wypisz(t):
    kody = []
    t = t+"\n"
    for x in t:
        if ord(x) not in kody:
                kody.append(int(ord(unichr(x))))

    kody.sort()

    for h in kody:
        print h, t.count(chr(h))

t = raw_input()
wypisz(t)
