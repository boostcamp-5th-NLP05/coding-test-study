from collections import deque
import copy
import sys
from itertools import combinations

n, m = map(int,input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

info_zero = []
info_two = []

for r in range(n): #0 위치 2위치 저장
    for c in range(m):
        if data[r][c] == 0:
            info_zero.append([r,c])
        if data[r][c] == 2:
            info_two.append((r,c))

answer = 0
comb = list(combinations(info_zero, 3)) #0에서 3개씩 조합

c_move = [1, 0, -1, 0]
r_move = [0, 1, 0, -1]

for i in comb: #모든 조합 돌려보기
    queue = deque()
    for k in info_two: #큐에 2위치 저장
        queue.append(k)

    copy_data = copy.deepcopy(data)
    copy_data[i[0][0]][i[0][1]] = 1 #벽 3개 설치
    copy_data[i[1][0]][i[1][1]] = 1
    copy_data[i[2][0]][i[2][1]] = 1

    while queue: #bfs로 채워넣기  #제대로 실행이 안되는듯함
        r,c = queue.popleft()
        for j in range(4):
            nc = c + c_move[j]
            nr = r + r_move[j]
            if nc >= 0 and nc < m and nr >= 0 and nr < n:
                if copy_data[nr][nc] == 0:
                    copy_data[nr][nc] = 2
                    queue.append((nc,nr))
    cnt = 0
    for i in copy_data:
        cnt += i.count(0)
    answer = max(answer, cnt)
    
print(answer)