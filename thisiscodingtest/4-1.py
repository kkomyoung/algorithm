# 상하좌우

"""
시작점은
x = 1
y = 1

y 증감
R - 오른쪽 한칸 이동 / y가 N일 경우 무시
L - 왼쪽 한칸 이동 / y가 1일 경우 무시

x 증감
U - 위 한칸 이동 / x가 1일 경우 무시
D - 아래 한칸 이동 / x가 N일 경우 무시 

# 입력예시
5
R R R U D D

# 출력예시
3 4
"""

N = int(input())
step = list(input().split())

x = 1
y = 1

for i in range(len(step)):
    if(step[i] == 'R'):
        if(y < N):
            y += 1
    elif(step[i] == 'L'):
        if(y > 1):
            y -= 1
    elif(step[i] == 'U'):
        if(x > 1):
            x -= 1
    elif(step[i] == 'D'):
        if(x < N):
            x += 1

print(x, y)


