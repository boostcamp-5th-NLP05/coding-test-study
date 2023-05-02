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


if __name__ == "__main__":
    N, M = map(int, input().split())
    parent = [i for i in range(N + 1)]

    roads = []
    for _ in range(M):
        a, b, cost = map(int, input().split())
        roads.append((cost, a, b))
    roads.sort()

    # 비용을 저장해둘 배열
    total = []
    for road in roads:
        cost, a, b = road

        # 같은 유니온에 있으면 사이클이 만들어지므로 같은 유니온이 아닐 때만 신장 트리에 더해주기
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total.append(cost)

    # cost가 가장 큰 도로를 제외한 나머지 합
    print(sum(total[:-1]))
