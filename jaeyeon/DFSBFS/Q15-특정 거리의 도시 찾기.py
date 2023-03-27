from collections import deque

if __name__ == "__main__":
    N, M, K, X = map(int, input().split())

    # 아직 순회하지 않은 곳까지의 거리는 INF로 둔다.
    INF = 987654321
    dist = [INF for _ in range(N + 1)]

    # 인접 행렬로 했더니 메모리 초과 나서 인접 리스트로 구현
    map_ = [[] for _ in range(N + 1)]
    for _ in range(M):
        src, dst = map(int, input().split())
        map_[src].append(dst)

    queue = deque([[X, 0]])

    while queue:
        cur_pos, depth = queue.popleft()
        # depth가 K보다 큰 곳은 볼 필요 없으므로 break
        if depth > K: break

        # 처음 순회하는 도시의 값만 업데이트
        if dist[cur_pos] == INF:
            dist[cur_pos] = depth

        for city in map_[cur_pos]:
            if dist[city] == INF:
                queue.append([city, depth + 1])

    # 거리가 K인 곳만 탐색
    answer = []
    for idx, d in enumerate(dist):
        if d == K:
            answer.append(idx)

    if len(answer) == 0:
        print("-1")
    else:
        for a in answer:
            print(a)

# 17분 21초
