N, M = map(int, input().split())

parent = [i for i in range(N + 1)]
sz = [1 for _ in range(N + 1)]


def Find(x):
    if parent[x] != x:
        parent[x] = Find(parent[x]) # 경로 압축 방식
    return parent[x]


def Union(x, y):
    x = Find(x)
    y = Find(y)
    # 사이즈가 더 큰 집합에 합치기
    if sz[x] < sz[y]:
        parent[x] = y
        sz[y] += sz[x]
    else:
        parent[y] = x
        sz[x] += sz[y]


for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 0:
        Union(a, b)
    else:
        if Find(a) == Find(b):
            print("YES")
        else:
            print("NO")
