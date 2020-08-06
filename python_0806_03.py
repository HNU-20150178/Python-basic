'''
1+2+3+4+5+6+7+8+9+10=55
1 2 3 4 5 6 7 8 9 10 = 55
1.for문 이용해서 만들고
2.while 문 이용해서 만들기
'''

tot=0
for x in range(10):
    if x+1==10:
        print(x+1,end='')
    else:
        print(x+1,end='+')
    tot+=x+1
print('=',tot)

tot=0
p=0
while p<10:
    p+=1
    print(p, end='')
    if p!=10:
        print(end='+')
    tot+=p
print("=",tot)
    


'''
#내가만든 조건문 잘만들었으나 모범답안과는 살짝다름 위의 for문이 그러함.
tot=0
for i in range(10):
    print(i+1,end=' ')
    if i !=9:
        print ("+",end=' ')
    tot+=i+1
print("=",tot)

x=0
tot=0
while x < 10:
    x+=1
    print(x, end=' ')
    tot+=x
print("=",tot)

'''
