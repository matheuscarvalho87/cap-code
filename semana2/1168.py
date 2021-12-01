n = int(input())
x=[]

for i in range(n):
  leds = 0
  x = input()
  for num in range(len(x)):
    if(x[num]=='1'):
      leds+=2
    elif(x[num]=='2' or x[num]=='3' or x[num]=='5' ):
      leds+=5
    elif(x[num]=='4'):
      leds+=4
    elif(x[num]=='6'):
      leds+=6
    elif(x[num]=='7'):
      leds+=3
    elif(x[num]=='8'):
      leds+=7
    elif(x[num]=='9' or x[num]=='0'):
      leds+=6
  print(leds,'leds')
