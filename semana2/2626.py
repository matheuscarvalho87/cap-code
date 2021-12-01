
while True:
    try:
      dodo,leo,peper = map(str,input().split())
      if((dodo == 'pedra' and leo == 'tesoura' and peper == 'tesoura') 
      or(dodo == 'tesoura' and leo == 'papel' and peper == 'papel') or
      (dodo == 'papel' and leo == 'pedra' and peper == 'pedra')):
          print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
      elif((leo == 'pedra' and dodo == 'tesoura' and peper == 'tesoura') 
      or(leo == 'tesoura' and dodo == 'papel' and peper == 'papel') or
      (leo == 'papel' and dodo == 'pedra' and peper == 'pedra')):
          print("Iron Maiden's gonna get you, no matter how far!" )
      elif((peper == 'pedra' and dodo == 'tesoura' and leo == 'tesoura') 
      or(peper == 'tesoura' and dodo == 'papel' and leo == 'papel') or
      (peper == 'papel' and dodo == 'pedra' and leo == 'pedra')):
          print("Urano perdeu algo muito precioso...")
      else:
          print("Putz vei, o Leo ta demorando muito pra jogar...")
    except EOFError:
        break