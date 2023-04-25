import sys


def input():
    return sys.stdin.readline().rstrip()


INF = int(1e9)
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 그래프 초기값 설정
    for _ in range(m):
        src, dst, cost = map(int, input().split())
        graph[src][dst] = min(graph[src][dst], cost)

    for src in range(1, n + 1):
        for dst in range(1, n + 1):
            if src == dst:
                graph[src][dst] = 0

    # 플로이드 워셜 알고리즘 실행
    for k in range(1, n + 1):
        for src in range(1, n + 1):
            for dst in range(1, n + 1):
                graph[src][dst] = min(graph[src][dst], graph[src][k] + graph[k][dst])

    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if graph[r][c] == INF:
                print("0", end=" ")
            else:
                print(graph[r][c], end=" ")
        print()
