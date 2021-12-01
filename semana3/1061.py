texto, dia_inicial =input().split()
hh_i,mm_i,ss_i = map(int,input().split(' : '))

texto, dia_final = input().split()
hh_f,mm_f,ss_f = map(int,input().split(' : '))

dias = int(dia_final) - int(dia_inicial)
hora_final = int(hh_f) - int(hh_i)
minuto_final = int(mm_f) - int(mm_i)
segundo_final = int(ss_f) - int(ss_i)
if dias == 0:
    if(hora_final < 0):
      hora_final = 24 + (hh_f-hh_i)
    if(minuto_final < 0):
      minuto_final = 60 + (mm_f-mm_i)
      if(hora_final != 0):
        hora_final = hora_final - 1
    if(segundo_final < 0):
      segundo_final = 60 + (ss_f-ss_i)   
elif dias > 0:
    dias = int(dias) - 1
    if(hora_final < 0):
      hora_final = 24 + (hh_f-hh_i)
    if(minuto_final < 0):
      minuto_final = 60 + (mm_f-mm_i)
      if(hora_final != 0):
        hora_final = hora_final - 1
    if(segundo_final < 0):
      segundo_final = 60 + (ss_f-ss_i) 
print(dias,'dia(s)')
print(hora_final,'hora(s)')
print(minuto_final,'minuto(s)')
print(segundo_final,'segundo(s)')

