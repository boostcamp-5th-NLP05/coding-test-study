import sys
from heapq import heappop, heappush


def input():
    return sys.stdin.readline().rstrip()


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    N = int(input())

    positions = []
    costs = []
    x_list = []
    y_list = []
    z_list = []

    parent = [i for i in range(N)]

    for idx in range(N):
        x, y, z = map(int, input().split())
        x_list.append((x, idx))
        y_list.append((y, idx))
        z_list.append((z, idx))

    x_list.sort()
    y_list.sort()
    z_list.sort()

    tunnels = []
    for idx in range(N - 1):
        heappush(
            tunnels,
            (x_list[idx + 1][0] - x_list[idx][0], x_list[idx + 1][1], x_list[idx][1]),
        )
        heappush(
            tunnels,
            (y_list[idx + 1][0] - y_list[idx][0], y_list[idx + 1][1], y_list[idx][1]),
        )
        heappush(
            tunnels,
            (z_list[idx + 1][0] - z_list[idx][0], z_list[idx + 1][1], z_list[idx][1]),
        )

    total_cost = 0
    while tunnels:
        cost, src, dst = heappop(tunnels)
        if find_parent(parent, src) != find_parent(parent, dst):
            union(parent, src, dst)
            total_cost += cost

    print(total_cost)
