
print('basic01.py')

# 1. 주석
# 앞에 #을 붙이면 그 라인은 주석

# 여러줄 주석은
'''
이렇게 사용하면
여러줄 주석으로
사용할 수 있다
'''

print('hello') # 뒤에 #부터 다시 주석

# 2. 세미콜론
# 세미콜론 안붙여도 오류나지 않음
print("hellow1");
print("hellow2")
print("hellow3")
print("hellow4"); print("hellow5") # 한줄에 여러문장 사용시에 ; 사용

# 3. 들여쓰기
# 구역, 범위를 나타낼때 사용하던 {} 대신에 들여쓰기 사용
# 들여쓰기는 tap 눌러서 적용 (공백 4칸)

print("들여쓰기")
    #print("들여쓰기") 의미없이 들여쓰기 x

x = 10 # 변수 선언
print(x)
if x == 10:
    print("x 는 10")
    print("들여쓰기 내부 범위")
    # if문 내부에 속한 코드 블록

print("여기는 if문 밖")

# 4. 코드 불록
if x > 5:
    print("5보다 크다")
    if x > 8:
        print("8보다 크다")
    print("x>5 블록")

if x > 100:
    pass # if문블록 안에 아무것도 없으면 에러가 발생하므로 pass 키워드로 자리 채워두기

print("if문 다음")