n = int(raw_input())
tab = []

for x in range(0,n):
    g = int(raw_input())
    tab.append(g)

cx = raw_input().split()

if cx[0]==">":
    for i in tab:
        if i>int(cx[1]):
            print i

elif cx[0]=="<":
    for i in tab:
        if i<int(cx[1]):
            print i
