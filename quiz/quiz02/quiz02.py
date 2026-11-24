
# [파이썬 퀴즈2 - 시퀀스]


# 문제1)
url = 'https://www.python.org/downloads'
# 위 문자열에서 슬라이스를 사용해 아래 값을 꺼내 출력하세요.
# - 'https'
# - 'www.python.org'
# - 'downloads'
print(url[0:5]) # print(url[0:5:1]), print(url[:5])
print(url[8:22])
print(url[-9:]) # print(url[23:]), print(url[23:len(url)])

# 문제2)
n = [-32, 5, 2, -10, 55, 7, 9, 0]
# - 홀수 번째 인덱스(1, 3, 5 ...)의 요소만 출력하세요.
# - 마지막 3개 요소를 출력하세요.
# - 리스트를 거꾸로 뒤집어서 출력하세요.
print(n[1::2]) # print(n[1:len(n):2])
print(n[-3:]) # print(n[5:])
print(n[::-1])

# 문제3)
# 날짜 문자열 '20261102' 를 입력 받아서 2026년 11월 02일 로 출력하세요.
date = input("날짜를 입력(YYYYMMDD) : ")
print(date[:4], "년 ", date[4:6],"월 ", date[6:], "일", sep="") # date[-2:]
print(f'{date[:4]}년 {date[4:6]}월 {date[6:]}일')
'''
퀴즈영역 - 입력받아서라고 했으므로 고정말고 input 사용이 적절
today = '20261102' # date ='20261102'
print(today[0:4] + "년 " + today[4:6] + "월 " + today[6:8] + "일")
'''

# 문제4)
year = (2021, 2022, 2023, 2024, 2025, 2026)
population = (10249679, 10195318, 10143645, 9994195, 9886021, 9810000)
# 최근 3년간의 연도와 인구 수를 출력하세요. (음수 인덱스 사용)
print(year[-3:])
print(population[-3:])
'''
print( str(year[-1])+"년", str(population[-1])+"명")
print( str(year[-2])+"년", str(population[-2])+"명")
print( str(year[-3])+"년", str(population[-3])+"명")
print( year[-3:], population[-3:])
'''