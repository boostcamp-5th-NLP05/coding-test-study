N, M = map(int, input().split())
INF = int(1e9)
dist = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())  # a 성적 < b 성적 : a -> b
    dist[a][b] = 1

for i in range(1, N + 1):
    dist[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][k] + dist[k][j] == 2:
                dist[i][j] = 1

ans = 0
for k in range(1, N + 1):
    cnt = 0
    for i in range(1, N + 1):
        if dist[i][k] or dist[k][i]:
            cnt += 1
    if cnt == N - 1:
        ans += 1

print(ans)
