
s = 'Hello, World!'
# 문자 바꾸기 (대체하기) replace(대상, 바꿀 값)
print(s.replace("World!", "Good")) # 원본 유지, 비파괴적
print(s)
s = s.replace("World!", "Good") # 원본 변경
print(s)

# 분리/합치기       split / join
words = "apple kiwi banana melon".split()
print(words)
print("apple,kiwi,banana,melon".split(','))

# 구분자.join(리스트)
print("-".join(words))
print("/".join(words))
print("".join(words))

# 대소문자
print("hello".upper())
print("GREAT".lower())
print('hello great'.title())
print('hello great'.capitalize())

# 공백제거 - 입력값 정리
text = '  wonderful   '
print('[', text  , ']')
print('[',   text.strip(),   ']')
print('[',   text.lstrip(),   ']')
print('[',   text.rstrip(),   ']')
print('[',   ".  this is text!!!".strip('.!')  , ']') # 양쪽 끝에있는 지정한 문자를 정리(공백포함)

# 문자열 폭 정렬 ()안의 숫자만큼 차지하며 정렬
print('[', "python".ljust(10) , ']')
print('[', "python".rjust(10) , ']')
print('[', "python".center(10) , ']')
print('[', "python".zfill(10) , ']') # 빈 공간 앞을 0으로 채운다
# f ' [2:0>5 ] '
print("2".zfill(2))
print('[', "python".ljust(10, "*") , ']')

# 문자 찾기
s = 'apple pineapple'
print(s.find('pl')) # 앞에서부터 찾아서 가장 먼저 찾은 위치
print(s.rfind('pl')) # 오른쪽에서부터 찾기
print(s.find('ex')) # 없으면 -1     if 찾은 결과 -1 ==: 없다
print(s.index('pl')) # 찾은 인덱스
# print(s.index('ex')) - 없으면(못찾으면) ValueError: substring not found에러 발생
print(s.count('p')) # 개수 찾기

# 시작 끝 확인
file_name = 'report.xlsx'
print(file_name.startswith('report')) # True
print(file_name.endswith('.xlsx')) # True
print(file_name.endswith('.pptx')) # False

# 문자 타입 종류 판단
print( '1234'.isdigit()) # True - 숫자형태임
print(int('1234'))
print( '12q34'.isdigit()) # False - 숫자형태가 아님
# print( int('12q34')) - ValueError: invalid literal for int() with base 10: '12q34'
print( '1234'.isalpha()) # False - 알파벳 형태가 아님
print( 'abcd'.isalpha()) # True - 알파벳 형태임
print( '1234'.isalnum()) # True 숫자 or 알파벳 형태임
print( 'abcd'.isalnum()) # True 숫자 or 알파벳 형태임
print( '1234abcd!@#$'.isalnum()) # True 숫자 or 알파벳가 아님

# 메소드 체이닝 (이어붙여서 수행)
raw = '  Hello, Python    '
raw = raw.strip()
raw = raw.lower()
raw = raw.replace('python', 'world')
print(raw)

raw2 = '      Hello, Python    '
raw2 = raw2.strip().lower().replace('python', 'world2')
print(raw2)

# 입력 한번에 정리
email = input("이메일: ").strip().lower() # 공백제거, 소문자로
print(email)
user_id, domaim = email.split('@')
print(user_id, domaim)
