# [파이썬 퀴즈5 - 반복문]


# 문제1)
# 단을 입력 받아서 구구단을 출력하세요. (for 사용)
# 입력 예) 7
# 출력 예) 7 * 1 = 7 ... 7 * 9 = 63

dan = int(input("몇 단? : "))
for i in range(1, 10):
    print(f'{dan} x {i} = {dan*i}')
    # print(dan, 'x', i, '=', (dan*i))

''' 퀴즈영역
multipl = int(input("구구단 몇단:"))
for i in range(1, 10):
    print(f'{multipl} x {i} = {multipl*i}')
'''


# 문제2)
# 1 부터 입력한 수까지의 짝수 합과 홀수 합을 각각 출력하세요.

num = int(input("숫자입력:"))
even_sum = 0
odd_sum = 0
for i in range(1, num+1): # +1을 해야 num까지 포함
    # print(i, end=' ')
    if i%2 == 0: # 짝수
        even_sum = even_sum + i
    else: # 홀수
        odd_sum = odd_sum + i
print('짝수합:', even_sum, "홀수합:", odd_sum)

''' 퀴즈영역
num = int(input("숫자입력:"))
even = 0
odd = 0
for i in range(1, num+1):
    if i%2 == 0:
        even = even + i
    else: odd = odd + i
print("짝수 합 :", even)
print("홀수 합 :", odd)
'''

# 문제3)
x = [49, -17, 25, 102, 8, 62, 21]
# 리스트의 각 요소에 10을 곱한 값을 한 줄에 출력하세요.

# print(x*10) - x를 10번 반복
for i in range(len(x)): # idex에 접근
    print(x[i]*10, end=' ')
print()

for v in x: # vlaue에 접근
    print(v*10, end=' ')
print()


''' 퀴즈영역
for i in range(len(x)):
    print(x[i]*10, end=' ')
print()
'''

# 문제4)
# 잔액 13000원 교통카드에서 1350원씩 차감하면서 잔액이 1350원 미만이 될 때까지
# '남은 잔액' 을 출력하세요. (while 사용)

money = 13000
while money >= 1350:
    money = money - 1350
    print('잔액:', money)
print('-'*50)
money = 13000
while True:
    if money < 1350: # True 시작이므로 해당 문이 밑에 오면 1350 미만이어도 실행됨
        break
    money = money - 1350
    print('잔액:', money)

''' 퀴즈영역
money = 13000
while money >= 1350:
    money = money - 1350
    print(money)
'''