import heapq
inf = int(1e9)
n,m,c = map(int,input().split())

graph = [[] for _ in range(n+1)]
distance = [inf] * (n+1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))
    
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(c)

cnt = 0
time = 0
for i in distance:
    if i != inf:
        cnt += 1
        time = max(time,i)

print(cnt-1,time)