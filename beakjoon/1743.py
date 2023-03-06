
"""
3 4 5
3 2
2 2
3 1
2 3
1 1

# . . .
. # # .
# # . .
"""
import sys
sys.setrecursionlimit(10**7)

n, m, k = map(int, input().split())

graph = [['.'] * m for _ in range(n)]

# 음쓰 떨어진 부분포함한 그래프
for _ in range(k):
    i, j = map(int, input().split())

    graph[i-1][j-1] = '#'

# 음쓰 크기
global size
size = 0


def dfs(x, y):
    global size

    if (x <= -1 or x >= n or y <= -1 or y >= m):
        return False

    if (graph[x][y] == '#'):
        size += 1
        graph[x][y] = '.'
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

        return True

    return False


result = []

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result.append(size)
            size = 0

print(max(result))
