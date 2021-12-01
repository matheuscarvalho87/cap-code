def calcula_rafael(x,y):
  return  pow(3*x,2) + pow(y,2)

def calcula_beto(x,y):
  return  (2 * pow(x,2)) + pow(5*y,2)

def calcula_carlos(x,y):
  return  (-100*x) + pow(y,3)

n = int(input())

for i in range(n):
  x,y = map(int,input().split())
  rafael = calcula_rafael(x,y)
  beto = calcula_beto(x,y)
  carlos = calcula_carlos(x,y)
  if rafael > beto and rafael > carlos:
    print('Rafael ganhou')
  elif beto > carlos and beto > rafael:
    print('Beto ganhou')
  else:
    print('Carlos ganhou')
    