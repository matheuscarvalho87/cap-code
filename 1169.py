n = int(input())
x=[]
for i in range(n):
  x.append(int(input()))
for i in x:
  grao = (pow(2,i)-1)/12000
  print(int(grao), "kg")
  