import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
exist = [] #시작도시와 도착도시를 연결하는 노선이 하나가 아닐 수 있으므로 최소를 저장
exist_cost = []

for i in range(m):
    a,b,c = map(int, input().split())
    if (a,b) not in exist:
        graph[a].append((b,c))
        exist.append((a,b))
        exist_cost.append(c)
    else:
        idx = exist.index((a,b))
        if exist_cost[idx] < c: #기존보다 비용이 작으면
            graph[a].append((b,c))
            exist_cost[idx] = c

def dijkstra(start):
    fee = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0,start))
    fee[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if fee[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
			# 현재 노드를 거쳐서 다른 노드로 이동하는 비용이 더 짧은 경우
            if cost < fee[i[0]]:
                fee[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        ans = fee[1:] # 1부터 고려하였기 때문에 인덱스 0 삭제
    return ans

# 다익스트라 알고리즘 수행
for city in range(1,n+1):
    temp = dijkstra(city)
    for a in range(n):
        if temp[a] == INF:
            temp[a] = 0
    print(temp)
