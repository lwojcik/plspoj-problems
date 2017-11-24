while True:
    try:
        b = raw_input()
        a = list(b)
        a.reverse()
        print ''.join(a)
        
    except EOFError:
        break
