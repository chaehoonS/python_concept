'''
list1=['abc','dfg','hij',123,456]
list1[2]='park'
'''
#변수 이름을 'arr'로 하고 아래 리스드를 대입(저장)하시오.
#[4,8,12,16,20,24,28,32]
arr=[4,8,12,16,20,24,28,32]

# 32=4*8
'''
arr1=[]
a=1
while True:
    if a==1000: break
    arr1.append(4*a)
    a=a+1
print(arr1)
'''

'''
arr=[12,21,4,32,31]
size=len(arr) # 리스트의 크기변수
print(size)

idx=0 #인덱스 변수
while True:
    idx1=idx+1
    if idx1==size: break
    if arr[idx]>arr[idx+1]:
        tmp = arr[idx]
        arr[idx]=arr[idx1]
        arr[idx1]=tmp
    idx=idx+1
    print(arr)
print('-----------------------')
print(sorted(arr))
print(list(reversed(arr)))
'''

# 내생일 요일 찾기
'''
import datetime
today= datetime.datetime.now()
print(f'오늘은 {today.year}년도 입니다')
print(f'오늘은 {today.month}월 입니다')
print(f'오늘은 {today.day}일 입니다')

if today.weekday() == 6 or today.weekend()==5:
    print('주말')
else:
    print('평일')
'''

import datetime
print('태어난 날의 요일 맞추기')
y = int(input('년 입력: '))
m = int(input('달 입력: '))
d = int(input('일 입력: '))

date=datetime.datetime(y,m,d)

if date.weekday()==0: print('월')
elif date.weekday()==1: print('화')
elif date.weekday()==2: print('수')
elif date.weekday()==3: print('목')
elif date.weekday()==4: print('금')
elif date.weekday()==5: print('토')
elif date.weekday()==6: print('일')

#8/1 금요일 26세 아님 


'''
import random

while True:
    #컴퓨터
    com=random.choice('RSP')
    user=input('R, S, P 중 하나를 고르시오:')

    if com==user :
        print('비김')
    elif (com=='R' and user=='p')or (com=='S' and user=='R')or (com=='P' and user=='S'):
        print('인간이 이김')
        break
    else:
        print('졌어요')
    print(f'컴퓨터 : {com}, 인간 : {user}')
'''
