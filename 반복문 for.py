'''
# 구구단 1~9단 출력
for j in range(1,10,1):
    for i in range(1,10,1):
        mul=j*i #mul 선언
        print(f'{j}*{i} = {mul}')
    print('--------------------')
'''
'''
#case 1
#1 부터 100까지 홀수만 출력
for i in range(1,101,2):
    print(i)

#case 2
for i in range(1,101,1):
    if i%2==1:
        print(i)
'''
'''
# 5부터 100까지 5의 배수 출력
for i in range(5,101,5):
    print(i)

#10000까지의 제곱수를 출력
for i in range(1,101,1):
    mul=i*i
    print(f'{i}*{i} = {mul}')
    print('----------------')
'''
'''
#146 pg 1번
a= 'life is too short, you need python'

if 'wife' in a: print('wife')
elif 'python' in a and 'you' not in a: print('python')
elif 'shirt' not in a: print('shirt')
elif 'need' in a: print('need')
else: print('none')
'''
'''
# 146PG 2번
result =0
i=1
while i<=1000:
    if i%3==0:
        result=result+i
    i=i+1
print(result)
'''
# for문으로 1000이하의 3의 배수의 합 출력
result=0
for i in range(1,1001,1):
    if i%3==0: #i는 3의 배수냐?
        result=result+i
    i=i+1
print(result)

