import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]

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

# 부모를 자기 자신으로 초기화
for i in range(0, N + 1):
    parent[i] = i


edges = []
for i in range(M):
    s, e, cost = map(int, input().split())
    edges.append((cost, s, e))

edges.sort()

result = []
for edge in edges:
    cost, s, e = edge
    if find_parent(parent, s) != find_parent(parent, e):
        union_parent(parent, s, e)
        result.append(cost)

# 최대값 빼주면 마을을 두개로 나누는 최단 거리
print(sum(result)-max(result))
