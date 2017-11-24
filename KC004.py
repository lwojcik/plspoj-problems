while True:
    try:
        t = raw_input().split()
        s = t[0]
        liczby = t[2:]
        print liczby.count(s)

    except EOFError:
        break
