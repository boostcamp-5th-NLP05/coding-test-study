import sys


def input():
    return sys.stdin.readline().rstrip()


def find_parent(parent, x):
    while parent[x] != x:
        x = parent[x]

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 같은 union에 있는지 확인하는 함수
def is_parent_same(a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    N, M = map(int, input().split())
    parent = [i for i in range(0, N + 1)]

    for _ in range(M):
        op, a, b = map(int, input().split())

        if op == 0:
            union_parent(parent, a, b)
        else:
            is_parent_same(a, b)
