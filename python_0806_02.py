'''
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''
cnt=0
for x in range(5):
    for y in range(5):
        cnt+=1
        print(cnt,end='\t')
    print()





'''

#cnt를 설정해서 반복문 하나로 만드는 방법
for i in range(0,26):
    print(i+1,end=' ')
print('')


for i in range(0,25):
    i+=1
    print(i,end="\t")
    if i%5 == 0:
        print("")

'''

