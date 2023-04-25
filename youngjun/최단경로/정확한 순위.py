inf = 1e9

n,m = map(int, input().split())

graph = [[inf] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1


for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            graph[b][c] = min(graph[b][c],graph[b][a]+graph[a][c])

answer = 0
for i in range(1,n+1):
    tmp = True
    for j in range(1,n+1):
        if graph[i][j] != inf or graph[j][i] != inf:
            continue
        else:
            tmp = False
            break
    if tmp:
        answer += 1

print(answer)

