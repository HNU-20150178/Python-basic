# 키보드로 10진수를 입력받아서 소수인지 판별하는 프로그램

'''10진수 :13
    판별 : 소수입니다
    10진수 : 20
    판별 ; 소수가 아님
    10진수 : -99
    프로그램을 종료합니다
    '''

while 1:
    num = int(input("10진수를 입력하시오"))
    if num  == -99:
        break
    for x in range(2,num+1): #적용범위는 num+1 (자기자신까지 포함시킴)
        if num%x == 0: # 나머지값이 0이면
            if num==x: # 안전하게  자기 자신값으로 나뉘어졌다면 소수
                print("소수입니다.")
                break
            else: #자기자신값에 도달하기 전에 나누어졌다면 소수가 아니다.
                print("소수가아닙니다")
                break
            
