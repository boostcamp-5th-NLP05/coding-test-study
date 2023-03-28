n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

#dfs를 정의내린 이유 -> 0의 끝을 탐색할 때까지 재귀함수 사용하기 위해
def dfs(x,y) :
    if x>=n or x<0 or y>=m or y<0: #범위넘어가면 멈춤
        return 'go'    
    if data[x][y] == 0: #0이면 상하좌우로 이동
        data[x][y] = 1 # 방문처리
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return 'stop'
    return 'go'
count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == 'stop':
            count +=1
print(count)
