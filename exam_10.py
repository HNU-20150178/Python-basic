#키보드로 정수 입력
#1~입력은 정수까지 출력하고, 마지막에 합계를 출력

'''
num = int(input("정수입력 : "))

tot = 0
for x in range (num):
    print(num-x,end="\t")
    tot += (num-x)
    print("합계 : ",tot)
print('')

'''
insu = int(input("정수 :" ))
tot = 0
for x in range(insu):
    print(x+1,end='\t')
    tot+=x+1

print("total:",tot)
