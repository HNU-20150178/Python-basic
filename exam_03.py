# 반복문 종류

'''
    for문
    while문

'''

for x in range (10):
    print("10번출력하시오")




for x in range(1,11,1): 
    print(x)

for x in range(0,10,1): #0에서 부터 10 까지 1 씩 증가시키는 것을 x가 10이 될때까지 반복하시오
    print(x+1)

a = [(1,2), (3,4), (5,6)]

for (first, last) in a:   #['one', 'two', 'three'] 리스트의 첫 번째 요소인 'one'이 먼저 i 변수에 대입된 후 print(i) 문장을 수행한다.
                        #다음에 두 번째 요소 'two'가 i 변수에 대입된 후 print(i) 문장을 수행하고 리스트의 마지막 요소까지 이것을 반복한
    print(first+last)
