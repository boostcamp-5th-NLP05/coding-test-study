from heapq import heappop, heappush
import sys


def input():
    return sys.stdin.readline().rstrip()


INF = int(1e9)

if __name__ == "__main__":
    N, M, C = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    # 입력 받으면서 graph 입력
    for _ in range(M):
        src, dst, dist = map(int, input().split())
        graph[src].append([dst, dist])

    visited = [False for _ in range(N + 1)]
    dist_map = [INF for _ in range(N + 1)]

    hq = []
    # 시작점 설정 
    heappush(hq, (0, C))
    visited[C] = True
    dist_map[C] = 0

    # 개선된 다익스트라 알고리즘 사용
    while hq:
        cur_dist, cur = heappop(hq)
        visited[cur] = True
        if dist_map[cur] < cur_dist:
            continue

        for next_dst, next_dist in graph[cur]:
            new_dist = cur_dist + next_dist
            if new_dist < dist_map[next_dst]:
                dist_map[next_dst] = new_dist
                heappush(hq, (new_dist, next_dst))

    # 결과 계산
    total_city = 0
    max_time = 0
    for dist in dist_map:
        if dist == INF:
            continue
        total_city += 1
        max_time = max(max_time, dist)
    print(total_city - 1, max_time)
