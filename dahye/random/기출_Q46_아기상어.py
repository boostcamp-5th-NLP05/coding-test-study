from collections import deque

n = int(input())
data = [] #전체 공간
fish = [] #물고기 정보 저장
for i in range(n):
    temp_list = list(map(int, input().split()))
    data.append(temp_list)
    for j in range(n):
        if temp_list[j] == 9:
            x = i
            y = j

#code
# bfs
def bfs(data, x, y) : 
    queue = deque([(x,y,0)])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    temp_weight = 2 # 아기상어 처음 무게
    temp_count = 0 # 먹은 물고기 수
    answer = 0
    while queue :
        x,y,t = queue.popleft()
        print(x,y,t)
        answer += t
        for i in range(4): #상하좌우
            nx = x+dx[i]
            ny = y+dy[i]
            if not (nx>=n or nx<0 or ny>=n or ny<0): #범위일 때
                if data[nx][ny] == temp_weight or data[nx][ny] == 0: #무게가 같으면 지나갈 수 있음
                    queue.append((nx,ny,t+1))
                elif data[nx][ny] < temp_weight and data[nx][ny] != 0: #무게가 작으면 먹고 지나갈 수 있음
                    queue.append((nx,ny,t+1))
                    temp_count += 1
                    data[nx][ny] = 0
                if temp_count == temp_weight: # 무게 증가
                    temp_weight += 1
                    temp_count = 0
    print(answer)

bfs(data, x, y)