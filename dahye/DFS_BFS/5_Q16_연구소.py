from itertools import combinations
import copy

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

#dfs를 정의내린 이유 -> 퍼진 바이러스 계산하기 위해
def dfs(x,y) :
    global temp_data
    for i in range(4): #상하좌우
        nx = x+dx[i]
        ny = y+dy[i]
        if not (nx>=n or nx<0 or ny>=m or ny<0): #범위일 때
            if temp_data[nx][ny] == 0: #0이면 1이 나올때까지 바이러스퍼뜨림
                temp_data[nx][ny] = 2
                dfs(nx,ny) 


#울타리를 3개씩 설치하는 모든 방법 -> 0갯수 count
#벽을 설치할 곳 후보
wall_list = []
for ti in range(n):
    for tj in range(m):
        if data[ti][tj] == 0:
            wall_list.append([ti,tj])
#3개벽 조합 combination
comb = list(combinations(wall_list, 3))

answer = []
for com1, com2, com3 in comb:
    temp_data = copy.deepcopy(data)
    com1_1, com1_2 = com1
    com2_1, com2_2 = com2
    com3_1, com3_2 = com3
    temp_data[com1_1][com1_2] = 1
    temp_data[com2_1][com2_2] = 1
    temp_data[com3_1][com3_2] = 1 #벽 설치
    for i in range(n): #2를 만나면 바이러스 퍼뜨리기
        for j in range(m):
            if temp_data[i][j] == 2:
                dfs(i,j)

    for i_i in range(n):
        answer.append(temp_data[i_i].count(0))


print(max(answer))