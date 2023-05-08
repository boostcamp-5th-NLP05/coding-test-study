import sys

def input():
    return sys.stdin.readline().rstrip()

from collections import deque
n = int(input())

map_ = []
for i in range(n):
    tmp = list(map(int,input().split()))
    map_.append(tmp)
    if 9 in tmp:
        row_nine = i
        col_nine = tmp.index(9)


move = [(-1,0),(0,-1),(0,1),(1,0)] #우선순위 북서동남 <- 상관없음

visited = [[False for _ in range(n)] for _ in range(n)]
visited[row_nine][col_nine] = True #처음 위치 방문표시

map_[row_nine][col_nine] = 0 #처음 상어 위치 0으로 최신화

queue = deque()
queue.append((row_nine,col_nine,0,2,0)) #상어row, 상어col,시간,상어크기,먹은 물고기 수

answer = 0
can_eat = []
pre = 0

while queue:
    r,c,time,size,eat = queue.popleft()
    
    time += 1
    
    if pre < time and len(can_eat) != 0: #깊이가 깊어지고, 그 전 깊이에서 먹을 수 있는 물고기가 있다면
        can_eat.sort(key = lambda x : (x[0],x[1])) #우선순위에 맞게 정렬
        r,c,time,size,eat = can_eat[0]
        can_eat = []
        
        map_[r][c] = 0
        answer = time
        
        eat += 1
        if size == eat: #크기만큼 먹었으면 크키 키움
            size += 1
            eat = 0
            
        queue = deque()#물고기 먹었을 때 queue 초기화
        queue.append((r,c,time,size,eat)) 
        visited = [[False for _ in range(n)] for _ in range(n)]
        visited[r][c] = True
        continue
        
    for i,j in move:
        nr = r + i
        nc = c + j
        
        if nr in [-1,n] or nc in [-1,n]:
            continue
        
        if not visited[nr][nc]:
            if map_[nr][nc] > size:
                continue
            
            elif map_[nr][nc] != 0 and map_[nr][nc] < size: #현재 위치에 먹을 수 있는 물고기가 있다면
                visited[nr][nc] = True
                can_eat.append((nr,nc,time,size,eat))
                queue.append((nr,nc,time,size,eat))


            elif map_[nr][nc] == 0 or map_[nr][nc] == size: #현재 위치가 지나다닐 수 있다면
                visited[nr][nc] = True
                queue.append((nr,nc,time,size,eat))

    pre = time
    

print(answer)