
import sys
sys.setrecursionlimit(10**7)

t = int(input())


def countSheep():
    n, m = map(int, input().split())

    graph = []

    for i in range(n):
        graph.append(list(input()))

    def dfs(x, y):
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False

        if graph[x][y] == '#':
            graph[x][y] = '.'

            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            return True
        return False

    count = 0

    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                count += 1

    print(count)


for i in range(t):
    countSheep()
