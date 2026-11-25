# [파이썬 퀴즈4 - 조건문]

# 문제1)
# 나이를 입력 받아서 요금을 출력하세요.
# - 8세 미만 : 무료
# - 8 ~ 13세 : 650원
# - 14 ~ 18세 : 1050원
# - 19 ~ 64세 : 1350원
# - 65세 이상 : 무료

age = int(input("나이 입력 : "))
# if 8 <= age <= 13 으로 시작해 마지막에 else로 무료 처리하는것도 가능
if age < 8:
    print("무료")
elif age <= 13:
    print("650원")
elif age <= 18:
    print("1050원")
elif age <= 64:
    print("1350원")
else:
    print("무료")

'''
퀴즈영역
조건문으로 age < 8이 거짓일때 elif로 넘어가므로 8 <= age <= 13에서 8<=는 불필요한 조건(낭비)
age = int(input("나이를 입력하세요:"))
if age < 8:
    print("무료")
    cost = 0
elif 8 <= age <= 13:
    print("650원")
    cost = 650
elif 14 <= age <= 18:
    print("1050원")
    cost = 1050
elif age >= 19 and age <=64:
    print("1350원")
    cost = 1350
else:
    print("무료")
    cost = 0
'''


# 문제2)
# 년도를 입력 받아서 윤년인지 출력하세요.
# - 4로 나누어 떨어지고 100으로 나누어 떨어지지 않으면 윤년
# - 또는 400으로 나누어 떨어지면 윤년

year = int(input("년도 입력:"))
if year%400 == 0:
    print("윤년")
elif year%100 == 0:
    print("윤년X")
elif year%4 == 0:
    print("윤년")
else:
    print("윤년X")

if year%4 == 0:
    if year%400 == 0:
        print("윤년")
    else:
        if year%100 == 0:
            print("윤년X")
        else:
            print("윤년")
else:
    print("윤년X")
# if문 안에 if문 중첩

# if year%400 == 0 or (year%4 == 0 and (not year%100 ==0)):
if year%400 == 0 or (year%4 == 0 and year%100 !=0):
    print("윤년")
else:
    print("윤년X")

# if year%400 == 0:
    # print("윤년")
# elif (year%4 == 0 and year%100 !=0):
    # print("윤년")

# 400으로 나누어 떨어지는지가 가장 1순위 조건(400=100*4), 그 다음은 100, 4 순서

'''퀴즈영역
year = int(input("년도를 입력하세요:"))
if year%4 == 0 and (year%100 != 0 or year%400 == 0):
    print("윤년입니다")
else:
    print("윤년이 아닙니다")
'''


# 문제3)
# 교통카드 잔액 9000원에서 나이에 따른 요금(문제1)을 차감하고
# 남은 잔액을 출력하세요.

fee = 0
money = 9000 # 보유한 돈
age = int(input("나이 입력 : "))
if age < 8:
    fee = 0
elif age <= 13:
    fee = 650
elif age <= 18:
    fee = 1050
elif age <= 64:
    fee = 1350
else:
    fee = 0
money = money - fee
print("요금", fee, "잔약", money)

'''퀴즈영역 - cost 변수를 0으로 미리 선언해두면 좋음
cash = 9000 - cost
print(cash)
'''


# 문제4)
# 세 정수를 공백으로 구분해 입력 받아서 가장 큰 수를 출력하세요. (max 함수 사용하지 않기)

a, b, c = map(int, input('정수 3개 (띄어쓰기 구분):').split())
print(a,b,c)
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

big = a
if b > big:
    big = b
if c > big:
    big = c
print(big)
# 뱐수 만들어 사용

print(max(a,b,c)) # 제일 큰 값 찾아주는 함수 - max

'''퀴즈영역 - 조건 중복되는것 잘 확인하여 최적화 하기
i1, i2, i3 = map(int, input("세 정수 공백으로 구분하여 입력:").split())
print(i1, i2, i3)
if i1 >= i2 and i1 >= i3:
    print(i1)
elif i2 >= i3 and i2 >= i1:
    print(i2)
elif i3 >= i1 and i3 >= i2:
    print(i3)
else:
    print("잘못된 입력")
'''