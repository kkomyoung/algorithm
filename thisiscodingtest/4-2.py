# 시각 p.113

"""
0~24시
0분~60분
0초~60초
"""

N = int(input())
count = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
    




