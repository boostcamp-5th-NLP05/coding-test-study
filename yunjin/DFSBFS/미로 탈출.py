from collections import deque

N, M = map(int, input().split())

map_ = []
for i in range(N):
    map_.append(list(map(int, str(input()))))

visited = [[False for c in range(M)] for r in range(N)]

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def BFS(row, col, time):
    d = deque()
    d.append((row, col, time))
    visited[row][col] = True

    while d:
        r, c, t = d.popleft()

        # 탈출 지점
        if r == N - 1 and c == M - 1:
            return t + 1  # 마지막 칸에 도착하고 다음 칸에 탈출하므로 +1 해준다.

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            # 갈 수 있는 지점을 방문하지 않은 경우에만 이동. 시간 초 증가
            if map_[nr][nc] == 1 and not visited[nr][nc]:
                d.append((nr, nc, t + 1))
                visited[nr][nc] = True


# 최소 거리 탈출 조건 -> BFS
print(BFS(0, 0, 0))
