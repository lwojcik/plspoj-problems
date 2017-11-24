import sys

while True:
    try:
        l = map(lambda x: int(x.strip()), sys.stdin.readlines()) 
        a = 0 
        for i in range(0, len(l)): 
        if l[i] == 42 and l[i-1] != 42: 
        a+=1 
        print l[i] 
        if a > 3: 
            break
    except EOFError:
        break
