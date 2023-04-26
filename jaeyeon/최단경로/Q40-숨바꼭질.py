from heapq import heappop, heappush
import sys


def input():
    return sys.stdin.readline().rstrip()


INF = int(1e9)

if __name__ == "__main__":
    N, M = map(int, input().split())

    # 값 입력 받기
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        src, dst = map(int, input().split())
        graph[src].append((dst, 1))
        graph[dst].append((src, 1))

    # 거리 저장 배열 선언 및 초기화
    dist_map = [INF] * (N + 1)
    dist_map[1] = 0

    # 힙큐 선언 및 초기값 push
    hq = []
    heappush(hq, (0, 1))

    # 다익스트라 알고리즘 수행
    while hq:
        cur_dist, cur_pos = heappop(hq)
        if cur_dist > dist_map[cur_pos]:
            continue

        for next_pos, next_dist in graph[cur_pos]:
            new_dist = cur_dist + next_dist
            if new_dist < dist_map[next_pos]:
                dist_map[next_pos] = new_dist
                heappush(hq, (new_dist, next_pos))

    # 도달할 수 없는 곳 처리
    for idx, val in enumerate(dist_map):
        if val == INF:
            dist_map[idx] = -1

    # 문제에 맞게 출력
    max_val = max(dist_map)
    print(dist_map.index(max_val), max(dist_map), dist_map.count(max_val))
