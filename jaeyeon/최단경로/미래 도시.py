import sys


def input():
    return sys.stdin.readline().rstrip()


INF = int(1e9)

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[INF] * (N + 1) for _ in range(N + 1)]

    # 입력 받으면서 바로 graph에 값 넣어주기
    for _ in range(M):
        a, b = map(int, input().split())
        # 양방향 그래프이기 때문에 둘 다 넣어주기
        graph[a][b] = 1
        graph[b][a] = 1
    X, K = map(int, input().split())

    # 같은 지점의 거리는 0으로 처리
    for src in range(1, N + 1):
        for dst in range(1, N + 1):
            if src == dst:
                graph[src][dst] = 0

    # 플로이드워셜 점화식 구현
    for k in range(1, N + 1):
        for src in range(1, N + 1):
            for dst in range(1, N + 1):
                graph[src][dst] = min(graph[src][dst], graph[src][k] + graph[k][dst])

    dist = graph[1][K] + graph[K][X]
    if dist >= INF:
        print("-1")
    else:
        print(dist)
