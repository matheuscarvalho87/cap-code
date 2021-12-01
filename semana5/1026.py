while True:
    try:
        m,n = map(int,input().split())
        print(n^m)
    except EOFError:
        break