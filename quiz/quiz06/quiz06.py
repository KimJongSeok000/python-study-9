# [파이썬 퀴즈6 - 별찍기]


# 높이를 입력 받아서 아래 모양을 각각 출력하세요. (높이 5 예시)


# 문제1) 역삼각형
# *****
# ****
# ***
# **
# *

# i가 커질때마다 j가 줄어든다
# i:0 j:0 1 2 3 4, i:1 j:0 1 2 3 ...
for i in range(5):
    for j in range(5):
        if j < 5-i:
            print("*", end="")
    print()

for i in range(5):    
    for j in range(5-i):
        print("*", end="")
    print()

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# "*" * 5  -  5회 반복
for i in range(5, 0, -1):
    print("*" * i)

''' 퀴즈 영역 j <= 4 - i 보단 j < 5 - i가 좀 더 간결
for i in range(5):
    for j in range(5):
        if j <= 4 - i:
            print("*", end='')
        else:
            print(" ", end="")
    print()
print()
'''


# 문제2) 피라미드
#     *
#    ***
#   *****
#  *******
# *********

# 5줄 + 4줄 / 4줄 + 5줄로 나눠서 볼 수 있다.
for i in range(5):
    for j in range(5):
        if j < 4 - i:
            print(" ", end="")
        else:
            print("*", end="")
    for k in range(i): # 0 1 2 3 4
        print("*", end="")
    print()

# 띄어쓰기 4 3 2 1 0 "*"출력 1 3 5 7 9
for i in range(5):
    # 띄어쓰기
    for j in range(4-i): # 4-0 4-1 4-2 4-3 4-4
        print(" ", end="")
    # 출력
    for k in range(2*i +1):
        print("*", end="")
    print()
print()
# i: 4 3 2 1 0      K: 9 - 2*i
for i in range(4, -1, -1):
    for j in range(i):
        print(" ", end="")
    for k in range(9 - 2*i):
            print("*", end="")
    print()

# 띄어쓰기 4일때 *는 1, 3일때 3, 2일때, 5 ...
for i in range(5):
    print(" "*(4-i) + "*"*(2*i + 1))

'''퀴즈영역
for i in range(5):
    for j in range(4): # 5로 하면 맨 앞에 공백이 하나씩 생김
        if i<4-j: # 여기도 5 말고 4로 맞춘다
            print(" ", end="")
        else:
            print("*", end="")
    for k in range(5):
        if i<k:
            print(" ", end="")
        else:
            print("*", end="")
    print()
print()
'''

n = int(input("숫자 입력:"))
for i in range(n):
    for j in range(n-i): # 4-0 4-1 4-2 4-3 4-4
        print(" ", end="")
    print()
for i in range(n):
    print(" "*((n-1)-i) + '*'*(2*i + 1))

print("-"*50)
# 문제3) 역피라미드 (문제2 를 뒤집은 모양)
for i in range(n-2, -1, -1):
    print(" "*((n-1)-i) + '*'*(2*i + 1))

print("-"*50)
# 문제4) 다이아몬드 (문제2 + 문제3, 가운데 줄은 한 번만)
for i in range(n):
    print(" "*((n-1)-i) + '*'*(2*i + 1))
for i in range(n-2, -1, -1):
    print(" "*((n-1)-i) + '*'*(2*i + 1))
