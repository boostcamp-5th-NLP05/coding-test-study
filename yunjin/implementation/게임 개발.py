import sys
from pprint import pprint

input = sys.stdin.readline

N, M = map(int, input().split())

# 행, 열, 방향
row, column, direction = map(int, input().split())

map = [list(map(int, input().split())) for i in range(N)]
answer = 1

# 방문 여부 체크 배열
visited = [[False for j in range(M)] for i in range(N)]
visited[row][column] = True

# 북, 서, 남, 동
move_row = [-1, 0, 1, 0]
move_column = [0, -1, 0, 1]
back_yn = False

# 바다인 것은 방문 불가능하므로 이미 방문했다고 체크한다.
for i in range(N):
    for j in range(M):
        if map[i][j] == 1:
            visited[i][j] = True

while True:

    '''
    STEP 1 -> 방향 반시계 방향 90도.
    '''
    direction = (direction + 1) % 4

    all_block = False
    block_cnt = 0

    # 동서남북 돌면서 사방이 막혀있는지 확인
    for i in range(1, 5):
        nrow = row + move_row[(direction + i) % 4]
        ncolumn = column + move_column[(direction + i) % 4]

        if ncolumn < 0 or ncolumn >= M or nrow < 0 or nrow >= N:
            block_cnt += 1
            continue

        if map[nrow][ncolumn] == 1 or visited[nrow][ncolumn]:
            block_cnt += 1

    # 사방이 모두 막힌 경우 all_block 체크
    if block_cnt >= 4:
        all_block = True

    '''
    STEP 3 -> 사방이 막혀있는 경우 바라보고 있는 방향에서 뒤로 이동한다.
    '''
    if all_block:

        direction = (direction - 1) % 4
        if direction == -1:
            direction = 3
        back_yn = True

        nrow = row - move_row[direction]
        ncolumn = column - move_column[direction]

        if ncolumn < 0 or ncolumn >= M or nrow < 0 or nrow >= N:
            break

        # 사방이 막혀 있고 뒤로 가던 도중, 뒤 칸이 바다였다면 멈추고 종료 (끝)
        if map[nrow][ncolumn] == 1 and back_yn:
            break

        row = nrow
        column = ncolumn
        back_yn = True # 뒤로 간다.
        visited[nrow][ncolumn] = True

        # 뒤로 이동한 상태를 유지하면서 재반복문.
        continue

    nrow = row + move_row[direction]
    ncolumn = column + move_column[direction]

    if ncolumn < 0 or ncolumn >= M or nrow < 0 or nrow >= N:
        continue

    '''
    STEP 2 -> 육지인경우
    '''
    if map[nrow][ncolumn] == 0:

        if back_yn:
            # 방문하지 않은 경우에만 더해준다.
            if not visited[nrow][ncolumn]:
                answer += 1
            visited[nrow][ncolumn] = True
            row = nrow
            column = ncolumn
            visited[nrow][ncolumn] = True
            continue

        # 방문하지 않은 경우에만 더해준다. (어차피 방문한 경우에는 위에서 걸러진다.)
        if not visited[nrow][ncolumn]:
            visited[nrow][ncolumn] = True
            row = nrow
            column = ncolumn
            answer += 1
            back_yn = False
            visited[nrow][ncolumn] = True


print(answer)
# pprint(visited)
