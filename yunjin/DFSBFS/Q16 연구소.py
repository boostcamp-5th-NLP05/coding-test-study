import itertools
import copy
from collections import deque

N, M = map(int, input().split())
map_ = [list(map(int, input().split())) for row in range(N)]

# 벽을 세울 수 있는 위치
possible_position = [(r, c) for c in range(M) for r in range(N) if map_[r][c] == 0]
position_combinations = list(itertools.combinations(possible_position, 3))

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

answer = -float('inf')


def BFS(sr, sc):
    global new_map, new_visited

    d = deque()
    d.append((sr, sc))
    new_visited[sr][sc] = True

    while d:
        r, c = d.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if new_map[nr][nc] == 0 and not new_visited[nr][nc]:
                new_map[nr][nc] = 2 # 안전영역을 바이러스 영역으로 만들기.
                d.append((nr, nc))

# 모든 조합에 대해서 BFS 를 수행
for combi in position_combinations:

    # 안전영역 수
    safe_zone_cnt = 0

    # 새로운 맵 생성
    new_map = copy.deepcopy(map_)
    new_visited = visited = [[False for col in range(M)] for row in range(N)]
    new_map[combi[0][0]][combi[0][1]] = 1
    new_map[combi[1][0]][combi[1][1]] = 1
    new_map[combi[2][0]][combi[2][1]] = 1

    # 바이러스가 완전히 퍼졌을 때
    for r in range(N):
        for c in range(M):
            if new_map[r][c] == 2 and not new_visited[r][c]:
                BFS(r, c) # 방문하지 않은 바이러스 지점에서 DFS 를 수행해서 바이러스가 퍼진 상황을 만든다.


    # 바이러스가 완전 탐색을 마쳤으므로 안전영역의 갯수는 단순히 0 의 개수다.
    for row in new_map:
        safe_zone_cnt += row.count(0)
    answer = max(safe_zone_cnt, answer)

print(answer)
