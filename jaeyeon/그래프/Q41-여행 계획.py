import sys


def input():
    return sys.stdin.readline().rstrip()


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def make_union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    parent[b] = a


def is_same_union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return True
    else:
        return False


if __name__ == "__main__":
    N, M = map(int, input().split())
    parent = [i for i in range(N)]
    for i in range(N):
        data = list(map(int, input().split()))
        # 우측 상삼각행렬에 대해서만 union 진행
        for idx, node in enumerate(data):
            if idx > i and node == 1:
                make_union(parent, i, idx)

    to_visit = list(map(int, input().split()))

    answer = "YES"
    for i in range(M - 1):
        if not is_same_union(parent, to_visit[i] - 1, to_visit[i + 1] - 1):
            answer = "NO"
            break

    print(answer)
