a,b,c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)
pi = 3.14159

print(f'TRIANGULO: {(a*c)/2:.3f}')
print(f'CIRCULO: {pi*pow(c,2):.3f}')
print(f'TRAPEZIO: {((a+b)*c)/2:.3f}')
print(f'QUADRADO: {pow(b,2):.3f}')
print(f'RETANGULO: {a*b:.3f}')