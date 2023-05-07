# 백준 2887 정답: 101984 KB, 1588 ms
import sys

N = int(sys.stdin.readline().rstrip())
x_pos = []
y_pos = []
z_pos = []
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    x_pos.append((x, i)) # x 좌표, 행성 번호
    y_pos.append((y, i)) # y 좌표, 행성 번호
    z_pos.append((z, i)) # z 좌표, 행성 번호

edges = []
# 좌표 정렬
x_pos.sort()
y_pos.sort()
z_pos.sort()
for i in range(N - 1):
    edges.append((abs(x_pos[i][0] - x_pos[i + 1][0]), x_pos[i][1], x_pos[i + 1][1])) # 비용, 행성1, 행성2
    edges.append((abs(y_pos[i][0] - y_pos[i + 1][0]), y_pos[i][1], y_pos[i + 1][1]))
    edges.append((abs(z_pos[i][0] - z_pos[i + 1][0]), z_pos[i][1], z_pos[i + 1][1]))

parent = [i for i in range(N)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    parent[y] = x


edges.sort()
ans = 0
for e in edges:
    if find_parent(e[1]) != find_parent(e[2]):
        ans += e[0]
        union_parent(e[1], e[2])

print(ans)
