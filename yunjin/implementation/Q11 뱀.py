import sys
input = sys.stdin.readline

N = int(input())
apple_cnt = int(input())

# 사과 표시하기
apple_map = [[False for i in range(N)] for j in range(N)]
for i in range(apple_cnt):
    r, c = list(map(int, input().split()))
    apple_map[r-1][c-1] = True

# 회전하기
turn_cnt = int(input())
turns = []
for i in range(turn_cnt):
    turns.append(list(map(str, input().split())))

# 뱀이 갈 수 있는 맵 선언
snake_able_map = [[True for i in range(N)] for j in range(N)]


turn_idx = 0
time = 0
row, col = 0, 0

# 동, 남, 서, 북
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

direction_idx = 0

tail_row, tail_col = 0, 0

# 뱀이 현재 위치하고 있는 영역을 보관한 리스트
trace = []
turn_time = int(turns[turn_idx][0])
trace.append([0, 0])

while True:

    # 주어진 방향대로 일단 이동한다.
    nrow = row + direction[direction_idx][0]
    ncol = col + direction[direction_idx][1]

    # 유효성 검사 1) 이동할려는 칸이 밖이라면 break
    if nrow < 0 or nrow >= N or ncol < 0 or ncol >= N:
        time += 1
        break

    # 유효성 검사 2) 자기 몸을 밟는 지 확인한다.
    if not snake_able_map[nrow][ncol]:
        time += 1
        break

    # 이제 이동해도 된다.


    # 새로운 머리 위치 snake_able_map 에 표시하고 이동할 위치를 trace 에 기록
    snake_able_map[nrow][ncol] = False
    trace.append([nrow, ncol])


    # 사과 먹었는지 확인한다.
    if apple_map[nrow][ncol] == True:
        # 사과 먹음 처리
        apple_map[nrow][ncol] = False
    else:

        # 사과를 안먹었다면 trace 에서 먼저 들어온것을 제거하고, 이제 갈 수 있는 영역이다.
        tail_row, tail_col = trace.pop(0)
        snake_able_map[tail_row][tail_col] = True


    # 실제 이동 처리
    row = nrow
    col = ncol
    time += 1

    # 이동까지 마치고 난 후 회전을 해야 한다면 회전한다.
    if time <= int(turns[-1][0]):

        # 움직이는 지 확인 검사.
        if time == turn_time:
            # 시계방향
            if turns[turn_idx][1] == 'D':
                direction_idx = (direction_idx + 1) % 4

            # 반시계 방향
            if turns[turn_idx][1] == 'L':
                direction_idx = (direction_idx - 1) % 4

            if turn_idx < len(turns)-1:
                turn_idx += 1
                turn_time = int(turns[turn_idx][0])

print(time)