
from collections import deque

n = int(input())


graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 방문 유무 확인 배열
visited = [[False]*n for _ in range(n)]

print(visited)

# 이동할 방향
dx = [1, 0]
dy = [0, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:

        # 쩰리가 지금 밟고 있는 곳
        x, y = queue.popleft()

        if graph[x][y] == -1:
            return True

        # 오른쪽, 아래쪽 두 방향 위치 확인
        for i in range(2):
            # graph[x][y] : 갈 수 있는 칸
            nx = x + dx[i] * graph[x][y]
            ny = y + dy[i] * graph[x][y]

            # 공간 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            # 방문 한 곳인 경우 무시
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])


print("HaruHaru" if bfs(0, 0) else "Hing")
