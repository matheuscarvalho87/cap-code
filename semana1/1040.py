a,b,c,d = input().split(' ')
a = float(a)
b = float(b)
c = float(c)
d = float(d)

media = ((a*2)+(b*3)+(c*4)+(d*1))/10;

print(f'Media: {media:.1f}')

if(media >= 7):
   print('Aluno aprovado.')
elif(media < 5):
   print('Aluno reprovado.')
elif(media >= 5 and media < 7):
   print('Aluno em exame.')
   e = float(input())
   print(f'Nota do exame: {e:.1f}')
   nova_media = (media+e)/2
   if(nova_media>=5):
     print('Aluno aprovado.')
   else:
     print('Aluno reprovado.')
   print(f'Media final: {nova_media:.1f}')  

