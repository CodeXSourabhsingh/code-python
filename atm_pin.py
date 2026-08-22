try:
    pin= 1234
    x=0
    chances=5
    while chances > 0:
       x= int(input('enter pin : '))
       if x == 1234:
          print('opening vault')
          break
       else:
         chance -= 1
         print('try again')
except:
   print('your money is safe try again')
