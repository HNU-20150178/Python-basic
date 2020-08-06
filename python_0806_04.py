'''
1~ 100 정수 한 줄에 10개씩 출력하고 마지막에 홀수 합, 짝수합 출력
1 2 3 4 5 6 7 8 9 10
. . . . . . . . . .
91 92 93 94 95 96 97 98 99

for % 사용
for switch 사용

while % 사용
while switch 사용
'''


#1번
print("===================")
EvenTot=0
OddTot=0
for i in range(100):
    print(i+1,end='\t')
    if (i+1)%10==0:
        print('')
    if (i+1)% 2 == 1:
        OddTot+=i+1
    else:
        EvenTot+=i+1
print("홀수는",OddTot,"\n","짝수는",EvenTot)
'''
'''
#2번 for switch
print("===================")
EvenTot=0
OddTot=0
sw = 1
for i in range(1,101):
    print(i,end='\t')
    if i%10 == 0:
        print("")
    if sw == 1 :
        OddTot+=i
        sw=0
    else:
        EvenTot+=i
        sw=1

print("홀수값 : ", OddTot)
print("짝수값 : ",EvenTot)
'''


'''
#3번 while % 이용
print("===================")
i=0
EvenTot=0
OddTot=0
while i <100:
    i+=1
    print(i,end='\t')
    if i%10 == 0:
        print("")
    if i%2 == 1:
        OddTot+=i
    else:
        EvenTot+=i
print("홀수값:",OddTot)
print("짝수값:",EvenTot)
'''

'''
#4번 while switch 이용
print("===================")
i=0
EvenTot=0
OddTot=0
sw=1

while i < 100:
    i+=1
    print(i,end='\t')
    if i%10==0:
        print("")
    if sw==1:
        OddTot+=i
        sw=0
    else:
        EvenTot+=i
        sw=1
print("홀수값:",OddTot)
print("짝수값:",EvenTot)
    

