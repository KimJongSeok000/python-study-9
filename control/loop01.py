
# 중첩 반복문

for i in range(3):
    for j in range(4):
        print(i, j)
print()

for i in range(3):
    for j in range(4):
        print(i)
print()

for i in range(3):
    for j in range(4):
        print(j)
print()

for _ in range(5):
    print('*', end="")
print()

for i in range(5): # 행
    for j in range(4): # 열
        print('*', end='')
    print()
print()

for i in range(3):
    print('*'*10)
print()


for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()
print()
# 횟수로 따지면 5번 반복

for i in range(5): # i:0 1 2 3 4  횟수:1 2 3 4 5 - i+1
    print('*'*(i+1))
print()

for i in range(5):
    for j in range(5):
        if i == j:
            print("*",end='')
        else:
            print(" ", end="")
    print()
print()

for i in range(5):
    for j in range(5):
        if j < 4 - i:
            print(' ',end='')
        else:
            print("*", end='')
    print()
print()

# 중첩 반복문 - 구구단
# 2단 ~ 9단 - *1 ~ *9

for x in range(2, 10):
    print(x, "단")
    for y in range(1, 10):
        # print(x, "단") - 2단 2 x 1 = 2 \n 2단 2 x 2 = 4... 어디서 실행되는지 잘 볼 것.
        print(f'{x} x {y} = {x*y}')
    print('-'*10)
print()