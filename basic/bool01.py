
# 불(bool) 자료형(boolean)
#   참 | 거짓
# True | False

print(True, False)
# print(true, false) - 소문자는 변수명으로 인식함
print(type(True)) # <class 'bool'>

# 비교연산자 -> 결과 True | False
print( 10 == 10)
print( 10 != 10)
print( 10 > 20)
print( 10 < 20)
print( 10 >= 10)
print( 10 <= 4)

# 문자열 비교
print( 'Python' == 'Python' )
print( 'Python' == 'python' )
print( 'Python' != 'python' )

# 값을 비교할 때 ==, 객체를 비교할 때 is
n1 = 1
n2 = 1.0
print(n1 == n2)
print(type(n1) == type(n2)) # int == float
# print(n1 is n2) 수치를 비교하는게 아니라 객체를 비교하는거라 의미가 다름
print(type(n1) is type(n2)) # int is float

x = None
print( x == None )
print( x is None ) # None 비교시 is 사용할 것

# 논리연산자 and or not
print(True and True)
print((1==1) and (2>1))
print(False or True)
print(not True)
print(not False)

age = 25
print( age >= 20 and age < 30)
print( 20 <= age < 30) # 파이썬은 해당 방식 사용가능, 대부분의 다른 언어는 따로 묶어서 사용
print( age > 10 or age < 100 )

# 정수, 실수 ,문자열을 bool로 연결
print( bool(1), bool(0) ) # 1->True
print( bool(501), bool(-20) ) # 숫자형은 0을 False로 인식, 나머지 숫자를 Treu로 인식
print( bool(5.5), bool(0.0) )
print( bool("a"), bool(" "), bool("") ) # 빈 문자열을 False로 인식
print( bool([]), bool([1,2,3]) ) # 빈 리스트를 False로 인식

# && ||
print(False and 'abc')
print(True and 'abc') # {True && <요소>}
print(False or "def")