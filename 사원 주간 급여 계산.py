'''
각 사원의 아이디(id), 등급, 근무시간을 입력받아 사원들에 대한 주간 급여를 계산하는 프로그램을 완성하시오
1) 사원 관리 학목
    아이디 , 등급 , 시급 , 근무시간, 주간 급여

2) 처리조건
    -사원의 주간급여는 근무시간과 시급을 곱한 값으로 한다.
    -시급은 사원의 등급이 1등급인 경우 10,000 2등급인 경우 5,000원 3등급인 경우 2,000원으로 한다.
    -근무시간이 36시간을 초과한 경우 초과근무시간에 대해 시급의 1.5배를 지급하여 근무시간은 최대 50시간까지만 인정된다.
    -사원의 id 가 "end"가 입력되면 자료출력 마지막에 급여 총합과 평균을 출력한다.
    

'''

import sys # 프로그램 종료를 위한 sys 라이브러리 불러오기

Payment=0 # 급여
Gpay=0 # 등급에 따른 시급
cnt = 0 # 몇번 반복한 값
Gpayave = 0 #급여평균
Gpaytot=0  # 급여합계


while(1):
    ID=str(input("ID를 입력하시오 : "))
    cnt += 1
    Gpaytot += Gpay 
    Gpayave = Gpaytot // cnt
    if ID == 'end': #여기에 프로그램 종료를 넣어줘야 밑의 Grade, Hour 값의 입력을 받지않고 끝난다.
        print("급여합계 : ", Gpaytot)
        print("급여평균 : ", Gpayave)
        sys.exit()
    Grade=int(input("등급을 입력하시오 : "))
    Hour=int(input("근무시간을 입력하시오 : "))
    
        
    if Grade == 1:                      #시급 설정
        Gpay += 10000
        
    elif Grade == 2:
        Gpay += 5000
        
    elif Grade == 3:
        Gpay += 2000                    #시급 설정 종료
        
    if Hour > 36 and Hour <=50:
        Payment = (Hour * Gpay) * 1.5
        
    elif Hour <= 36: 
        Payment = (Hour * Gpay)
        
    else:
        Payment = ((Hour-50) * Gpay) + (1.5 * Hour * Gpay) # 50시간 초과 근무시 50시간까지만 추가수당인정


    
    print("아이디\t등급\t시급\t근무시간\t주간급여")
    print(ID,"\t",Grade,"\t",Gpay,"\t\t",Hour,"\t",Payment,"\n")

