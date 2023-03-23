import sys
def gl():
    return sys.stdin.readline().rstrip()


N = int(gl())
# 0: 빈칸, 1: 사과, 2: 뱀
board = [[0 for _ in range(N)] for _ in range(N)]

K = int(gl())
for _ in range(K):
    r, c = map(int, gl().split())
    board[r - 1][c - 1] = 1  # board 인덱스는 0부터 시작

L = int(gl())
change = []
for _ in range(L):
    change.append(gl().split())

# dir: 0(북), 1(동), 2(남), 3(서)
step = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = 1 # 현재 방향
board[0][0] = 2
snake = [(0, 0)] # 뱀 몸 있는 칸 [꼬리, ..., 머리]

time = 0
while True:
    time += 1
    nr = snake[-1][0] + step[dir][0]
    nc = snake[-1][1] + step[dir][1]

    if nr < 0 or nr >= N or nc < 0 or nc >= N:
        break  # 벽 만남
    if board[nr][nc] == 2:
        break  # 자기 몸 만남

    if board[nr][nc] == 0:  # 사과 없는 칸이면
        # 꼬리 있었던 칸 제거
        tail = snake.pop(0)
        board[tail[0]][tail[1]] = 0

    # 새로운 머리 추가
    snake.append((nr, nc))
    board[nr][nc] = 2

    # 방향 전환
    if len(change) > 0 and int(change[0][0]) == time:
        if change[0][1] == "L":
            dir = (dir + 3) % 4
        else:
            dir = (dir + 1) % 4
        change.pop(0)

print(time)  # answer
