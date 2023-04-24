import heapq

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
X, K = map(int, input().split())

INF = int(1e9)

dist = [INF for _ in range(N + 1)]
dist[K] = 0

q = []
heapq.heappush(q, (0, K))
while q:
    curd, cur = heapq.heappop(q)
    if curd > dist[cur]:
        continue
    for nxt in edges[cur]:
        d = curd + 1
        if d < dist[nxt]:
            dist[nxt] = d
            heapq.heappush(q, (d, nxt))

ans = dist[1] + dist[X]
if ans < INF:
    print(ans)
else:
    print(-1)
# print(dist)
