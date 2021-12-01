while True:
    try:
       k = 1
       while k != 0:
        k = int(input())
        n,m = map(int,input().split())
        x=[]
        y=[]
        for i in range(k):
          w,z = map(int,input().split())
          x.append(w)
          y.append(z)
          if(x[i]>n and y[i]>m):
            print("NE")
          elif(x[i]< n and y[i]>m):
            print("NO")
          elif(x[i]< n and y[i]<m):
            print("SO")
          elif(x[i]>n and y[i]<m):
            print("SE")
          elif(x[i]==n or y[i]==m):
            print("divisa")
    except EOFError:
        break