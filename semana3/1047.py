hi,mi,hf,mf = map(int,input().split())

hora_final = hf - hi
minuto_final = mf - mi
if(hora_final < 0):
  hora_final = 24 + (hf-hi)
if(minuto_final < 0):
  minuto_final = 60 + (mf-mi)
  if(hora_final != 0):
    hora_final = hora_final - 1
if(hi == hf and mi == mf):
  print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
  print("O JOGO DUROU",hora_final, "HORA(S) E",minuto_final,"MINUTO(S)")