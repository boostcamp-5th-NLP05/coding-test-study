# 책 통과 풀이
n, m, k = map(int, input().split())

# 모든 상어의 위치와 방향 정보를 포함하는 2차원 리스트
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 모든 상어의 현재 방향 정보
directions = list(map(int, input().split()))

# 각 위치마다 [특정 냄새의 상어 번호, 특정 냄새의 남은 시간]을 저장하는 2차원 리스트
smell = [[[0, 0]] * n for _ in range(n)]

# 각 상어의 회전 우선순위 정보
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

# 특정 위치에서 이동 가능한 4가지 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 냄새 정보를 업데이트
def update_smell():
    # 각 위치를 하나씩 확인하며
    for i in range(n):
        for j in range(n):
            # 냄새가 존재하는 경우, 시간을 1만큼 감소시키기
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어가 존재하는 해당 위치의 냄새를 k로 설정
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]

# 모든 상어를 이동시키는 함수
def move():
    # 이동 결과를 담기 위한 임시 결과 테이블 초기화
    new_array = [[0] * n for _ in range(n)]
    # 각 위치를 하나씩 확인하며
    for x in range(n):
        for y in range(n):
            # 상어가 존재하는 경우
            if array[x][y] != 0:
                direction = directions[array[x][y] - 1] # 현재 상어의 방향
                found = False
                # 일단 냄새가 존재하지 않는 곳이 있는지 확인
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][1] == 0: # 냄새가 존재하지 않는 곳이면
                            # 해당 상어의 방향 이동시키기
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]
                            # 상어 이동시키기 (만약 이미 다른 상어가 있다면 번호가 낮은 것이 들어가도록)
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[x][y]
                            else:
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
                            found = True
                            break
                if found:
                    continue
                # 주변에 모두 냄새가 남아 있다면, 자신의 냄새가 있는 곳으로 이동
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][0] == array[x][y]: # 자신의 냄새가 있는 곳이면
                            # 해당 상어의 방향 이동시키기
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]
                            # 상어 이동시키기
                            new_array[nx][ny] = array[x][y]
                            break
    return new_array

time = 0
while True:
    update_smell() # 모든 위치의 냄새를 업데이트
    new_array = move() # 모든 상어를 이동시키기
    array = new_array # 맵 업데이트
    time += 1 # 시간 증가

    # 1번 상어만 남았는지 체크
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False
    if check:
        print(time)
        break

    # 1000초가 지날 때까지 끝나지 않았다면
    if time >= 1000:
        print(-1)
        break















# 기존 풀이

import sys

N, M, k = map(int, input().split())

# 상어 맵 (현재 상어 번호, 방향, 냄새 남긴 상어 번호, 남은 초)
map_ = [[] for r in range(N)]

for i in range(N):
    numbers = list(map(int, input().split()))
    for num in numbers:
        if num == 0:
            map_[i].append([0, 0, 0, 0])
        else:
            map_[i].append([num, 0, num, k])

init_direction = list(map(int, input().split()))

for r in range(N):
    for c in range(N):
        if map_[r][c][0] != 0:
            map_[r][c][1] = init_direction[map_[r][c][0] - 1] - 1  # 1 을 빼서 더해준다.


# (num-1)%4 ~ (num-1)%4 +3 까지가 num 번째 상어의 상하좌우 우선순위임.
prioritys = [list(map(int, input().split())) for i in range(M * 4)]

# 북 남 서 동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_all_sharks():
    sharks = []

    for r in range(N):
        for c in range(N):
            if map_[r][c][0] != 0:
                sharks.append([map_[r][c][0],
                               map_[r][c][1],
                               map_[r][c][2],
                               map_[r][c][3],
                               r, c]) # r,c 는 좌표임.

    # 작은 상어부터 이동해서 첫번째걸 가져오는 방식.
    sharks.sort()
    return sharks


