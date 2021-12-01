import math
while True:
    try:
      m,n = map(int,input().split())
      resultado = math.factorial(m) + math.factorial(n)
      print(resultado) 
    except EOFError:
        break