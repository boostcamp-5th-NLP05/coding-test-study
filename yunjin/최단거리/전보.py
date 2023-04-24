import sys
import heapq

input = sys.stdin.readline

N, M, C = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

INF = int(1e9)
distance = [INF] * (N + 1)

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


# 다익스트라 실시
dijkstra(C)

answer = 0
time_answer = 0


for dis in distance:
    if dis != INF:
        answer += 1
        time_answer = max(time_answer, dis)

print(answer-1, time_answer)

