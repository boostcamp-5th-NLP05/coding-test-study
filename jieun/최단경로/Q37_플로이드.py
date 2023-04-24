# 백준 11404 정답, 31256 KB, 640 ms
import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

INF = int(1e9)
dist = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    dist[a][b] = min(dist[a][b], c)  # 노선 여러개 일수도 있음
    # a->b, 비용 c

for i in range(1, N + 1):
    dist[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dist[i][j] < INF:
            print(dist[i][j], end=" ")
        else:
            print(0, end=" ")
    print()
