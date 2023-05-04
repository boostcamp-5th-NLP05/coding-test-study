import sys
input = sys.stdin.readline
N = int(input())

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

edges = []
x = []
y = []
z = []

# x 좌표, y 좌표, z 좌표 분리하여 넣는다.
for i in range(N):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

# 각각 정렬
x.sort()
y.sort()
z.sort()

# x,y,z 독립적으로 edges 에 넣어준다.
for i in range(N - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i+1][1], x[i][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i+1][1], y[i][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i+1][1], z[i][1]))

edges.sort()

# 유니온 파인드 실시.
result = 0
for edge in edges:
    cost, s, e = edge
    if find_parent(parent, s) != find_parent(parent, e):
        union_parent(parent, s, e)
        result += cost

print(result)