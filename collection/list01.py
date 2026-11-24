
# 리스트와 튜플

# 리스트(list) : 대괄호 [] 형태로 여러 값을 묶어서 저장
a = [12.34,67,22]
print(a)
print(type(a)) # <class 'list'>

# 자료형 상관없이 함께 저장가능
person = ["홍길동", 25, 175.5, True]
print(person)

# 빈 리스트
b = []
c = list()
print(b, c)

# range() 함수를 활용해 리스트 만들기. range(start, stop, step) - start>=, stop<
print( list(range(10))) # 0에서 9까지
print( list(range(5, 12))) # 5부터 11까지
print( list(range(0, 20, 2))) # 0부터 18까지 2씩 증가
print( list(range(10, 0, -1))) # 10부터 1까지 1씩 감소

# 튜플 : 소괄호 () 형태로 묶어서 값을 저장. 생성 후 값 변경 불가
t = (11,22,33,44)
print(t)
print(type(t)) # <class 'tuple'>

t2 = 11, 22, 33 # 튜플로 저장됨
print(t2)

t3 = (38) # 그냥 정수
print(t3)
t4 = (38,) # 튜플로 인식
print(t4)

# 리스트는 값 변경 가능, 튜플은 불가능
print(a[1])
print(t[2])
a[1] = 99
print(a[1])
# t[2] = 88 #TypeError: 'tuple' object does not support item assignment

# a:list, t:tuple
# list/tuple 변환
print( tuple(a) )
print( list(t) )

print( list('Hello')) # 문자열 분해해서 한글자씩 리스트로만든다

x, y, z = [10, 20, 30]
q, w = (40, 50)
print(x, y, z, q, w)