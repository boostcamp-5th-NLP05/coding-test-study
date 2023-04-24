import heapq

N, M, C = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))  # a -> b ; 비용 c

INF = int(1e9)
dist = [INF for _ in range(N + 1)]  # 각 도시에 전보가 도달하는 최소 시간
dist[C] = 0

q = []
heapq.heappush(q, (0, C))
while q:
    curd, cur = heapq.heappop(q)
    if curd > dist[cur]:
        continue
    for nxt in edges[cur]:  # nxt = (도시, 시간)
        t = curd + nxt[1]
        if t < dist[nxt[0]]:
            dist[nxt[0]] = t
            heapq.heappush(q, (t, nxt[0]))

cnt = -1  # 메시지 보내는 도시 C 제외
time = 0
for t in dist:
    if t < INF:
        cnt += 1
        time = max(time, t)

print(cnt, time)
