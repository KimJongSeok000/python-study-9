# [파이썬 퀴즈7 - 제어문 종합 : 업다운 숫자 맞추기 게임]


# 1 ~ 100 사이 랜덤 숫자를 하나 정하고
# 사용자가 숫자를 입력하면 'UP' / 'DOWN' 힌트를 주세요.
# 맞추면 몇 번 만에 맞췄는지 출력하고 종료합니다.
# +옵션1) 기회는 7번. 7번 안에 못 맞추면 정답을 알려주고 종료
# +옵션2) 1 ~ 100 범위를 벗어난 입력은 기회를 차감하지 않고 다시 입력 받기
import random
answer = random.randint(1, 100) # 1 ~ 100 랜덤값
count = 0
print(answer)
while True:
    #사용자가 숫자를 입력
    num = int(input("숫자 입력 (1~100): "))
    # 정상 범위 벗어나면 필터링
    # if num < 1 or num > 100:
    if not (1 <= num <= 100):
        print("잘못입력하셨습니다. 1~100사이의 값 입력")
        continue
    count += 1
    # if count == 7: 6번째에서 걸림
    #     print("기회 7번 모두 소진, 정답은 ", answer)
    #     break
    #정답에 맞는지, UP, DOWN인지
    if num == answer:
        print(answer, "정답입니다!")
        print(count, "회 만에 맞췄습니다!")
        break
    elif num > answer:
        print("DOWN")
    elif num < answer:
        print("UP")
    if count == 7:
        print("기회 7번 모두 소진, 정답은 ", answer)
        break
# print("기회 7번 모두 소진, 정답은 ", answer) - 이미 끝났으므로 밖에서 출력해도 됨

    #출력
    #정답이면 종료
    #들리면 돌아가서 입력부터 재시도

''' 퀴즈영역
import random
n = random.randint(1, 100)
count = 0
while True:
    i = int(input(f'1~100 숫자 UP or DOWN! 기회는 {7-count}번) : '))
    count += 1
    if not 0 < i <= 100:
        continue
    elif count == 7:
        print(f'7번의 기회 끝. 정답은 {n}')
        break
    elif i<n:
        print("UP")
    elif i>n:
        print("DOWN")
    else:
        print(f'{count}번 만에 정답! 정답은 {n}')
        break
'''