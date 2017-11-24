while True:
    try:
        a = raw_input().split()
        y = ""
        c = list(a[1])

        for x in c:
            if x != a[0]:
                y = y + x
        print y
        
    except EOFError:
        break
