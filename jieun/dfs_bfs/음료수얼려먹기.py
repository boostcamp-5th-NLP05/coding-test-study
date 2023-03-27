from collections import deque

N, M = map(int, input().split())
map_ = []  # ["행"], 0: 구멍, 1: 칸막이
for _ in range(N):
    map_.append(input())

visited = [[False for _ in range(M)] for _ in range(N)]  # 방문 여부 기록
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상하좌우 인접 칸 상대 위치


def bfs(sr, sc):
    # (sr,sc)와 연결된 모든 칸을 방문한다.
    q = deque()
    visited[sr][sc] = True
    q.append((sr, sc))
    while q:
        r, c = q.popleft()
        for dr, dc in steps:
            nr = r + dr
            nc = c + dc
            if (
                0 <= nr and nr < N
                and 0 <= nc and nc < M
                and map_[nr][nc] == "0"
                and not visited[nr][nc]
            ):
                # map_ 범위 안에 속하고, 구멍이고, 방문하지 않은 칸이면
                visited[nr][nc] = True
                q.append((nr, nc))


ans = 0
for i in range(N):
    for j in range(M):
        if map_[i][j] == "0" and not visited[i][j]:
            # 구멍이고, 방문하지 않은 칸이면
            ans += 1
            bfs(i, j)  # 해당 아이스크림에 속하는 칸 전체를 찾는다.

print(ans)
