N, M = map(int, input().split())
edges = []
total = 0
for _ in range(M):
    x, y, z = map(int, input().split())  # 집, 집, 길이
    edges.append((z, x, y))
    total += z

parent = [i for i in range(N + 1)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    parent[y] = x


edges.sort()
dist = 0
for e in edges:
    if find_parent(e[1]) != find_parent(e[2]):
        dist += e[0]
        union_parent(e[1], e[2])

ans = total - dist
print(ans)
