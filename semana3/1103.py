while True:
    try:
        h1,m1,h2,m2 = map(int,input().split())
        if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
            break
        minutes = (h2-h1)*60 + (m2-m1)
        if minutes < 0:
            minutes = minutes * -1
        if minutes > 0:
            print(minutes)
    except EOFError:
        break