import sys
from collections import deque


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
    N, M = map(int, input().split())
    roads = []
    parent = [i for i in range(N)]

    total_cost = 0
    for _ in range(M):
        src, dst, cost = map(int, input().split())
        roads.append([cost, src, dst])
        total_cost += cost

    cost_use = 0
    roads.sort()
    for road in roads:
        cost, src, dst = road
        if find_parent(parent, src) != find_parent(parent, dst):
            union(parent, src, dst)
            cost_use += cost

    print(total_cost - cost_use)
