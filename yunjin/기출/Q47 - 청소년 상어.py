# 통과 풀이(책)
import copy

# 4 X 4 크기 격자에 존재하는 각 물고기의 번호(없으면 -1)와 방향 값을 담는 테이블
array = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    # 매 줄마다 4마리의 물고기를 하나씩 확인하며
    for j in range(4):
        # 각 위치마다 [물고기의 번호, 방향]을 저장
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]

# 8가지 방향에 대한 정의
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


# 현재 위치에서 왼쪽으로 회전된 결과 반환
def turn_left(direction):
    return (direction + 1) % 8


result = 0  # 최종 결과


# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None


# 모든 물고기를 회전 및 이동시키는 함수
def move_all_fishes(array, now_x, now_y):
    # 1번부터 16번까지의 물고기를 차례대로 (낮은 번호부터) 확인
    for i in range(1, 17):
        # 해당 물고기의 위치를 찾기
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            # 해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 해당 방향으로 이동이 가능하다면 이동 시키기
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                direction = turn_left(direction)


# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    # 현재의 방향으로 쭉 이동하기
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        # 범위를 벗어나지 않는지 확인하며
        if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4:
            # 물고기가 존재하는 경우
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions


# 모든 경우를 탐색하기 위한 DFS 함수
def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)  # 리스트를 통째로 복사

    total += array[now_x][now_y][0]  # 현재 위치의 물고기 먹기
    array[now_x][now_y][0] = -1  # 물고기를 먹었으므로 번호 값을 -1로 변환

    move_all_fishes(array, now_x, now_y)  # 전체 물고기 이동 시키기

    # 이제 다시 상어가 이동할 차례이므로, 이동 가능한 위치 찾기
    positions = get_possible_positions(array, now_x, now_y)
    # 이동할 수 있는 위치가 하나도 없다면 종료
    if len(positions) == 0:
        result = max(result, total)  # 최댓값 저장
        return
        # 모든 이동할 수 있는 위치로 재귀적으로 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)


# 청소년 상어의 시작 위치(0, 0)에서부터 재귀적으로 모든 경우 탐색
dfs(array, 0, 0, 0)
print(result)












# 기존 실패 풀이
# import sys
#
# map_ = [[] for _ in range(4)]
#
# dr = [-1, -1, 0, 1, 1, 1, 0, -1]
# dc = [0, -1, -1, -1, 0, 1, 1, 1]
#
# for i in range(4):
#     numbers = list(map(int, sys.stdin.readline().split()))
#     for j in range(0, 8, 2):
#         # 물고기 번호, 방향, 생존여부
#         map_[i].append([numbers[j], numbers[j + 1] - 1])
#
# # 물고기 위치 찾기
# def find_fish(num):
#     for r in range(4):
#         for c in range(4):
#             if map_[r][c][0] == num:
#                 return r, c, map_[r][c][1]
#
#     return None
#
# result = []
#
#
# # 시뮬
# def simul(r, c, d, eating, dead):
#     print(r, c, d, eating, dead)
#
#
#     # 물고기 무브
#     for i in range(1, 17):
#
#         # 안 잡힌 물고기 중에서만.
#         if i not in dead:
#             if find_fish(i) == None:
#                 continue
#
#             r, c, direction = find_fish(i)
#
#
#             # 교체 될때까지 계속함
#             while True:
#
#                 nr = r + dr[direction]
#                 nc = c + dc[direction]
#
#                 if nr < 0 or nr >= 4 or nc < 0 or nc >= 4: # 맵 밖이면 회전함
#                     direction += 1
#                     direction %= 8
#                     continue
#
#                 if map_[nr][nc][0] == 99:  # 상어여도 회전함
#                     direction += 1
#                     direction %= 8
#                     continue
#
#
#                 # 교체
#                 nn = map_[nr][nc][0]
#                 nd = map_[nr][nc][1]
#
#                 map_[nr][nc][0] = i
#                 map_[nr][nc][1] = direction
#
#                 map_[r][c][0] = nn
#                 map_[r][c][1] = nd
#
#                 break
#
#     # 상어 움직임 처리
#     flag = False
#
#     for i in range(4):
#         nr = r + dr[d] * i
#         nc = c + dc[d] * i
#
#         if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
#             continue
#
#         # 물고기 공간만 갈 수 있음.
#         if map_[nr][nc][0] != 0:
#             dead.append(map_[nr][nc][0])
#             u = map_[nr][nc][0]
#             eating += u
#             map_[nr][nc][0] = 99
#             map_[r][c][0] = 0
#             flag = True
#
#             # 백트래킹
#             simul(nr, nc, map_[nr][nc][1], eating, dead)
#
#
#             # 원복
#             eating -= u
#             map_[r][c][0] = 99
#             map_[nr][nc][0] = 0
#             dead.pop()
#
#
#     # 한 번도 이동 할 수 없으면 종료함.
#     if not flag:
#         result.append(eating)
#         return
#
#
# # 잡아 먹힌 물고기
# dead = []
# init_fish = map_[0][0][0]
# dead.append(init_fish)
# map_[0][0][0] = 99  # 상어 자리
#
#
# # 시뮬 시작.
# r = simul(0, 0, map_[0][0][1], init_fish, dead)
#
# print(max(r))
