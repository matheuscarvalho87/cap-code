def calcula_juros_simples(capital,taxa,meses ):
  return round(capital*taxa*meses)
def calcula_juros_composto(capital,taxa,meses ):
  return capital*(pow(1+taxa,meses))  

c = float(input())  
i = float(input())
n = int(input())
 
if(calcula_juros_simples(c,i,n) >= calcula_juros_composto(c,i,n)):
  print(f"DIFERENCA DE VALOR = {(calcula_juros_simples(c,i,n) - calcula_juros_composto(c,i,n)) :.2f}")
else:
  print(f"DIFERENCA DE VALOR = {(calcula_juros_composto(c,i,n) - calcula_juros_simples(c,i,n)) :.2f}")
print(f"JUROS SIMPLES = {c - calcula_juros_simples(c,i,n):.2f} ",  )
print(f"JUROS COMPOSTO = {(calcula_juros_composto(c,i,n) - c):.2f}")

 