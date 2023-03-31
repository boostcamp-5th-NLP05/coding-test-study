from collections import deque

N, L, R = map(int,input().split())

data = []
for _ in range(N):
    data.append(list(map(int, input().split())))


move = [[1,0], [-1,0], [0,1], [0,-1]]

def bfs(r,c,data,is_move,N,L,R,visited):
    queue = deque()
    queue.append([r,c])

    while queue:
        r,c = queue.popleft()
        for i in move:
            nr = r + i[0]
            nc = c + i[1]
            
            if nr in [-1,N] or nc in [-1,N]: #범위 밖
                continue
            
            #기준에 맞으면 같은 연합으로
            if abs(data[r][c]-data[nr][nc]) >= L and abs(data[r][c]-data[nr][nc]) <=R and visited[nr][nc] == False:
                union[nr][nc] = union[r][c] #같은 연합처리
                visited[nr][nc] = True
                queue.append([nr,nc])
                is_move = True #한번이라도 있으면 이동하게
                continue

    return is_move

#같은 연합 인구수 같게 만드는 함수
def distribution(data):
    for i in range(N*N):
        sum_ = 0
        cnt = 0
        a = []
        for r in range(N):
            for c in range(N):
                if union[r][c] == i: #연합 총 N^2 개 다 확인하면서 돌기
                    sum_ += data[r][c]
                    cnt += 1
                    a.append([r,c])

        if cnt != 0:
            union_population = sum_ // cnt
        
        for r,c in a:
            data[r][c] = union_population
    return data
    
    
            
answer = 0
is_move = True


while True:
    union = [[i+(j*N) for i in range(N)] for j in range(N)]
    visited = [[False for i in range(N)] for j in range(N)]
    is_move = False
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                visited[r][c] = True
                is_move = bfs(r,c,data,is_move,N,L,R,visited)

    if not is_move: #인구 이동이 없었으면 탈출
        break
    else:
        answer += 1
        data = distribution(data) #인구 이동

print(answer)