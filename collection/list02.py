
# 리스트 조작
a = [10, 20, 30]
a.append(40) # 뒤에 추가
print(a)

# 함수 메소드
# 메소드 : 특정 객체에 속한 함수

a.append( [100, 200] )
print(a) # [10, 20, 30, 40, [100, 200]] - 리스트 안에 리스트가 중첩된 형태
print(a[4]) # [100, 200]
print(a[4][0]) # 100

print(len(a)) # 5

b = [1,2,3]
# b.append([4,5])
b = [1,2,3] + [4,5]
print(b)

# 리스트를 연결해서 확장
b.extend([6,7,8])
print(b)

# 특정 위치의 추가 insert
c = [10,20,30]
c.insert(1, 500) # 1인덱스에 추가
print(c)
c.insert(0, 100) # 앞에 추가
c.insert(len(c), 900) # 뒤에 추가
print(c)

# 리스트 요소 삭제
d = [10,20,30]
print(d)
print(d.pop()) # 제일 뒤의 요소를 삭제하면서 반환(return)한다
print(d)
print(d.pop(0)) # 제일 앞 요소 삭제후 반환 - pop(index)
print(d)

# 값으로 요소 삭제
e = [10,20,30,40,20]
e.remove(30)
print(e)
# e.remove(50) 없는 값. ValueError: list.remove(x): x not in list
e.remove(20) # 처음 나오는 값 한개만 삭제
print(e)

# 겁색
e = [10,20,30,40,20]
print(e.index(30)) # 해당 값이 위치한 인덱스를 반환
# print(e.index(50)) 없는 값. ValueError: list.index(x): x not in list
print(e.count(20)) # 해당 값의 개수

# 뒤집기
e.reverse()
print(e)

# 정렬
e.sort() # 리스트를 오름차순으로 정령
print(e)
e = [1,6,3,62,8,9,10]
e.sort(reverse=True) # 리스트를 내림차순으로 정렬. False는 기본값이라 사용X
print(e)

# sorted() vs sort()
q = [7,9,1,2,3,5,8,6]
# q.sort() 원본 리스트를 그대로 정렬
w = sorted(q) # 정렬을 해서 정렬된 리스트를 반환(return), 새로운 리스트 반환(원본유지)
print(q)
print(w)
e = sorted(q, reverse=True)
print(e)
q.sort() 
print(q)

print(sorted(q, reverse=True))
print(e.sort()) # None - e.sort()는 내부적으로 정렬을 할 뿐 반환(return)이 없음
print(e)

# 모든 요소 삭제
e.clear()
print(e) # []  -  빈 리스트

# 복사
a = [1,2,3,4] # 참조타입변수라 주소값임
b = a # 실제 복사가된 것이 아님
print(a is b) # 같은 주소를 가진 객체, True
a[0] = 99 # a, b 둘 다 바뀐것으로 출력
print(a)
print(b)

a = [1,2,3,4]
b = a.copy()
c = a[:]
d = a[::-1]
print(a == b) # [1,2,3,4]로 값은 동일 True
print(a is b) # 같은 객체인가? False - 새로운 주소로 만들어졌기때문
a[0] = 99
print(a, b, c, d)
