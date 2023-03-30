import itertools
import sys

input = sys.stdin.readline

N = int(input())

map_ = [list(map(str, input().split())) for i in range(N)]

coords = [(r, c) for c in range(N) for r in range(N) if map_[r][c] == 'X']
combinations = list(itertools.combinations(coords, 3))

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 선생님 한명이 특정 지점에서 감시해서 학생이 걸렸는지 안걸렸는지 리턴하는 DFS
def is_caught_dfs(row, col, map_):
    stack = []
    stack.append((row, col))

    while stack:

        r, c = stack.pop()

        for i in range(4):

            # 멀리볼 수 있으므로 감시가 map_의 상하좌우 끝 까지 간다. 이를 watch_depth 로 실행.
            for watch_depth in range(1, N + 1):

                nr = r + dr[i] * watch_depth
                nc = c + dc[i] * watch_depth

                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue

                # 해당 방향에 장애물이 존재하면 해당 방향으로 더 이상 감시 종료
                if map_[nr][nc] == 'O':
                    break

                # 학생이 감시에 걸림.
                if map_[nr][nc] == 'S':
                    return True  # 걸렸다

    # 여기 까지 왔다면 아무도 걸리지 않았다는 것.
    return False  # 안걸렸다.


# 완전 탐색
for combination in combinations:

    # 장애물 설치
    map_[combination[0][0]][combination[0][1]] = 'O'
    map_[combination[1][0]][combination[1][1]] = 'O'
    map_[combination[2][0]][combination[2][1]] = 'O'

    answer = 'YES'

    # 맵 내의 모든 선생님들이 감시할 수 있는 범위를 DFS 를 통해 조사.
    for r in range(N):
        for c in range(N):
            if map_[r][c] == 'T':
                if is_caught_dfs(r, c, map_):  # 걸렸다면
                    answer = 'NO'
        if answer == 'NO':
            break

    # 한 번도 감시에 걸리지 않았다면 56행의 answer = 'YES' 가 보존 되었을 것임.
    if answer == 'YES':
        break

    # 원복
    map_[combination[0][0]][combination[0][1]] = 'X'
    map_[combination[1][0]][combination[1][1]] = 'X'
    map_[combination[2][0]][combination[2][1]] = 'X'

print(answer)