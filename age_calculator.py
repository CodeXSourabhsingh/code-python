BIRTH_YEAR= int(input("enter birth year : "))
import time
current_year= int(time.strftime("%Y"))
age= current_year -BIRTH_YEAR
if(age>=18):
    print('adult')
else:
    print("not adult")


