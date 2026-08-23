# the smart grade & attendance tracker

dict_x= { 
            'sourabh':{ 'attendance': 80,'marks':[70,79,85] },
            'harry':{'attendance':56, 'marks':[60,65,70]},
            "sid":{'attendance':82, 'marks': [89,98,82]},
            'neha':{'attendance': 70, 'marks':[78,78,89]}
}

def logia():
     while True :
          y= input('enter student name : ')
          student_data= dict_x.get(y)
          if student_data['attendance']<75:
               print('low attendance')
          else:
               print('good attendence') 
          print(f" average result")   
                 
          print(sum(student_data['marks']) / len(student_data['marks']))
         
logia()    


            

   
