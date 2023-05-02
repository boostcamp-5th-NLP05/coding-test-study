import sys

input = sys.stdin.readline

N, M = map(int, input().split())


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

for i in range(M):
    what, a, b = map(int, input().split())
    if what == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) != find_parent(parent, b):
            print("NO")
        else:
            print("YES")



