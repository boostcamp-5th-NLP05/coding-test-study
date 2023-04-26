import sys
import heapq

input = sys.stdin.readline

T = int(input())
INF = 1e9

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]



for _ in range(T):
    N = int(input())

    graph = [list(map(int, input().split())) for r in range(N)]

    INF = int(1e9)
    distance = [[INF] * N for _ in range(N)]

    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]

    # 다익스트라 (동서남북 연결)
    while q:
        dist, r, c = heapq.heappop(q)

        if distance[r][c] < dist:
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            cost = dist + graph[nr][nc]

            if cost < distance[nr][nc]:
                distance[nr][nc] = cost
                heapq.heappush(q, (cost, nr, nc))

    print(distance[N-1][N-1])
