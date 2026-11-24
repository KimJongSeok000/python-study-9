# 문제1)
# 사각형의 가로, 세로 길이를 한 줄에 공백으로 구분해서 입력 받고
# 넓이와 둘레를 아래처럼 출력하세요.
# 입력 예) 10 5
# 출력 예)
# 넓이 : 50
# 둘레 : 30

# 강의영역
width, height = input("가로 세로 입력 : ").split()
width = int(width)
height = int(height)
area = width * height
perm = (width+height)*2
print("넓이 :", area)
print("둘레 :", perm)
'''
퀴즈영역
width, height = map(int, input("가로 세로 : ").split())
print("넓이 :", (width * height))
print("둘레 :", (width + height)*2)
'''

# 문제2)
# 국어, 영어, 수학 점수를 콤마로 구분해서 입력 받고
# 총점과 평균(소수점 둘째 자리까지)을 출력하세요.
# 입력 예) 90,85,77
# 출력 예) 총점 252, 평균 84.0

# 강의영역
kor, eng, math = map(int, input("국어, 영어, 수학 점수를 콤마로 구분해서 입력 :").split(","))
total = kor + eng + math
avg = total/3
print("총점 ", total, ", 평균", round(avg, 2))
# print(f'총점 {total}, 평균{round(avg, 2)}')
# print(f'총점 {total}, 평균{avg:.2f}')
# print("총점 ", total, end=", ")
# print("평균", round(avg, 2))
'''
퀴즈영역
kor, eng, mat = map(int, input("국어, 영어, 수학 : ").split(','))
total = kor + eng + mat
ave = round(total/3, 2)
print(f'총점 {total}, 평균 {ave}')
'''


# 문제3)
# 초(second)를 입력 받아서 '몇 시간 몇 분 몇 초' 로 출력하세요.
# 입력 예) 3725
# 출력 예) 1시간 2분 5초

# 1초 1분=60초 5분=300초 1시간=3600초
# 강의영역
inp = int(input("초를 입력 : "))
hour = inp//3600
minute = (inp%3600)//60
second = (inp%3600)%60  #minute%60
# hour = inp//3600
# inp = inp%3600
# minute = inp//60
# inp = inp%60
# second = inp
print(f'{hour}시간 {minute}분 {second}초')

'''
퀴즈영역 - minute 오타수정, 변수 지정 수정(분 계산을 hour%60으로 해버림)
sec = input("초(second) 입력 : ")
sec = int(sec)
hour = sec//3600
minute = (sec%3600)//60
second = minite%60
print(f'{hour}시간 {minute}분 {second}초')
'''

# 문제4)
# 년, 월, 일을 입력 받아서 sep 을 사용해 2026/11/02 형태로 출력하세요.
# 강의영역
year, month, day = input("년 월 일 입력 :").split()
print(year, month, day, sep='/')
print(f'{year}{month:0>2}/{day:0>2}') # 월/일 자리수 2자리로 맞추기, :는 붙을 위치, 0은 채울 값, 2는 2자리
print(year, month.zfill(2), day.zfill(2), sep='/') # zfill 함수 사용. ()안의 숫자로 자리수 맞춤
# int() 숫자형태로
#{day:02d}
'''
퀴즈영역
year, month, day = input("년, 월, 일 :").split(',')
print(year, month, day, sep='/')
'''