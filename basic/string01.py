
hello = "Hello, World!"
hi = "안녕하세요"

print(hello)
print(hi)
print(type(hi))

s1 = "my name's ..."
s2 = 'hi"hello"'
s3 = '큰"따옴표 작은\'\"따옴표' # \' 이스케이프 문자. \n : 줄바꿈
print(s1)
print(s2)
print(s3)

# 여러줄 문자열 - 작은 따옴표는 주석으로 쓰기도 한다
s4 = '''
    여러줄
    문자열을
    나타낼때
    사용할 수 있다
'''
print(s4)
s5 = """
    여러줄
    문자열을
    나타낼때
    "큰따옴표가능
"""
print(s5)

# 이스케이프 문자
print('줄바꿈\n문자')
print('탭 띄어쓰기\t문자')
print('역슬레시 \\ \\ 문자')

# 문자열 연산
a = "hello"
b = "world"

print(a + b)
print(a + ' ' + b)
print(a, b, sep=" ")
print( a * 3) # 반복의 의미
print('-' * 30) # 구분선 역할

# 문자함수
print(len(a))
print(len("글자길이찾아봐라"))
print('ll' in a) # ll이라는 문자가 a 안에 있느냐
print('ll' in b)
print('ll' not in b) # ll이라는 문자가 b 안에 없느냐

num = '123'
print(int(num) + 123)
print(str(12) + "456")
