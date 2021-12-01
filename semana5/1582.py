def MDC(a, b, c):
    if b == 0:
        return a
    else:
        return MDC(b, a % b, c)
def is_triangle_rectangle(a, b, c):
   #maior numero
   maior = max(a, b, c)
   menor = min(a, b, c)
   medio = a + b + c - maior - menor
   if(pow(maior,2) == pow(menor,2) + pow(medio,2)):
       return True
   else:
       return False
    
while True:
    try:
        x,y,z = map(int,input().split())
        #confere se x,y,z pode ser um triangulo retangulo
        if (is_triangle_rectangle(x,y,z)):
          mdc = MDC(x,y,z)
          if(mdc == 1):
              print("tripla pitagorica primitiva")
          else:
              print("tripla pitagorica")
        else:
            print("tripla")


    except EOFError:
        break