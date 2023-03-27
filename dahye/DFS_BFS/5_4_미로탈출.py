from collections import deque
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

def bfs(x,y) :
    queue = deque()
    queue.append((0,0))
    while queue:
        i, j = queue.popleft()
        for di, dj in ([-1, 0], [1, 0], [0, -1], [0, 1]): #다음 step 확인
            ni, nj = i + di, y + dj

            if ni>=n or ni<0 or nj>=m or nj<0: #범위넘어가면 다른 경우로
                continue
            if data[ni][nj] == 0: #괴물이 있으면 다른 경우로
                continue
            
            if data[ni][nj] == 1: #지름길이면 원래 거리count에 1더해줌
                queue.append((ni,nj)) 
                data[ni][nj] = data[i][j] + 1
            
    return data[n-1][m-1] + 1

print(bfs(0,0))
