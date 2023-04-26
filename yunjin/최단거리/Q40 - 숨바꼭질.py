import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

INF = 1e9

graph = [[] for i in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append((e, 1))
    graph[e].append((s, 1))

distance = [INF for i in range(N + 1)]

# 다익스트라
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(1)

answer_dis = max(distance[1:])
answer_idx = 0
answer_cnt = 0

# 거꾸로
for _ in range(N, 1, -1):
    if distance[_] == answer_dis:
        answer_idx = _
        answer_cnt += 1

print(answer_idx, answer_dis, answer_cnt)
