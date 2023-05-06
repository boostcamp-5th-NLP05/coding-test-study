import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = [list(map(int, input().split())) for i in range(M)]

edges.sort(key=lambda x: x[2])


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [0] * (N + 1)
for i in range(0, N + 1):
    parent[i] = i


total_sum = 0
result = 0

for i in range(M):
    s, e, cost = edges[i]
    total_sum += cost

    if find_parent(parent, s) != find_parent(parent, e):
        union_parent(parent, s, e)
        result += cost

print(total_sum - result)















