# [파이썬 퀴즈8 - 리스트]


# 문제1)
# scores = [88, 92, 75, 64, 95, 81, 70]
# - 최고점, 최저점, 평균을 출력하세요.
# - 80점 이상인 점수만 모은 리스트를 만들어 출력하세요. (for 와 리스트 표현식 두 가지 방법)
# - 점수를 높은 순서로 정렬한 새 리스트를 출력하세요. (원본 유지)

scores = [88, 92, 75, 64, 95, 81, 70]
smallest = scores[0]
largest = scores[0]
total = 0
for v in scores:
    if v <= smallest:
        smallest = v
    if v >= largest:
        largest = v
    total = total + v
print("최대", largest, "최소", smallest, "평균", (total/len(scores)))
print("최대", max(scores), "최소", min(scores), "평균", (sum(scores)/len(scores)))

over80 = []
for v in scores:
    if v >= 80:
        over80.append(v)
print(over80)
print([v for v in scores if v >= 80])
over80_2 = [v for v in scores if v >= 80]
print(over80_2)
print(sorted(scores, reverse=True))
print(scores)

''' 퀴즈영역
scores = [88, 92, 75, 64, 95, 81, 70]
print(f'최고점 : {max(scores)}, 최저점 : {min(scores)}, 평균 : {sum(scores)/len(scores)}')

over80 = []
for v in scores:
    if v >= 80:
        over80.append(v)
print("80점 이상 :",over80)

over_80 = [v for v in scores if v>=80]
print("80점 이상 :",over_80)

print(sorted(scores, reverse=True))
print(scores)
'''


# 문제2)
# 공백으로 구분된 단어들을 입력 받아서
# - 단어 개수
# - 가장 긴 단어
# - 길이가 5 이상인 단어만 대문자로 바꾼 리스트
# 를 출력하세요.

inp = input("단어 띄어쓰기 구분해서 입력 : ").split()
print(inp)
# inp = ['apple', 'note', 'book', 'morning', 'afternoon']
print("단어 개수 :", len(inp))
longest = inp[0]
for v in inp:
    if len(v) >= len(longest):
        longest = v
print("가장 긴 단어 :", longest)
# print("가장 긴 단어", max(inp)) - abcd... 알파벳 순으로 max/min을 따진다. 문자를 데이터화는 숫자 매핑(사전)이 있기 때문
print("가장 긴 단어 :", max(inp, key=len)) # key=함수 - 함수를 기준으로 크기를 비교
num = [ 5, 10, -15, 1]
print(max(num))
print(max(num, key=abs)) # abs = 절대값

up5 = []
for v in inp:
    if len(v) >= 5:
        up5.append(v.upper())
print(up5)
up5_2 = [v.upper() for v in inp if len(v) >= 5]
print(up5_2)

''' 퀴즈영역 - 숫자포함되어도 가능
texts = input("공백으로 구분해 단어 입력 :").split()
print(texts)
print("단어 개수 :",len(texts))

longest_text = [texts[0]]
max_len = 0
for v in texts:
    if len(str(v)) > max_len:
        longest_text = [v]
        max_len = len(str(v))
    elif len(str(v)) == max_len:
        longest_text.append(v)
print(longest_text)

text5 = [i.upper() for i in texts if len(i)>=5]
print(text5)
'''


# 문제3)
# 장바구니 프로그램
# cart = []
# 'add 상품명' 을 입력하면 추가, 'del 상품명' 을 입력하면 삭제, 'q' 입력시 종료
# 종료할 때 장바구니 목록을 번호와 함께 출력하세요.

cart = []

while True:
    cmd = input("명령어 입력(add/del/q) 상품명:").split()
    print(cmd)
    if cmd[0] == 'q':
        for idx, value in enumerate(cart):
            print((idx + 1), value) # 장바구니 목록 + 번호
        break
    print(cmd[0], cmd[1]) # if문보다 위에 있고 q만 입력시 에러 발생 IndexError: list index out of range
    if cmd[0] == 'add':
        # 이미 리스트에 있는지 체크
        if cmd[1] in cart:
            print("이미 있는 상품입니다.")
        else : cart.append(cmd[1])
    elif cmd[0] == 'del':
        if cmd[1] in cart:
            cart.remove(cmd[1])
        # cart.remove(cmd[1]) - 옵션 추가하면서 위치 변동
        else : print("없는 상품입니다.")
    else : print("잘못 입력하셨습니다.")


''' 퀴즈영역 - 미완성
item_list = []
while True:
    item = input("add 상품명:추가, del 상품명:삭제. 'q' 입력시 종료:")
    if item[0:3] == "add":
        item_list.append(item[3:])
        break
print(item)
'''

# +옵션1) 이미 있는 상품을 add 하면 '이미 담긴 상품' 출력
# +옵션2) 없는 상품을 del 하면 '없는 상품' 출력