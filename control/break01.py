
# break 멈추기
# continue 계속 진행(다음 턴으로 건너뛰기)

i = 1
while True:
    print(i)
    if i==5:
        break
    i=i+1
# break 시점이 어디냐에 따라 값이 달라질 수 있다.
print('-'*50)
for i in range(100):
    print(i)
    if i == 7:
        break

for i in range(1, 11):
    if i == 5:
        break
    print(i, end=' ')
print()

for i in range(1, 11):
    if i == 5:
        continue # 건너뛰기(skip)
    print(i, end=' ')
print()

i = 0
while i<10:
    i = i+1
    if i%2 == 0:
        continue
    print(i, end=" ")
    # i = i+1  - 반복의 조건식이 거짓이 되는 케이스를 만드는 기존 변수의 변화 continue 앞|뒤
    # 해당 위치에 오면 i = 0으로 i<10이 참이되는 무한순환이 됨
print()

# 메뉴 선택 반복 : 반복으로 입력을 받고 q를 입력하면 종료
while True:
    cmd = input("명령어 입력(q 입력시 종료):")
    if cmd == 'q':
        break
    if cmd == '':
        continue # 빈 입력 무시
    print("입력한 명령어:", cmd)

# for else      while else
# 해당 반복이 끝까지 다 돌면 else도 실행
for n in [1,3,5,7]:
    if n%2 == 0:
        print("짝수 발견")
        break
    # else 여기 들여쓰기에 쓰면 if에 엮인 else
else: # for에 엮인 else
    print("짝수가 없다")