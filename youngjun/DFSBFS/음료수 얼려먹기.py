n, m = map(int,input().split())

map_ = []

for i in range(n):
    map_.append(list(map(int, input())))
    
answer = 0

def DFS(r,c):
    if r < 0 or r >= n or c < 0 or c >= m:
        return False
    
    if map_[r][c] == 0:
        
        map_[r][c] =1
        DFS(r+1,c)
        DFS(r-1,c)
        DFS(r,c+1)
        DFS(r,c-1)
        
        return True
    
    if map_[r][c] == 1:
        return False

for i in range(n):
    for j in range(m):
        if DFS(i,j):
            answer += 1
            
print(answer)