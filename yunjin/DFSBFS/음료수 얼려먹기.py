import sys
from collections import deque

N, M = map(int, input().split())

# 맵 선언
map_ = []
for i in range(N):
    map_.append(list(map(int, str(input()))))

# 방문 배열
visited = [[False for col in range(M)] for row in range(N)]

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def BFS(r, c):
    d = deque()
    d.append((r, c))
    visited[r][c] = True

    while d:
        r, c = d.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 밖으로는 안됨
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if map_[nr][nc] == map_[r][c] and not visited[nr][nc]:
                d.append((nr, nc))
                visited[nr][nc] = True


icecream_cnt = 0
for r in range(N):
    for c in range(M):
        if map_[r][c] == 0 and not visited[r][c]:
            BFS(r, c)
            icecream_cnt += 1

print(icecream_cnt)