# 특정 상어의 좋은 방향 찾기.
def find_direction(shark):

    global map_

    num, d, scent_num, second, r, c = shark

    priority = prioritys[(num - 1) * 4 + d]

    no_scent_direction = []
    my_scent_dirction = []



    for i in range(4):

        # priority 에서 꺼내줄 때는 1  빼준 값으로.
        new_direction = priority[i] - 1

        # 우선 순위가 1 ~ 4 이므로 0 ~ 3 으로 빼주면 됨. 방향 순서는 일치함. (북남서동)
        nr = r + dr[new_direction]
        nc = c + dc[new_direction]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue

        if map_[nr][nc][2] != 0 and map_[nr][nc][3] > 0:
            # 자신의 냄새가 있으면.
            if map_[nr][nc][2] == num and map_[nr][nc][3] > 0:
                my_scent_dirction.append(new_direction)
                continue

        # 냄새가 없는 것도 우선순위 순으로 추가.
        else:
            no_scent_direction.append(new_direction)

    # 우선 순위로 돌았으므로 0 번째 꺼를 리턴해주면 됨.
    if no_scent_direction:
        return no_scent_direction[0]

    # 자신의 냄새가 있었다면.
    if my_scent_dirction:
        return my_scent_dirction[0]

    return priority[0] - 1


# 모든 상어 이동하기.
def move_all_shark():
    global map_

    global k

    # 상어 중복 체크용 맵
    dupli_shark_map_ = [[[] for i in range(N)] for r in range(N)]

    # 모든 상어 찾기.
    sharks = find_all_sharks()

    # 모든 상어에 대해 이동 처리
    for shark in sharks:

        num, direc, sent_num, second, r, c = shark

        # 방향 최신화
        direc = find_direction(shark)

        nr = r + dr[direc]
        nc = c + dc[direc]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue

        # 중복 체크용에 넣어줌.
        dupli_shark_map_[nr][nc].append([num, direc, num, k, r, c])


    for r in range(N):
        for c in range(N):


            # 두 마리 이상의 상어가 들어왔으면 1번째 이후의 것들은 내쫓음.
            if len(dupli_shark_map_[r][c]) >= 2:

                # 첫 상어만 이동 처리.
                map_[r][c] = dupli_shark_map_[r][c][0][0:4]

                # 그 외 상어는 내 쫓음.
                for i in range(1, len(dupli_shark_map_[r][c])):
                    num, direc, num, k, pre_r, pre_c = dupli_shark_map_[r][c][i]

                    map_[pre_r][pre_c][0] = 0 # 상어
                    map_[pre_r][pre_c][1] = 0 # 방향


            elif len(dupli_shark_map_[r][c]) == 1:

                num, direc, num, k, pre_r, pre_c = dupli_shark_map_[r][c][0]

                map_[r][c] = [num, direc, num, k]
                map_[pre_r][pre_c][0] = 0
                map_[pre_r][pre_c][1] = 0

            # # 아무 것도 없었으면 0, 0
            else:
                map_[r][c][0] = 0
                map_[r][c][1] = 0


    for r in range(N):
        for c in range(N):

            if map_[r][c][0] == 0:
                # 1 초만 남았으면
                if map_[r][c][3] == 1:
                    map_[r][c][2] = 0
                    map_[r][c][3] -= 1

                # 그 이상 남았으면
                elif map_[r][c][3] > 1:
                    map_[r][c][3] -= 1


# 1번 상어만 남아있는 지 여부 체크 함수
def is_only_first_shark():

    global map_

    for r in range(N):
        for c in range(N):
            if map_[r][c][0] != 0 and map_[r][c][0] != 1:
                return False

    return True


time = 0

while True:

    # 1 번 상어만 존재하는 지 여부
    if is_only_first_shark():
        break

    time += 1

    # 모든 상어 움직이기
    move_all_shark()

    if time >= 1000:
        time = -1
        break

print(time)