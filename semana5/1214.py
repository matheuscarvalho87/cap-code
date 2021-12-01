n = int(input())

for i in range(n):
  valores=input().split()
  valores = [int(x) for x in valores]
  media = sum(valores[1:])/(valores[0])
  print("%.3f" % media,"%")