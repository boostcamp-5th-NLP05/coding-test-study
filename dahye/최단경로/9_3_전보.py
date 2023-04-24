import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
time = [INF] * (N+1)

for i in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) 

# 이론에서 언급했던 거리 개념을 시간으로 생각하여 풀이
def dijkstra(C):
    q = []
    heapq.heappush(q, (0,C))
    time[C] = 0
    while q:
        t, now = heapq.heappop(q)
        if time[now] < t:
            continue
        for i in graph[now]:
            cost = t + i[1]
			# 현재 노드를 거쳐서 다른 노드로 이동하는 시간이 더 짧은 경우
            if cost < time[i[0]]:
                time[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(C)

ans = 0
count = -1 # 시작 도시는 count되지 않으므로 -1부터 시작
# 모든 노드를 한번 이상 가기 위한 최단 시간을 출력
for i in range(1, N+1):
    # 도달할 수 없는 경우, pass
    if time[i] == INF:
        pass
        
    # 도달할 수 있는 경우 최대시간 저장
    else:
        ans = max(ans, time[i])
        count+=1
print(count, ans)