import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
map_ = []
for _ in range(N):
    map_.append(list(map(int, sys.stdin.readline().rstrip().split())))
S, X, Y = map(int, sys.stdin.readline().rstrip().split())

# 바이러스 칸만 추출
virus = [(r, c, 0) for c in range(N) for r in range(N) if map_[r][c] > 0]
virus.sort(key=lambda x: map_[x[0]][x[1]])  # 바이러스 종류 오름차순으로 정렬

step = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque(virus)
while q:
    r, c, time = q.popleft()
    if time == S:
        # S초인 칸이 처음 나왔을 때 바로 탈출
        break
    for dr, dc in step:
        nr = r + dr
        nc = c + dc
        if nr in [-1, N] or nc in [-1, N] or map_[nr][nc] > 0:
            continue
        map_[nr][nc] = map_[r][c]
        q.append((nr, nc, time + 1))

print(map_[X - 1][Y - 1])
