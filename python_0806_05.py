'''
3개의 정수를 입력 대 중 소 찾기
80 70 85
=> 85 80 70

* 오름차순 , 내림차순에서 쓰는 교환 방법 *
'''

max = 00
min = 999
mid = 0

a = int(input("3개의 정수를 입력하세요"))
b = int(input("3개의 정수를 입력하세요"))
c = int(input("3개의 정수를 입력하세요"))



if a<b:
    t=a
    a=b
    b=t
if a<c:
    t=a
    a=c
    c=t
if b<c:
    t=b
    b=c
    c=t
print(a,b,c,end='')

if a>b:
    k=a
    a=b
    b=k


'''
max = a
    if a > b:
        if b > c:
            max = a
            mid = b
            min = c
        if c < b:
            min = c
#내가 시도한 어려웠던 방법
        '''
