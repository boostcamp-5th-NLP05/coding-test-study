from collections import deque

n, k1 = map(int, input().split())
data = [] #전체 시험관
virus = [] #바이러스 저장소
for i in range(n):
    temp_list = list(map(int, input().split()))
    data.append(temp_list)
    for j in range(n):
        if temp_list[j] != 0:
            virus.append((temp_list[j],i,j))


S, X, Y = map(int, input().split())
virus.sort()  

#code
# bfs로 푼 이유 - 한칸씩 바이러스가 퍼져야 하므로
def bfs(virus, data, S, X, Y, k1) : 
    queue = deque(virus)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    time = 0
    while queue and time <S*k1: #S초 뒤에 멈춰야하는데 k1개의 바이러스가 있으므로 
        k,x,y = queue.popleft()
        for i in range(4): #상하좌우
            nx = x+dx[i]
            ny = y+dy[i]
            if not (nx>=n or nx<0 or ny>=n or ny<0): #범위일 때
                if data[nx][ny] == 0: #바이러스가 존재하지 않을 때 채울 수 있음
                    data[nx][ny] = k
                    queue.append((k,nx,ny))
        time +=1
    print(data[X][Y])

bfs(virus, data, S, X, Y, k1)


