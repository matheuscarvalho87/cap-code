x=1

while(x!=2):
  nota1 = float(input())
  nota2 = float(input())
  while(nota1 < 0 or nota1 > 10):
    print("nota invalida")
    nota1 = float(input())
  while(nota2 < 0 or nota2 > 10):
    print("nota invalida")
    nota2 = float(input())

  media = (nota1 + nota2) / 2
  print("media = %.2f" % media)
  x = int(input('novo calculo (1-sim 2-nao)\n'))
  while(x<1 or x>2):
    x = int(input('novo calculo (1-sim 2-nao)\n'))
  
  
