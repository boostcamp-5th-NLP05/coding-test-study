from collections import deque
from heapq import heappush, heappop
import sys

def input():
    return sys.stdin.readline().rstrip()

data = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]] #전체 공간
for i in range(4):
    temp_list = list(map(int, input().split()))
    for j in range(4):
            data[i][j] = temp_list[j*2:j*2+2]

#code
dr = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 0, -1, -1, -1, 0, 1, 1, 1]
# 물고기를 이동시키는 함수
def move_fish(idx, r, c, dir):
    for i in range(8):
        cur_dir = dir + i
        if cur_dir >= 9:
            cur_dir -= 8
        cr = r + dr[cur_dir]
        cc = c + dc[cur_dir]
        # 범위 안에 있으면서 숫자가 맞을 경우
        if 0 <= cr < 4 and 0 <= cc < 4 and 0 <= data[cr][cc][0] <= 16:
            temp_fish = data[r][c][0]
            data[r][c] = data[cr][cc]
            data[cr][cc] = [temp_fish, cur_dir]
            break

x = 0
y = 0
while 1:
    # bfs로 먹을 수 있는 물고기 번호의 최대값 구함
    q = deque()
    q.append([x, y, 0, data[x][y][1]]) #상어의 좌표, 먹은 무게, 방향
    visit = [[False] * 4 for _ in range(4)]
    visit[x][y] = True
    can_eat = []
    max_fish = 0
    while q:
        r, c, weight, direc = q.popleft()
        if direc == 1:
            temp_x = 0
            temp_y = -1
        elif direc == 2:
            temp_x = -1
            temp_y = -1
        elif direc == 3:
            temp_x = -1
            temp_y = 0
        elif direc == 4:
            temp_x = -1
            temp_y = 1
        elif direc == 5:
            temp_x = 0
            temp_y = 1
        elif direc == 6:
            temp_x = 1
            temp_y = 1
        elif direc == 7:
            temp_x = 1
            temp_y = 0
        else:
            temp_x = 1
            temp_y = -1
          
        if not (x>=4 or x<0 or y>=4 or y<0):
            x = x+ temp_x
            y = y+ temp_y
            weight += data[x][y][0]
            q.append([x, y, weight, data[x][y][1]])
    # 물고기 이동
    visited = [0] * 17
    for idx in range(1, 17):
        for r in range(4):
            for c in range(4):
                # 아직 이동하지 않은 물고기들 이동시키기
                if data[r][c][0] == idx and visited[idx] == 0:
                    visited[idx] = 1
                    move_fish(idx, r, c, data[r][c][1])
                    break

    print(weight)