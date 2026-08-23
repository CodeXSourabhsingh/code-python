Qpaper = [
    ['what is water?\na. h20\nb.h50\nc.52\nd.54','a',1000],
    ['what is dog? \na.human \nb.animal \nc.fish \nd.mouse','b',2000],
    ['what is 5? \na.word \nb.fuse \nc.number \nd.got','c',3000.],
    ['what is fish need to survive? \na.eater \nb.rad \nc.water \nd.kill','c',4000],
]
total_money= 0
for question_text,correct_answer,prize_money in Qpaper:
    valid_option={'a': True,'b': True,'c': True, 'd': True}
    while True:
        try:
            print(question_text)
            user_answer=(input('answer : ')).lower()
            valid_option[user_answer]
            break
        except:
              print('invalid answer')
    if user_answer==correct_answer:
        total_money += prize_money
        print('correct')
    else:
        print('wrong')
        break
 
print(total_money)       