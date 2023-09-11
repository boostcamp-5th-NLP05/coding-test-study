#방향 우선순위가 위쪽, 왼쪽이기때문에 bfs로 조정해주었지만
#방향 우선순위를 모두 고려하지 못하기 때문에 따로 list를 만들어서
#가장 위쪽, 왼쪽에 해당하는 물고기를 선택해야함


from collections import deque

n = int(input())
data = [] #전체 공간

for i in range(n):
    temp_list = list(map(int, input().split()))
    data.append(temp_list)
    for j in range(n):
        if temp_list[j] == 9: #상어의 위치 저장
            next_x = i
            next_y = j

#code
# bfs
def bfs(map_, x, y, temp_weight): # 상어의 다음위치를 결정하는 함수 (현재지도, 상어위치, 현재무게)
    visited = [[False for _ in range(n)] for _ in range(n)] # 방문 여부
    queue = deque([(x,y,0)]) # 현재상어의 위치, 시간
    dx = [-1,0,0,1] #가장 위쪽, 왼쪽 순으로 우선순위
    dy = [0,-1,1,0]
    while queue :
        x,y,t = queue.popleft()
        for i in range(4): #상좌우하
            nx = x+dx[i]
            ny = y+dy[i]
            if not (nx>=n or nx<0 or ny>=n or ny<0): #범위일 때
                if (map_[nx][ny] == temp_weight or map_[nx][ny] == 0) and visited[nx][ny] == False: #무게가 같으면 지나갈 수 있음
                    queue.append((nx,ny,t+1))
                    visited[nx][ny] = True
                elif map_[nx][ny] < temp_weight and map_[nx][ny] != 0 and visited[nx][ny] == False: # 물고기를 발견하면 먹고 다시 리셋
                    return nx, ny, t+1
    return False

shark_weight = 2 # 아기상어 처음 무게
temp_count = 0 # 먹은 물고기 수
answer = 0
while True:
    data[next_x][next_y] = 0
    if bfs(data, next_x, next_y, shark_weight) == False: #먹을 수 있는 물고기가 없어서 False를 return할 때
        break
    next_x, next_y, next_t = bfs(data, next_x, next_y, shark_weight) # 상어의 다음 위치
    answer += next_t   
    temp_count += 1
    if temp_count == shark_weight: # 무게 증가
        shark_weight += 1
        temp_count = 0

print(answer)
        
    