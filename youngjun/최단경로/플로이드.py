import sys

def input():
    return sys.stdin.readline().rstrip()

inf = 1e9

n = int(input())
m = int(input())

graph = [[inf] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b],c) #중복 노선이 있기 때문에 최솟값으로
    
for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            graph[b][c] = min(graph[b][c],graph[b][a]+graph[a][c])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] >= inf:
            graph[i][j] = 0
        print(graph[i][j],end = ' ')
    print()
            