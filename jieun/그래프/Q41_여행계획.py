# 백준 1976 정답: 31256 KB, 52 ms
import sys
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
edges = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
plan = list(map(lambda x: int(x) - 1, input().split()))  # 도시 인덱스를 0부터 시작

parent = [i for i in range(N)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    parent[y] = x


for s in range(N):
    for e in range(N):
        if edges[s][e] == 1 and find_parent(s) != find_parent(e):
            union_parent(s, e)


par = find_parent(plan[0])
flag = True
for p in plan[1:]:
    if par != find_parent(p):
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
