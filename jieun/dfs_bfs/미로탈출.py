from collections import deque

N, M = map(int, input().split())
map_ = []  # ["행"] , 0: 괴물 있음, 1: 괴물 없음
for _ in range(N):
    map_.append(input())

# visited[r][c] = (r,c)까지 가는데 방문한 최소 칸 개수. 시작 칸, (r,c)칸 포함.
visited = [[0 for _ in range(M)] for _ in range(N)]
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상하좌우 인접 칸 상대 위치

q = deque()

# 문제 인덱스에서 1 빼기
# 시작: (0,0), 끝: (N-1, M-1)
q.append((0, 0))
visited[0][0] = 1

# bfs
while q:
    r, c = q.popleft()
    if r == N - 1 and c == M - 1:
        break
    for dr, dc in steps:
        nr = r + dr
        nc = c + dc
        if (
            0 <= nr and nr < N
            and 0 <= nc and nc < M
            and map_[nr][nc] == "1"
            and visited[nr][nc] == 0
        ):
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))

print(visited[N - 1][M - 1])
