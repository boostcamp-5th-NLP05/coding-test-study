from collections import deque

n, k = map(int, input().split())
data = [] #전체 시험관
virus = [] #바이러스 저장소
for i in range(n):
    temp_list = list(map(int, input().split()))
    data.append(temp_list)
    for j in range(n):
        if temp_list[j] != 0:
            virus.append((temp_list[j],i,j,0))


S, X, Y = map(int, input().split())
virus.sort()

#code
# bfs로 푼 이유 - 한칸씩 바이러스가 퍼져야 하므로
def bfs(virus, data, S, X, Y) : 
    queue = deque(virus)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue :
        k,x,y,t = queue.popleft()
        if t == S: #S초일때 멈춤
            break
        for i in range(4): #상하좌우
            nx = x+dx[i]
            ny = y+dy[i]
            if not (nx>=n or nx<0 or ny>=n or ny<0): #범위일 때
                if data[nx][ny] == 0: #바이러스가 존재하지 않을 때 채울 수 있음
                    data[nx][ny] = k
                    queue.append((k,nx,ny,t+1))
    print(data[X-1][Y-1])

bfs(virus, data, S, X, Y)


