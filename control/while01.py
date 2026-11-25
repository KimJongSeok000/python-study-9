
# 초기화 -> 조건식 -> 코드실행문 -> 증감식(변환식) -> 조건식 -> 코드실행문 -> ...

i = 0
while i < 5:
    print(i)
    i = i + 1

i = 10
while i > 0:
    print(i, end=' ')
    i = i - 1 # ++ -- 같은 연산자는 불가능. i -= 1 같은 복합연산자는 가능
    # --i  = -(-i)
    # ++i  = +(+i)
print()

# count = int(input("숫자입력:"))
count = 0
while count > 0:
    print(count, end=" ")
    count = count - 1
print()

# 몇번 돌리겠다 범위지정엔 for문이, 일단 반복은 while문이 유리하다
# 랜덤
import random
print(random.randint(1, 6)) # 1 ~ 6 사이의 랜덤값
print(random.randint(1, 45)) # 1 ~ 45 사이의 랜덤값

dice = 0
while dice != 3: # 특정 조건이 만족할때 끝 (사전에 몇번 반복할지 확정짓기 힘든 경우)
    dice = random.randint(1,6) # 주사위 굴리기
    print("dice", dice)

# 입력값이 0이 될 때까지 입력된 모든 수의 합
# break  - 종료
total = 0
while True:
    num = int(input("숫자입력(0입력시종료):"))
    total = total + num
    if num == 0:
        break
print("총 합계", total)

