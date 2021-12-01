n = int(input())

for i in range(n):
    a,b = map(str,input().split())
    if a[-len(b):] == b:
        print (a[-len(b):])
        print("encaixa")
    else:
        print("nao encaixa")
    
   