# 백준 6118 정답: 39640 KB, 168 ms
import sys
import heapq

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

INF = int(1e9)
dist = [INF for _ in range(N + 1)]

q = []
heapq.heappush(q, (0, 1))  # 거리, 헛간
dist[1] = 0

while q:
    curd, cur = heapq.heappop(q)
    if curd > dist[cur]:
        continue
    for nxt in edges[cur]:
        nxtd = curd + 1
        if nxtd < dist[nxt]:
            dist[nxt] = nxtd
            heapq.heappush(q, (nxtd, nxt))

hut = 1 # 최단거리가 가장 먼 헛간 (중 가장 작은 번호)
same = 1 # 헛간 hut과 같은 최단거리를 갖는 헛간 개수
for i in range(2, N + 1):
    if dist[i] > dist[hut]:
        hut = i
        same = 1
    elif dist[i] == dist[hut]:
        same += 1

print(hut, dist[hut], same)
