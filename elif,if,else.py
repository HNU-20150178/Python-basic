'''점수를 입력으로 받아서 입력된 점수가
    100~90 -> A , 80~89-> B , 70~79 -> C , 60~69->D 0~59->F
 '''

import sys
a= int(input("당신의 점수를 입력해주세요 : "))
if a>=90 and a<=100:
    print("A")   
elif a>=80 and a<=89:
    print("B")
elif a>=70 and a<=79:
    print("C")
elif a>=60 and a<=69:
    print("D")
else:
    print("F")
