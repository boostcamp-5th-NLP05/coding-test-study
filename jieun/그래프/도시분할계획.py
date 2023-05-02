import sys

N,M = map(int, sys.stdin.readline().rstrip().split())
edges = []
for _ in range(M):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((c,a,b))
    
parent = [i for i in range(N+1)]
sz = [1 for _ in range(N+1)]

def Find(x):
    if parent[x] != x:
        parent[x] = Find(parent[x]) # 경로 압축 방식
    return parent[x]


def Union(x, y):
    x = Find(x)
    y = Find(y)
    # 사이즈가 더 큰 집합에 합치기
    if sz[x] < sz[y]:
        parent[x] = y
        sz[y] += sz[x]
    else:
        parent[y] = x
        sz[x] += sz[y]
        
edges.sort()
ans = 0
max_val = 0

# 최소 스패닝 트리 찾기
for e in edges:
    if Find(e[1]) == Find(e[2]): continue
    ans += e[0]
    Union(e[1], e[2])
    max_val = max(max_val, e[0])
    
ans -= max_val # 최소 스패닝 트리 중 가장 큰 간선 제거
print(ans)