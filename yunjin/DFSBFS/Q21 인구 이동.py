from collections import deque
import sys

input = sys.stdin.readline

N, L, R = map(int, input().split())

countries = [list(map(int, input().split())) for i in range(N)]

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 모두 같은 지 확인하는 함수
def is_population_all_same(arr):
    total = 0
    count = 0
    for row in arr:
        for value in row:
            total += value
            count += 1
    avg = total / count

    for row in arr:
        for value in row:
            if value != avg:
                return False

    return True


# 인구 이동을 진행하고 인구 이동이 있었는지 확인하는 DFS 함수
def population_move_dfs(row, col, visited):
    stack = []
    stack.append((row, col))
    move_contries = set()
    visited[row][col] = True

    while stack:
        r, c = stack.pop()
        move_contries.add((r, c))

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            # 인구 차이
            population_gab = abs(countries[nr][nc] - countries[r][c])

            # 규칙에 부합한다면 이동을 한다.
            if not visited[nr][nc] and (L <= population_gab and population_gab <= R):
                stack.append((nr, nc))
                visited[nr][nc] = True
                move_contries.add((nr, nc))

    # 두 나라 이상이 이동을 했다면 인구 조정을 해주고 True 를 리턴한다.
    if len(move_contries) >= 2:
        total_population = 0
        for i, j in move_contries:
            total_population += countries[i][j]

        # 인구 규칙에 맞게 인구 조정 작업
        for i, j in move_contries:
            countries[i][j] = total_population // len(move_contries)
        return True  # 이동을 했다.


    # 여기 까지 왔다면 이동을 안했다는 것.
    return False  # 이동을 안했다.


# 이동일자
move_days = 0


# 인구 이동이 없을 떄 까지 population_move_dfs 를 진행한다.
while True:

    # 모두 인구 수가 같다면 인구 이동은 없다.
    if is_population_all_same(countries):
        break

    visited = [[False for c in range(N)] for r in range(N)]

    is_updated = False
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                if population_move_dfs(r, c, visited): # 이동이 있었다면 while 문 계속 진행
                    is_updated = True

    # 한 번도 이동이 없었다면
    if not is_updated:
        break

    # 여기까지 왔다면 인구 이동이 정상적으로 이뤄졌으므로 하루 지남.
    move_days += 1

print(move_days)
