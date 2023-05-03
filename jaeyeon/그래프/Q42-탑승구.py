import sys


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
    G = int(input())
    P = int(input())

    parent = [i for i in range(G + 1)]
    ans = 0
    for _ in range(P):
        g = int(input())
        g = find_parent(parent, g)

        if g == 0:
            break

        union(parent, g, g - 1)
        ans += 1

    for _ in range(P - ans - 1):
        input()

    print(ans)
