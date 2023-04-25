import sys

sys = sys.stdin.readline

INF = int(1e9)

N = int(input())
M = int(input())

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(M):

    s, e, distance = map(int, input().split())

    if graph[s][e] > distance:
        graph[s][e] = distance

# 플로이드
for k in range(1, N + 1):
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            graph[r][c] = min(graph[r][c], graph[r][k] + graph[k][c])

for r in range(1, N + 1):
    for c in range(1, N + 1):

        if graph[r][c] == INF:
            print(0, end=" ")

        else:
            print(graph[r][c], end=" ")
    print()
