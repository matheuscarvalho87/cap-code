testes = int(input())
c=[]
for i in range(testes):
    c.append(float(input()))
for i in c:
  dias = []
  while(i>1):
    i=i/2
    dias.append(i)
  print(len(dias),'dias') 
  