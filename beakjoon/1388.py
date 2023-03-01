"""
#깊이 우선 탐색

def dfs

-- 같은행
ㅣ
ㅣ 같은 열

"""


def dfs_horizontal(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == "-":

        graph[x][y] = "x"

        dfs_horizontal(x, y - 1)
        dfs_horizontal(x, y + 1)

        return True
    return False


def dfs_vertical(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == "|":

        graph[x][y] = "x"

        dfs_vertical(x - 1, y)
        dfs_vertical(x + 1, y)

        return True
    return False


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input()))

count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == "-":
            dfs_horizontal(i, j)
            count += 1
        elif graph[i][j] == "|":
            dfs_vertical(i, j)
            count += 1


print(count)
