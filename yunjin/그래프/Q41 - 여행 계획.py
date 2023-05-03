import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

indegree = [0] * (N)
graph = [list(map(int, input().split())) for i in range(N)]

numbers = list(map(int, input().split()))

parent = [0] * (N + 1)

for i in range(0, N + 1):
    parent[i] = i


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


# 여행 가능한 지점에 대해서 union 해준다.
for r in range(N):
    for c in range(N):
        if graph[r][c] == 1:
            union_parent(parent, r + 1, c + 1)

answer = "YES"

s = set()
for numbers in numbers:
    s.add(parent[numbers])

if len(s) != 1:  # 한 번이라도 같은 부모가 아닌 경우가 있다면 len(s) != 1 일 것임.
    answer = "NO"

print(answer)
