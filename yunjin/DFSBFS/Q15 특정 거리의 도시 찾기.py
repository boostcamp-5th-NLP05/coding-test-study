from collections import deque
import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

visited = [False for i in range(N + 1)]

adjacent = [[] for i in range(N + 1)]

# 인접 리스트
for i in range(M):
    s, e = map(int, input().split())
    adjacent[s].append((e))


def BFS(s, distance):
    d = deque()
    d.append((s, distance))
    visited[s] = True
    result = []

    while d:
        x, dis = d.popleft()

        # 특정 거리인 것들을 result 에 담아주기
        if dis == K:
            result.append(x)

        # K+1 이상이 되면 BFS 탐색 종료
        if dis >= K+1:
            return result

        for adj in adjacent[x]:
            if not visited[adj]:
                d.append((adj, dis + 1))
                visited[adj] = True

    return result


result = BFS(X, 0)
result.sort()


if len(result) > 0:
    for r in result:
        print(r)
else:
    print(-1)
