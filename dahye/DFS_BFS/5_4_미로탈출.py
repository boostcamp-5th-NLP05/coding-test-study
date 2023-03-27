n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

#dfs를 정의내린 이유 -> 미로 탈출할 때까지 재귀함수 사용하기 위해

def dfs(x,y) :
    if x>=n or x<0 or y>=m or y<0: #범위넘어가면 멈춤
        return 'nope'    
    if data[x][y] == 1: #1이면 상하좌우로 이동
        data[x][y] = 0 # 방문처리
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return 'go'
    if x == n and y == m:
        return 'stop'
    return 'nope'

count = 0
temp_break = 'nb'
for i in range(n):
    for j in range(m):
        if dfs(i,j) == 'go':
            count +=1
        elif dfs(i,j) == 'stop':
            temp_break = 'b'
            break
        
    if temp_break == 'b':
        break
print(count)
