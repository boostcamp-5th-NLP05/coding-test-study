import heapq

n,m = map(int,input().split())
inf = 1e9

graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append((b,1)) #양방향으로 간선 입력
    graph[b].append((a,1))
distance = [inf] * (n+1)

q = []
distance[1] = 0
heapq.heappush(q,(0,1))

while q: #다익스트라
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

distance = distance[1:]

max_dist = max(distance)
hide_idx = distance.index(max_dist)
cnt_dist = distance.count(max_dist)

print(hide_idx + 1, max_dist, cnt_dist)