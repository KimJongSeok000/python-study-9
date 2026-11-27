# [파이썬 퀴즈9 - 2차원 리스트]


scores = [
    ['김철수', 90, 85, 77],
    ['이영희', 72, 95, 88],
    ['박민수', 65, 70, 92],
    ['최지우', 98, 89, 94],
]
# (이름, 국어, 영어, 수학)


# 문제1)
# 학생별 총점과 평균을 출력하세요.
# 출력 예) 김철수 총점 252 평균 84.0

for row in scores:
    total = sum(row[1:])
    avg = total / 3
    print(row[0], "총점", total, "평균", avg)

for name, kor, eng, math in scores:
    total = kor + eng + math
    avg = total / 3

''' 퀴즈 영역 - 평균 잘못함, 접근 잘못함
for i in range(len(scores)):
    for j in range(i):
        print(scores[j][0], "총점", sum(scores[j][1:4]),
            "평균", (sum(scores[j][1:4])/3))
print('-'*50)
'''


# 문제2)
# 과목별(국어, 영어, 수학) 평균을 출력하세요.

kor_total = 0
eng_total = 0
math_total = 0
for row in scores:
    kor_total += row[1]
    eng_total += row[2]
    math_total += row[3]
print("국어 평균", kor_total/len(scores))
print("영어 평균", eng_total/len(scores))
print("수학 평균", math_total/len(scores))

''' 퀴즈영역 - 미완성
# for i in range(len(scores)):
#     for j in range(len(scores[0])):
#         print((sum(scores[j][1])/len(scores)))
# print(scores[0][1]+scores[1][1])
'''


# 문제3)
# 총점이 가장 높은 학생의 이름을 출력하세요.

largest = 0
largest_name = ''
for row in scores:
    total = sum(row[1:])
    if total >= largest:
        largest = total
        largest_name = row[0]
print("제일 높은 총점", largest, "1등", largest_name)
print('-'*10)
totals = [sum(row[1:]) for row in scores]
print(total)
max_total = max(totals)
idx_max_total = totals.index(max_total)
print(scores[idx_max_total][0], "1등인 사람")

''' 퀴즈 영역 - 뒤에 s[1:4]에 sum을 붙여야함, 4 안붙여도 됨
h =  max(scores, key=lambda s: s[1:4])
print (h[0])
'''


# 문제4)
# 3행 4열 2차원 리스트를 만들고 아래처럼 1부터 순서대로 채워서 출력하세요.
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

table = []
num = 1
# table[i][i] = num
# num += 1

for i in range(3):
    row = []
    for j in range(4):
        row.append(num)
        num += 1
    table.append(row)
print(table)

table = []
for i in range(3):
    row = []
    for j in range(4):
        row.append(i*4 + (j+1))
    table.append(row)
print(table)

table2 = [[ i*4 + (j+1) for j in range(4)] for i in range(3)]
print(table2)