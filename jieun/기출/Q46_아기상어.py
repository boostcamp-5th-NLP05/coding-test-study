# 백준 16236 정답: 33324 KB, 64ms
import sys
import heapq

N = int(sys.stdin.readline().rstrip())
space = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

INF = int(1e9)

time = 0
size = 2
ate = 0
baby = None  # (r,c)
for r in range(N):
    for c in range(N):
        if space[r][c] == 9:
            baby = (r, c)
            space[r][c] = INF

steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_food(baby, size, space):
    # 다음에 먹을 물고기 위치와 거기까지 가는 이동 시간 반환

    vis = [[False for _ in range(N)] for _ in range(N)]
    q = []

    heapq.heappush(q, (0, baby[0], baby[1]))
    # 거리, r, c 오름차순 정렬
    vis[baby[0]][baby[1]] = True
    res = (-1, -1)
    dur = 0
    while q:
        dist, r, c = heapq.heappop(q)
        if space[r][c] > 0 and space[r][c] < size:
            # 상어 크기보다 작은 물고기 위치 발견
            res = (r, c)
            dur = dist
            break
        for dr, dc in steps:
            nr = r + dr
            nc = c + dc
            if nr in [-1, N] or nc in [-1, N]:
                continue
            if vis[nr][nc] or size < space[nr][nc]:
                # 방문한 칸이거나 상어 크기보다 큰 물고기면
                continue
            heapq.heappush(q, (dist + 1, nr, nc))
            vis[nr][nc] = True

    return res, dur


while True:
    food, duration = find_food(baby, size, space)

    if food[0] == -1:
        break

    space[baby[0]][baby[1]] = 0  # 상어가 기존에 위치한 칸
    baby = food
    space[baby[0]][baby[1]] = INF  # 상어가 새로 이동한 칸

    ate += 1
    if size == ate:  # 상어 크기만큼 물고기 먹었으면
        size += 1
        ate = 0  # 먹은 개수 리셋

    time += duration

print(time)
