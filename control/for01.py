
# for 반복문 - range 사용
# for 변수 in range():

for i in range(5):
    print(i)
for i in range(3,10):
    print(i, end=" ")
print() # end로 인해 뒤에 오는것도 붙어서 출력되므로 for문 밖에서 줄바꿈처리
for i in range(0, 20, 2):
    print(i, end=' ')
print()
for i in range(10, 0, -1):
    print(i , end=' ')
print()

for i in reversed(range(0, 10)): # reversed - 뒤집어 배열하는 함수
    print(i, end=' ')
print()

# 입력 활용
count = int(input("횟수입력:"))
for i in range(count):
    print(i, end=' ')
print()

# 합계 1 ~ 100 합계
sum = 0
for i in range(1, 101):
    sum = sum + i
print("총합", sum)

# 반복문 사용. 구조 자료형으로 사용 가능 : 리스트, 튜플, 문자형  (시퀀스)
fruits = ["사과", "바나나", "딸기"]
for fruit in fruits:
    print(fruit)
for ch in 'pyton':
    print(ch, end=' ')
print()

# 인덱스 형태로 접근
for i in range(len(fruits)):
    print(i, fruits[i])

for idx, item in enumerate(fruits): # enumerate - 값을 pairs(쌍)로 돌려준다. 앞이 인덱스 뒤가 밸류
    print(idx, item)

# 구구단 2단 출력
for i in range(1, 10):
    print(f'2 X {i} = {2*i}')

# 안쓰는 값 _
for _ in range(10):
    print('*', end='')
print()