''' 키보드입력
    번호 : 1
    이름 ; 홍길동
    국어 : 88
    영어 : 79
    수학 : 85

    [출력예시]
    번호 이름 국어 영어 수학 총점 평균 학점 판정
    1   홍길동 88  79     85  x    x    x  x

    판정은 세과목 모두 40이상이고 평균이 60점이상 "합격"
    한과목이라도 40미만이 있으면 "과락"
    세과목 모두 40이상이나 평균이 60점미만이라면  "불합격"
                
    '''

import sys

print("당신의 정보를 보여주는 시스템입니다,\n 지시에 따라주세요 ")
num = int(input("번호를 입력해주세요 : "))
name = input("이름을 입력해주세요 : ")
kor = int(input("국어점수를 입력해주세요 : "))
eng = int(input("영어점수를 입력해주세요 : "))
math = int(input("수학점수를 입력해주세요 : "))

tot = kor+eng+math
ave =int(tot/3*100+0.5)/100




if 100>=ave and 93<=ave:
    degree="A"
elif 92>=ave and 85<=ave:
    degree="B"
elif 84>=ave and 70<=ave:
    degree="C"
elif 69>=ave and 55<=ave:
    degree="D"
else:
    degree="F"

if kor>=40 and eng>=40 and math>=40:
    pan = 1
else:
    pan =0

if pan == 1 and ave>=60:
    graduation="합격"
elif pan == 1 and ave<60:
    graduation="평균미만"
else:
    graduation="과락"
    
print("번호\t이름\t\t국어\t영어\t수학\t총점\t평균\t학점\t판정")
print(num,"\t",name,"\t",kor,"\t",eng,"\t",math,"\t",tot,"\t",ave,"\t",degree,"\t",graduation)
