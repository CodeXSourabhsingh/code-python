# lets make a code thaat will say good morning,good evening and good night
# when we give him the time 
#using if else statement and function
import time
Morning_timezone  = "6  to 12 "
afternoon_timezone ='12 to 16' 
evening_timezone ='16 to 21'
night_timezone ='21 to 24'
hour= int(time.strftime('%H'))
if(0 <= hour < 12):
    print("godd morning")
elif(12 <= hour < 16):
    print('good afternoon')
elif(16 <= hour < 21):
    print('godd evening')
elif(21 <= hour < 24):
    print('good night')

    