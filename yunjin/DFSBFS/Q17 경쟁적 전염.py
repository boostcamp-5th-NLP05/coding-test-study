from collections import deque

N, K = map(int, input().split())
map_ = [list(map(int, input().split())) for i in range(N)]
S, X, Y = map(int, input().split())

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

orders = []

for r in range(N):
    for c in range(N):
        if map_[r][c] != 0:
            orders.append((r, c, 0, map_[r][c]))

# 숫자 순으로 정렬
orders = sorted(orders, key=lambda x: x[3])
orders = deque(orders)


# 적은 초, 작은 숫자 부터 증식하므로 규칙을 만족하게 된다.
def BFS(orders):
    global map_

    while orders:
        r, c, dep, num = orders.popleft()

        # S 시간 까지 퍼지고 다음엔 진행이 안되어야 하므로 S 에서 멈춘다.
        if dep == S :
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if map_[nr][nc] == 0:
                map_[nr][nc] = num  # BFS 로직에 따라 우선순위 바이러스가 공간을 먼저 차지함.
                orders.append((nr, nc, dep + 1, num))


BFS(orders)

print(map_[X - 1][Y - 1])  # S 초후 (X,Y) 에 존재하는 바이러스